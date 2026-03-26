import matplotlib.pyplot as plt
import numpy as np


def main():
    # Sample data
    x = np.linspace(0, 10, 100)
    y = 5 * np.sin(x) + 2 * np.cos(x)

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='5*sin(x) + 2*cos(x)')
    plt.scatter(x, y, alpha=0.3, s=10, color='blue', marker='o')

    # Styling
    plt.title('Sample Graph', fontsize=14, fontweight='bold')
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Save plot
    plt.savefig('sample_graph.png', dpi=150, bbox_inches='tight')

    # Show plot if in interactive environment
    # plt.show()

    print("Graph saved to sample_graph.png")


if __name__ == "__main__":
    main()
