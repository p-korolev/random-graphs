import numpy as np
import matplotlib.pyplot as plt

def simulate_2d_walk(num_steps=10000, p_right=0.25, p_left=0.25, p_up=0.25, p_down=0.25):
    probabilities = [p_right, p_left, p_up, p_down]
    if not np.isclose(sum(probabilities), 1.0):
        raise ValueError(f"Probabilities must sum to 1.0! Current sum: {sum(probabilities)}")
        
    possible_moves = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    
    random_indices = np.random.choice(4, size=num_steps, p=probabilities)
    step_vectors = possible_moves[random_indices]
    
    origin = np.array([[0, 0]])
    path = np.vstack((origin, np.cumsum(step_vectors, axis=0)))
    
    is_at_origin = np.all(path[1:] == [0, 0], axis=1)
    return_indices = np.where(is_at_origin)[0] + 1
    
    plt.figure(figsize=(10, 8))
    plt.plot(path[:, 0], path[:, 1], color='blue', alpha=0.6, linewidth=1, label='Walk Path')
    plt.scatter(0, 0, color='green', edgecolors='black', s=120, zorder=5, label='Start / Origin (0,0)')
    plt.scatter(path[-1, 0], path[-1, 1], color='red', edgecolors='black', s=120, zorder=5, label=f'End Point {tuple(path[-1])}')
    
    if len(return_indices) > 0:
        return_coordinates = path[return_indices]
        plt.scatter(return_coordinates[:, 0], return_coordinates[:, 1], color='gold', edgecolors='black', s=50, zorder=4, label=f'Returns to Origin ({len(return_indices)}x)')
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)
    plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)
    
    title_text = f"Biased 2D Random Walk ({num_steps:,} Steps)\nP(Right)={p_right}, P(Left)={p_left}, P(Up)={p_up}, P(Down)={p_down}"
    plt.title(title_text, fontsize=12, fontweight='bold')
    plt.xlabel("X Coordinate", fontsize=11)
    plt.ylabel("Y Coordinate", fontsize=11)
    plt.legend(loc='best', framealpha=0.9)
    plt.axis('equal') 
    plt.show()
    
    return return_indices

returns = simulate_2d_walk(num_steps=200, p_right=0.25, p_left=0.25, p_up=0.25, p_down=0.25)
print(f"The walker returned to the origin {len(returns)} times.")
