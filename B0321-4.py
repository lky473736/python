# 문자입력
str = input ("입력 : ")
str = str + "ok" # compactnate
print (str)

# 숫자입력
val = input ("입력 = ") # 여기선 문자열을 입력받는다
val = int(val) # 숫자 연산을 하기 위해서는 변수 val을 숫자형으로 바꾸어 주어야 한다 (문자열 + 숫자형은 성립 x -> int로 형태변환한다)
val = val + 100 
print (val)
