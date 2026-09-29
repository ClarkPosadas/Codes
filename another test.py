numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += 'x'
    print(output)

#Due to the beauty of Python you can simply write it as
numbers = [5,2,5,2,2]
for x_count in numbers:
    print(x_count * 'x')


