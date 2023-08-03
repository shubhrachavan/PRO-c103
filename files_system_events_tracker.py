import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir='c:\Users\Dell\Downloads'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("Hey, {event.src_path}, is created!")

    def on_modified(self,event):
        print("{event.src_path} is modified!")

    def on_moved(self,event):
        print("{event.src_path} is moved to another folder!")

    def on_deleted(self, event):
        print("Opps,someone delted {event.src_path}!")

event_handler = FileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()    
