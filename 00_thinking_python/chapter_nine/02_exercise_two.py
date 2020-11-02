"""
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.

In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of words in the list that have no “e”.
"""

def has_no_e(file, letter):
    """Function used to return True if a given word doesn't have the letter e in it."""
    with open(file, "r") as fin:
        words = []
        for word in fin.readlines():
            if word.find(letter) ==  -1:
                word = word.strip()
                words.append(word)
        return words

def percentile(num1, num2):
    percentage = (num1 * 100) / num2
    return percentage

def compute_difference(file, letter):
    """Function to computer the percentage of words containing {letter} in relation to total"""
    with open(file, "r") as fin:
        less_letter = []
        total = []
        for word in fin.readlines():
            word = word.strip()
            if word.find(letter) == -1:
                total.append(word)
                less_letter.append(word)
            else:
                total.append(word)

        total_count = len(total)
        less_letter_count = len(less_letter)
        return int(percentile(less_letter_count, total_count))


has_no_e("words.txt", "e")

print(compute_difference("words.txt", "e"))