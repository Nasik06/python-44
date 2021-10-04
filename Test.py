# ERROR_MESSAGE = "{} should be positive numer"
 
 
# class Window:
 
#     def __init__(self, x, y, name='unk'):
#         self.square = x * y
 
 
# class Room:
 
#     def __init__(self, x, y, z):
#         self.width = x
#         self.length = y
#         self.height = z
#         self.windows = []
 
#     def add_window(self, x, y):
#         self.windows.append(Window(x, y))
 
#     @property
#     def width(self):
#         return self.__x
 
#     @property
#     def length(self):
#         return self.__y
 
#     @property
#     def height(self):
#         return self.__z
 
#     @width.setter
#     def width(self, x):
#         if x > 0:
#             self.__x = x
#         else:
#             raise ValueError(ERROR_MESSAGE.format('Width'))
 
#     @height.setter
#     def height(self, z):
#         if z > 0:
#             self.__z = z
#         else:
#             raise ValueError(ERROR_MESSAGE.format('Height'))
 
#     @length.setter
#     def length(self, y):
#         if y > 0:
#             self.__y = y
#         else:
#             raise ValueError(ERROR_MESSAGE.format('Length'))
 
#     @property
#     def square(self):
#         return (self.__x + self.__y) * 2 * self.__z
 
#     @property
#     def work_square(self):
#         new_square = self.square
#         for window in self.windows:
#             new_square -= window.square
#         return new_square
 
# class Oboi:
 
#     def __init__(self, height, width, price):
#         self.height = height
#         self.width = width
#         self.price = price
 
#     def calucalate_price(self, room):
#         square = room.work_square
#         return square / (self.height * self.width) * self.price
 
 
# r = Room(10, 20, 3)
# o = Oboi(10, 1, 15)
# r.add_window(3, 2)
# print(r.work_square)
# print(o.calucalate_price(r))


# import abc
# from abc import ABC, abstractclassmethod

# from abc import ABC, abstractmethod
# class ChessPiece(ABC):
# # общий метод, который будут использовать все наследники этого класс
#     def draw(self):
#         print("Drew a chess piece")
#  
# # абстрактный метод, который будет необходимо переопределять для каждого подкласса
# @abstractmethod
#     def move(self):
#         pass



class Donkey:
    def move(self):
        print('Donkey Move')
    
    def weight(self):
        print('100 kg')

class Horse:
    def move(self):
        print('Horse Move')

    def speed(self):
        print('100 miles/h')

class Myl(Donkey, Horse):
    ...

m = Myl()
m.move()
m.weight()