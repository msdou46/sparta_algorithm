
print('----------------------- 2-9 재귀 함수 - 팩토리얼 -----------------------')

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)   # 5를 입력했으면, 5*4! 를 리턴하면서 4*3! 를 실행하러 가는거지. 그렇게 n 이 1이 되면 1을 리턴. 2*1! 이 마지막.
                                # 2*1! 까지 실행이 됬으면, 다시 위로 거슬러 올라가서 5*4! 까지 올라간 뒤 값을 반영하고 최종적으로 리턴 완료.
                                # 즉 최종적으로는 5 * 4 * 3 * 2 * factorial(1) 이 되는거야.
print(factorial(5))



print('----------------------- 2-9 재귀 함수 - 회문 검사  -----------------------')

def is_palindrome(string):
    n = len(string)
    for i in range(n):      # i = n-1 까지 반복이 되겠지.
        if string[i] != string[n - 1 - i]:
            return False
    return True

input = "abcba"
print(is_palindrome(input))



print('----------------------- 2-9 재귀 함수 - 회문 검사 >> 재귀 함수로 문제 해결해보기. -----------------------')

def is_palindrome2(string):
    if len(string) <= 1:        # 문자열을 계속 자르면 마지막에는 홀수면 한 문자만 남거나 짝수면 다 사라지겠지.
        return True             # 그 때 까지 검사를 했는데 False 가 리턴되지 않았으니 true 를 리턴하며 재귀 함수를 종료시켜.
    if string[0] != string[-1]:     # 인덱스를 -1 로 하면, 0번째 인덱스의 바로 이전 인덱스이니까, 돌아서 맨 마지막 인덱스를 반환해.
        return False
    return is_palindrome2(string[1: -1])    # 맨 앞, 맨 뒤 문자를 자른 문자열을 다시 입력해서 재귀 함수 호출. 1 < -1

input2 = "소주만병만주소"
print(is_palindrome2(input2))


