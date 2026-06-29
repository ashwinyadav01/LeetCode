class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1 
        digit_sum = 0
        while n > 0:
            digit = n % 10
            product = product * digit
            digit_sum = digit_sum + digit 
            n //=10
        return product - digit_sum