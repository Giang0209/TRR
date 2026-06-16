import heapq
from collections import deque

INF = 10**18


def dijkstra(start, graph, n):
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def get_moves(u, graph):
    """
    Robot có thể đứng yên tại u
    hoặc đi sang một đỉnh kề với u.
    """
    moves = [u]

    for v, w in graph[u]:
        moves.append(v)

    return moves


def find_schedule(n, graph, a, b, c, d, r):
    # Tính khoảng cách ngắn nhất giữa mọi cặp đỉnh
    all_dist = []

    for i in range(n):
        all_dist.append(dijkstra(i, graph, n))

    start = (a, b)
    target = (c, d)

    # Kiểm tra trạng thái đầu và cuối có hợp lệ không
    if all_dist[a][b] <= r or all_dist[c][d] <= r:
        return None, all_dist

    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        u, v = queue.popleft()

        if (u, v) == target:
            path = []
            cur = target

            while cur != start:
                path.append(cur)
                cur = parent[cur]

            path.append(start)
            path.reverse()

            return path, all_dist

        # Robot A có thể đi hoặc đứng yên
        for next_u in get_moves(u, graph):

            # Robot B có thể đi hoặc đứng yên
            for next_v in get_moves(v, graph):

                new_state = (next_u, next_v)

                # Hai robot không được ở quá gần nhau
                if all_dist[next_u][next_v] <= r:
                    continue

                if new_state not in visited:
                    visited.add(new_state)
                    parent[new_state] = (u, v)
                    queue.append(new_state)

    return None, all_dist


# =========================
# ĐỌC INPUT
# =========================

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))

a, b = map(int, input().split())
c, d = map(int, input().split())
r = int(input())

# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================

schedule, all_dist = find_schedule(n, graph, a, b, c, d, r)

if schedule is None:
    print("Khong the!")
else:
    print("Lich di chuyen   khoang cach")

    for u, v in schedule:
        print(u, v, all_dist[u][v])
