"""
Напишите скрипт который выводит надпись "Привет мир" если не было передано никаких аргументов.
Если 1 из аргументов "--name" то следующий аргумент должен быть имя. В таком случае выведите надпись "Привет {Имя}"
Пример ввода: python file.py kakoitoArgument --name Oleg(Скрипт должен напечатать привет Oleg)
"""
import sys
if len(sys.argv)==1:
    print("Привет мир!")
elif "--name" in sys.argv:
    name_index=sys.argv.index('--name')+1

if name_index<len(sys.argv):
   name=sys.argv[name_index]
   print(f"Привет{name}")
else:
    print('нет имени')

    print('неправельный формат')




