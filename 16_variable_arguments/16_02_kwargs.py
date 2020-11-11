'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def my_dict(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

my_dict(car1="Ferrari", car2="Maserati", car3="Lamborghini", car4="Bugatti")