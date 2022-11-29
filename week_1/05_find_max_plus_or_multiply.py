

print('-------------------------- 1-9 곱하기 or 더하기 ---------------------------------')
def find_max_plus_or_multiply(array):

    last_num = array[0]
    a_array = array[1:]
    for num in a_array:
        if last_num == 0:
            last_num += num
        elif num <= 1:
            last_num += num
        else:
            last_num = last_num * num

    return last_num

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))



print('---------- 정답 ----------')
def find_max_plus_or_multiply(array):
    last_num = 0

    for num in array:
        if num <= 1 or last_num <= 1:
            last_num += num
        else:
            last_num *= num
    return last_num

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))











