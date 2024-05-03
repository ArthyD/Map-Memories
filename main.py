import tkinter as tk
from tkinter import ttk
import tkintermapview as tkmap
from PIL import ImageTk, Image
import json

class App(tk.Tk):
    
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

        frame = Map(container, self.album.photoList)
        self.frames[Map]= frame
        frame.grid(row=0,column=0,sticky="nsew")
        self.map = frame

        self.show_frame(Map)
        

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Map(tk.Frame):
    def __init__(self, parent, position_list):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.map_widget=tkmap.TkinterMapView(self, width=parent.winfo_screenwidth(),height=parent.winfo_screenheight(), corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.map_widget.set_position(48.653103594064795, -2.356723508882328)
        self.map_widget.set_zoom(15)
        
        for position in position_list:
            self.add_marker(position)

    def show_image(self, marker):
        self.photo = PhotoFrame(self, self.parent, marker.data)
        self.photo.place(in_=self,anchor=tk.CENTER,relx=0.5,rely=0.5)
        print(f"Opening : {marker.text}")

    def add_marker(self, data_json):
        marker = self.map_widget.set_marker(data_json["lat"], data_json["long"], text=data_json["name"], command=self.show_image, data=data_json["photo"])
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
        self.photoList.append(self.get_location("./photo/1/info.json"))
        print(self.photoList)

    def get_location(self, file_to_parse):
        with open(file_to_parse) as file:
            file_contents = file.read()
        parsed_json = json.loads(file_contents)
        return parsed_json

def get_tk_image(image):
    return ImageTk.PhotoImage(image)

if __name__ == '__main__':
    app = App()
    app.mainloop()
