"""
Data Collection Helper Script
Use this to organize your test results into the format needed for graphs.

INSTRUCTIONS:
1. Run your url_hash.exe program in batch mode (option 2)
2. Test all 6 configurations:
   - Bitwise + Linear
   - Bitwise + Quadratic
   - Polynomial + Linear
   - Polynomial + Quadratic
   - Universal + Linear
   - Universal + Quadratic
3. For each configuration, record the stats from all 10 table sizes
4. Fill in the values below
5. Run this script to generate a formatted data file
"""

# Configuration 1: Bitwise Hash + Linear Probing
bitwise_linear = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

# Configuration 2: Bitwise Hash + Quadratic Probing
bitwise_quadratic = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

# Configuration 3: Polynomial Hash + Linear Probing
polynomial_linear = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

# Configuration 4: Polynomial Hash + Quadratic Probing
polynomial_quadratic = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

# Configuration 5: Universal Hash + Linear Probing
universal_linear = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

# Configuration 6: Universal Hash + Quadratic Probing
universal_quadratic = {
    'load_factors': [0.33, 0.50, 0.65, 0.73, 0.78, 0.88, 0.89, 0.92, 0.93, 0.96],
    'avg_comparisons': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
    'max_comparisons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fill from test
    'avg_time': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Fill from test
}

def validate_data():
    """Check if data has been filled in"""
    configs = [
        ('Bitwise + Linear', bitwise_linear),
        ('Bitwise + Quadratic', bitwise_quadratic),
        ('Polynomial + Linear', polynomial_linear),
        ('Polynomial + Quadratic', polynomial_quadratic),
        ('Universal + Linear', universal_linear),
        ('Universal + Quadratic', universal_quadratic),
    ]
    
    all_filled = True
    for name, config in configs:
        if sum(config['avg_comparisons']) == 0:
            print(f"⚠ {name}: No data entered yet")
            all_filled = False
        else:
            print(f"✓ {name}: Data looks good")
    
    return all_filled

def export_for_graphing():
    """Export data in format ready for generate_graphs.py"""
    
    output = f"""
# Copy this data into generate_graphs.py
data = {{
    'load_factors': {bitwise_linear['load_factors']},
    
    'bitwise_linear_avg': {bitwise_linear['avg_comparisons']},
    'bitwise_linear_max': {bitwise_linear['max_comparisons']},
    'bitwise_linear_time': {bitwise_linear['avg_time']},
    
    'bitwise_quad_avg': {bitwise_quadratic['avg_comparisons']},
    'bitwise_quad_max': {bitwise_quadratic['max_comparisons']},
    'bitwise_quad_time': {bitwise_quadratic['avg_time']},
    
    'poly_linear_avg': {polynomial_linear['avg_comparisons']},
    'poly_linear_max': {polynomial_linear['max_comparisons']},
    'poly_linear_time': {polynomial_linear['avg_time']},
    
    'poly_quad_avg': {polynomial_quadratic['avg_comparisons']},
    'poly_quad_max': {polynomial_quadratic['max_comparisons']},
    'poly_quad_time': {polynomial_quadratic['avg_time']},
    
    'universal_linear_avg': {universal_linear['avg_comparisons']},
    'universal_linear_max': {universal_linear['max_comparisons']},
    'universal_linear_time': {universal_linear['avg_time']},
    
    'universal_quad_avg': {universal_quadratic['avg_comparisons']},
    'universal_quad_max': {universal_quadratic['max_comparisons']},
    'universal_quad_time': {universal_quadratic['avg_time']},
}}
"""
    
    with open('data_for_graphs.txt', 'w') as f:
        f.write(output)
    
    print("\n" + "="*60)
    print("Data exported to: data_for_graphs.txt")
    print("Copy the contents and paste into generate_graphs.py")
    print("="*60)

if __name__ == '__main__':
    print("="*60)
    print("DATA COLLECTION VALIDATOR")
    print("="*60)
    print()
    
    if validate_data():
        print("\n✓ All configurations have data!")
        export_for_graphing()
    else:
        print("\n⚠ Please run tests and fill in the data arrays above.")
        print("\nHow to collect data:")
        print("1. Run: .\\url_hash.exe")
        print("2. Select mode 2 (Multiple table size test)")
        print("3. Choose hash function")
        print("4. Choose probing method")
        print("5. Record the stats from the summary table")
        print("6. Repeat for all 6 configurations")
