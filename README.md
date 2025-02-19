# Word-Composition
This program reads two input files (Input_01.txt and Input_02.txt), each containing a sorted list of words (one per line). It identifies:

* The longest compounded word (a word formed entirely from smaller words in the list).
* The second longest compounded word.
* The execution time taken to process the files.

Design Decisions & Approach

Efficient Data Storage:
The program uses a set to store words for O(1) lookup time, improving efficiency.

Recursive Breakdown:
Each word is checked to see if it can be formed by combining other words in the set.

Performance Optimization:
The algorithm ensures fast processing even for large files (100,000+ words).
