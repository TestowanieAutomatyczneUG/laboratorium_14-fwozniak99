class FizzBuzz:
    def game(self, num):
        if ((num % 5) == 0) and ((num % 3) != 0):
            return "Buzz"
        elif ((num % 5) != 0) and ((num % 3) == 0):
            return "Fizz"
        elif (num % 15) == 0:
            return "FizzBuzz"
        elif num % 5 != 0 and num % 3 != 0 and type(num) == int:
            return str(num)
        else:
            raise Exception("Error in FizzBuzz")
