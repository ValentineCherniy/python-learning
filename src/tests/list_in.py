lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
lst3 = []
for i in range(len(lst1)):
    if lst1[i] not in lst2:
        lst3.append(lst1[i])
print(lst3)