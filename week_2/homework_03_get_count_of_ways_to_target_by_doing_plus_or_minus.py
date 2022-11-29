
numbers = [2, 3, 1]
                    # (연산자의 개수)^(숫자의 개수) => 즉, 연산자가 +/- 두 개이고 숫자의 개수는 3개니까, 2의 3승 (2^3) 의 경우의 수가 발생.
target_number = 0
every_result = []
result_count = 0  # 모든 경우의 수를 체크

                                        #  정수배열    타겟        for let i     각 분기 당 계산식의 값
def get_all_ways_to_by_doing_plus_or_minus(array, target_num, current_index, current_sum):
    if current_index == len(array):  # 탈출조건! 예를 들어 정수배열의 길이가 6개다. current_index는 0, 1, 2, 3, 4, 5 만큼 돌아.
        global every_result
        every_result.append(current_sum)
        if current_sum == target_num:  # 함수가 정수 배열만큼 분기를 완료했어. 그렇게 해서 각 분기별로 최종값들을 타겟과 비교.
            global result_count        # 함수 외부의 전역 변수를 함수 내부에서 사용하겠다.
            result_count += 1          # 정수 배열의 계산 분기 중에서 타겟과 같은 값을 최종적으로 산출한 경우의 총 횟수.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, target_num, current_index + 1, current_sum + array[current_index])
    get_all_ways_to_by_doing_plus_or_minus(array, target_num, current_index + 1, current_sum - array[current_index])


get_all_ways_to_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(f"모든 경우의 수의 최종값들 : {every_result}")
print(result_count)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
# 모든 경우의 수가 출력됩니다!
# [6, 4, 0, -2, 2, 0, -4, -6]