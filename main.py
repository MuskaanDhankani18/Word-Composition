import time

def word_is_compounded(word, wordset):
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in wordset and (suffix in wordset or word_is_compounded(suffix, wordset)):
            return True
    return False

def longest_compounded_words(words):
    wordset = set(words)  # Store words in a set for quick lookup
    longest = ""
    second_longest = ""

    for word in words:
        if word_is_compounded(word, wordset):
            if len(word) > len(longest):
                second_longest = longest
                longest = word
            elif len(word) > len(second_longest):
                second_longest = word

    return longest, second_longest

# Read words from input files
def read_words_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Main function to process the files
def main():
    start_time = time.time()

    # Read words from files
    words1 = read_words_from_file("Input_01.txt") 
    words2 = read_words_from_file("Input_02.txt")

    # Find the longest and second longest compounded words
    longest1, second_longest1 = longest_compounded_words(words1)
    longest2, second_longest2 = longest_compounded_words(words2)

    time_taken = time.time() - start_time

    print("Output 1 : ")
    print(f"Longest compounded word: {longest1}")
    print(f"Second longest compounded word: {second_longest1}")
    print(f"Time taken: {time_taken:.4f} seconds")


    print("\nOutput 2 : ")
    print(f"Longest compounded word: {longest2}")
    print(f"Second longest compounded word: {second_longest2}")
    print(f"Time taken: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main()
