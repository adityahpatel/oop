# Recursion means a function calls itself in its own definition.
# e.g. n factorial of fibonacci or Binary Search Tree or string reversal
# Recursion can be employed when a function is called again and again in a particular sequence.

def reverse_string_recursive_approach(s:str) -> str:
      if len(s) > 1:
            reverse = s[-1] + reverse_string_recursive_approach(s[:-1])
      else:
            reverse = s
      return reverse


def sum_recursive_approach(x:int):
      total = 0
      if x !=1:
            total = x + sum_recursive_approach(x-1)
      else:
            total = total + 1
      return total

def fibonacci(n:int) -> None:
      """
      Just prints fibonacci sequence upto n number of terms e.g. 0,1,1,2,3,5,8,13...
      When n=2, it only prints 0 and 1
      When n=3, it prints 0,1,1
      When n=4, it prints 0,1,1,2
      Logic: Fib(4) = Fib(3) + Fib(2) and Fib(0) = 0, Fib(1) = 1, Fib(2) = 1 
      """
      if n == 0:
            return 0
      elif n == 1 or n == 2:
            return 1
      return fibonacci(n-1) + fibonacci(n-2)



if __name__ == "__main__":
      print(sum_recursive_approach(4))
      print(reverse_string_recursive_approach('california'))
      assert fibonacci(6) == 8



