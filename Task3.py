"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""

import concurrent.futures
import queue
import os


def add_file_paths_to_queue(file_path, queue):
    with open(file_path, 'r') as file:
        names = file.readlines()
        for name in names:
            cleaned_name = name.strip()
            path = os.path.join('generated_files', cleaned_name + '.txt')
            queue.put(path)


def create_files_from_queue(queue):
    while not queue.empty():
        file_path = queue.get()
        with open(file_path, 'w') as file:
            file.write("This file was generated for: " + os.path.basename(file_path))


file_paths_queue = queue.Queue()


add_file_paths_to_queue('Names.txt', file_paths_queue)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(create_files_from_queue, file_paths_queue)
