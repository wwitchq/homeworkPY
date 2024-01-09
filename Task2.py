"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""
import threading
import time

def reminder():
    remind_text = input("Чем вас напомнить? ")
    delay = int(input("Через сколько секунд напомнить? "))
    time.sleep(delay)
    print(f"Напоминание: {remind_text}")

reminder_thread = threading.Thread(target=reminder)
reminder_thread.start()

time.sleep(10)

print("Программа завершается")
