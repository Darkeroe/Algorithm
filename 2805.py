def cut(arr, target):
    res = 0
    for i in arr:
        if i-target > 0:
            res += i-target
    return res




n, m = map(int, input().split())
tree = list(map(int,input().split()))
tree.sort()
res = 0
left = 0
right = len(tree) - 1
while left <= right:
    mid = (left+right)//2
    res = cut(tree,tree[mid])
    # print('left,right: ',left, right,mid, res)
    if res == m:
        print(tree[mid])
        break
    elif res > m:
        left = mid +1
    else:
        right = mid -1
    
    if left > right:
        grow = tree[mid]
        if res > m:
            if mid == 0:
                left = 0
                right = tree[mid]
            else:
                left = tree[mid]
                right = tree[mid+1]
            while left <= right:
                mid = (left+right)//2
                res = cut(tree,mid)
                if res == m:
                    print(res)
                elif res > m:
                    left = mid + 1
                else:
                    right = mid -1
            while True:
                grow += 1
                resres = cut(tree,grow)
                if resres < m:
                    print(grow-1)
                    break
                elif resres == m:
                    print(grow)
                    break
        else:
            left = tree[mid-1]
            right = tree[mid]
            while True:
                grow -= 1
                resres = cut(tree,grow)
                if resres >= m or grow == 0:
                    print(grow)
                    break