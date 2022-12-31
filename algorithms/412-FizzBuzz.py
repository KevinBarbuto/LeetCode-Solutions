class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        # Define initial array
        fbarray = []
        print(fbarray)
        
        # For loop to construct array
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                fbarray.append("FizzBuzz")
            elif i % 3 == 0:
                fbarray.append("Fizz")
            elif i % 5 == 0:
                fbarray.append("Buzz")
            else:
                fbarray.append(str(i))
        return fbarray
