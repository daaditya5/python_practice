num = raw_input()
# print num[1]
num = num.split(' ')
# print num
# for a_num in num:
#     int(a_num)
#     print type(a_num)
for a_trk in range(len(num)):
    num[a_trk] = int(num[a_trk])
# print num
smallest = 100
for a_num in num:
    if a_num < smallest:
        smallest = a_num
print smallest
# a = 2
