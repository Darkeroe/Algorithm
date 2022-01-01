import sys

input = sys.stdin.readline


def clac():
    for i in range(N):
        print(dist[i].count(float("inf")))


def transform():
    for i in range(N):
        for j in range(N):
            if dist[i][j] != float("inf"):
                dist[j][i] = dist[i][j]


def floyd():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])


def initialize():
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        a, b = map(int, input().split())
        dist[a - 1][b - 1] = 1


N = int(input())
M = int(input())
dist = [[float("inf") for _ in range(N)] for _ in range(N)]
initialize()
floyd()
transform()
clac()
