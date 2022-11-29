
print('--------------------------- 3-2 정렬-1. 버블 정렬 실습. ---------------------------')
    # 가장 높은 수를 가장 오른쪽으로 보내. 그리고 마지막 인덱스를 제외하고, 처음부터 또 실행. 그리고 마지막 인덱스 제외. 이걸 반복.
print('----- 내가 한 것 -----')
def bubble_sort(array):

    for all_i in range(len(array) - 1):  # 예를 들어 len(arr)가 5다, 그럼 4번만 반복 해주면 가장 큰 숫자가 맨 뒤로 어차피 오게 되어 있어.
        for i in range(len(array) - 1 - all_i):     # i와 i+1 을 비교해. 그래서 마지막 i 는 비교 하지 않아도 돼.
            if array[i] > array[i + 1]:             # 또한, 매번 가장 큰 수를 맨 뒤로 보내고 있는데, 맨 뒤로 보낸 수는 다음 for 때는 고려할 필요가 없어.
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

input = [4, 6, 2, 9, 1]
bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))



print('----- 튜터님 코드 -----')

def bubble_sort2(array):

    n = len(array)
    for i in range(n): # 0, 1, 2, 3, 4
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


input2 = [4, 6, 2, 9, 1]
bubble_sort2(input2)
print(input)

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort2([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort2([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort2([100,56,-3,32,44]))



print('----- 실습 -----')



