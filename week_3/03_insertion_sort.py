
print('--------------------------- 3-3 정렬-2. 삽입 정렬 실습. ---------------------------')


print('---------- 내가 시도해 본 것 ----------')
def insertion_sort(array):

    n = len(array)

    for all_i in range(n - 1): # 0, 1, 2, 3
        for i in range(all_i + 1): # 0 / 0, 1 / 0, 1, 2 / 0, 1, 2, 3
            if array[all_i - i] > array[all_i + 1 - i]: # 3, 4 -> 2, 3
                array[all_i - i], array[all_i + 1 - i] = array[all_i + 1 - i], array[all_i - i]
            else:
                break
    return array


input = [4, 6, 2, 9, 1]
insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))




print('---------- 튜터님의 답 ----------')
def insertion_sort2(array):

    n = len(array) # 5

    for i in range(1, n): # 왜 1부터 시작하는가. 배열의 0번째 요소는 이미 정렬이 되어있다 라고 치기 때문에, 있지도 않은 이전 요소와 비교할 필요가 없어.
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array


input2 = [4, 6, 2, 9, 1]
insertion_sort2(input2)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort2([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort2([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort2([100,56,-3,32,44]))