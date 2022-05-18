import numpy as np
import random
import time
import search
from collections import defaultdict
import codecs
from utilities import load_textfile, FirstWords
import matplotlib.pyplot as plt
import os

LEN_RANDOM_TEXT = 1000


def random_validation_single_pattern(pattern: str):
    random_text = ''.join(random.choices('ab', k=LEN_RANDOM_TEXT))
    # print("Text: {}".format(random_text))

    results = defaultdict(list)
    results['N'] = search.find_N(random_text, pattern)
    results['KMP'] = search.find_KMP(random_text, pattern)
    results['KR'] = search.find_KR(random_text, pattern)

    are_results_equal = (results['N'] == results['KMP']) & \
                        (results['N'] == results['KR']) & \
                        (results['KMP'] == results['KR'])

    return results, are_results_equal


def random_validation_random_patterns(tries: int):
    are_results_equal_list = []
    for _ in range(tries):
        rand_pattern_len = random.randint(a=0, b=(LEN_RANDOM_TEXT // 10))
        random_pattern = ''.join(random.choices('ab', k=rand_pattern_len))
        _, are_results_equal = random_validation_single_pattern(random_pattern)
        are_results_equal_list.append(are_results_equal)

    return are_results_equal_list


def main():
    # # VALIDATION OF SINGLE PATTERN
    # results, are_results_equal = random_validation_single_pattern('as')
    # print(are_results_equal)

    # # VALIDATION OF `tries` PATTERNS
    # result = random_validation_random_patterns(tries=100)
    # print("Are results the same? {}".format(all(result)))

    filename = "../lab02/pan-tadeusz.txt"
    content = load_textfile(filename)
    fw = FirstWords(filename)

    search_algorithms = [search.find_N, search.find_KMP, search.find_KR]
    # search_algorithms = [search.find_N]

    # n_words_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    n_words_list = [10, 20, 30, 50, 100, 200, 300, 500, 750, 1000]
    # n_words_list = [10, 20]

    results = defaultdict(dict)
    fig, ax = plt.subplots()

    for search_algorithm in search_algorithms:
        for n_words in n_words_list:
            time_start = time.time()
            print("Algorithm: {} Words: {}".format(search_algorithm.__name__, n_words))

            for word in fw.get(n_words):
                search_algorithm(text=content, pattern=word)

            time_end = time.time()
            results[search_algorithm.__name__][n_words] = time_end - time_start

        ax.plot(results.get(search_algorithm.__name__).keys(), results.get(search_algorithm.__name__).values(),
                label=search_algorithm.__name__)

    # print(results)
    ax.set_xlabel("N")
    ax.set_ylabel("Time [s]")
    ax.legend()
    fig.tight_layout()
    plt.savefig(os.path.join("graphics", "plot.pdf"))
    plt.show()


if __name__ == '__main__':
    main()