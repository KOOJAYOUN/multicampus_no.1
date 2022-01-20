# 4개의 과목을 합계(개인 합계, 전체 합계) + 평균(개인 평균 / 전체 평균) 
# 홍길동1 : { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50}
# 홍길동2 : { '국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90}
# 홍길동3 : { '국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40}
# 홍길동4 : { '국어' : 55, '영어' : 80, '수학' : 80, '과학' : 60}

# for / while / if / elif
# 7가지 방법으로 코드를 작성 : 결과는 모두 갈아야 함


hong1 = [95, 90, 80, 50]
hong2 = [100, 50, 90, 90]
hong3 = [99, 60, 100, 40]
hong4 = [55, 90, 80, 60]

sumhong1 = 0
i = 0
while i < len(hong1):
    sumhong1 = sumhong1 + hong1[i]
    i = i + 1


sumhong2 = 0
i = 0
while i < len(hong2):
    sumhong2 = sumhong2 + hong2[i]
    i = i + 1


sumhong3 = 0
i = 0
while i < len(hong3):
    sumhong3 = sumhong3 + hong3[i]
    i = i + 1


sumhong4 = 0
i = 0
while i < len(hong4):
    sumhong4 = sumhong4 + hong4[i]
    i = i + 1


totalhong = [sumhong1, sumhong2, sumhong3, sumhong4]

sumallhong = 0
i = 0
while i < len(totalhong):
    sumallhong = sumallhong + totalhong[i]
    i = i + 1



print('홍길동 1의 합계는', sumhong1)
print('홍길동 2의 합계는', sumhong2)
print('홍길동 3의 합계는', sumhong3)
print('홍길동 4의 합계는', sumhong4)
print('홍길동들의 합계는', sumallhong)
print('홍길동 1의 평균은', sumhong1/len(hong1))
print('홍길동 2의 평균은', sumhong2/len(hong2))
print('홍길동 3의 평균은', sumhong3/len(hong3))
print('홍길동 4의 평균은', sumhong4/len(hong4))
print('홍길동들의 평균은', sumallhong/len(totalhong))


temp = 0
