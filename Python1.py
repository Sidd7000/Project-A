from itertools import permutations

def find_anagrams(word):
    # Generate all possible permutations of the letters in the word
    all_permutations = [''.join(perm) for perm in permutations(word)]

    # Filter permutations to find valid words using a dictionary (you may need a word list file)
    with open('wordlist.txt', 'r') as wordlist_file:
        wordlist = set(word.strip().lower() for word in wordlist_file)

    anagrams = [perm for perm in all_permutations if perm in wordlist]

    return anagrams

if __name__ == "__main__":
    input_word = input("Enter a word: ").lower()
    anagrams = find_anagrams(input_word)

    if anagrams:
        print(f"Anagrams of '{input_word}':")
        for anagram in anagrams:
            print(anagram)
    else:
        print(f"No valid anagrams found for '{input_word}'.")
