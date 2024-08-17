import os
import shutil
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file types and target directories
file_types = {
    ".jpeg": "Pictures",
    ".png": "Pictures",
    ".jpg": "Pictures",
    ".gif": "Pictures",
    ".svg": "Pictures",
    ".mp3": "Sound",
    ".wav": "Sound",
    ".m4a": "Sound",
    ".exe": "Setups",
    ".lnk": "Setups",
    ".c": "Code",
    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".php": "Code",
    ".torrent": "Torrents"
}

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_name)[1]
            dest_dir = file_types.get(file_ext)
            if not dest_dir:
                dest_dir = 'Unsorted'
            dest_path = os.path.join(os.path.expanduser('DOWNLOADS_PATH'), dest_dir)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            dest_file_path = os.path.join(dest_path, file_name)
            
            # Handle file name conflicts
            base, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.exists(dest_file_path):
                dest_file_path = os.path.join(dest_path, f"{base}_{counter}{ext}")
                counter += 1
            try:
                shutil.move(file_path, dest_file_path)
                logging.info(f'Moved {file_name} to {dest_dir}')
            except Exception as e:
                logging.error(f'Error moving {file_name}: {e}')
if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.path.expanduser('DOWNLOADS_PATH'), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()