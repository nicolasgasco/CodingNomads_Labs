word = 'banana'

def count_letter(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)


def count_double(word, letter):
    count = 0
    for l in word:
        if l == l + 1:
            print("Ciao")

count_double("Mississippi", "s")
