def read_file(file_name):
    try:
        with open(file_name, "r", encoding="UTF-8") as file: 
            return file.read()
    except FileNotFoundError:
        print("File not found")
        return None

def count_characters(text):
    return len(text)

def count_words(text):
    words = text.split() # Splits text into words using a space (' ') as a separator
    return len(words)

def count_unique_words(text):
    words = text.lower().split()
    return len(set(words)) # Converts a list of words into a set (The set contains only unique elements, eliminating duplicates)


def main(file_name):
    text = read_file(file_name)
    if text is None:
        return
    
    print(f"Number of characters: {count_characters(text)}")
    print(f"Number of words: {count_words(text)}")
    print(f"Number of unique words: {count_unique_words(text)}")

if __name__ == "__main__":
    main("D:\SB Python\Project python\Text Analyzer\sample.txt")