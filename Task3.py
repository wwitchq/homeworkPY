"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""
import threading
import time

def demon_function():
    while True:
        time.sleep(3)
        print("Вводите быстрее")

demon_thread = threading.Thread(target=demon_function)
demon_thread.daemon = True
demon_thread.start()

bomb_code = input("Введите код от бомбы: ")

if bomb_code != "12345":
    print("Вы взорвались")
else:
    print("Бомба разминирована")
