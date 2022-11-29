import GROUP

bites = GROUP.ModGroup(3)

bites.print_elements()

tmp_elem = bites.get_elements()

print((tmp_elem[2]*tmp_elem[2]).get_value())

print((tmp_elem[0]*tmp_elem[2]).get_value())

print(tmp_elem[2].inv().get_value())

print(tmp_elem[1].inv().get_value())

print(tmp_elem[1].neq().get_value())
