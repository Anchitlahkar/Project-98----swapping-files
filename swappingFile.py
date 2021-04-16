with open('sample1.txt', 'r') as a:
    data_a = a.read()

with open('sample2.txt', 'r') as b:
    data_b = b.read()

print("Text in file 1:\t "+data_a)
print("Text in file 2:\t "+data_b)


with open('sample1.txt', 'w') as file1:
    file1.write(data_b)

with open('sample2.txt', 'w') as file2:
    file2.write(data_a)

print("\n\nUpdated Text in file 1:\t "+data_b)
print("Updated Text in file 2:\t "+data_a)