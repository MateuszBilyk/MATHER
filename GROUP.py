
# This file defines everything connected to groups

import algos

class _GroupElement:
    def __init__(self, value, addition, multiplication, subtraction, inversion):
        self.__value = value
        self.__addition = addition
        self.__multiplication = multiplication
        self.__subtraction = subtraction
        self.__inversion = inversion

    def __add__(self, other):
        tmp_value = self.__addition(self.__value, other.get_value())
        return _GroupElement(tmp_value, self.__addition, self.__multiplication, self.__subtraction, self.__inversion)

    def __mul__(self, other):
        tmp_value = self.__multiplication(self.__value, other.get_value())
        return _GroupElement(tmp_value, self.__addition, self.__multiplication, self.__subtraction, self.__inversion)

    def __it__(self, other):
        return 1 if self.__value == other.get_value() else 0

    def inv(self):
        tmp = self.__inversion(self.__value)
        return _GroupElement(tmp, self.__addition, self.__multiplication, self.__subtraction, self.__inversion)

    def neq(self):
        tmp = self.__subtraction(self.__value)
        return _GroupElement(tmp, self.__addition, self.__multiplication, self.__subtraction, self.__inversion)

    def get_value(self):
        return self.__value


class Group:
    __elements = []

    def __init__(self, elements_values, addition, multiplication, subtraction, inversion, zero_value, identity_value):
        for e in elements_values:
            self.__elements.append(_GroupElement(e, addition, multiplication, subtraction, inversion))
        self.__addition = addition
        self.__subtraction = subtraction
        self.__multiplication = multiplication
        self.__inversion = inversion
        self.__identity = _GroupElement(identity_value, addition, multiplication, subtraction, inversion)
        self.__zero = _GroupElement(zero_value, addition, multiplication, subtraction, inversion)

    def print_elements(self):
        for i in self.__elements:
            print(i.get_value(), " ")

    def get_elements(self):
        return self.__elements


class ModGroup(Group):

    def __init__(self, p):
        super().__init__(range(0, p), lambda a, b: (a+b) % p, lambda a, b: (a*b) % p, lambda a: (p-a) % p , lambda a: algos.mod_inv(a,p), 1, 0)
