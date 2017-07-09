num = input('please enter number')
num = num.split(' ')
number_exists = False
searchNumber = int(input('please enter the number you want to seach'))
for f_n in range(len(num)):
    num[f_n] =  int(num[f_n])
    if num[f_n] == searchNumber:
        print(num[f_n])
        number_exists = True
        break 
if not number_exists:
    print('wrong number')    
