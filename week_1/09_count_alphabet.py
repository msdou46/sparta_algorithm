
print('-------------------------- 1-11_3 입력값 알파벳 중복 갯수 나타내기. ---------------------------------')

def summarize_string(input_str):

    input_str_len = len(input_str)
    count = 0
    result = ''

    for i in range(input_str_len - 1):
        print(i)
        if input_str[i] == input_str[i+1]:
            count += 1
        else:
            print(input_str[i])
            result += input_str[i] + str(count + 1) + '/'
            count = 0
    result += input_str[input_str_len -1] + str(count +1)


    return result

input_str = "acccdeeeh"  # e 5 6 7   h 8   총 길이는 9
print(summarize_string(input_str))
