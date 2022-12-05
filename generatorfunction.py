def generator_file():
    with open('test.txt', 'r') as file:
        for line in file:
            yield line




if __name__ == '__main__':
    for line in generator_file():
        print(line)

