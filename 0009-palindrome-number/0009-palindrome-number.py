class Solution(object):
    def isPalindrome(self, x):
        num=x
        reversed_number=0
        while num>0:
            last_digit=num%10
            reversed_number=(reversed_number*10)+last_digit
            num=num//10

        if x==reversed_number:
            return True
        else:
            return False

    

        