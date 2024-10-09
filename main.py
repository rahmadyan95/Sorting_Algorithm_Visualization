from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class sorting_algoritm(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.rects = None
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        master.protocol("WM_DELETE_WINDOW",self.on_closing)

        side_bar = CTkLabel(master,text='',height=100,width=1280,bg_color='grey30')
        side_bar.place(x=0,y=0)

        image_home = os.path.join(self.script_dir, 'asset', 'sortinglogo.png')
        imagehome = CTkImage(light_image=Image.open(image_home), size=(68,60))
        image_label = CTkLabel(side_bar,image=imagehome,text='',bg_color='grey30')
        image_label.place(x=15,y=10)


        text_sidebar = CTkLabel(side_bar,text='SORTING ALGORITHM',bg_color='grey30',
                                font=("Bahnschrift SemiBold SemiConden",32))
        text_sidebar.place(x=100,y=5)

        text_sidebar = CTkLabel(side_bar,text='VISUALIZATION',bg_color='grey30',height=32,
                                font=("Bahnschrift SemiBold SemiConden",32))
        text_sidebar.place(x=100,y=40)

        config_bar = CTkButton(master,height=580,width=350,text="",bg_color='transparent',fg_color="grey30",
                               border_color="white",border_width=1,state='disabled')
        config_bar.place(x=910,y= 120 )


        text_configbar = CTkLabel(config_bar,text='CONFIGURATION',bg_color='grey30',height=40,width=100,
                                font=("Bahnschrift SemiBold SemiConden",28))
        text_configbar.place(x=85,y=15)

        sort_choose_text = CTkLabel(config_bar,text='Choose Sorting to proceed',bg_color='grey30',height=18,width=30,
                                font=("Bahnschrift SemiBold SemiConden",16))
        sort_choose_text.place(x=20,y=80)
        

        self.box = CTkOptionMenu(config_bar,values=["Bubble Sort","Selection Sort","Insertion Sort","Shell Sort"],
                               font=("Bahnschrift SemiBold SemiConden",18),width=300,height=40)
        self.box.place(x=20,y=110)

        sort_numtosort_text = CTkLabel(config_bar,text='Input Number To Sort (seperate by comma)',bg_color='grey30',height=18,width=30,
                                font=("Bahnschrift SemiBold SemiConden",16))
        sort_numtosort_text.place(x=20,y=170)

        self.num_to_sort = CTkEntry(config_bar,height=40,width=300,font=("Bahnschrift SemiBold SemiConden",18))
        self.num_to_sort.place(x=20,y=200)


        speed_of_visualization_text = CTkLabel(config_bar,text='Set Visualization Speed',bg_color='grey30',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",16))
        speed_of_visualization_text.place(x=20,y=260)

   
        self.slider = CTkSlider(config_bar, from_= 1, to=2000, height=20,width=300,number_of_steps=100,fg_color='grey10',
                           command=self.slidering)
        self.slider.place(x=20,y=280)
        self.slider.set(1)
        

        lower_speed_visual = CTkLabel(config_bar,text='1',bg_color='grey30',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",14))
        lower_speed_visual.place(x=15,y=300)

        upper_speed_visual = CTkLabel(config_bar,text='2000',bg_color='grey30',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",14))
        upper_speed_visual.place(x=300,y=300) 

        self.choosen_speed_visual = CTkLabel(config_bar,text='1',bg_color='grey30',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",16))
        self.choosen_speed_visual.place(x=155,y=320)     

        self.button_acc = CTkButton(config_bar,height=40,width=310,text='Proceed',text_color='white',
                                    font=("Bahnschrift SemiBold SemiConden",16),fg_color='grey50',hover_color='green',command=self.handle_proceed)
        self.button_acc.place(x=15,y=360)

        self.button_acc = CTkButton(config_bar,height=40,width=310,text='Terminate',text_color='white',
                                    font=("Bahnschrift SemiBold SemiConden",16),fg_color='grey50',hover_color='Red',command=self.handle_terminate)
        self.button_acc.place(x=15,y=410)


        # untuk ploting ====================================================================================

        # graph_place = CTkButton(master,height=580, width=880,bg_color='grey10',fg_color='grey30',text='',
        #                         state='disabled',border_color="white",border_width=1)
        # graph_place.place(x=15,y=120)

        # self.canvas = FigureCanvasTkAgg(plt.Figure(figsize=(14, 9)), master=graph_place)
        # self.canvas.draw()

        # self.canvas.get_tk_widget().place(x=30, y=70)
        # self.toolbar = NavigationToolbar2Tk(self.canvas, graph_place)
        # self.toolbar.config(height=10, width=30)
        # self.toolbar.update()
        # self.toolbar.place(x=30, y=20)

        self.box1 = CTkButton(master, height=580, width=880,fg_color='grey30',state='disabled',border_color='white',border_width=1)
        self.box1.place(x=15, y=120)
        
        self.graphbox = CTkCanvas(self.box1, height=950, width=1700)
        self.graphbox.place(x=30, y=160)

        self.canvas = FigureCanvasTkAgg(plt.Figure(figsize=(17, 10)), master=self.graphbox)
        self.canvas.draw()

        # Create a separate frame for the toolbar
        # toolbar_frame = CTkFrame(graph_place,height=20,width=119)
        # toolbar_frame.place(x=30, y=20)

        # self.toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        # self.toolbar.config(height=10, width=30)
        # self.toolbar.update()
        # self.toolbar.place(x=0, y=0)

        self.title_plot = CTkLabel(self.box1,text='CHOOSE SORTING ALGORITHM',bg_color='grey30',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",24))
        self.title_plot.place(x=300,y=25)

        # FOR ITERATE COUNT 

        self.iterationbox = CTkButton(side_bar,height=80, width=150,fg_color='grey20',bg_color='grey30',text='',
                                      border_color='white',border_width=1,state='disabled')
        self.iterationbox.place(x=790,y=10)

        self.iterationbox_value = CTkLabel(self.iterationbox,text='0',font= self.font(28),height=30,width=100)
        self.iterationbox_value.place(x=25,y=30)


        self.swapbox = CTkButton(side_bar,height=80, width=150,fg_color='grey20',bg_color='grey30',text='',
                                      border_color='white',border_width=1,state='disabled')
        self.swapbox.place(x=950,y=10)

        self.swapbox_value = CTkLabel(self.swapbox,text='0',font= self.font(28),height=30,width=100)
        self.swapbox_value.place(x=25,y=30)


        self.exect_time = CTkButton(side_bar,height=80, width=150,fg_color='grey20',bg_color='grey30',text='',
                                      border_color='white',border_width=1,state='disabled')
        self.exect_time.place(x=1110,y=10)

        self.exect_time_value = CTkLabel(self.exect_time,text='0',font= self.font(28),height=30,width=100)
        self.exect_time_value.place(x=25,y=30)




        self.title_iter= CTkLabel(self.iterationbox,text='ITERATION',bg_color='grey20',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",14))
        self.title_iter.place(x=10,y=5)
        
        self.swapbox= CTkLabel(self.swapbox,text='SWAP',bg_color='grey20',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",14))
        self.swapbox.place(x=10,y=5)

        self.swapbox= CTkLabel(self.exect_time,text='EXECUTION TIME',bg_color='grey20',height=18,width=30,
                                                font=("Bahnschrift SemiBold SemiConden",14))
        self.swapbox.place(x=10,y=5)

    def font(self,n):
        return ("Bahnschrift SemiBold SemiConden",n)


    def on_closing(self):
        return sys.exit(0)
    
    def handle_terminate(self):
        self.canvas.get_tk_widget().destroy()
        self.iterationbox_value.configure(text=0)
        self.swapbox_value.configure(text=0)
        self.slider.set(0)
        self.exect_time_value.configure(text='0')
    

    
    
    def slidering(self,value):
        self.choosen_speed_visual.configure(text=int(value))

    def bubble_sort_animation(self, bars, n, rects, speed):
        global iteration_count, swaps_list
        a = self.canvas.get_tk_widget()
        
        def update_bars(bars, n, rects):
            global iteration_count, swaps_list
            swaps = 0

            for i in range(n - 1):
                if bars[i] > bars[i + 1]:
                    rects[i].set_color('green')
                    rects[i + 1].set_color('green')
                    bars[i], bars[i + 1] = bars[i + 1], bars[i]
                    rects[i].set_height(bars[i])
                    rects[i + 1].set_height(bars[i + 1])
                    swaps += 1

                else:
                    rects[i].set_color('grey')
                    rects[i + 1].set_color('grey')

            iteration_count += 1
            swaps_list.append(swaps)
            # ax.set_title("Iteration: {}, Swaps: {}".format(iteration_count, sum(swaps_list)))
            self.iterationbox_value.configure(text=iteration_count)
            self.swapbox_value.configure(text=sum(swaps_list))
            if sorted(bars) == bars:
                a.event_source.stop()

            return rects, swaps

        def init():
            return rects

        def animate(i):
            nonlocal bars, rects
            rects, swaps = update_bars(bars, n, rects)
            return rects

        n = len(bars)
        iteration_count = 0
        swaps_list = []
        fig, ax = plt.subplots(figsize=(20, 11))
        rects = ax.bar(range(n), bars, color='grey')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')

        self.canvas = FigureCanvasTkAgg(fig, master=self.graphbox)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=-150,y=-80)

        a = animation.FuncAnimation(fig, animate, init_func=init, interval=speed)
        
   
    def shell_sort_animation(self, bars, n, rects, speed):
        global iteration_count, swaps_list
        a = self.canvas.get_tk_widget()

        def update_bars(i, bars, n, gap, rects):
            global iteration_count, swaps_list
            swaps = 0

            for j in range(i + gap, n, gap):
                key = bars[j]
                iteration_count += 1

                # Move elements of arr[0..i] that are greater than key to right by gap
                k = j
                while k >= gap and bars[k - gap] > key:
                    rects[k].set_color('green')
                    rects[k - gap].set_color('green')

                    # Draw the bars before swap
                    self.canvas.draw()
                    self.canvas.get_tk_widget().update()
                    self.canvas.get_tk_widget().after(speed)  # Add a delay to visualize the swap

                    bars[k], bars[k - gap] = bars[k - gap], bars[k]
                    rects[k].set_height(bars[k])
                    rects[k - gap].set_height(bars[k - gap])
                    k -= gap
                    swaps += 1

                    # print(f"i: {i}, j: {j}, gap: {gap}, swaps: {swaps}")

                # Draw the bars after swap
                self.canvas.draw()
                self.canvas.get_tk_widget().update()

                # Reset color for the bars involved in the last swap
                rects[j].set_color('grey')
                rects[j - gap].set_color('grey')

            swaps_list.append(swaps)
            self.iterationbox_value.configure(text=iteration_count)
            self.swapbox_value.configure(text=sum(swaps_list))
            # if i == len(gaps) - 1 and gap == 1 and all(bars[j] <= bars[j + 1] for j in range(len(bars) - 1)):
            #     a.event_source.stop()

        def init():
            return rects

        def animate(i):
            nonlocal bars, rects
            gap = gaps[i]
            update_bars(i, bars, n, gap, rects)
            
            print(f"Animate - i: {i}, gap: {gap}, swaps: {swaps_list[-1]}")

            # Check if it's the last pass with a gap of 1, and all swaps are done
            if i == len(gaps) - 1 and gap == 1:
                if all(bars[j] <= bars[j + 1] for j in range(len(bars) - 1)):
                    print("Stopping animation.")
                    a.event_source.stop()

        

            return rects

        # Define the sequence of gaps for Shell Sort (you can modify this)
        gaps = [5, 3, 1]

        iteration_count = 0
        swaps_list = []
        fig, ax = plt.subplots(figsize=(20, 11))
        rects = ax.bar(range(n), bars, color='grey')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')

        self.canvas = FigureCanvasTkAgg(fig, master=self.graphbox)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=-150, y=-80)

        a = animation.FuncAnimation(fig, animate, init_func=init, frames=len(gaps), interval=speed, repeat=False)

    def selection_sort_animation(self, bars, n, rects, speed):
        global iteration_count, swaps_list
        a = self.canvas.get_tk_widget()

        def update_bars(i, bars, n, rects):
            global iteration_count, swaps_list
            swaps = 0

            if i < n - 1:
                min_index = i
                for j in range(i + 1, n):
                    if bars[j] < bars[min_index]:
                        min_index = j
                        iteration_count += 1

                rects[i].set_color('green')
                rects[min_index].set_color('green')

                # Draw the bars before swap
                self.canvas.draw()
                self.canvas.get_tk_widget().update()
                self.canvas.get_tk_widget().after(speed)  # Add a delay to visualize the swap

                bars[i], bars[min_index] = bars[min_index], bars[i]
                swaps += 1
                rects[i].set_height(bars[i])
                rects[min_index].set_height(bars[min_index])
                

                # Draw the bars after swap
                self.canvas.draw()
                self.canvas.get_tk_widget().update()

                rects[i].set_color('grey')
                rects[min_index].set_color('grey')

            
            swaps_list.append(swaps)
            self.iterationbox_value.configure(text=iteration_count)
            self.swapbox_value.configure(text=sum(swaps_list))
            if sorted(bars) == bars:
                a.event_source.stop()

            return rects


        def init():
            return rects

        def animate(i):
            nonlocal bars, rects
            update_bars(i, bars, n, rects)
            return rects

        n = len(bars)
        iteration_count = 0
        swaps_list = []
        fig, ax = plt.subplots(figsize=(20, 11))
        rects = ax.bar(range(n), bars, color='grey')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')

        self.canvas = FigureCanvasTkAgg(fig, master=self.graphbox)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=-150, y=-80)

        a = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=speed, repeat=False)

    def insertion_sort_animation(self, bars, n, rects, speed):
        global iteration_count, swaps_list
        a = self.canvas.get_tk_widget()

        def update_bars(i, bars, rects):
            global iteration_count, swaps_list
            j = i
            while j > 0 and bars[j] < bars[j - 1]:
                iteration_count += 1
                rects[j].set_color('green')
                rects[j - 1].set_color('green')

                # Draw the bars before swap
                self.canvas.draw()
                self.canvas.get_tk_widget().update()
                self.canvas.get_tk_widget().after(speed)  # Add a delay to visualize the swap

                bars[j], bars[j - 1] = bars[j - 1], bars[j]
                rects[j].set_height(bars[j])
                rects[j - 1].set_height(bars[j - 1])

                # Draw the bars after swap
                self.canvas.draw()
                self.canvas.get_tk_widget().update()

                rects[j].set_color('grey')
                rects[j - 1].set_color('grey')

                j -= 1

            swaps_list.append(i - j)
            self.iterationbox_value.configure(text=iteration_count)
            self.swapbox_value.configure(text=sum(swaps_list))
            if sorted(bars) == bars:
                a.event_source.stop()

            return rects

        def init():
            return rects

        def animate(i):
            nonlocal bars, rects
            update_bars(i, bars, rects)
            return rects

        iteration_count = 0
        swaps_list = []
        fig, ax = plt.subplots(figsize=(20, 11))
        rects = ax.bar(range(n), bars, color='grey')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')

        self.canvas = FigureCanvasTkAgg(fig, master=self.graphbox)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=-150, y=-80)

        a = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=speed, repeat=False)


    def handle_proceed(self):
        import timeit
        sort_type = self.box.get()
        numbers = [int(num.strip()) for num in self.num_to_sort.get().split(',')]
        speed = int(self.slider.get())

        if sort_type == "Bubble Sort":
            self.canvas.get_tk_widget().destroy()
            self.title_plot.configure(text="BUBBLE SORTING ALGORITHM")
            self.bubble_sort_animation(numbers, len(numbers), self.rects, speed)
            exect_time = timeit.timeit(number=50)
            self.exect_time_value.configure(text=f"{exect_time:.2e}")
        # Add more sorting algorithm cases as needed
        elif sort_type == "Selection Sort":
            self.canvas.get_tk_widget().destroy()
            self.title_plot.configure(text="SELECTION SORTING ALGORITHM")
            self.selection_sort_animation(numbers, len(numbers), self.rects, speed)
            exect_time = timeit.timeit(number=50)
            self.exect_time_value.configure(text=f"{exect_time:.2e}")

        elif sort_type == "Shell Sort":
            self.canvas.get_tk_widget().destroy()
            self.title_plot.configure(text="SHELL SORTING ALGORITHM")
            self.shell_sort_animation(numbers, len(numbers), self.rects, speed)
            exect_time = timeit.timeit(number=50)
            self.exect_time_value.configure(text=f"{exect_time:.2e}")
        
        elif sort_type == 'Insertion Sort' :
            self.canvas.get_tk_widget().destroy()
            self.title_plot.configure(text="INSERTION SORTING ALGORITHM")
            self.insertion_sort_animation(numbers, len(numbers), self.rects, speed)
            exect_time = timeit.timeit(number=50)
            self.exect_time_value.configure(text=f"{exect_time:.2e}")
        


if __name__ == "__main__":


    root = ctk.CTk()
    root.title('Sorting Algoritm')
    root.geometry("1280x720")
    root._set_appearance_mode("dark")
    root.resizable(False,False)
    app = sorting_algoritm(root)

    root.mainloop()