
print('--------------------------- 3-3 정렬-2. 선택 정렬 실습. ---------------------------')
# min_index 를 가장 앞으로 보내고, 점점 스코프를 하나씩 하나씩 뒤로 이동. 0,1,2,3,4 -> 1,2,3,4 -> 2,3,4 이렇게 뒤로 이동.

print('---------- 내가 시도해 본 것 ----------')
def selection_sort(array):

    a_len = len(array)

    for all_i in range(a_len - 1): # 1
        min_index = all_i   # 시작 부분.
        for i in range(all_i, a_len): # 1, 2, 3, 4
            if array[min_index] > array[i]:
                min_index = i
        array[all_i], array[min_index] = array[min_index], array[all_i]
    return array

input = [4, 6, 2, 9, 1] # [1, 6, 2, 9, 4]
selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))




print('---------- 튜터님의 답 ----------')

def selection_sort2(array):

    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i): # 5-0 5-1 5-2 5-3  // 5, 4, 3, 2 //  i => 00000 1111 222 33 j => 01234 0123 012 01 출력
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[min_index], array[i] = array[i], array[min_index]


    return array


input2 = [4, 6, 2, 9, 1]
selection_sort2(input2)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort2([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort2([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort2([100,56,-3,32,44]))



print('---------- 실습 ----------')

def selection_sort3(array):

    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):  # 본인부터 끝까지 다 검사한다. i가 갈수록 증가하잖아. i+0, i+1 i+2,,, i+0, i+1, i+2 이게 반복되면서 스코프가 뒤로 이동.
            if array[i + j] < array[min_index]: # 검사 대상을 뒤쪽의 요소들과 비교해야 하니까.
                min_index = i + j
            array[min_index], array[i] = array[i], array[min_index]


    return array


input3 = [4, 6, 2, 9, 1]
selection_sort2(input3)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort3([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort3([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort3([100,56,-3,32,44]))



