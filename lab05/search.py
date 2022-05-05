import numpy as np

def find_N(string, pattern):
    """
    Naive algorithm

    Parameters:
    string (str): string to search
    pattern (str): searched text

    Returns:
    (list): positions of string in text (in ascending order)
    """
    print("STRING: {} PATTERN: {}".format(string, pattern))
    str_len = len(string)
    pattern_len = len(pattern)
    occurences = []

    if str_len < pattern_len:
        return []

    for i in range(str_len - pattern_len + 1):
        j = 0

        # Check for pattern for current i        
        while(j < pattern_len):
            if(string[i+j] != pattern[j]):
                break
            
            j += 1
    
        if(j==pattern_len):
            occurences.append(i)

    return occurences


def find_KMP(string, text):
    """
    Knuth-Morris-Pratt algorithm

    Parameters:
    string (str): string to search
    pattern (str): searched text

    Returns:
    (list): positions of string in text (in ascending order)
    """
    pass


def find_KR(string, text):
    """
    Karp-Rabin algorithm

    Parameters:
    string (str): string to search
    pattern (str): searched text

    Returns:
    (list): positions of string in text (in ascending order)
    """
    pass