from fileinput import filename


def cwf():
    filename = input("Enter your File Name: ")
    file = open(filename)
    filelines = file.read()
    for line in filelines:
        print(line)

cwf()