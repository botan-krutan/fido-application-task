# тестове на розробника(-цю) проєкту на Python
# виконані завдання необхідно залити на публічний GitHub репозиторій (разом із інструкцією для запуску в README.md) та у відповідь до кожного завдання надіслати посилання на цей репозиторій із зробленим завданням.
# 7.
# Дано однозв'язний список, що містить n елементів. Потрібно знайти елемент, що знаходиться на позиції [2n/3] - 1, якщо n > 1, інакше повернути null.  


# Наприклад:
#      1) 0 -> 1 -> 2, n = 3, позиція = [2 * 3 / 3] - 1 = 1, елемент = 1     
#      2) 0 -> 1 -> 2 -> 3, n = 4, позиція = [2 * 4 / 3] - 1 = 1, елемент = 1
#      3) 0 -> 1 -> 2 -​> 3 -> 4, n = 5, позиція = [2 * 5 / 3] - 1 = 2, елемент = 2
from random import randint 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class List():
    def __init__(self):
        self.first = None
        self.node = None
    def append(self, data):
        node = Node(data)
        if self.first:
            self.node.next = node    
        else:
            self.first = node
        self.node = node
    def list_all(self):
        current = self.first
        while current:
            print(current.data)
            current = current.next

listy = List()
for i in range(0,randint(0,0)):
    listy.append(i)

listy.list_all()
