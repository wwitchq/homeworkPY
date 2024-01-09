"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""
import concurrent.futures
import queue


def print_divisors(number):
    divisors = [x for x in range(1, number + 1) if number % x == 0]
    print(f"Делители числа {number}: {divisors}")


numbers_queue = queue.Queue()
for i in range(1, 21):
    numbers_queue.put(i)


with concurrent.futures.ThreadPoolExecutor() as executor:
    while not numbers_queue.empty():
        number = numbers_queue.get()
        executor.submit(print_divisors, number)
