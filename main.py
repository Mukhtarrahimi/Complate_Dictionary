import json
import os
from difflib import get_close_matches

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
        # جستجوی هوشمند
        matches = get_close_matches(word, dic.keys(), n=3, cutoff=0.6)
        if matches:
            print(f"Word not found! Did you mean: {', '.join(matches)}?")
        else:
            print("Word not found!")


# Search a word-
def search_word(dic):
    word = input("Enter the word to search: ").strip()
    display_word(dic, word)


# Add a new word


def add_word(dic):
    word = input("New word: ").strip()
    if word in dic:
        print("This word already exists!")
        return
    meaning = input("Meaning: ").strip()
    examples = []
    while True:
        ex = input("Example (press Enter to stop): ").strip()
        if not ex:
            break
        examples.append(ex)
    synonyms = input("Synonyms (comma separated): ").strip().split(",")
    synonyms = [s.strip() for s in synonyms if s.strip()]
    antonyms = input("Antonyms (comma separated): ").strip().split(",")
    antonyms = [a.strip() for a in antonyms if a.strip()]
    category = input("Category: ").strip()
    tags = input("Tags (comma separated): ").strip().split(",")
    tags = [t.strip() for t in tags if t.strip()]

    dic[word] = {
        "meaning": meaning,
        "examples": examples,
        "synonyms": synonyms,
        "antonyms": antonyms,
        "category": category,
        "tags": tags,
    }
    save_dictionary(dic)
    print("Word added successfully!")


# Edit an existing word
def edit_word(dic):
    word = input("Enter the word to edit: ").strip()
    if word not in dic:
        print("This word does not exist!")
        return
    data = dic[word]
    print("Press Enter to keep current value.")
    meaning = input(f"Meaning ({data['meaning']}): ").strip()
    examples = input("Add more examples (comma separated, leave blank to skip): ").strip().split(",")
    synonyms = input(f"Synonyms ({', '.join(data['synonyms'])}): ").strip()
    antonyms = input(f"Antonyms ({', '.join(data['antonyms'])}): ").strip()
    category = input(f"Category ({data['category']}): ").strip()
    tags = input(f"Tags ({', '.join(data['tags'])}): ").strip()

    if meaning:
        data["meaning"] = meaning
    if examples and examples != ['']:
        data["examples"].extend([ex.strip() for ex in examples if ex.strip()])
    if synonyms:
        data["synonyms"] = [s.strip() for s in synonyms.split(",") if s.strip()]
    if antonyms:
        data["antonyms"] = [a.strip() for a in antonyms.split(",") if a.strip()]
    if category:
        data["category"] = category
    if tags:
        data["tags"] = [t.strip() for t in tags.split(",") if t.strip()]

    save_dictionary(dic)
    print("Word updated successfully!")


def show_stats(dic):
    print(f"\nTotal words: {len(dic)}")
    categories = {}
    for w in dic:
        cat = dic[w].get("category", "Uncategorized")
        categories[cat] = categories.get(cat, 0) + 1

        print("Words per category:")
        for cat, count in categories.items():
            print(f"  {cat}: {count}")

# Main menu
def main_menu():
    dictionary = load_dictionary()

    while True:
        print("\n--- Python Dictionary ---")
        print("1. Search word")
        print("2. Add new word")
        print("3. Edit word")
        print("4. Delete word")
        print("5. Show all words")
        print("6. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            search_word(dictionary)
        elif choice == "2":
            add_word(dictionary)
        elif choice == "3":
            edit_word(dictionary)
        elif choice == "4":
            delete_word(dictionary)
        elif choice == "5":
            if dictionary:
                for w in dictionary:
                    display_word(dictionary, w)
            else:
                print("Dictionary is empty.")
        elif choice == "5":
            if dictionary:
                for w in dictionary:
                    display_word(dictionary, w)
            else:
                print("Dictionary is empty.")

#
if __name__ == "__main__":
    main_menu()
