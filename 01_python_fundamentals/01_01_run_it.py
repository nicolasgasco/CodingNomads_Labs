'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses? I get different errors, mostly unexpected EOL
        * How helpful are the error messages? Pretty helpful if you know what they mean
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year. 31536000

'''

# def right_justify(s):
#    print(" "*(70-len(s))+ s)
# right_justify("Ciao bella mia")


'''

def do_twice(f, val):
    f(val)
    f(val)

def print_spam(val):
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, val):
   do_twice(f, val)
   do_twice(f, val)

do_four(print_spam, "Ciao")

'''


def titlecase(text):
    titlecase =   []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return " ".join(titlecase)

user_input = input("Enter your sentence (type exit to quit): ")
print(titlecase(user_input))

while user_input.lower() != "exit":
    user_input = input("Enter your sentence (type exit to quit): ")
    crash_blossom = titlecase(user_input)
    print(crash_blossom)
