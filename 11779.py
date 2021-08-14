import heapq
INF = int(1e8)

def dijkstra(graph,start,goal):
    distances = {node: INF for node in graph}
    path_stack = {node: start for node in graph}
    distances[start] = 0
    queue = []
    path = []
    heapq.heappush(queue, [distances[start], start, path])
    while queue:
        current_distance, current_node, current_way = heapq.heappop(queue)
        tmp = current_way
        if distances[current_node] < current_distance:
            continue
        for adajacent, weight in graph[current_node].items():
            current_way = tmp[:]
            distance = current_distance + weight
            if distance < distances[adajacent]:
                distances[adajacent] = distance
                current_way.append(adajacent)
                path_stack[adajacent] = current_way
                heapq.heappush(queue, [distance, adajacent, current_way])
    print(distances[goal])
    print(len(path_stack[goal])+1)
    print(start, end=' ')
    print(*path_stack[goal])

n = int(input())
m = int(input())
path = [list(map(int,input().split())) for i in range(m)];
start, goal = map(int,input().split())

graph = {}
for i in range(1,n+1):
    graph[i] = {}
for i in path:
    if i[1] in graph[i[0]]:
        graph[i[0]][i[1]] = min(graph[i[0]][i[1]], i[2])
    else:
        graph[i[0]][i[1]] = i[2]
dijkstra(graph,start,goal)