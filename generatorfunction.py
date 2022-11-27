def generator_file():
    with open('test.txt', 'r') as file:
        yield file.readline()
        yield file.readline()
        yield file.readline()





if __name__ == '__main__':
    for line in generator_file():
        print(line)

