# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for x in range(0, n + 1, 1):
    sum += x
  return print(sum)

sum_to(6)  # returns 21
sum_to(10) # returns 55
