import sys

def fact_polin(num):
    num = int(num)
    def fact(num):
        f =1
        # print (num)
        for i in range (num, 2, -1):
            # print (i)
            f *= i 
        return f
    
    def polin(num):
        s_num = str(num)
        if s_num == s_num[::-1]:
            return f"{num} is palindrome"
        else:
            return f"{num} is not palindrome"
    
    if num < 10:
        # print('here')
        print(f"res of factorial {fact(num)}")
    else:
        print(f"res of polindrome {polin(num)}")
    
if __name__ == '__main__':
    fact_polin(sys.argv[1])