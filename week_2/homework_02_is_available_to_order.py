shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    set_all_menus = set(menus)
    check_menu = []

    for order in orders:
        if order in set_all_menus:
            check_menu.append(order)
    return check_menu


result = is_available_to_order(shop_menus, shop_orders)
print(result)