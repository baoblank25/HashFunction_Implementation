"""
Graph Generation Script for Hash Table Performance Analysis
Generates the three required graphs for the formal report.
"""

import matplotlib.pyplot as plt
import numpy as np

# TODO: Replace this sample data with your actual test results
# Run your batch tests and fill in the real values

# ACTUAL TEST RESULTS - Collected on Nov 16 2025
# Data sorted by load factor for cleaner graphs
raw_data = {
    'load_factors': [0.3241, 0.4861, 0.6484, 0.7294, 0.7779, 0.8751, 0.9236, 0.8873, 0.9279, 0.9630],

    'bitwise_linear_avg': [0.259330, 0.485167, 0.803828, 1.322488, 1.632536, 3.543541, 4.681340, 2.877512, 5.293780, 14.856459],
    'bitwise_linear_max': [7, 11, 17, 29, 49, 144, 270, 65, 262, 685],
    'bitwise_linear_time': [9.569377990e-07, 1.913875598e-06, 9.569377990e-07, 9.569377990e-07, 1.913875598e-06, 1.913875598e-06, 9.569377990e-07, 9.569377990e-07, 0.000000000e+00, 1.913875598e-06],

    'bitwise_quad_avg': [0.244019, 0.413397, 0.671770, 0.915789, 1.062201, 1.610526, 1.818182, 1.592344, 2.268900, 2.740670],
    'bitwise_quad_max': [5, 10, 10, 23, 22, 34, 74, 23, 77, 58],
    'bitwise_quad_time': [9.569377990e-07, 9.569377990e-07, 9.569377990e-07, 9.569377990e-07, 1.913875598e-06, 9.569377990e-07, 9.569377990e-07, 1.913875598e-06, 0.000000000e+00, 1.913875598e-06],

    'poly_linear_avg': [0.288995, 0.477512, 0.891866, 1.531100, 2.109091, 2.946411, 3.773206, 4.444019, 7.908134, 14.905263],
    'poly_linear_max': [5, 10, 17, 52, 68, 97, 131, 186, 450, 753],
    'poly_linear_time': [9.569377990e-07, 0.000000000e+00, 9.569377990e-07, 9.569377990e-07, 0.000000000e+00, 9.569377990e-07, 9.569377990e-07, 9.569377990e-07, 9.569377990e-07, 0.000000000e+00],

    'poly_quad_avg': [0.283254, 0.417225, 0.664115, 1.020096, 1.169378, 1.581818, 1.949282, 1.801914, 1.952153, 2.656459],
    'poly_quad_max': [5, 7, 8, 25, 22, 42, 43, 29, 46, 83],
    'poly_quad_time': [1.913875598e-06, 0.000000000e+00, 1.913875598e-06, 0.000000000e+00, 0.000000000e+00, 9.569377990e-07, 9.569377990e-07, 2.870813397e-06, 0.000000000e+00, 0.000000000e+00],

    'universal_linear_avg': [97.618182, 74.914833, 11.155024, 26.091866, 19.947368, 14.517703, 46.039234, 24.632536, 22.000957, 74.662201],
    'universal_linear_max': [612, 284, 77, 302, 203, 204, 603, 489, 456, 769],
    'universal_linear_time': [5.741626794e-06, 1.913875598e-06, 9.569377990e-07, 4.784688995e-06, 2.870813397e-06, 9.569377990e-07, 4.784688995e-06, 2.870813397e-06, 1.913875598e-06, 2.870813397e-06],

    'universal_quad_avg': [91.716746, 78.266986, 8.703349, 10.568421, 9.272727, 5.082297, 14.060287, 5.123445, 5.978947, 15.926316],
    'universal_quad_max': [438, 382, 66, 143, 57, 52, 1100, 45, 65, 139],
    'universal_quad_time': [5.741626794e-06, 3.827751196e-06, 9.569377990e-07, 0.000000000e+00, 0.000000000e+00, 2.870813397e-06, 9.569377990e-07, 2.870813397e-06, 1.913875598e-06, 1.913875598e-06],
}

# Sort data by load factor to eliminate zigzag lines
sorted_indices = sorted(range(len(raw_data['load_factors'])), key=lambda i: raw_data['load_factors'][i])

data = {}
for key in raw_data:
    data[key] = [raw_data[key][i] for i in sorted_indices]

# Replace zeros in time data with small value for smoother visualization
for key in ['bitwise_linear_time', 'bitwise_quad_time', 'poly_linear_time', 'poly_quad_time', 'universal_linear_time', 'universal_quad_time']:
    data[key] = [max(val, 1e-7) for val in data[key]]

# Create output directory
import os
os.makedirs('graphs', exist_ok=True)

# Set style for professional-looking graphs
plt.style.use('seaborn-v0_8-whitegrid')

# Graph 1A: Average Comparisons - Bitwise & Polynomial Only (exclude Universal)
def plot_avg_comparisons_main():
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot data points with polynomial best fit curves
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Bitwise + Linear
    y1 = np.array(data['bitwise_linear_avg'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise + Linear')
    
    # Bitwise + Quadratic
    y2 = np.array(data['bitwise_quad_avg'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Linear
    y3 = np.array(data['poly_linear_avg'])
    z3 = np.polyfit(x, y3, 3)
    p3 = np.poly1d(z3)
    ax.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial + Linear')
    
    # Polynomial + Quadratic
    y4 = np.array(data['poly_quad_avg'])
    z4 = np.polyfit(x, y4, 3)
    p4 = np.poly1d(z4)
    ax.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Average Comparisons vs. Load Factor\n(Bitwise & Polynomial Hash Functions)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits to keep curves within bounds
    all_y = np.concatenate([y1, y2, y3, y4])
    y_max = np.max(all_y) * 1.15
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/avg_comparisons_main.png', dpi=300, bbox_inches='tight')
    plt.close()

# Graph 1B: Average Comparisons - Universal Hash (separate due to scale)
def plot_avg_comparisons_universal():
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Universal + Linear
    y1 = np.array(data['universal_linear_avg'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#6A4C93', alpha=0.8, label='Universal + Linear')
    
    # Universal + Quadratic
    y2 = np.array(data['universal_quad_avg'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#1B998B', alpha=0.8, label='Universal + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Average Comparisons vs. Load Factor\n(Universal Hash Function - Note Different Scale)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2])
    y_max = np.max(all_y) * 1.15
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/avg_comparisons_universal.png', dpi=300, bbox_inches='tight')
    plt.close()

# Graph 1C: Linear vs Quadratic Comparison
def plot_probing_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Linear Probing
    y1 = np.array(data['bitwise_linear_avg'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax1.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise')
    
    y2 = np.array(data['poly_linear_avg'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax1.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial')
    
    y3 = np.array(data['universal_linear_avg'])
    z3 = np.polyfit(x, y3, 3)
    p3 = np.poly1d(z3)
    ax1.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#6A4C93', alpha=0.8, label='Universal')
    
    ax1.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Average Comparisons', fontsize=14, fontweight='bold')
    ax1.set_title('Linear Probing', fontsize=15, fontweight='bold')
    
    # Set proper axis limits for linear probing
    all_y_linear = np.concatenate([y1, y2, y3])
    y_max_linear = np.max(all_y_linear) * 1.15
    ax1.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax1.set_ylim(0, y_max_linear)
    
    ax1.legend(loc='upper left', fontsize=11, framealpha=0.95)
    ax1.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Quadratic Probing
    y4 = np.array(data['bitwise_quad_avg'])
    z4 = np.polyfit(x, y4, 3)
    p4 = np.poly1d(z4)
    ax2.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise')
    
    y5 = np.array(data['poly_quad_avg'])
    z5 = np.polyfit(x, y5, 3)
    p5 = np.poly1d(z5)
    ax2.plot(x_smooth, p5(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial')
    
    y6 = np.array(data['universal_quad_avg'])
    z6 = np.polyfit(x, y6, 3)
    p6 = np.poly1d(z6)
    ax2.plot(x_smooth, p6(x_smooth), marker="", linewidth=2.5, color='#1B998B', alpha=0.8, label='Universal')
    
    ax2.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Average Comparisons', fontsize=14, fontweight='bold')
    ax2.set_title('Quadratic Probing', fontsize=15, fontweight='bold')
    
    # Set proper axis limits for quadratic probing
    all_y_quad = np.concatenate([y4, y5, y6])
    y_max_quad = np.max(all_y_quad) * 1.15
    ax2.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax2.set_ylim(0, y_max_quad)
    
    ax2.legend(loc='upper left', fontsize=11, framealpha=0.95)
    ax2.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    fig.suptitle('Probing Method Comparison (All Hash Functions)', fontsize=17, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('graphs/probing_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

# Graph 2A: Maximum Comparisons - Bitwise & Polynomial Only (exclude Universal)
def plot_max_comparisons_main():
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Bitwise + Linear
    y1 = np.array(data['bitwise_linear_max'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise + Linear')
    
    # Bitwise + Quadratic
    y2 = np.array(data['bitwise_quad_max'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Linear
    y3 = np.array(data['poly_linear_max'])
    z3 = np.polyfit(x, y3, 3)
    p3 = np.poly1d(z3)
    ax.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial + Linear')
    
    # Polynomial + Quadratic
    y4 = np.array(data['poly_quad_max'])
    z4 = np.polyfit(x, y4, 3)
    p4 = np.poly1d(z4)
    ax.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Maximum Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Maximum Comparisons vs. Load Factor\n(Bitwise & Polynomial Hash Functions)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2, y3, y4])
    y_max = np.max(all_y) * 1.1
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/max_comparisons_main.png', dpi=300, bbox_inches='tight')
    plt.close()

# Graph 2B: Maximum Comparisons - Universal Hash (separate due to scale)
def plot_max_comparisons_universal():
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Universal + Linear
    y1 = np.array(data['universal_linear_max'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#6A4C93', alpha=0.8, label='Universal + Linear')
    
    # Universal + Quadratic
    y2 = np.array(data['universal_quad_max'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#1B998B', alpha=0.8, label='Universal + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Maximum Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Maximum Comparisons vs. Load Factor\n(Universal Hash Function - Note Different Scale)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2])
    y_max = np.max(all_y) * 1.1
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/max_comparisons_universal.png', dpi=300, bbox_inches='tight')
    plt.close()

# Graph 3: Best Performers Only (Quadratic Probing)
def plot_best_performers():
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Bitwise + Quadratic
    y1 = np.array(data['bitwise_quad_avg'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=3, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Quadratic
    y2 = np.array(data['poly_quad_avg'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=3, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Best Performing Configurations\n(Quadratic Probing Methods)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2])
    y_max = np.max(all_y) * 1.2
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    # Add annotation for optimal load factor range
    ax.axvspan(0.65, 0.78, alpha=0.2, color='green', zorder=1)
    
    # Create custom legend with optimal range
    from matplotlib.patches import Patch
    handles, labels = ax.get_legend_handles_labels()
    handles.append(Patch(facecolor='green', alpha=0.2))
    labels.append('Optimal Range (α=0.65-0.78)')
    ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=13, framealpha=0.95, borderaxespad=0)
    
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/best_performers.png', dpi=300, bbox_inches='tight')
    plt.close()

# Update old graph files with new style
def plot_avg_comparisons():
    """Legacy filename - creates avg_comparisons.png"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Bitwise + Linear
    y1 = np.array(data['bitwise_linear_avg'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise + Linear')
    
    # Bitwise + Quadratic
    y2 = np.array(data['bitwise_quad_avg'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Linear
    y3 = np.array(data['poly_linear_avg'])
    z3 = np.polyfit(x, y3, 3)
    p3 = np.poly1d(z3)
    ax.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial + Linear')
    
    # Polynomial + Quadratic
    y4 = np.array(data['poly_quad_avg'])
    z4 = np.polyfit(x, y4, 3)
    p4 = np.poly1d(z4)
    ax.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Average Comparisons vs. Load Factor\n(All Configurations)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2, y3, y4])
    y_max = np.max(all_y) * 1.15
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=12, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/avg_comparisons.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_max_comparisons():
    """Legacy filename - creates max_comparisons.png - now excludes Universal"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Bitwise + Linear
    y1 = np.array(data['bitwise_linear_max'])
    z1 = np.polyfit(x, y1, 3)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise + Linear')
    
    # Bitwise + Quadratic
    y2 = np.array(data['bitwise_quad_max'])
    z2 = np.polyfit(x, y2, 3)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Linear
    y3 = np.array(data['poly_linear_max'])
    z3 = np.polyfit(x, y3, 3)
    p3 = np.poly1d(z3)
    ax.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial + Linear')
    
    # Polynomial + Quadratic
    y4 = np.array(data['poly_quad_max'])
    z4 = np.polyfit(x, y4, 3)
    p4 = np.poly1d(z4)
    ax.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Maximum Comparisons per Query', fontsize=14, fontweight='bold')
    ax.set_title('Maximum Comparisons vs. Load Factor\n(Bitwise & Polynomial Hash Functions)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2, y3, y4])
    y_max = np.max(all_y) * 1.1
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=11, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/max_comparisons.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_avg_time():
    """Legacy filename - creates avg_time.png"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    x = np.array(data['load_factors'])
    x_smooth = np.linspace(x.min(), x.max(), 100)
    
    # Convert to microseconds
    # Bitwise + Linear
    y1 = np.array(data['bitwise_linear_time']) * 1e6
    z1 = np.polyfit(x, y1, 2)
    p1 = np.poly1d(z1)
    ax.plot(x_smooth, p1(x_smooth), marker="", linewidth=2.5, color='#2E86AB', alpha=0.8, label='Bitwise + Linear')
    
    # Bitwise + Quadratic
    y2 = np.array(data['bitwise_quad_time']) * 1e6
    z2 = np.polyfit(x, y2, 2)
    p2 = np.poly1d(z2)
    ax.plot(x_smooth, p2(x_smooth), marker="", linewidth=2.5, color='#A23B72', alpha=0.8, label='Bitwise + Quadratic')
    
    # Polynomial + Linear
    y3 = np.array(data['poly_linear_time']) * 1e6
    z3 = np.polyfit(x, y3, 2)
    p3 = np.poly1d(z3)
    ax.plot(x_smooth, p3(x_smooth), marker="", linewidth=2.5, color='#F18F01', alpha=0.8, label='Polynomial + Linear')
    
    # Polynomial + Quadratic
    y4 = np.array(data['poly_quad_time']) * 1e6
    z4 = np.polyfit(x, y4, 2)
    p4 = np.poly1d(z4)
    ax.plot(x_smooth, p4(x_smooth), marker="", linewidth=2.5, color='#C73E1D', alpha=0.8, label='Polynomial + Quadratic')
    
    # Universal + Linear
    y5 = np.array(data['universal_linear_time']) * 1e6
    z5 = np.polyfit(x, y5, 2)
    p5 = np.poly1d(z5)
    ax.plot(x_smooth, p5(x_smooth), marker="", linewidth=2.5, color='#6A4C93', alpha=0.8, label='Universal + Linear')
    
    # Universal + Quadratic
    y6 = np.array(data['universal_quad_time']) * 1e6
    z6 = np.polyfit(x, y6, 2)
    p6 = np.poly1d(z6)
    ax.plot(x_smooth, p6(x_smooth), marker="", linewidth=2.5, color='#1B998B', alpha=0.8, label='Universal + Quadratic')
    
    ax.set_xlabel('Load Factor (α)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Average Time per Query (microseconds)', fontsize=14, fontweight='bold')
    ax.set_title('Average Running Time vs. Load Factor\n(All Configurations)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Set proper axis limits
    all_y = np.concatenate([y1, y2, y3, y4, y5, y6])
    y_max = np.max(all_y) * 1.15
    ax.set_xlim(x.min() - 0.02, x.max() + 0.02)
    ax.set_ylim(0, y_max)
    
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=11, framealpha=0.95, borderaxespad=0)
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('graphs/avg_time.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate all graphs
if __name__ == '__main__':
    print("Generating cleaner, more readable performance graphs...")
    print("\nCreating graphs (this may take a moment)...")
    
    plot_avg_comparisons_main()
    print("✓ Generated: graphs/avg_comparisons_main.png (Bitwise & Polynomial)")
    
    plot_avg_comparisons_universal()
    print("✓ Generated: graphs/avg_comparisons_universal.png (Universal Hash)")
    
    plot_probing_comparison()
    print("✓ Generated: graphs/probing_comparison.png (Side-by-side comparison)")
    
    plot_max_comparisons_main()
    print("✓ Generated: graphs/max_comparisons_main.png (Bitwise & Polynomial worst-case)")
    
    plot_max_comparisons_universal()
    print("✓ Generated: graphs/max_comparisons_universal.png (Universal worst-case)")
    
    plot_best_performers()
    print("✓ Generated: graphs/best_performers.png (Recommended configurations)")
    
    print("\nUpdating legacy graph files...")
    plot_avg_comparisons()
    print("✓ Updated: graphs/avg_comparisons.png")
    
    plot_max_comparisons()
    print("✓ Updated: graphs/max_comparisons.png")
    
    plot_avg_time()
    print("✓ Updated: graphs/avg_time.png")
    
    print("\n" + "="*60)
    print("All graphs generated successfully!")
    print("="*60)
    print("Total graphs: 9 (cleaner, easier to read)")
    print("Data: 60 test runs (6 configurations × 10 load factors)")
    print("Dataset: 1,045 URLs from test1.txt")
    print("\nGraph Summary:")
    print("  1. avg_comparisons_main.png - Best configurations (4 lines)")
    print("  2. avg_comparisons_universal.png - Universal hash (2 lines)")
    print("  3. probing_comparison.png - Linear vs Quadratic split view")
    print("  4. max_comparisons_main.png - Worst-case (4 lines)")
    print("  5. max_comparisons_universal.png - Universal worst-case (2 lines)")
    print("  6. best_performers.png - Top 2 configurations with optimal range")
    print("="*60)
