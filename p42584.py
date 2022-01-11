def calc(i, stack, answer):
    pop_price, pop_i = stack.pop()
    answer[pop_i] = i - pop_i


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[-1][0] > price:
            calc(i, stack, answer)
        stack.append((price, i))
    while stack:
        calc(len(prices) - 1, stack, answer)
    return answer
