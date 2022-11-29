print('hello 안녕')



print('-------------------------------- 1-4 알고리즘과 친해지기. 최대값 찾기 --------------------------------------')

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if max_num < num:
            max_num = num
    return max_num

def find_max_num2(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:       # num이 compare_num 보다 작냐고 물었을 때 단 한번도 true가 나오지 않는다면,
                break                   # 해당 num이 가장 크다는 의미. 따라서 else 에서 바로 함수를 종료시킨다.
        else:
            return num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

print('----- 최댓값 구하기 다른 방법 -----')
print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num2([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num2([6, 9, 2, 7, 1888]))














