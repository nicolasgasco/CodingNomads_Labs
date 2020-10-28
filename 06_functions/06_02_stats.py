'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(your_list):
  maxi = max(your_list)
  mini = min(your_list)
  average = sum(your_list) / len(your_list)
  summ = sum(your_list)
  return f"Maximum number is {maxi}; Mininum number is {mini}; Average is {average}: Sum is {summ}"

# call the function below here
print(stats(example_list))
