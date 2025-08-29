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
    example = input("Example: ").strip()
    synonyms = input("Synonyms (comma separated): ").strip().split(",")
    synonyms = [s.strip() for s in synonyms if s.strip()]
    antonyms = input("Antonyms (comma separated): ").strip().split(",")
    antonyms = [a.strip() for a in antonyms if a.strip()]
    #
    dic[word] = {
        "meaning": meaning,
        "example": example,
        "synonyms": synonyms,
        "antonyms": antonyms,
    }
    save_dictionary(dic)
    print("Word added successfully!")


# Edit an existing word
def edit_word(dic):
    word = input("Enter the word to edit: ").strip()
    if word not in dic:
        print("This word does not exist!")
        return
    print("Press Enter to keep the current value.")
    meaning = input(f"Meaning ({dic[word]['meaning']}): ").strip()
    example = input(f"Example ({dic[word]['example']}): ").strip()
    synonyms = input(f"Synonyms ({', '.join(dic[word]['synonyms'])}): ").strip()
    antonyms = input(f"Antonyms ({', '.join(dic[word]['antonyms'])}): ").strip()

    if meaning:
        dic[word]["meaning"] = meaning
    if example:
        dic[word]["example"] = example
    if synonyms:
        dic[word]["synonyms"] = [s.strip() for s in synonyms.split(",") if s.strip()]
    if antonyms:
        dic[word]["antonyms"] = [a.strip() for a in antonyms.split(",") if a.strip()]

    save_dictionary(dic)
    print("Word updated successfully!")


def delete_word(dic):
    word = input("Enter the word to delete: ").strip()
    if word in dic:
        confirm = (
            input(f"Are you sure you want to delete '{word}'? (y/n): ").strip().lower()
        )
        if confirm == "y":
            del dic[word]
            save_dictionary(dic)
            print("Word deleted successfully!")
    else:
        print("Word not found!")


def show_stats(dic):
    print(f"\nTotal words: {len(dic)}")
    categories = {}
    for w in dic:
        cat = dic[w].get("category", "Uncategorized")
        categories[cat] = categories.get(cat, 0) + 1


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
