#-*-coding:utf-8 -*_
# chapter 02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본 출력
print('python start!')
print("chanmin!")
print('''chanmin''')
print("""chanmin!""")

# separator 옵션 (띄어쓰기 공간에 () 넣기 )
print('p', 'y', 't', 'h', 'o', 'n', sep='-')
print('python', 'google.com', sep='@')
print('010', '6569', '1234', sep='-')

# end 옵션 (프린트문 뒤에 무엇을 넣을건지)
print('welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()
#file 옵션 (프린트되는 것을 파일로 만들 수 있음)
import sys
print('Learn Python', file=sys.stdout) #sys.stdout는 콘솔 아웃을 의미(밑에 나옴)

# format 사용(d (정수), s (문자열), f (실수) 등..)
print('%s %s' % ('one', 'two')) # 첫 번째 s는 첫 번째 'one'/두 번째 s는 두 번째 'two'가 들어감. %는 연결시켜주는 개념
print('{} {}'.format('one', 'two')) #format함수가 {}안의 형식을 유연하게 처리해줌 (문자열이든 숫자가 들어가든 상관없음)
print('{1} {0}'.format('one', 'two')) #컴퓨터는 0이 시작. 그렇기 때문에 두 번째인 two가 앞으로 출력됨.

# %s(s는 생략 가능함)  
print('%10s' % 'nice') # 10= 10개의 자릿수 , 남는 자릿 수는 왼쪽에 공백으로 프린트
print('{:>10}' .format('nice')) # 10자리 수를 확보하고 Nice를 출력해줘 <>는 방향을 말함. <는 왼쪽에 공란, >는 오른쪽에 공란

print('%-10s' % 'nice') # 음수 일 때는 오른쪽을 공백
print('{:10}' .format('nice')) # <> 부등호가 없으면 오른쪽을 공백(기본값)

print('{:_>10}' .format('nice')) # 원하는 기호를 부등호 옆에 붙히면 공란에 해당 기호가 들어감
print('{:^10}' .format('nice')) # 부등호 대신 ^ 은 중간 정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # .을 붙혀야 5자리에서 절삭을 함 (내가 원하는 자릿수 만큼 출력)
print('%5s' % ('pythonstudy')) # .을 안붙히면 전부 다 출력됨

print('{:10.5}'.format('pythonstudy')) # 총 10개 자리를 확보하는데 5개만 나타내라

# %d

print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42)) # 4개의 공간을 만들어라 , 하지만 4개가 넘어가도 그대로 출력됨
print('{:4d}'.format(42)) # s와는 다르게 d앞에 숫자를 붙혀줘야함 

# %f

print('%2.8f' % (3.14124125)) # 정수 부분은 2자리 나오고, 소수부분은 8자리 나와라
print('{:f}'.format(3.14125125)) # 기본값은 소수 6자리 까지 인듯
print('%06.2f' %(3.141592653589793)) # 총 6자리 나오고, 소수는 2번째까지 나와라. 남은 공간은 정수부분 앞에 0 으로 채움
print('{:06.2f}'.format(3.141592653589793))