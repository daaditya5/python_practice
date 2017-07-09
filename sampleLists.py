names=['sukesh','goutham','srikanth']
ages=[26,28,29]
print(names+ages)
names.append('ravi')
print(names)
ages.append('23')
print(ages)
names.extend(ages)
print(names)
names.remove('23')
print(names)
ages.extend(names)
print(ages)

# to add list use symbol +
# to add list save to first variable use firstVariable.extend(sencondVariable)
# to add single value either string or interger use variable.append(value) value is anytype ' '," ",""" """, or just value
# to remove a value from list use variable.remove(value), value should be similar in the list string or interger
# position of values start from 0,1,2,...... but number of values I mean 1+2+3+.....
# position of values in negetive also but start from end .....,-3,-2,-1

print(names[-1])
print(ages[0])
print(names[-7])
print(ages[5])


print(ages, names)
print(ages)






