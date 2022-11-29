
print('-------------------------- 1-11 입력받은 정수 이하의 소수를 모두 반환 ---------------------------------')
# 소수는 1과 자기 자신 만으로 나눌 수 있는 수. 즉 (2~ 자기자신-1) 범위 내의 어떤 수로 나누어도 나머지가 0이 나오면 안되는 거야.

input = 20

print('----- 1차 시도 -----')
def find_prime_list_under_number(number):

    prime_list = []
    for num in range(2, number+1):
        for i in range(2, num):
            if num % i == 0:    # num = 7  i = 2, 3, 4, 5, 6,
                break           # 즉, 뭔 수로 나누 어도 딱 나누어 떨어 지지 않는 다면, 다시 말해 나머지가 0이 아니 라면, else 가 발동.
        else:
            prime_list.append(num)
    return prime_list


result = find_prime_list_under_number(input)
print(result)

print('----- 2차 시도 -----')
def find_prime_list_under_number_2(number):

    prime_list = []

    for num in range(2, number+1):          # num 이 2부터 number-1 까지의 '모든 소수' 로 나누어 떨어지지 않는지를 확인.
        for i in prime_list:
            if num % i == 0:
                break
        else:
            prime_list.append(num)

    return prime_list


result_2 = find_prime_list_under_number_2(input)
print(result_2)


print('----- 3차 시도 -----')
def find_prime_list_under_number_3(number):

    prime_list = []

    for num in range(2, number+1):          # num 이 2부터 number-1 까지의 '모든 소수' 로 나누어 떨어지지 않는지를 확인.
        for i in prime_list:
            if num % i == 0 and i*i <= num:
                break       # 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
        else:               # 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문.
            prime_list.append(num)

    return prime_list


result_3 = find_prime_list_under_number_3(input)
print(result_3)
