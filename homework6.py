#Словари  множества



my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Katy'))
my_dict['Koly'] = 1991
my_dict['Cat'] = 1995
print(my_dict)
my_dict.pop('Egor')
print(my_dict)

#множества
my_set =  {1,2,1,'груша', 42.314}
print(my_set)
my_set.add(10)
new_set = my_set.add((5, 6, 1.6))
print(my_set,new_set )