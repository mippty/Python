#-*-coding:utf-8 -*_
# Chapter_02 파이썬 기초
# 파이썬 변수

# 기본선언
n=700 #오른쪽에 있는 걸 왼쪽에 할당한다

# 출력
print(n)
print(type(n)) # n의 타입을 알려주는 것. 700은 정수이니 int로 나옴.

# 동시 선언
x=y=z= 700
print(x ,y, z) 

#선언
var = 75 

#재선언
var ='change value'

#출력
print(var)
print(type(var)) #var 는 가장 마지막에 선언된 값이 들어감

#object references
#변수 값 할당 상태
#1. 타입에 맞는 object 생성 
#2. 값 생성
#3. 콘솔 출력

#예1)
print(300) # 자동으로 int가 들어감
print(int(300)) #위 아래 같음

#예2)
# n->777
n = 777
print(n, type(n))


m = n 
# m-> 777 <- n
print(m, n)
print(type(m), type(n))

m = 400

print(m, n, type(m))

# id(identity) 확인 : 객체의 고유값 확인 !!중요중요!!

m = 800
n = 655

print(id(m))  # 둘의 id(고유값) 다르게 나옴
print(id(n))

print(id(m) == id(n)) # == 는 같냐 라는 뜻

#같은 오브젝트 참조 
m = 800 
n = 800
z = 800
i = 800 # 우리가 4개의 변수를 지정했지만 파이썬은 하나의 인스턴스로 인식 (효율화를 위해)

print(id(m))  
print(id(n))

print(id(m) == id(n))

#다양한 변수 선언 방법
# camel case : numberOfCollegeGraduates (맨 앞 소문자, 다음 단어 시작은 대문자로 구분)-> Method 선언할 때 사용
# pascal case : NumberOfCollegeGraduates (단어 시작할 때마다 대문자로 구분)-> class 선언할 때 사용
# snake case : number_of_college_graduates (단어 시작할 때마다 _로 구분) -> 파이썬에서는 주로 이렇게 선언

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5 
_age = 6
age_ = 7
_AGE_ = 8 
# 특수문자가 들어갈 수 있는건 $ 와 _ 뿐 , 앞에 숫자가 들어가면 에러뜸
# 예) 1age = 9 는 에러

# 예약어(Python reserve words)는 변수명으로 불가능 , 한 20개됨.
#for = 3 #에러
#as = 3 #에러
#class = 3 #에러

