num = [12,23,45,21,11]
print (num)
largest = 0
for a_txt in range(len(num)):
    num[a_txt] = int(num[a_txt])
    if num[a_txt] > largest:
        largest = num[a_txt]
print (largest)
        
    
    
