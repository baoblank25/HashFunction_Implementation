To run:
1. cl.exe /EHsc /Iinclude /Fe:url_hash.exe src\HashEntry.cpp src\HashFunctions.cpp src\Statistics.cpp src\URLHashTable.cpp src\main.cpp
2. .\url_hash.exe

URL Hash Table with Open Addressing
Course: CSE310 - Data Structures and Algorithms
University: Arizona State University
Author: [Your Name]
ASU ID: [Your ID]

Project Overview
This project implements a high-performance hash table for URL storage using open addressing collision resolution. It demonstrates the trade-offs between different hash functions (Division and Universal Hashing) and probing methods (Linear and Quadratic Probing) with real-time performance metrics.

Key Applications: Web browser history caching, URL dictionary management, efficient string storage.

Features
Hash Functions
Division Hashing - Polynomial rolling hash (base 31) with modulo operation

Universal Hashing - Base-256 Horner's rule implementation with collision guarantees

Collision Resolution
Linear Probing - Simple, cache-friendly probing for low load factors

Quadratic Probing - Reduces clustering, optimal for medium-to-high loads

Performance Tracking
Average comparisons per query

Maximum comparisons (worst-case)

Query execution time

Load factor analysis

Performance ratio calculation

Project Structure
text
URLHashTable/
├── include/              # Header files
│   ├── HashTypes.h       # Enumerations and type definitions
│   ├── HashEntry.h       # Hash table entry structure
│   ├── HashFunctions.h   # Hash function class
│   ├── Statistics.h      # Performance statistics tracking
│   └── URLHashTable.h    # Main hash table class
├── src/                  # Implementation files
│   ├── main.cpp          # Interactive user interface
│   ├── HashEntry.cpp     # Entry implementation
│   ├── HashFunctions.cpp # Hash algorithms
│   ├── Statistics.cpp    # Performance metrics
│   └── URLHashTable.cpp  # Hash table operations
├── Makefile              # Build configuration (Linux/macOS)
├── build.bat             # Build script (Windows)
└── README.md             # This file
Compilation & Execution
Windows
text
build.bat
.\url_hash.exe
Linux/macOS
bash
make
./url_hash
Manual Compilation
bash
g++ -std=c++11 -Iinclude -o url_hash src/*.cpp
Usage Guide
Initial Setup
Enter hash table size - Positive integer (recommended: 101, 1009, 10007)

Select hash function - 1=Division, 2=Universal

Select probing method - 1=Linear, 2=Quadratic

Enter URLs - Must start with http:// or https:// (type InsertionEnd when done)

Available Commands
Command	Usage	Purpose
hashSearch,<URL>	hashSearch,http://www.google.com/	Search for URL
hashDelete,<URL>	hashDelete,http://www.google.com/	Remove URL
hashDisplay	hashDisplay	Display table contents
hashStats	hashStats	Show performance metrics
hashReset	hashReset	Reset statistics
InsertionContinue	InsertionContinue	Add more URLs
End	End	Exit program
Example Session
text
Enter the hash table size: 101

Select hash function:
1. Division Hashing
2. Universal Hashing
Enter choice (1 or 2): 1
Using Division Hashing

Select probing method:
1. Linear Probing
2. Quadratic Probing
Enter choice (1 or 2): 1
Using Linear Probing

Enter URLs (type 'InsertionEnd' to finish)
http://www.google.com/
https://www.github.com/
https://www.stackoverflow.com/
InsertionEnd

Hash table size is: 101
Total URLs entered: 3

hashStats

Hash Function: Division Hashing
Probing Method: Linear Probing
Table Size: 101
Number of Elements: 3
Load Factor: 0.0297
Total Queries: 1
Average Comparisons per Query: 1.0000
Maximum Comparisons: 1
Average Time: 0.00000045 seconds
Performance Ratio: 1.00

hashSearch,http://www.google.com/

"http://www.google.com/" is found in the hash table.

End
Implementation Details
Hash Functions
Division Hashing Formula:

text
hash = (hash * 31 + char) % tableSize
Simple and fast

Works with any table size

Good for general-purpose use

Universal Hashing Formula:

text
#(x) = sum of char_value * 256^i
ha,b(x) = ((a * #(x) + b) mod k*Hsize) / k
where k=1000003, a=31415, b=27183
Provides theoretical collision guarantees

Uses Horner's rule for efficiency

Optimal for worst-case analysis

Probing Methods
Linear Probing: h(k,i) = (h(k) + i) mod m

Advantages: Cache-friendly, simple

Disadvantages: Primary clustering

Best for: Low load factors (< 0.5)

Quadratic Probing: h(k,i) = (h(k) + i²) mod m

Advantages: Reduces clustering

Disadvantages: Slightly more complex

Best for: Medium-high load factors (0.5-0.8)

Performance Analysis
Load Factor Impact
α < 0.5: Excellent performance, minimal collisions

0.5 ≤ α < 0.7: Good balance

0.7 ≤ α < 0.9: More collisions, acceptable

α ≥ 0.9: Performance degradation

Performance Ratio Guidelines
< 1.0: Excellent (nearly optimal)

1.0 - 1.5: Good

1.5 - 2.0: Acceptable

> 2.0: Consider resizing table

Input Validation
Table Size: Must be positive integer

Hash/Probing Choice: Must be 1 or 2

URLs: Must begin with http:// or https://

Commands: Must match exact format

Requirements
C++ Standard: C++11 or higher

Compilers: g++, clang, MSVC 2015+

Operating Systems: Windows, Linux, macOS

Memory: ~50MB minimum

Troubleshooting
Issue	Solution
Compilation error	Verify all .cpp files included, check -Iinclude flag
"Hash table is full"	Use larger table size
Poor performance (ratio > 2.0)	Increase table size or try Universal Hashing
Input validation loop	Ensure input format matches requirements
Future Enhancements
Implement dynamic rehashing when load factor exceeds 0.75

Add double hashing support

File-based URL input/output

Performance comparison reports

Visualization of table distribution

References
Cormen, Leiserson, Rivest, Stein - Introduction to Algorithms

Knuth - The Art of Computer Programming Vol. 3

Carter & Wegman - Universal Hashing Theory (1979)

Status: Complete and Ready for Submission
Last Updated: November 2025
Version: 1.0
