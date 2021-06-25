# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def odd_or_even():
    num = int(input("숫자를 입력하세요. : "))
     
    if num % 2 == 1:
        print("%d는 홀수입니다." % num )
    else :
        print("%d는 짝수입니다." % num )

odd_or_even()     

