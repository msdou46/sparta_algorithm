
print('--------------------------- 3-9 숙제 2. 올바른 괄호 ---------------------------')


print('----- 내가 한 거 -----')
def is_correct_parenthesis(string):

    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            if stack.pop() != "(":      # 사실 여기서 굳이 검사할 필요 없이 바로 stack.pop() 해주면 됐어.
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(()(()))"))

'''
0. 우선, 문자열의 첫 글자가 ")" 로 시작한다면 바로 false 를 리턴한다.
1. 들어온 문자열을 for 문을 돌릴건데, "(" 랑 ")" 를 일일이 비교하면서 카운트를 센다.
2. 각각의 카운트 숫자를 비교해서 다르다면, 올바르지 않기 때문에 false 를 리턴한다.
3. ())))(((  이런 식으로 되어 있다면, 카운트가 같더라도 올바르지 않은 케이스다. 이건 어떻게 검사할까.
4. ( 가 하나 나왔으면, ) 가 하나 나와야 해.
5. 닫는 괄호가 나오면, 직전에 여는 괄호가 나왔는지 확인해야 해.
6. 즉, 열린 괄호가 나오면 저장해 둬야 해. 어떻게? 스택으로.
7. 왜 후입선출인가. ")" 이 나오면, 가장 최근에 나온 "(" 를 확인해 주면 되니까.
'''


print('----- 튜터님 께서 한 것 -----')
def is_correct_parenthesis2(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 여기 아무런 값이 들어가도 상관없습니다! ( 가 들어가있는지 여부만 저장해둔 거니까요
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis2("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis2(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis2("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis2("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis2("((())"))
