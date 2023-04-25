def output(*args):
    print(f"{'=' * 30}\n{args[0]}{'=' * 30}")
    for string in args[1]:
        print(string)


def main():
    strings = [
        'Hello! How are you?',
        'Wow! It`s amazing!',
        'How old are you?',
        'Are you joking, John? What is it?',
        "Hello world!",
        'Testing string in lab#5'
    ]

    max_len = max(len(string) for string in strings)

    output("Начальные строки\n", strings)

    for string in strings:
        if len(string) > max_len:
            index = strings.index(string)
            strings[index] = string[:max_len]
        elif len(string) < max_len:
            index = strings.index(string)
            count_missing_char = max_len - len(string)
            strings[index] += '_' * count_missing_char

    output("Строки после изменения\n", strings)


if __name__ == '__main__':
    main()