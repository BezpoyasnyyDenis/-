import random

connect = True

while connect == True:
    a = input("Від: ")
    b = input("До: ")
    if b < a:
        print("Друге число менше першого! Введіть правильно!")
        break

    fin = random.randint(int(a),int(b))

    print("Випадкове число: ", int(fin))

input()
