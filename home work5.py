immutable_var = 10, "apple", True, 3.14
print(immutable_var)
# В отличие от списков, кортежи неизменяемы.
# Это значит, что элементы кортежа нельзя изменять после добавления в кортеж.
mutable_list = ([10, "apple", "True", 3.14])
#print(mutable_list)
mutable_list[0] = 5, [3.14] * 2
print(mutable_list)



