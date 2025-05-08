import os
from collections import Counter
import re
import unicodedata

def generate_ngrams(corpus_file, n):
    ngram_counter = Counter()
    
    with open(corpus_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Tokenization: split on spaces
            words = line.strip().split()
            
            # Add n-1 start markers and one end marker
            words = ["<s>"] + words + ["</s>"]
            
            # Extract n-grams
            for i in range(len(words) - n + 1):
                ngram = tuple(words[i:i + n])
                ngram_counter[ngram] += 1
    
    return ngram_counter

def get_most_frequent_words(corpus_file, threshold=0.02):
    """Identifie les mots les plus fréquents dans un corpus."""
    word_counter = Counter()
    total_words = 0

    with open(corpus_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = preprocess_text(line)
            words = line.split()
            word_counter.update(words)
            total_words += len(words)

    frequent_words = {word for word, count in word_counter.items() if count / total_words > threshold}
    return frequent_words

def preprocess_text(line):
    """Nettoyage de texte : minuscule, suppression des accents, des nombres isolés et de la ponctuation."""
    line = line.lower()
    line = unicodedata.normalize("NFKD", line).encode("ascii", "ignore").decode("utf-8")
    line = re.sub(r"\b\d+\b", " ", line)
    line = re.sub(r"[^\w\s']", " ", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line


def process_language_files(directory, n):
    # Charger les mots les plus fréquents pour chaque langue
    language_frequent_words = {}
    for filename in os.listdir(language_files_directory):
        if filename.endswith("_cleaned.txt"):
            language = filename.split("_")[0]
            file_path = os.path.join(language_files_directory, filename)
            language_frequent_words[language] = get_most_frequent_words(file_path)

            print(f"Processing file: {filename}")
            
            # Generate n-grams for the current file
            ngram_counter = generate_ngrams(file_path, n)
            
            # Create an output file for each input file
            output_filename = f"{os.path.splitext(filename)[0]}_ngrams.txt"
            output_path = os.path.join(directory, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as output_file:
                # Write n-grams and their counts to the output file
                for ngram, count in ngram_counter.items():
                    output_file.write(" ".join(ngram) + " " + str(count) + "\n")
            
            print(f"Output written to: {output_filename}")

# Usage
language_files_directory = "language_files2"  # Replace with the correct path
n = 3  # Example n-gram size, change as needed
process_language_files(language_files_directory, n)
