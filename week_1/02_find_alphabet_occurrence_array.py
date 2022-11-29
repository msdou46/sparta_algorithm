

print('-------------------------------- 1-5 알고리즘과 친해지기. 최빈값 찾기 --------------------------------------')
def find_max_occurred_alphabet2(string):
    alphabet_occurrence_array = [0] * 26    # 요소가 0인 인덱스 26개를 생성.

    for alphabet in string:
        if alphabet.isalpha():
            count = ord(alphabet) - ord('a')  # ord() 는 해당 알파벳의 아스키 코드를 반환.
                                                # 그리고 알파벳의 아스키 코드는 a부터 1씩 증가. a는 97.
            alphabet_occurrence_array[count] += 1  # 알파벳 빈도수 저장 완료.

    most_alphanet_count = alphabet_occurrence_array[0]
    for i, num in enumerate(alphabet_occurrence_array):
        if most_alphanet_count < num:
            most_alphanet_count = num

    return chr(ord('a') + alphabet_occurrence_array.index(most_alphanet_count))
                            # 가장 높은 빈도수를 요소로 가진 인덱스를 97에 더해서, 나오는 아스키 코드를 chr() 를 사용해 알파벳으로 변환.

print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet2("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet2("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet2("best of best sparta"))


print('----- for문 안에서 index 를 알 수 있는 경우. 이게 더 좋아 ------')

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26    # 요소가 0인 인덱스 26개를 생성.

    for alphabet in string:
        if alphabet.isalpha():
            count = ord(alphabet) - ord('a')  # ord() 는 해당 알파벳의 아스키 코드를 반환.
                                                # 그리고 알파벳의 아스키 코드는 a부터 1씩 증가. a는 97.
            alphabet_occurrence_array[count] += 1  # 알파벳 빈도수 저장 완료.

    max_occurrence = 0
    max_alphabet_index = 0
    for i, num in enumerate(alphabet_occurrence_array):
        if max_occurrence < num:   # max_occurrence 는 빈도수를 비교하기 위해 계속 값을 최신화 해야 해.
            max_occurrence = num
            max_alphabet_index = i                  # 인덱스를 구했어.

    return chr(ord('a') + max_alphabet_index)


print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", find_max_occurred_alphabet("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", find_max_occurred_alphabet("best of best sparta"))


print('----- 또 다른 방법. ------')
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if alphabet == char:
                occurrence += 1
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
    return max_alphabet

result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))

