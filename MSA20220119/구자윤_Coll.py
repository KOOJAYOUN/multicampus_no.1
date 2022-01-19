# 1, 딕션어리를 이용해서 평균 점수 구하기
# : { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50}
dicData1 = { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50}

resultData1 = dicData1["국어"]
resultData2 = dicData1["영어"]
resultData3 = dicData1["수학"]
resultData4 = dicData1["과학"]

totalData1 = (resultData1 + resultData2 + resultData3 + resultData4)/4

print("평균 점수 = ", totalData1)



# 2. 셋을 이용해서 1~100까지 숫자 중에 공배수를 구함 : 3과 5의 공배수만 구하고, 합집합을 구하기 &
# hint : 표현식을 이용하면 쉽다. 반복문의 리스트 표현식 i for i range(100)
setData3 = {i for i in range(0, 101, 3)}
setData5 = {i for i in range(0, 101, 5)}

resultData = setData3 | setData5

print("3과 5의 공배수의 합집합은 = ", resultData)



# 3. 리스트 데이터 : 7,5,3,1,-1,-3,-5,-7 을 출력하는데 이 때 range를 활용할 것
listData1 = [i for i in range(-7,7,2)]

print("리스트 데이터 는", listData1)



# 4. 3번째의 결과를 튜플로 변경(형변환)
changeData = tuple(listData1)

print("튜플로 형변환 된 데이터 는", changeData)

temp = 0
