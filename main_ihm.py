from map_project.ihm import IHM
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

ihm = IHM()
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
 
        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
            ihm.reload()
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)
            ihm.reload()

        elif event.event_type == 'deleted':
            print("Watchdog received deleted event - % s." % event.src_path)
            ihm.reload()

if __name__ == '__main__':
    event_handler = Handler()
    folder = "./map_project/upload"
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=True)
 
    # Start the observer
    observer.start()
    
    ihm.mainloop()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    
    
    
