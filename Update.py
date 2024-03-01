import urllib.request
from bs4 import BeautifulSoup
import os
import urllib.parse
import zipfile
import io
import traceback
import tkinter as tk
from tkinter import ttk
import threading

def download_and_extract_zip(source_folder_address, saving_directory, progress_bar, window):
    try:
        if not source_folder_address.endswith('/'):
            source_folder_address += '/'

        response = urllib.request.urlopen(source_folder_address)
        html_content = response.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            file_url = link.get('href')
            if not file_url or file_url.endswith("/") or file_url.startswith("../") or '?' in file_url or not file_url.endswith('.zip'):
                continue

            file_url = urllib.parse.quote(urllib.parse.unquote(file_url))
            full_file_url = urllib.parse.urljoin(source_folder_address, file_url)

            with urllib.request.urlopen(full_file_url) as response:
                file_size = int(response.getheader('Content-Length'))
                downloaded = 0
                zip_data = io.BytesIO()

                while True:
                    buffer = response.read(1024)
                    if not buffer:
                        break
                    zip_data.write(buffer)
                    downloaded += len(buffer)
                    percent_completed = downloaded / file_size * 100
                    progress_bar['value'] = percent_completed
                    window.update_idletasks()
            #Extract zip files 
            zip_data.seek(0)
            with zipfile.ZipFile(zip_data, 'r') as opened_zip:
                opened_zip.extractall(saving_directory)

    except Exception as e:
        print(f"Error encountered: {str(e)}")
        traceback.print_exc()

    finally:
        # Close the window after download completes
        window.destroy()

def main():
    window = tk.Tk()
    window.title("Download MuUniverse Files")

    progress_bar = ttk.Progressbar(window, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack(pady=20)
    #Here write your host address example: http://23.45.67.89/update 
    source_folder_address = "YOUR HOST ADDRESS"
    saving_directory = os.path.dirname(os.path.realpath(__file__))

    download_thread = threading.Thread(target=download_and_extract_zip, args=(source_folder_address, saving_directory, progress_bar, window))
    download_thread.start()

    window.mainloop()

if __name__ == "__main__":
    main()
