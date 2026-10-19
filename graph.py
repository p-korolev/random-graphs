import matplotlib.pyplot as plt
import random

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

    def visualize_vertices(self):
        x, y = zip(*self.V)
        plt.scatter(x, y)
        plt.axis("equal")
        plt.show()
