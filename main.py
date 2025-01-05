def main():
    word_count = 0
    character_count = {}
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)

    print("--- Printing report of books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    for char in character_count:
        print(f"The '{char}' as found {character_count[char]} times.")
    print("--- Report Complete ---")

def count_words(text):
    return len(text.split())

def count_characters(text: str):
    characters = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        c = char.lower()
        if c in alphabet:
            if c not in characters:
                characters[c] = 0
            characters[c] += 1

    return characters

main()
