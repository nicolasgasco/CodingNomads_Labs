'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def p_html(inititial_func):
    def wrapper_func(input, tag):
        print(f"<{tag}>{input}</{tag}>")
    return wrapper_func

@p_html
def simple_print(text):
    print(text)

simple_print("This is the first paragraph", "h1")
simple_print("This is the first paragraph", "p")
simple_print("This is the first paragraph", "i")
simple_print("This is the first paragraph", "b")

