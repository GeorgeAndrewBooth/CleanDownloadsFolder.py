import os 
import time 

time_now = time.time() 
Download_path = os.path.join(os.path.expanduser("~"), "Downloads") 
week = 7 * 86400

for filename in os.listdir(Download_path):
    full_path = os.path.join(Download_path, filename)
    if os.path.isfile(full_path): 
        file_age = os.path.getmtime(full_path)

        if(time_now - file_age) > week: 
            os.remove(full_path) 
            print(f"Deleted: {full_path}")
