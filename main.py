import tkinter as tk
import tkintermapview as tkmap
from PIL import ImageTk, Image

class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        container = tk.Frame(self)
        self.title("Map")
        self.geometry(f"{800}x{600}")
        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Map(container, self)
        self.frames[Map]= frame
        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(Map)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Map(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        map_widget=tkmap.TkinterMapView(self, width=800,height=600, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        map_widget.set_position(48.653103594064795, -2.356723508882328)
        map_widget.set_zoom(15)
        marker_1 = map_widget.set_marker(48.68321841376174, -2.3191363028489853, text="Cap Frehel", command=self.show_image("./photo/1/IMG_1980.jpeg"))

    def show_image(self,path):
        image=ImageTk.PhotoImage(Image.open(path))
        print(f"Opening : {path}")

if __name__ == '__main__':
    app = App()
    app.mainloop()
