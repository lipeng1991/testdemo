# coding: utf-8
""" 
@author: lipeng
@file: 0093_observer_pattern.py 
@time: 2019/12/23
"""
from abc import ABCMeta, abstractmethod

"""
观察者模式
观察者模式定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，
它的所有依赖着都会收到通知并自动更新
"""


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, o: Observer):
        pass

    @abstractmethod
    def remove_observer(self, o: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class DisplayEment(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers = set()
        self.temp = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        if o in self.observers:
            self.observers.remove(o)

    def notify_observers(self):
        pass