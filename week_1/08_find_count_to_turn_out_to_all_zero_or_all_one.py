
print('-------------------------- 1-11_2 문자열 뒤집기 ---------------------------------')

def find_count_to_turn_out_to_all_zero_or_all_one(string):

    all_to_one = 0
    all_to_zero = 0

    if string[0] == "0":        # 첫 숫자가 바뀌어야 하는 경우도 있으니 미리 계산해 두는거야.
        all_to_one += 1
    elif string[0] == "1":
        all_to_zero += 1

    for i in range(len(string) - 1):   # 총 길이는 6.   순서는 0, 1, 2, 3, 4, 5   최종은 0, 1, 2, 3, 4
        if string[i] != string[i + 1]:
            if string[i] == "0":
                all_to_zero += 1
            elif string[i] == "1":
                all_to_one += 1
                    # 지금 알고리즘에서는 i와 i+1 이 다르다면, i 에 맞춰서 i+1 을 바꿔야 하는 횟수를 계산하고 있어.
                    # 헌데 마지막 i 는 i+1이 없잖아? '다음 숫자를 뒤집을까 말까' 를 알아 보고 있는데, i+1 이 없다면 알아 볼 필요가 없지.
                    # 그래서 len(string) 에서 -1 을 해준거야. 마지막 i 는 검사할 필요가 없으니까.

    print(f'all_to_one = {all_to_one} // all_to_zero = {all_to_zero}')
    return min(all_to_one, all_to_zero)

input = "0111101010101010001101010100"
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
