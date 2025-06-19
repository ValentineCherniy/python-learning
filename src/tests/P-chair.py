text = input()
# Write your code below
text = text.lower()
counter_P = 0
for char in text:
    if char == 'p':
        counter_P +=1
print(counter_P)