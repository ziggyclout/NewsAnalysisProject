import string
import re
from collections import Counter

# 1. Count Specific Word

def count_specific_word(text, search_word):
    """Count occurrences of a specific word. Returns 0 if empty."""
    if not text.strip():  # conditional
        return 0

    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()

    count = 0
    for word in words:  # for loop
        if word == search_word.lower():  # conditional
            count += 1
    return count

# 2. Identify Most Common Word

def identify_most_common_word(text):
    """Return the most common word. Returns None if empty."""
    if not text.strip():  # conditional
        return None

    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()

    if not words:  # conditional
        return None

    word_counts = Counter(words)
    most_common = None
    max_count = 0
    for word, freq in word_counts.items():  # for loop
        if freq > max_count:  # conditional
            max_count = freq
            most_common = word
    return most_common

# 3. Calculate Average Word Length

def calculate_average_word_length(text):
    """Calculate average word length. Returns 0 if empty."""
    if not text.strip():  # conditional
        return 0

    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()

    if not words:  # conditional
        return 0

    total_length = 0
    for word in words:  # for loop
        total_length += len(word)
    return total_length / len(words)

# 4. Count Paragraphs

def count_paragraphs(text):
    """Count paragraphs separated by empty lines. Returns 1 if empty."""
    if not text.strip():  # conditional
        return 1

    paragraphs = text.split("\n\n")
    non_empty = []
    for p in paragraphs:  # for loop
        if p.strip():  # conditional
            non_empty.append(p)
    return len(non_empty)

# 5. Count Sentences

def count_sentences(text):
    """Count sentences ending with ., !, or ?. Returns 1 if empty."""
    if not text.strip():  # conditional
        return 1

    sentences = re.split(r"[.!?]+", text)
    non_empty = []
    for s in sentences:  # for loop
        if s.strip():  # conditional
            non_empty.append(s)
    return len(non_empty)

# Main program for user interaction

def main():
    filename = "news_article.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            article_text = file.read()
    except FileNotFoundError:
        print("Error: news_article.txt not found.")
        return

    print("\n==============================")
    print("   NEWS ARTICLE ANALYSIS")
    print("==============================\n")

    # While loop for repeated word count
    while True:
        search_word = input("Enter a word to count (or type 'exit' to finish): ").strip()
        if search_word.lower() == "exit":  # conditional
            break
        count = count_specific_word(article_text, search_word)
        print(f"The word '{search_word}' appears {count} time(s).\n")

    print(f"Most common word: {identify_most_common_word(article_text)}")
    print(f"Average word length: {calculate_average_word_length(article_text):.2f}")
    print(f"Number of paragraphs: {count_paragraphs(article_text)}")
    print(f"Number of sentences: {count_sentences(article_text)}")

    print("\nAnalysis Complete.\n")


# Ensure functions can be imported by autograder
if __name__ == "__main__":
    main()