def main():
    path = "books/frankenstein.txt"
    text = get_file_contents(path)

    print(f"--- Book report for {path} ---")
    print(f"Number of words: {count_words(text)}\n")

    letter_count = count_letters(text)
    sorted_letters = sorted(
        [letter for letter in letter_count.keys() if letter.isalpha()]
    )
    for letter in sorted_letters:
        print(f"The '{letter}' character was found {letter_count[letter]} times")

    print(f"\n--- End of report ---")


def get_file_contents(path):
    with open(path) as f:
        return f.read()


def count_words(file_contents):
    return len(file_contents.split())


def count_letters(file_contents):
    letter_count = {}
    for word in file_contents.lower().split():
        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count


main()
