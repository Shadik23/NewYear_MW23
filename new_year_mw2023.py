# -*- coding: utf-8 -*-
"""New_Year_MW2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fvz7fF4VUHO6Ff8EJ39wwm2bpqZRoikU
"""

class Operator:
  
  def __init__(self):
     self._name = None
     self._age = None

  def set_name(self, name):
      self._name = name

  def get_name(self):
      return self._name

  def set_age(self, age):
      self._age = age

  def get_age(self):
      return self._age

  def info(self):
      print("Имя", self._name, "Возраст", self._age)

class Task_Force(Operator):

  def __init__(self):

    super().__init__()
    self._Class = None
    self._nationaly = None

  def set_Class(self, Class):
    self._Class = Class

  def get_Class(self):
    return self._Class

  def set_nationaly(self, nationaly):
    self._nationaly = nationaly

  def get_nationaly(self):
    return self._nationaly

  def info(self):
      super().info()
      print("Роль", self._Class, "Национальность", self._nationaly)

price = Task_Force()
price.set_name("Джонатан Прайс")
price.set_age(37)
price.set_Class("Капитан, Разведчик, Снайпер")
price.set_nationaly("Британец")
price.info()
print("\n")