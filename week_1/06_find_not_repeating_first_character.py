
print('-------------------------- 1-10 반복 되지 않는 문자 찾기 ---------------------------------')

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for alphabet in string:
        if alphabet.isalpha():
            count = ord(alphabet) - ord('a')
            alphabet_occurrence_array[count] += 1

    not_repeating_char_array = []
    for i, num in enumerate(alphabet_occurrence_array):
        if num == 1:
            alphabet = chr(ord('a') + i)
            not_repeating_char_array.append(alphabet)

    for char in string:                         # 반복되지 않는 알파벳들을 위에서 찾았어.
        if char in not_repeating_char_array:    # 입력값 중에서 가장 먼저 나오는 not_repeating 알파벳을 찾는거야.
            return char

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))




print('----- 다시 한 번 연습 -----')

def find_not_repeating_first_character2(string):
    alphabet_occurrence_array = [0] * 26

    for alphanet in string:
        index = ord(alphanet) - ord('a')
        alphabet_occurrence_array[index] += 1

    not_repeating_character = []
    for i, count in enumerate(alphabet_occurrence_array):
        if count == 1:
            not_repeating_character.append(chr(ord('a') + i))

    for char in string:
        if char in not_repeating_character:
            return char

    return '_'

result2 = find_not_repeating_first_character2
print("정답 = d 현재 풀이 값 =", result2("abadabac"))
print("정답 = c 현재 풀이 값 =", result2("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result2("aaaaaaaa"))






