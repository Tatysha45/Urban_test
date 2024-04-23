import os #Методы из библиотеки os, модуль os
print(os.name) #узнать имя текущей ОС
print(os.environ) #Получить сведения, которые касаются конфигурации компьютера,  словарь с переменными окружения
print(os.getenv("TMP")) #доступ к различным переменным среды
print(os.getcwd()) #путь к рабочей директории
# os.chdir(r"D:\folder") #переход к новой рабочей директории(уже существующей)
print(os.path.exists("D:/test.txt")) #проверка существования объекта(файла), пути
print(os.path.isfile("D:/test.txt")) #Проверить, является ли определенный объект файлом
print(os.path.isdir("D:/test.txt"))  #проверка объекта на принадлежность к классу директорий
# os.mkdir(r"D:\folder") #созданиеновой папки
# os.makedirs(r"D:\folder\first\second\third") #создание нескольких папок (генерация целой цепочки папок из
     #folder, first, second и third.)
print(os.path)
# os.remove(r"D:\test.txt") #удалить ненужный файл
# os.rmdir(r"D:\folder") #удалить из памяти папку
# os.removedirs(r"D:\folder\first\second\third") #быстрое удаление множествапустых папок
# os.startfile(r"D:\test.txt") #запуск на исполнение файлов
print(os.path.basename("D:/test.txt")) #преобразование пути test.txt в простое имя файла.
print(os.path.dirname("D:/folder/test.txt")) #возвращает путь к заданному документу в строковом представлении
#print(os.path.getsize("D:\\test.txt")) #определить размер документа или папки и для измерения объема директорий.
#os.rename(r"D:\folder", r"D:\catalog") #смена названия для любого файла или же каталога (метод может
     # генерировать исключение, если по указанному пути нет файла.)
#os.renames(r"D:\folder\first\second", r"D:\catalog\one\two") #переименование несколько папок сразу, только
     # если все они находятся в одной иерархической цепочке
#print(os.listdir(r"D:\folder")) #Проверить наличие в каталоге определенных объектов, получить информацию о файлах
     # и папках в виде списка
for root, directories, files in os.walk(r"D:\folder"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file) # получить доступ к названиям и путям всех подпапок и файлов, относящихся к заданному каталогу
#print(os.stat(r"D:\test.txt")) #Вывести на экран или в любое другое место основные сведения об объекте
print(os.path.split(r"D:\folder\test.txt")) #разъединить путь к файлу и имя файла в различные строки.
print(os.path.join(r"D:\folder", "test.txt")) #соединить путь к документу с его названием
