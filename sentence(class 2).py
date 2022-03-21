from posixpath import split

def sentence():
    now = input("Enter your File Name: ")
    hello = 0
    clause = open(now , "r")
    for phrase in clause:
        subclause = phrase.split()
        hello = hello + len(subclause)

    print("Number of words: ")
    print(hello)

sentence()
