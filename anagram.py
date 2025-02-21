from collections import Counter

# Checking the anagram
def check_anagrams(word1, word2):
    # Compares 2 objects. The first object (number of each letter in the first word) and the second object (number of each letter in the second word)
    return Counter(word1.lower()) == Counter(word2.lower()) 

# Search for anagram words from a list compared to a given word
def find_anagrams(word, word_list):
    # Creating a letter counter for a word
    word_counter = Counter(word.lower())
    # Search for anagrams through the list
    return [i for i in word_list if Counter(i.lower()) == word_counter]

def main():
    word = input('Input word for search anagram: ')
    words = ['part', 'trap', 'prat', 'rapt', 'tarp']

    anagrams = find_anagrams(word, words)

    if anagrams:
        print(f'Anagrams found: {", ".join(anagrams)}')
    else:
        print('Anagrams not found')


if __name__ == '__main__':
    main()
