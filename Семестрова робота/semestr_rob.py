import os
import json
import csv
import sys
from PIL import Image
        
        
def menu():
    while (True):
         print("        МЕНЮ        ")
         x = int(input("Виберіть режим роботи: \n [1] - Вивести файли \n [2] - Завершити роботу \n"))
         mode = ' '
         if x == 1:
             start()
         elif x == 2:
             close()
         else:
             print("Немає такого варіанту")
             
            
consol = lambda : os.system('cls')
consol_command = "table.txt"


def console(consol_command):
     consol()
     file = open(consol_command, "r")
     reader = csv.reader(file, delimiter="\t")
     for row in reader:
        print(row)
     file.close()
     
            
def start():
     consol()
     v = int(input("Оберіть формат файлу: \n [1] - Таблиця  \n [2] - Текстовий файл \n [3] - Файл у форматі JSON \n [4] - Excel \n [5] - Графік\n"))
     
     if v == 1:
         consol()
         console(consol_command)
         Return()
         
     elif v == 2:
         consol()
         os.system('start notepad.exe table.txt')
         
     elif v == 3:
         consol()
         os.system('start notepad.exe table.json')
         
     elif v == 4:
         os.system('start excel.exe tables.xlsx')
         open()
         
     elif v == 5:
         consol()
         photo = Image.open('graphic.png')
         photo.show()
         
     else:
         print("Немає такого варіанту")
     
        
def Return():
     p = int(input("Натисніть: \n [1] Головне меню \n [2] Вийти \n"))
     if p == 1:
         consol()
         menu()
     elif p == 2:
         close()
        
         
def close():
     sys.exit()
    
    
menu()


