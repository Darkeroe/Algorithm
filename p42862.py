def search(target, lost, reserve):
    if target in reserve:
        reserve[reserve.index(target)] = -1
        return 1
    return 0


def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    answer = n - len(lost)
    for number in lost:
        if search(number - 1, lost, reserve) or search(number + 1, lost, reserve):
            answer += 1
    return answer
