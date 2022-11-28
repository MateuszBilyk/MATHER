
class _GroupElement:
    def __init__(self, value, multiplication, inversion):
        self.__value = value
        self.__multiplication = multiplication
        self.__inversion = inversion

    def __mul__(self, other):
        tmp_value = self.__multiplication(self.__value, other.get_value())
        return _GroupElement(tmp_value, self.__multiplication, self.__inversion)

    def inv(self):
        tmp = self.__inversion(self.__value)
        return _GroupElement(tmp, self.__multiplication, self.__inversion)

    def get_value(self):
        return self.__value


class Group:
    __elements = []

    def __init__(self, multiplication, inversion, identity_value):
        self.__multiplication = multiplication
        self.__inversion = inversion
        self.__identity = _GroupElement(identity_value, multiplication, inversion)
        self.__elements.append(self.__identity)

    def new_element(self, value):
        self.__elements.append(_GroupElement(value, self.__multiplication, self.__inversion))

    def print_elements(self):
        for i in self.__elements:
            print(i.get_value(), " ")

    def get_elements(self):
        return self.__elements


# EXAMPLES

mod3group = Group(lambda a, b: (a*b) % 3, lambda a: a, 1)

mod3group.print_elements()

mod3group.new_element(2)

mod3group.print_elements()

tmp = mod3group.get_elements()

mod3group.new_element((tmp[1]*tmp[0]).get_value())

mod3group.print_elements()

tmp = mod3group.get_elements()

print((tmp[1]*tmp[2]).get_value())

print(tmp[1].inv().get_value())

