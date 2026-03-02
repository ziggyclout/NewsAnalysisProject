import string
import re
from collections import Counter

# File Handling

def load_article(filename):
    """Read the contents of a text file into a string."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""

# Text Cleaning

def clean_text(text):
    """Remove punctuation and convert to lowercase."""
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

# 1. Count Specific Word

def count_specific_word(text, search_word):
    """Count occurrences of a specific word. Edge case: return 0 if empty."""
    if not text.strip():
        return 0

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    count = 0
    for word in words:  # explicit for loop
        if word == search_word.lower():  # conditional
            count += 1
    return count

# 2. Identify Most Common Word

def identify_most_common_word(text):
    """Return the most common word. Edge case: None if empty."""
    if not text.strip():
        return None

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    if not words:  # conditional
        return None

    word_counts = Counter(words)
    # Using for loop to find the max manually (optional, shows for loop usage)
    most_common = None
    max_count = 0
    for word, freq in word_counts.items():
        if freq > max_count:  # conditional
            max_count = freq
            most_common = word
    return most_common

# 3. Calculate Average Word Length

def calculate_average_word_length(text):
    """Return average length of words. Edge case: return 0 if empty."""
    if not text.strip():
        return 0

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    if not words:
        return 0

    total_length = 0
    for word in words:  # explicit for loop
        total_length += len(word)
    return total_length / len(words)



# 4. Count Paragraphs

def count_paragraphs(text):
    """Count paragraphs separated by blank lines. Edge case: return 1 if empty."""
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")
    non_empty = []
    for p in paragraphs:  # explicit for loop
        if p.strip():  # conditional
            non_empty.append(p)
    return len(non_empty)

# 5. Count Sentences

def count_sentences(text):
    """Count sentences ending with ., !, or ?. Edge case: return 1 if empty."""
    if not text.strip():
        return 1

    sentences = re.split(r"[.!?]+", text)
    non_empty = []
    for s in sentences:  # explicit for loop
        if s.strip():  # conditional
            non_empty.append(s)
    return len(non_empty)

# Main Program

def main():
    filename = "news_article.txt"
    article_text = load_article(filename)

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

    # Most common word
    common_word = identify_most_common_word(article_text)
    print(f"Most common word: {common_word}")

    # Average word length
    avg_length = calculate_average_word_length(article_text)
    print(f"Average word length: {avg_length:.2f}")

    # Paragraph count
    paragraphs = count_paragraphs(article_text)
    print(f"Number of paragraphs: {paragraphs}")

    # Sentence count
    sentences = count_sentences(article_text)
    print(f"Number of sentences: {sentences}")

    print("\nAnalysis Complete.\n")


if __name__ == "__main__":
    main()