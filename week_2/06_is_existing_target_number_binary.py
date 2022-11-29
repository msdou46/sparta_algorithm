finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# target 과 array 가 입력되었을 때, array 안에 target 이 있으면 true 를, 없으면 false 를 반환.

def is_existing_target_number_binary(target, array):
    current_min = 0                 # 최솟값. array의 0번째 인덱스.
    current_max = len(array) - 1    # 최대값. array의 마지막 인덱스.
    current_guess = (current_min + current_max) // 2    # 최솟값과 최대값의 중간값을 찾아낸 거야. 이걸로 up,down 을 시도할거야.
    find_count = 0      # 이건 그냥 while 문이 몇 번 반복됬는지 검사해 보려고.

    while current_min <= current_max:   # min 이 max 보다 같거나 작을 때 까지. 범위를 좁혀가는 과정에서 min 에 +1, max에 -1 을 하기 때문에,
        find_count += 1                 # 마지막의 마지막에는 min 과 max 의 값이 같아진 상태에서 연산이 일어나며 while문의 조건이 false로 변해.
        if array[current_guess] == target:  # 만약 시도값이 타겟과 같다면? 그냥 바로 return True
            print(find_count)
            return True
        elif array[current_guess] < target:   # target 이 시도값보다 크다, 즉 up.
            current_min = current_guess + 1     # 시도값보다 타겟이 더 크니, 시도값의 인덱스보다 1 만큼 더 큰 인덱스부터 다시 탐색을 시도하라.
        else:
            current_max = current_guess - 1    # target 이 시도값보다 작다, 즉 down
                                                # 시도값보다 타겟이 더 작으니, 시도값의 인덱스보다 1 만큼 더 작은 인덱스부터 아래를 다시 탐색.
        current_guess = (current_min + current_max) // 2
    print(find_count)
    return False    # 만약 끝까지 while 문을 돌리며 값을 찾아봤는데 없다, 그러면 최종적으로는 False 를 반환하겠다.

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)