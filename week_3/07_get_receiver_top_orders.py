
print('--------------------------- 3-5 스택. "탑" 퀴즈 풀어 보기 ---------------------------')

def get_receiver_top_orders(heights):

    result_arr = [0] * len(heights)     # 결과값을 담을 배열을 만들어 놔. 0으로 초기화한 이유는,
                                        # 어차피 레이저가 가로막히지 않는다면 송신해 줄 수 있는 탑이 없다는 뜻이니.

    while heights:      # heights 전체를 하나의 스택 구조라 한다면, 내부의 요소들은 모두 쌓인 스택들.
                        # pop 으로 마지막 요소를 매번 제거해줄거야. height 가 빈 상태가 되면 while문이 종료.
        height = heights.pop() # 배열의 마지막, 그니까 후입선출에 의거하여 배열의 마지막 요소를 제거하고는 리턴.
        for i in range(len(heights) -1, 0, -1):  # range(a, b, c)  a = 시작하는 점, b = 끝나는 점, c = 매번 연산을 얼마나 줄일 것인가.
                                                # 왜 len(heights) - 1 부터 인가. 배열의 마지막 요소를 이미 pop 했으니까.
            if heights[i] > height:     # 만약 전파가 막힌다면?
                result_arr[len(heights)] = i + 1   # 어차피 pop 으로 길이가 줄어들어서 바로 길이를 인덱스에 넣어도 돼.
                                                            # 현재 남아있는 길이가 pop 의 인덱스 번째야.
                                                    # 그리고, pop 한 배열의 마지막 요소가 어디에서 막혔는가, heights[i]번째 탑에서 막혔다.
                                                    # i는 0부터 시작한 인덱스 값이고, 물리적인 탑의 순서를 나타내주기 위래선 + 1 해줘야지.
                break       # 전파가 이미 가로 막혔으니, 더 이상 앞쪽 인덱스들과 크기를 비교하지 않아도 돼.
    return result_arr

top_heights = [6, 9, 5, 7, 4]
print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))