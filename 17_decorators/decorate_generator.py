""""

Write a decorator function that wraps text passed to it in a specified HTML tag. The user should be able to decide which tag to use.

"""

def p_html(inititial_func):
    def wrapper_func(input, tag):
        print(f"<{tag}>{input}</{tag}>")
    return wrapper_func

@p_html
def simple_print(text):
    print(text)

text = input("Please insert here the text that you want to wrap: ")
tag = input("Please enter here the tag that you want to use (letter only): ")

simple_print(text, tag)
