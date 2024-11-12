my_dict = {'Ivan':85555555555,'Gor':86666666666,'Timur':87777777777}
print(my_dict)
print(my_dict.get('Timur'))
print(my_dict.get('Andrey'))
my_dict['Anton'] = 84444444444
my_dict['Masha'] = 82222222222
print(my_dict)
s = my_dict.pop('Ivan')
print(s)
print(my_dict)


my_set = {1,1,1,2,2,'Hello','Hello',(4,5,6),(4,5,6)}
print(my_set)
my_set.add(7)
my_set.add(8)
print(my_set)
my_set.remove((4,5,6))
print(my_set)