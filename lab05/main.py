import numpy as np
import search


def main():
    # result = search.find_N('', 'ab')
    # result = search.find_KR('abcdabcdababc', 'abc')
    result = search.find_KMP('abcdabcdababc', 'abc')

    print(result)


if __name__=='__main__':
    main()