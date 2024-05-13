import tkinter as tk
from tkinter import ttk
import tkintermapview as tkmap
from PIL import ImageTk, Image
import os
from . import db, script_directory
from .models import ImageServer
from sqlalchemy import create_engine, text


class IHM(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        container = tk.Frame(self)
        self.album=PhotoAlbum()
        self.title("Map")
        self.attributes('-fullscreen', True)
        self.fullScreenState=True
        print(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Map(container, self.album.photoList, os.path.dirname("/Volumes/Crucial X6/tiles.db"))
        self.frames[Map]= frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.map = frame

        self.show_frame(Map)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Map(tk.Frame):
    def __init__(self, parent, position_list, database_path):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.map_widget=tkmap.TkinterMapView(self, width=parent.winfo_screenwidth(),height=parent.winfo_screenheight(), corner_radius=0)
        #self.map_widget=tkmap.TkinterMapView(self, width=parent.winfo_screenwidth(),height=parent.winfo_screenheight(), corner_radius=0, use_database_only=True, database_path=database_path)
        #self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga")
    
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.map_widget.set_position(48.653103594064795, -2.356723508882328)
        self.map_widget.set_zoom(15)
        
        for position in position_list:
            self.add_marker(position)

    def show_image(self, marker):
        self.photo = PhotoFrame(self, self.parent, marker.data)
        self.photo.place(in_=self,anchor=tk.CENTER,relx=0.5,rely=0.5)
        print(f"Opening : {marker.text} with data : {marker.data}")

    def add_marker(self, position):
        print(position)
        marker = self.map_widget.set_marker(position['lat'], position['long'], position['name'], command=self.show_image, data=position['path'])
        return marker

class PhotoFrame(tk.Frame):
    def __init__(self, parent, controller, path):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.image = Photo(path)
        self.photoLabel = self.image.get_photo_label(self.parent, self, 2)                                       
        self.photoLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.photoLabel.bind("<Button-1>", self.photo_clicked)
        self.photoLabel.pack()

    def photo_clicked(self, event):
        print("Photo clicked")
        self.destroy()


class Photo():
    def __init__(self, path):
        self.image = Image.open(path)

    def resize_image(self, canvas_w, canvas_h, coeff):
        print(canvas_w)
        img_w, img_h = self.image.size
        if img_w < canvas_w//coeff or img_h < canvas_h:
            return self.image
        else:
            ratio_w = img_w//(canvas_w//coeff)
            ratio_h = img_h//(canvas_h//coeff)
            max_ratio = max(ratio_w, ratio_h)
            print(f"{ratio_w},{ratio_h},{max_ratio}")
            return self.image.resize((img_w//max_ratio,img_h//max_ratio))
    
    def get_photo_label(self, window, parent, coeff):
        image_resized = self.resize_image(window.winfo_width(), window.winfo_height(), coeff)
        tk_image = get_tk_image(image_resized)
        label = tk.Label(parent, image=tk_image)
        label.image = tk_image
        return label

class PhotoAlbum():
    def __init__(self):
        print("Album Creation")
        self.photoList = [] 
        database_path = os.path.join(script_directory, "../instance/database.db")
        engine = create_engine('sqlite:///'+database_path)

        with engine.connect() as connection:
            result = connection.execute(text("select * from image_server"))
            for row in result:
                image = dict(name=row.name, lat=row.lat, long=row.long, comment=row.comment, path=row.path)
                print(image)
                self.photoList.append(image)
        

def get_tk_image(image):
    return ImageTk.PhotoImage(image)