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
print('%s %s' % ('one, 'two'))