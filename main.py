import json
import os

FILE_NAME = "dictionary.json"


# Load dictionary from file
def load_dictionary():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# Save dictionary to file
def save_dictionary(dic):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)


# Display a word and its details
def display_word(dic, word):
    if word in dic:
        print(f"\nWord: {word}")
        print(f"Meaning: {dic[word]['meaning']}")
        print(f"Example: {dic[word]['example']}")
        print(
            f"Synonyms: {', '.join(dic[word]['synonyms']) if dic[word]['synonyms'] else 'None'}"
        )
        print(
            f"Antonyms: {', '.join(dic[word]['antonyms']) if dic[word]['antonyms'] else 'None'}"
        )
    else:
        print("Word not found!")
