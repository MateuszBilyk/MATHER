import math

"""
    Hilbert_Space
        *init
            --scalar_product should satisfy scalar product axioms
        *__norm norm of this Hilbert Space generated from scalar_product 
"""


class HilbertSpace:
    def __init__(self, scalar_product):
        self.__scalar_product = scalar_product
        self.__norm = lambda a: math.sqrt(scalar_product(a, a))
