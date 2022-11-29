from collections import deque

print('------------------- 5-4 2020년 카카오 신입 개발자 블라인드 채용 1차 코테 - 2 올바른 괄호 문자열 만들기 -------------------')

def is_correct_parenthesis(string):     # 올바른 괄호 문자열인지 검사
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break

    v = "".join(list(queue))
    return u, v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ')'
        else:
            reversed_string += "("
    return reversed_string

def change_to_correct_parenthesis(string):
    if string == "":
        return ""
    u, v = separate_to_u_v(string)

    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):

    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)



print('----- 1 -----')
balanced_parentheses_string = "()))((()"
print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
print('----- 2 -----')
print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print('----- 3 -----')
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print('----- 4 -----')
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))