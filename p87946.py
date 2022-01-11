def dfs(k, dungeons, cnt):
    global answer, visited
    answer = max(answer, cnt)
    for idx, dungeon in enumerate(dungeons):
        required, consumed = dungeon
        if k >= required and visited[idx]:
            visited[idx] = False
            dfs(k - consumed, dungeons, cnt + 1)
            visited[idx] = True


def solution(k, dungeons):
    global answer, visited
    answer = -1
    visited = [True for _ in range(k)]
    dfs(k, dungeons, 0)
    return answer
