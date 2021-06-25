# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

num = 0
result = 0

while num <= 1000:
    if num % 3 == 0:
        result += num
    num += 1

print(result)