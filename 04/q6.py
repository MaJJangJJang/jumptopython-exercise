# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

wirte_user = input("내용을 입력하세요. : ")
f1 = open("write_textfile.txt", "a")
f1.write(wirte_user)
f1.write("\n")
f1.close()

