import matplotlib.pyplot as plt
import random
import itertools

class IntegerLattice:
    def __init__(self, radius: int):
        self.radius = radius
        self.xrange = [i for i in range(-radius, radius + 1)]
        self.yrange = self.xrange
        self.points = [(x,y) for x in self.xrange for y in self.yrange]

    def visualize(self):
        x, y = zip(*self.points)
        fig, ax = plt.subplots()
        ax.scatter(x, y, color="black")
        ax.set_xticks(range(min(x), max(x) + 1))
        ax.set_yticks(range(min(y), max(y) + 1))
        ax.grid(True, color="black", linestyle="-", linewidth=0.3)
        ax.set_aspect("equal")
        plt.show()

class RandomGraph:
    def __init__(self, radius: int, v_exist_prob: float, e_exist_prov: float):
        self.lattice = IntegerLattice(radius=radius)

        # Build set of vertices
        self.V = []
        for point in self.lattice.points:
            thresh = random.random()
            if thresh <= v_exist_prob:
                self.V.append(point)

        # Build set of edges
        self.E = []
        # no self-loops or symmetric edges
        for point, other in itertools.combinations(self.V, 2):
            if random.random() <= e_exist_prov:
                d = abs(point[0] - other[0]) + abs(point[1] - other[1])
                self.E.append([point, other, d])

    def Vsize(self):
        return len(self.V)

    def Esize(self):
        return len(self.E)

    # returns total Manhattan distance of graph
    def Mtotal(self):
        sum=0
        for e in self.E:
            sum += e[2]
        return sum

    def avg_edge_length(self):
        return self.Mtotal()/self.Esize()
    
    def visualize_vertices(self):
        x, y = zip(*self.V)
        plt.scatter(x, y)
        plt.axis("equal")
        plt.show()

    def visualize_graph(self):
        if not self.V:
            print("No vertices to visualize.")
            return

        fig, ax = plt.subplots(figsize=(8, 8))

        # 1. Draw the edges (lines connecting the points)
        for point1, point2, distance in self.E:
            x_coords = [point1[0], point2[0]]
            y_coords = [point1[1], point2[1]]
            
            # Optional: Visual styling (thinner lines for longer distances)
            linewidth = max(0.5, 2.5 / (distance ** 0.5)) 
            
            ax.plot(x_coords, y_coords, color="blue", alpha=0.6, linewidth=linewidth, zorder=1)

        # 2. Draw the vertices on top of the lines
        x, y = zip(*self.V)
        ax.scatter(x, y, color="red", s=50, edgecolors="black", zorder=2)

        # 3. Configure the grid alignment using the underlying lattice boundaries
        all_x, all_y = zip(*self.lattice.points)
        ax.set_xticks(range(min(all_x), max(all_x) + 1))
        ax.set_yticks(range(min(all_y), max(all_y) + 1))
        ax.grid(True, color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
        
        ax.set_aspect("equal")
        ax.set_title(f"Random Graph (Vertices: {self.Vsize()}, Edges: {self.Esize()})")
        plt.show()


test_graph = RandomGraph(radius=5, v_exist_prob=0.3, e_exist_prov=0.05)
print(f"Vertices: {test_graph.Vsize()}\nEdges: {test_graph.Esize()}")
test_graph.visualize_graph()
