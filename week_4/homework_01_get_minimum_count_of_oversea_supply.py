import heapq

print('--------------------------- 4-9 숙제. 농심 라면 공장 ---------------------------')

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    result_count = 0    # 최종적으로 리턴할, 밀가루를 공급받아야 할 횟수
    max_heap = []       # supplies 의 값들을 꺼내서 heap 에 넣어준 뒤, 가장 큰 값을 꺼내서 stock 에 더해 줄거야.
    last_added_date_index = 0       # stock 이 떨어 지기 전에, 가장 큰 값의 supplies 를 알아내야 해.
                                    # 공장이 멈추지 않은 한, 가장 최근에 넣은 날짜의 인덱스.

    while stock <= k:       # stock 이 k일 까지 버텨야 하니까. 버틸 수 있게, 즉 충분히 많은 stock 이 쌓인다면 while문 종료.
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
                            # 공급할 수 있는 횟수가 남아있냐를 묻고, 다음으로 남아 있는 stock이 공급 가능한 날짜까지 버틸 수 있는 양이냐 물어.
            heapq.heappush(max_heap, -supplies[last_added_date_index])  # dates 와 supplies 의 인덱스를 맞춰주면서.
            last_added_date_index += 1 # n번째 dates 의 suply 를 했다. 다음에 또 공급을 시도할 경우, 다음 인덱스의 날짜와 공급량을 매칭시켜야 해.
            # 이렇게 해서 날짜에 맞춰서 stock 에 공급을 줄 수 있는 최대값들을 순차적으로 heap 에 저장해줘. [20, 5, 10] 이면 [20, 10, 5] 이렇게 저장되겠지.

        print('max_heap : ', max_heap)
        result_count += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return result_count

print('--- 1 ---')
print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print('--- 2 ---')
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print('--- 3 ---')
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print('--- 4 ---')
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))