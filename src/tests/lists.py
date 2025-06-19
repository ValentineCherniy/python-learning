lst = input().split(",")
new_lst = []
for item in lst:
    if len(item) > 5:
        new_lst.append(item)
print(new_lst)
