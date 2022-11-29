
print('--------------------------- 3-9 숙제 1. 쓱 최대로 할인 적용하기 ---------------------------')


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)       # 내림차순 정렬. 즉 가장 비싼 제품과, 가장 할인률이 높은 쿠폰부터 차례대로 인덱스에 위치.
    coupons.sort(reverse=True)
    prices_index = 0
    coupons_index = 0
    discounted_price = 0

    while prices_index < len(prices) and coupons_index < len(coupons):
        discounted_price += round(prices[prices_index] * ((100 - coupons[coupons_index]) / 100))
        prices_index += 1
        coupons_index += 1

    while prices_index < len(prices):
        discounted_price += prices[prices_index]
        prices_index += 1
        '''
        왜 prices, 즉 상품 배열만 재검사 하는가.
        케이스가 총 3 가지가 있어.
            1. 상품이 더 많을 경우
            2. 쿠폰이 더 많을 경우
            3. 상품, 쿠폰 둘 다 수량이 같을 경우
        2번의 경우, 어차피 쿠폰은 하나 당 한 상품에 밖에 사용할 수 없어서 남아봤자 사용할 수가 없어.
        3번의 경우, 둘 다 수량이 같으니 첫 while문에서 그냥 끝나겠지.
        즉 우리는 1번의 경우만 대비를 하면 된다는 거야. 
        이 경우 더 이상 적용 가능한 쿠폰이 없으니, 그냥 가격을 그대로 최종값에 더해주면 되지.
        '''

    return discounted_price

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))