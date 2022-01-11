def correct_dist(target):
    if target == 1:
        return 3
    if target == 2 or target == 4:
        return 6
    if target == 5 or target == 7:
        return 9
    if target == 8:
        return 10
    else:
        return target


def compare_equal_dist(target, hand):
    global left, right
    left_dist = correct_dist(abs(target - left))
    right_dist = correct_dist(abs(target - right))

    if left_dist < right_dist or (left_dist == right_dist and hand == "left"):
        left = target
        return "L"

    else:
        right = target
        return "R"


def compare_dist(target, hand):
    global left, right
    if target == 0:
        target = 11

    if target % 3 == 1:
        left = target
        return "L"

    elif target % 3 == 0:
        right = target
        return "R"

    else:
        return compare_equal_dist(target, hand)


def solution(numbers, hand):
    global left, right
    answer = ""
    left = 10
    right = 12
    for number in numbers:
        answer += compare_dist(number, hand)
    return answer
