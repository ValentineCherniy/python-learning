lst = input().split(",")
# Write your code below
if len(lst) % 2 ==0:
    middle_item = int(len(lst) / 2)
   # print(middle_item)
    print(lst[middle_item-1:middle_item + 1])
else:
    middle_item = int(len(lst) / 2+1)
   #print(middle_item)
    print(lst[middle_item - 2:middle_item + 1])
