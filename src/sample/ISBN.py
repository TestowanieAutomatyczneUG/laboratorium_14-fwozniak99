class ISBN:
    def validate(self, isbn):
        if type(isbn) != str:
            return False
        numbers = isbn.split('-')
        number = ''.join(numbers)
        if len(number) != 13:
            return False
        sum = 0
        i = 0
        for digit in number:
            if digit not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return False
            elif i % 2 == 0:
                sum += int(digit)
            else:
                sum += 3 * int(digit)
            i = i + 1
        if sum % 10 != 0:
            remainder = sum % 10
        else:
            remainder = 10
        if 10 - remainder == 0:
            return True
        else:
            return False
