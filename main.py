from collections import OrderedDict
def main():
    base_path = "books/"
    file_name = "frankenstein.txt"
    file_path = base_path + file_name
    text = read_file(file_path)
    num_words = count_words(text)
    character_dict = count_characters(text)
    print(f"-- Begin report of {file_name} --")
    print(f"The book has {num_words} words.")
    print("")

    for character, count in character_dict.items():
        print(f"The '{character}' was found {count} times.")
    print("")
    print("-- End of report --")

def sort_dict_by_value(dictionary):
    sorted_dict = OrderedDict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

def count_characters(text):
    character_dict = {}
    for character in text:
        character_lowered = character.lower()
        if character_lowered.isalpha():
            if character_lowered in character_dict:
                character_dict[character_lowered] += 1
            else:
                character_dict[character_lowered] = 1

    sorted_dict = sort_dict_by_value(character_dict)

    return sorted_dict

def count_words(text):
    words = text.split()
    return len(words)

def read_file(file_path):
    try:
        with open(file_path) as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        text = ""
    return text

main()