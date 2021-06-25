# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. 
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def average():
    howmany_num = int(input("몇개의 숫자를 넣겠습니까? : "))
    num = []
    
    for i in range(0,howmany_num):
        number = int(input("숫자를 입력해주세요. : "))
        num.append(number)

    average = int(sum(num)) / howmany_num
    print("평균값은 %s 입니다" % average)

average()
        
    