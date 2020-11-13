
'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''

def p_html(inititial_func):
    def wrapper_func(input):
        print(f"<p>{input}</p>")
    return wrapper_func

@p_html
def simple_print(text):
    print(text)

simple_print("This is the first paragraph")




