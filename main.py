import time

def word_is_compound(word, words_list):
    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in words_list and (suffix in words_list or word_is_compound(suffix, words_list)):
            return True
    return False

def find_longest_compounded_words(filename):
    start_time = time.time()

    with open(filename, 'r') as file:
        words = [line.strip() for line in file]

    words_set = set(words)
    compounded_words = [word for word in words if word_is_compound(word, words_set)]

    compounded_words.sort(key=len, reverse=True)

    longest = compounded_words[0] if compounded_words else None
    second_longest = compounded_words[1] if len(compounded_words) > 1 else None

    print("Longest Compounded Word:", longest)
    print("Second Longest Compounded Word:", second_longest)
    print("Time taken:", round(time.time() - start_time, 4), "seconds")

find_longest_compounded_words("Input_01.txt")
find_longest_compounded_words("Input_02.txt")
