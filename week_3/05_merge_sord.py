
print('--------------------------- 3-4 정렬-3. 병합 정렬 - mergeSort 실습. ---------------------------')
# 재귀 함수에서는 동일한 함수를 계속해서 호출될 때마다 함수를 위한 메모리가 계속해서 할당된다. 함수가 호출될 때마다 사용되는 임시 저장 메모리를 스택이라고 부른다.
# 스택은 LIFO(후입선출) 구조이기 때문에 가장 마지막에 호출된 함수 factorial(1)를 먼저 완료하고, 값을 아래로 전달하여 최초로 호출된 함수 factorial(3)가 최종 값을 계산한다.
# 재귀 함수를 이용하다보면 함수가 종료되지 않고, 함수가 계속해서 호출이 되는데 이 경우 스택 공간이 초과되는 스택 오버플로(stack overfolw)가 발생하여 오류가 생긴다. 그렇기 때문에 재귀를 사용할 떄는 과도하게 스택 메모리가 사용되지 않도록 주의해야 한다.

# 병합 벙렬.
def merge_sort(array, num=2):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid], 0)
    right_array = merge_sort(array[mid:], 1)
    print(array)
    print('left_array, ', left_array)
    print('right_array, ', right_array)
    return merge(left_array, right_array)


# 병합
def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):    # 둘 중 하나는 모조리 다 array_c 에 들어가. 남는 건?
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1): # 만약 array1 의 요소=원소들이 다 array_c 로 넘어가서, index 카운트가 len 만큼 찼다면? 남은 array2는?
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2): # 만약 array2 의 요소=원소들이 다 array_c 로 넘어가서, index 카운트가 len 만큼 찼다면? 남은 array1는?
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1

    return array_c

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

print('------- merge. 병합 --------')

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))


array = [5, 3, 2, 1, 6, 8, 7, 4, 9, 10]
print('------- merge_sort. 병합 정렬 --------')
print(merge_sort(array))


