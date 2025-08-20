import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # bidirectional

    def dijkstra(self, start, end):
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            (dist, current, path) = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                return dist, path

            for neighbor, weight in self.edges.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (dist + weight, neighbor, path + [neighbor]))

        return float("inf"), []


if __name__ == "__main__":
    g = Graph()
    g.add_edge("Warehouse", "A", 4)
    g.add_edge("Warehouse", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 7)
    g.add_edge("C", "D", 2)
    g.add_edge("C", "Destination", 5)
    g.add_edge("D", "Destination", 1)

    distance, path = g.dijkstra("Warehouse", "Destination")
    print("🚚 Dijkstra Distance:", distance)
    print("📍 Dijkstra Route:", " → ".join(path))
