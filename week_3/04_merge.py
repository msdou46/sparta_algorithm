
print('--------------------------- 3-4 정렬-3. 병합 정렬 - merge 실습. ---------------------------')


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

    if array1_index == len(array1): # 만약 array1 의 요소=원소들이 다 array_c 로 넘어가서, index 카운트가 len 만큼 찼다면?
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2): # 만약 array2 의 요소=원소들이 다 array_c 로 넘어가서, index 카운트가 len 만큼 찼다면?
        while array1_index < len(array1):
            array_c.append(array2[array1_index])
            array1_index += 1

    return array_c


array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))



