# 🚚 Route Optimization System

Applied graph algorithms (Dijkstra & A*) to find the shortest delivery routes.  
This project demonstrates **DSA applied in real-world problems** like logistics and delivery services.

---

## 📌 Features
- Implemented **Dijkstra’s Algorithm** for guaranteed shortest paths.
- Implemented **A\* Algorithm** for faster GPS-style route finding.
- Works on weighted, bidirectional graphs.
- Example: Optimizing delivery from Warehouse → Destination.

---

## ⚡ Algorithm Comparison

| Algorithm    | Time Complexity  | Handles Negative Weights? | Notes |
|--------------|------------------|----------------------------|-------|
| Dijkstra     | O(E log V)       | ❌ No                     | Standard for shortest path |
| A*           | O(E) (with good heuristic) | ❌ No | Faster in practice, used in maps/GPS |

---

## ▶️ Run the Project

```bash
# Run Dijkstra
python graph.py

# Run A*
python astar.py
