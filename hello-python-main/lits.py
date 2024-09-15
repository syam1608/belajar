data_range = range(0,10,2)#star,stop,step
print(data_range)
data_list = list (data_range)
print(data_list)
list_pakefor = [i for i in range(0,10)if i != 5]
print(list_pakefor)
list_pakefor = [i for i in range(0,10)if i %2 == 0]
print(list_pakefor)
list_pakefor = [i**2 for i in range(0,10)if i %2 != 0]
print(list_pakefor)
