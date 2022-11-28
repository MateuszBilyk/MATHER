import math

"""
    Hilbert_Space
        *init
            --zero should be the zero element of the Hilbert Space
            --elements should be the function which gives one when element is in Hilbert space
                should have the property elements(x) and elements(y) implies elements(ax+by)
            --scalar_product should satisfy scalar product axioms
        *__norm norm of this Hilbert Space generated from scalar_product 
"""


class HilbertSpace:
    def __init__(self, zero, element, scalar_product):
        self.__zero = zero
        self.__element = element
        self.__scalar_product = scalar_product
        self.__norm = lambda a: math.sqrt(scalar_product(a, a))
