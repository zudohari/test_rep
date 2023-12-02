from random import *

print(random()) #0~1
print(int(random()*100))

print(randrange(1,45))   #45 포함 않함
print(randint(1,45))  #45 포함


s1 = 'I am Tom'
s2 = "You are jane"
s3 = """
I'm a teacher.
You are student.
"""
print(s1)
print(s2)
print(s3)


jumin ='720725-1636816'
print("성별 :",jumin[7])
print("년: ",jumin[0:2])  #0부터 2직전까지
print('생년월일 :', jumin[:6]) #처음부터 6직전까지
print(jumin[7 :]) #7부터 끝까지
print(jumin[-7:]) #맨뒤에서 7번째부터 끝까지