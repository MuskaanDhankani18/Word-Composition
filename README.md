# Word-Composition
This program reads two input files (Input_01.txt and Input_02.txt), each containing a sorted list of words (one per line). It identifies:

* The longest compounded word (a word formed entirely from smaller words in the list).
* The second longest compounded word.
* The execution time taken to process the files.

## Design & Approach

### Efficient Data Storage:
The program uses a set to store words for O(1) lookup time, improving efficiency.

### Recursive Breakdown:
Each word is checked to see if it can be formed by combining other words in the set.

### Performance Optimization:
The algorithm ensures fast processing even for large files (100,000+ words).

## Steps to Execute:
1. Install Python (if not installed)
Ensure you have Python installed (version 3.x recommended).

2. Prepare Input Files
Create two text files:

  * Input_01.txt
  * Input_02.txt
Each file should contain a sorted list of words, one per line (lowercase, no spaces).

3. Run the Program
Save the provided Python script (main.py) and execute it using:

python main.py
