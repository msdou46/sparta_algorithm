# BOJ 1158

def josephus_problem(n, k):
    result_arr = []

    next_target = k - 1
    people_arr = list(range(1, n + 1))

    while len(people_arr) != 0:
        result = people_arr.pop(next_target)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_target = (next_target + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)
