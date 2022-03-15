import re


def string_input():
    string = input("Input string: ")
    string = re.sub('[,.!?\n]', '', string)
    return string


def input_k_n():
    k = input("Input k: ")
    n = input("Input n: ")
    if (k == "" and n == ""):
        k = 10
        n = 4

    k = int(k)
    n = int(n)
    return [k, n]


def get_list(string: str):
    words = string.split()
    return words


def get_amount_of_words(words: list):
    words_count = {}
    for item in words:
        if words_count.__contains__(item):
            continue
        words_count[item] = words.count(item)
    return words_count


def get_average_amount_of_words(words: list, words_count: dict):
    return len(words) / len(words_count)


def get_median_amount_of_words(words_amount: dict):
    words = words_amount.values()
    words = list(words)
    if len(words) % 2 == 0:
        med = (words[int(len(words) / 2 - 1)] + words[int(len(words) / 2)]) / 2
    else:
        med = words[len(words) // 2]
    return med


def get_ngrams(words: list, string: str, n: int):
    ngram = {}
    for item in words:
        for i in range(len(item)):
            if i + n > len(item):
                break
            if not ngram.__contains__(item[i:i + n]):
                ngram[item[i: i + n]] = string.count(item[i:i + n])
    return ngram


def show_top_ngrams(ngram: dict, k: int):
    ngram = sorted(ngram, key=ngram.get)
    ngram.reverse()
    for i in range(k if len(ngram) > k else len(ngram)):
        print(ngram[i])


def main():
    k, n = input_k_n()
    string = string_input()

    words = get_list(string)
    words_amount = get_amount_of_words(words)

    print("Words amount: " + str(words_amount))
    average_words_amount = get_average_amount_of_words(words, words_amount)

    print("Average words amount: " + str(average_words_amount))
    median_words_amount = get_median_amount_of_words(words_amount)

    print("Median words amount: " + str(median_words_amount))
    n_grams = get_ngrams(words, string, n)
    show_top_ngrams(n_grams, k)


if __name__ == '__main__':
    main()