###ИЗМЕНЯЕМОСТЬ ТИПОВ ДАННЫХ###

# list, dict, set - изменяемые типы данных
# str, int, turple, frozenset  - НЕизменяемые типы данных

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = l1

print(id(l1))
print(id(l2))
print("-" * 100)


l2.insert(2,"A")
print(l2)
