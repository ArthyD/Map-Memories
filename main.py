import tkinter as tk
from tkinter import ttk
import tkintermapview as tkmap
from PIL import ImageTk, Image
class App(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        container = tk.Frame(self)
        self.title("Map")
        self.attributes('-fullscreen', True)
        self.fullScreenState=True
        print(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
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
        self.parent = parent
        self.controller = controller
        map_widget=tkmap.TkinterMapView(self, width=parent.winfo_screenwidth(),height=parent.winfo_screenheight(), corner_radius=0)
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        map_widget.set_position(48.653103594064795, -2.356723508882328)
        map_widget.set_zoom(15)
        marker_1 = map_widget.set_marker(48.68321841376174, -2.3191363028489853, text="Cap Frehel", command=self.show_image)

    def show_image(self, marker):
        photo = Photo(self, self.parent)
        photo.place(in_=self,anchor=tk.CENTER,relx=0.5,rely=0.5)
        print(f"Opening : {marker.text}")

class Photo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        image = Image.open("./photo/1/IMG_1980.jpeg")
        w, h = self.image_size(image)
        photo = ImageTk.PhotoImage(image.resize((w,h)))
        self.photoLabel = tk.Label(self, image=photo)                                          
        self.photoLabel.image = photo
        self.photoLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.photoLabel.pack()

    def image_size(self, image):
        imgw, imgh = image.size
        windw, windh = self.parent.winfo_width(), self.parent.winfo_height()
        if imgw < windw//2 or imgh < windh//2:
            return imgw, imgh 
        else :
            ratiow = imgw//(windw//2)
            ratioh = imgh//(windh//2)
            max_ratio = max(ratiow, ratioh)
            return imgw//max_ratio, imgh//max_ratio




if __name__ == '__main__':
    app = App()
    app.mainloop()
