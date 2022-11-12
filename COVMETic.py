import requests 
import json
import telebot

api = '5739603192:AAGlZaoJw9ilCYb8FDh10QQ8ZAKXBn6odxY'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def greet(message):

    chatid = message.chat.id
    bot.send_photo(chatid, open('lawak.png','rb'))

    spill = ('''
Selamat Datang di COVMETic BOT (Disaster & COVID Info)
Tekan perintah Berikut Untuk Mengakses Data Yang Diinginkan

COVID SERVICE

/covcs (untuk melihat total data covid seluruh provinsi)
/covcs [nama provinsi] (untuk melihat total data covid salah satu provinsi)
/covnw (untuk covid baru di Indonesia)
/covrs (untuk menampilkan rumah sakit covid seluruh Indonesia) (TIDAK DISARANKAN)
/covrs[nama provinsi/kota](untuk menampilkan rumah sakit covid regional)
/covnws (untuk mencari berita terkait covid)
/covbook(untuk buku panduan Isolasi mandiri)
/covgej (Untuk Gejala Covid varian XBB)

DISASTER SERVICE

/gmptr (untuk menampilkan gempa terbaru)
/gmptr15(menampilkan 15 daftar gempa yang dirasakan)


SYSTEM SERVICE

/help (untuk meminta panduan penggunaan)


    ''')
    bot.reply_to (message, spill)

@bot.message_handler(commands=['help'])
def help (message):

    spill = ('''

Help Menu 

COVID SERVICE

/covcs (untuk melihat total data covid seluruh provinsi)
/covcs [nama provinsi] (untuk melihat total data covid salah satu provinsi)
/covnw (untuk covid baru di Indonesia)
/covrs (untuk menampilkan rumah sakit covid seluruh Indonesia) (TIDAK DISARANKAN)
/covrs[nama provinsi/kota](untuk menampilkan rumah sakit covid regional)
/covnws (untuk mencari berita terkait covid)
/covbook(untuk buku panduan Isolasi mandiri)
/covgej (Untuk Gejala Covid varian XBB)

DISASTER SERVICE

/gmptr (untuk menampilkan gempa terbaru)
/gmptr15(menampilkan 15 daftar gempa yang dirasakan)


SYSTEM SERVICE

/help (untuk meminta panduan penggunaan)

    ''')
    bot.reply_to (message, spill)

@bot.message_handler(commands=['covbook'])
def covid_book_manual (message):
    chatid = message.chat.id
    bot.send_document(chatid,open('panduan.pdf','rb'))
    bot.reply_to(message,'''Berikut buku panduan untuk isolasi mandiri
    !!! HUBUNGI 112 APABILA DARURAT !!!
    ''')


@bot.message_handler(commands=['covcs'])
def covid(message):
    text = message.text
    provinsi = text[7:]
    page = requests.get('https://data.covid19.go.id/public/api/prov.json')
    #print(page.text)

    page_json = page.json()
    list_data = page_json['list_data']

    for i in list_data :
        
        prov = i['key']
        kasus = i['jumlah_kasus']
        sembuh = i['jumlah_sembuh']
        mati = i['jumlah_meninggal']
        rawat = i['jumlah_dirawat']
        
        data = ('''
Provinsi    = {}
kasus       = {} 
sembuh      = {}
meninggal   = {}
Dirawat     = {}
        '''.format(prov,kasus,sembuh,mati,rawat))
        if provinsi.upper() in prov.upper():
            bot.reply_to(message, data)
        else :
            pass

@bot.message_handler(commands=['covnw'])
def new_covid(message):
    web = requests.get('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json')
    page_json = web.json()

    query = page_json['IDN']

    terakhir_update = query['last_updated_date']
    total_kasus     = query['total_cases']
    kasus_baru      = query['new_cases']
    total_mati      = query['total_deaths']
    baru_mati       = query['new_deaths']
    total_kasus_persatujuta = query['total_cases_per_million']
    kasus_baru_persatujuta = query['new_cases_per_million']
    total_vaksinasi = query['total_vaccinations']
    vaksin1 = query['people_vaccinated']
    vaksin2 = query['people_fully_vaccinated']
    vaksin3 = query['total_boosters']

    spill = ('''
Terakhir Update = {}

Total kasus = {}
kasus Baru = {}

total kematian = {}
Kematian Baru  = {}

total kasus persatujuta = {}
total kasus baru persatujuta = {}

total vaksinasi 1 = {}
total vaksinasi 2 = {}
total vaksinasi 3 = {}

sumber data John Hopkins University 


    '''.format(terakhir_update,total_kasus,kasus_baru,total_mati,baru_mati,total_kasus_persatujuta,kasus_baru_persatujuta,
total_vaksinasi,vaksin1,vaksin2,vaksin3))
    bot.reply_to (message, spill)

@bot.message_handler(commands=['gmptr'])
def gempa_terbaru(message):
    web = requests.get('https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json')
    halaman_json = web.json()

    query = halaman_json['Infogempa']['gempa']

    tanggal = query['Tanggal']
    jam     = query['Jam']
    Data_time = query ['DateTime']
    koordinat = query ['Coordinates']
    lintang   = query ['Lintang']
    bujur   = query['Bujur']
    magnitude = query['Magnitude']
    kedalaman = query ['Kedalaman']
    wilayah   = query ['Wilayah']

    data = ('''
    Data Gempa Terbaru BMKG

tanggal     = {}
jam         = {}
Data Time   = {}
 Koordinat  = {}
Lintang     = {}
bujur       = {}
Magnitude   = {}
kedalaman   = {}
kedalaman   = {}
wilayah     = {}

APABILA ANDA MENGALAMI KEADAAN DARURAT HUBUNGI 112 UNTUK RESPON CEPAT
sumber : BMKG
    '''.format(tanggal,jam,Data_time,koordinat,lintang,bujur,magnitude,kedalaman,
    kedalaman,wilayah))
    bot.reply_to(message, data)

@bot.message_handler(commands=['covrs'])
def rs (message):

    web = requests.get('https://dekontaminasi.com/api/id/covid19/hospitals')
    halaman_json = web.json()

    text = message.text
    provinsi1 = text[7:]

    for i in halaman_json:
        nama = i['name']
        alamat = i['address']
        region = i['region']
        telepon =i['phone']
        provinsi = i['province']

        data = ('''
Nama RS     = {}
Alamat RS   = {}
Region RS   = {}
telepon RS  = {}
provinsi RS = {}
        '''.format(nama,alamat,region,telepon,provinsi))
        if provinsi1.upper() in provinsi.upper():
            bot.reply_to(message, data)
        else :
           pass

@bot.message_handler(commands=['covnws'])
def covid_news(message):
    web = requests.get('https://dekontaminasi.com/api/id/covid19/news')
    halaman_json = web.json()

    for i in halaman_json:
        title = i['title']
        url = i['url']
        
        data = ('''
{}
{}
        '''.format(title,url))
        bot.reply_to(message,data)

@bot.message_handler(commands=['gmptr15'])
def daftar_gempa(message):
    web = requests.get('https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json')
    list_data = web.json()

    query = list_data['Infogempa']['gempa']

    for i in query:
        tanggal = i['Tanggal']
        jam     = i['Jam']
        date_time = i['DateTime']
        kordinat = i['Coordinates']
        lintang  = i['Lintang']
        bujur    = i['Bujur']
        magnitude = i ['Magnitude']
        kedalaman = i ['Kedalaman']
        wilayah   = i ['Wilayah']
        dirasakan = i['Dirasakan']
        
        print = ('''
Tangggal    = {}
jam         = {}
Server Time = {}
Koordinat   = {}
Lintang     = {}
Bujur       = {}
Magnitude   = {}
Kedalaman   = {}
Wilayah     = {}
Dirasakan   = {}
        '''.format(tanggal,jam,date_time,kordinat,lintang,bujur,
magnitude,kedalaman,wilayah,dirasakan))
        bot.reply_to(message, print)

@bot.message_handler(commands=['covgej'])
def gejala_covid(messsage):

    chatid = messsage.chat.id
    bot.send_photo(chatid, open('xbb.jpg','rb'))


print('bot running')
bot.polling()
