import heapq

class GraphAStar:
    def __init__(self):
        self.edges = {}
        self.heuristics = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

    def set_heuristic(self, node, value):
        self.heuristics[node] = value

    def astar(self, start, end):
        pq = [(0 + self.heuristics.get(start, 0), 0, start, [start])]
        visited = set()

        while pq:
            (f, g, current, path) = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == end:
                return g, path

            for neighbor, weight in self.edges.get(current, []):
                if neighbor not in visited:
                    g_new = g + weight
                    f_new = g_new + self.heuristics.get(neighbor, 0)
                    heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))

        return float("inf"), []


if __name__ == "__main__":
    g = GraphAStar()
    g.add_edge("Warehouse", "A", 4)
    g.add_edge("Warehouse", "B", 2)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 7)
    g.add_edge("C", "D", 2)
    g.add_edge("C", "Destination", 5)
    g.add_edge("D", "Destination", 1)

    # Heuristic values (straight-line estimate to Destination)
    g.set_heuristic("Warehouse", 7)
    g.set_heuristic("A", 6)
    g.set_heuristic("B", 4)
    g.set_heuristic("C", 2)
    g.set_heuristic("D", 1)
    g.set_heuristic("Destination", 0)

    distance, path = g.astar("Warehouse", "Destination")
    print("🚀 A* Distance:", distance)
    print("📍 A* Route:", " → ".join(path))
