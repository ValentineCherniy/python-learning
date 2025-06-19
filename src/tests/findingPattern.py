def find_occurrences(text, pattern):
    is_pattern_exiting = False
    counter = 0
    position_list = []
    for i in range(len(text)):
        checking = text[i:i+len(pattern)]
        if checking == pattern:
            position_list.append(i)
            counter += 1
            is_pattern_exiting = True
    output_list = (is_pattern_exiting, counter, position_list)
    return output_list

text = input()
pattern = input()

result = find_occurrences(text, pattern)
print(result)