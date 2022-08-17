## List files in a directory
import os
my_files = [f.name for f in os.scandir('C:/Users/MJimenezMorfin/Downloads') if f. is_file()]
print(my_files)


## List files in a directory, using as entries methond 
import os 

import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:/Users/MJimenezMorfin/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)




