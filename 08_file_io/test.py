class MyCustomException(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

try:
    raise (MyCustomException(10))
except MyCustomException as error:
    print('A New Exception occurred:', error.value)