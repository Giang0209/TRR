from collections import defaultdict, deque

URL = "http://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"


# =========================
# ĐỌC DỮ LIỆU
# =========================
def load_words(filename="sgb-words.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]


# =========================
# PHẦN A - ĐỒ THỊ VÔ HƯỚNG
# =========================

def differ_one_position(w1, w2):
    count = 0
    for a, b in zip(w1, w2):
        if a != b:
            count += 1
    return count == 1


def build_undirected_graph(words):
    graph = defaultdict(list)

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if differ_one_position(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    return graph


def count_connected_components(graph, words):
    visited = set()
    count = 0

    for word in words:
        if word not in visited:
            count += 1
            stack = [word]
            visited.add(word)

            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)

    return count


def shortest_path_undirected(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        u, path = queue.popleft()

        if u == end:
            return path

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append((v, path + [v]))

    return None


# =========================
# PHẦN B - ĐỒ THỊ CÓ HƯỚNG
# =========================

def last_four(word):
    return word[1:]


def build_directed_graph(words):
    graph = defaultdict(list)

    for u in words:
        suffix = last_four(u)

        for v in words:
            if u != v and suffix in v:
                graph[u].append(v)

    return graph


def reverse_graph(graph, words):
    rev = defaultdict(list)

    for u in words:
        for v in graph[u]:
            rev[v].append(u)

    return rev


def dfs_order(graph, words):
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        order.append(u)

    for word in words:
        if word not in visited:
            dfs(word)

    return order


def count_strongly_connected_components(graph, words):
    rev = reverse_graph(graph, words)
    order = dfs_order(graph, words)

    visited = set()
    count = 0

    def dfs_rev(u):
        visited.add(u)
        for v in rev[u]:
            if v not in visited:
                dfs_rev(v)

    for word in reversed(order):
        if word not in visited:
            count += 1
            dfs_rev(word)

    return count


def strongly_connected_component_of(graph, words, start):
    rev = reverse_graph(graph, words)

    # Các đỉnh đi được từ start
    reachable_from_start = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u not in reachable_from_start:
            reachable_from_start.add(u)
            for v in graph[u]:
                stack.append(v)

    # Các đỉnh đi được tới start
    can_reach_start = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u not in can_reach_start:
            can_reach_start.add(u)
            for v in rev[u]:
                stack.append(v)

    return reachable_from_start & can_reach_start


def shortest_path_directed(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        u, path = queue.popleft()

        if u == end:
            return path

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append((v, path + [v]))

    return None


# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================

words = load_words("sgb-words.txt")

# ----- Phần A -----
G = build_undirected_graph(words)

print("PHẦN A")
print("Số thành phần liên thông:", count_connected_components(G, words))

u = input("Nhập từ bắt đầu u: ")
v = input("Nhập từ kết thúc v: ")

path = shortest_path_undirected(G, u, v)

if path:
    print("Đường đi ngắn nhất:")
    print(" -> ".join(path))
else:
    print("Không có đường đi")


# ----- Phần B -----
D = build_directed_graph(words)

print("\nPHẦN B")
print("Số thành phần liên thông mạnh:",
      count_strongly_connected_components(D, words))

word = input("Nhập một từ để tìm thành phần liên thông mạnh: ")

scc = strongly_connected_component_of(D, words, word)
print("Các từ cùng thành phần liên thông mạnh:")
print(sorted(scc))

u = input("Nhập từ bắt đầu u: ")
v = input("Nhập từ kết thúc v: ")

path = shortest_path_directed(D, u, v)

if path:
    print("Đường đi ngắn nhất có hướng:")
    print(" -> ".join(path))
else:
    print("Không có đường đi")
