from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    received: int

@dataclass
class MoveOfMainAssets:
    name: str
    code: int
    remainder: int
    received: int

type_array = []
type_array.append(TypeOfMainAssets(10, "План розрахунків бухгалтерського обліку підприємств", "40"))
type_array.append(TypeOfMainAssets(20, "ППП УЗПИКС", "900"))
type_array.append(TypeOfMainAssets(30, "ППП УТЕП", "900"))
type_array.append(TypeOfMainAssets(40, "ППП УОС", "600"))
type_array.append(TypeOfMainAssets(50, "ППП УФРО", "1245"))
type_array.append(TypeOfMainAssets(60, "АРМ бухгалтера матеріально-технічного відділу", "500"))
type_array.append(TypeOfMainAssets(70, "АРМ бухгалтера фінансового відділу", "500"))
type_array.append(TypeOfMainAssets(80, "ППП Облік договорів", "150"))

move_array = []
move_array.append(MoveOfMainAssets("КНТЕУ", 202, 10, 10))
move_array.append(MoveOfMainAssets("КНЕУ", 203, 20, 10))
move_array.append(MoveOfMainAssets("КНУ", 205, 30, 5))
move_array.append(MoveOfMainAssets("КНТЕУ", 207, 40, 10))
move_array.append(MoveOfMainAssets("КНЕУ", 211, 20, 5))
move_array.append(MoveOfMainAssets("КНУ", 204, 10, 5))
move_array.append(MoveOfMainAssets("КНТЕУ", 206, 30, 5))
move_array.append(MoveOfMainAssets("КНЕУ", 210, 50, 3))
move_array.append(MoveOfMainAssets("КНУ", 212, 60, 4))
move_array.append(MoveOfMainAssets("КНтЕУ", 213, 70, 5))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Замовлення на літературу"
    with names and values'''

    print("Клієнт: {name}, Номер заказ: {code}, Код товара: {remainder}, Кількість: {received}"
          .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                  received=moveOfMainAssets.received)) 
for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник товарів"
    with names and values'''

    print("Код товару: {code}, Найменування товару: {name}, Ціна:{received}"
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name, received=typeOfMainAssets.received))

for data in type_array:
    printTypeOfMainAssets(data)