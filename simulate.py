import numpy as np
import matplotlib.pyplot as plt

from graph import *
from walk import *

def run_academic_plots(radius: int, p_v: float, p_e: float, num_trials: int = 2000):
    plt.rcParams.update({
        'font.family': 'monospace',
        'font.monospace': ['Consolas', 'Courier New', 'DejaVu Sans Mono'],
        'text.usetex': False,
        'axes.edgecolor': '#111111',
        'axes.linewidth': 0.8,
        'figure.titlesize': 13
    })

    # 1. Compute theoretical properties
    lattice_size = (2 * radius + 1) ** 2
    expected_v = p_v * lattice_size
    expected_e = p_e * ((expected_v ** 2) - expected_v) / 2
    expected_deg = p_e * (expected_v - 1) if expected_v > 1 else 0.0

    # 2. Collect Monte Carlo samples
    empirical_v = []
    empirical_e = []
    empirical_deg = []

    for _ in range(num_trials):
        graph = RandomGraph(radius=radius, v_exist_prob=p_v, e_exist_prov=p_e)
        v_count = graph.Vsize()
        e_count = graph.Esize()
        
        empirical_v.append(v_count)
        empirical_e.append(e_count)
        if v_count > 0:
            empirical_deg.append((2 * e_count) / v_count)

    # 3. Initialize publication layout (Stacked vertically or single row depending on space)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    
    # Subplot configurations: (Data, Theoretical Target, X-Label, Subplot Header)
    plot_configs = [
        (empirical_v, expected_v, "Vertex Count (n)", "a) Distribution of Vertex Count"),
        (empirical_e, expected_e, "Edge Count (|E|)", "b) Distribution of Edge Count"),
        (empirical_deg, expected_deg, "Average Degree (deg(u))", "c) Distribution of Vertex Degree")
    ]

    for i, (data, theoretical, x_label, sub_title) in enumerate(plot_configs):
        ax = axes[i]
        
        # Plot standard normalized probability distribution using a muted academic tone
        ax.hist(data, bins=25, color="#e0e0e0", edgecolor="#444444", alpha=0.8, density=True, label="Simulation")
        
        emp_mean = np.mean(data)
        
        # High contrast statistical tracking lines
        ax.axvline(emp_mean, color="#d32f2f", linestyle="-", linewidth=1.5, 
                   label=f"Emp. Mean: {emp_mean:.2f}")
        ax.axvline(theoretical, color="#1976d2", linestyle="--", linewidth=1.5, 
                   label=f"Theo. E: {theoretical:.2f}")
        
        # Complete axis tracking and labeling
        ax.set_title(sub_title, fontsize=11, pad=10, loc="left", weight="bold")
        ax.set_xlabel(x_label, fontsize=10, labelpad=8)
        ax.set_ylabel("Probability Density (f)", fontsize=10, labelpad=8)
        
        # Layout refinements
        ax.grid(True, linestyle=":", color="#cccccc", alpha=0.7)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="none", fontsize=8)

    plt.tight_layout()
    plt.show()

# Execute stylized report
if __name__ == "__main__":
    run_academic_plots(radius=3, p_v=0.7, p_e=0.4, num_trials=2000)
