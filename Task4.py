"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import threading
import time

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace('ids', 'id')

    with open(file_path, 'w') as file:
        file.write(content)

folder_path = "files"
file_list = os.listdir(folder_path)
threads = []

start_time = time.time()

for file in file_list:
    file_path = os.path.join(folder_path, file)
    thread = threading.Thread(target=process_file, args=(file_path,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Программа выполнена за {end_time - start_time} секунд")
