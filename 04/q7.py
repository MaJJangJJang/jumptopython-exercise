# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
'''
Life is too short
you need java
'''
f1 = open("test.txt", "r")
data = f1.read()
f1.close()

data = data.replace("java","python")

f1 = open("test.txt", "w")
f1.write(data)
f1.close

