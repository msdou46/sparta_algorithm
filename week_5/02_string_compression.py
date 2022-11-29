print('--------------------------- 5-3 2020년 카카오 신입 개발자 블라인드 채용 1차 코테 - 1 문자열 압축 ---------------------------')

input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_len_array = []

    for split_size in range(1, n // 2 + 1): # 어차피 문자열을 절반 초과의 길이로 쪼개봤자 패턴이 반복되지 못해. 그래서 최대 절반까지만 쪼갤 수 있도록.
        splited = [string[i:i + split_size] for i in range(0, n, split_size)]
        print(splited)

        compressed = ''
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]

        compression_len_array.append(len(compressed))

    return min(compression_len_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))