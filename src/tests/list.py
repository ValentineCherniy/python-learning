lst = list(map(int, input().split(",")))
# Write your code below
lst_out = []
for index, num in enumerate (lst):
    # print (num)
    # print(index)
    if num <50 or num % 5 ==0:
        lst_out.append(index)
print(lst_out)