import string
import re
from collections import Counter

# File Handling

def load_article(filename):
    """
    Reads the content of a text file and returns it as a string.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return ""

# Text Cleaning Utility

def clean_text(text):
    """
    Removes punctuation and converts text to lowercase.
    """
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

# 1. Count Specific Word

def count_specific_word(text, search_word):
    """
    Counts occurrences of a specific word in the text.
    Returns integer count.
    Edge case: empty text returns 0.
    """
    if not text.strip():
        return 0

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    return words.count(search_word.lower())

# 2. Identify Most Common Word

def identify_most_common_word(text):
    """
    Identifies and returns the most common word.
    Edge case: empty string returns None.
    """
    if not text.strip():
        return None

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    if not words:
        return None

    word_counts = Counter(words)
    return word_counts.most_common(1)[0][0]

# 3. Calculate Average Word Length

def calculate_average_word_length(text):
    """
    Calculates average length of words.
    Excludes punctuation.
    Edge case: empty string returns 0.
    """
    if not text.strip():
        return 0

    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    if not words:
        return 0

    total_characters = sum(len(word) for word in words)
    return total_characters / len(words)

# 4. Count Paragraphs

def count_paragraphs(text):
    """
    Counts number of paragraphs.
    Paragraphs are separated by empty lines.
    Edge case: empty string returns 1.
    """
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")
    non_empty_paragraphs = [p for p in paragraphs if p.strip()]

    return len(non_empty_paragraphs)

# 5. Count Sentences

def count_sentences(text):
    """
    Counts number of sentences.
    Sentences end with '.', '!', or '?'.
    Edge case: empty string returns 1.
    """
    if not text.strip():
        return 1

    sentences = re.split(r"[.!?]+", text)
    non_empty_sentences = [s for s in sentences if s.strip()]

    return len(non_empty_sentences)

# Main Program Execution

def main():
    """
    Main driver function.
    """
    filename = "news_article.txt"
    article_text = load_article(filename)

    print("\n==============================")
    print("  NEWS ARTICLE TEXT ANALYSIS")
    print("==============================\n")

    # Count specific word
    search_word = input("Enter a word to count: ").strip()
    word_count = count_specific_word(article_text, search_word)

    print(f"\nThe word '{search_word}' appears {word_count} time(s).")

    # Most common word
    most_common = identify_most_common_word(article_text)
    print(f"\nMost common word: {most_common}")

    # Average word length
    average_length = calculate_average_word_length(article_text)
    print(f"\nAverage word length: {average_length:.2f} characters")

    # Paragraph count
    paragraph_total = count_paragraphs(article_text)
    print(f"\nNumber of paragraphs: {paragraph_total}")

    # Sentence count
    sentence_total = count_sentences(article_text)
    print(f"\nNumber of sentences: {sentence_total}")

    print("\nAnalysis Complete.\n")


if __name__ == "__main__":
    main()