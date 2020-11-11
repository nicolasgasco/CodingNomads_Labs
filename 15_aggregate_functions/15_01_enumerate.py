'''
Demonstrate the use of the .enumerate() function.
'''

thingsToDo = ["shopping", "cleaning up", "mopping", "vacuuming", "wiping windows", "dusting"]

print([f"{i}: {n}" for i, n in enumerate(thingsToDo, 1)])