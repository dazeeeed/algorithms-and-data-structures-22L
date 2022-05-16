import numpy as np

def find_N(text: str, pattern: str):
    """
    Naive algorithm

    Parameters:
    text (str): text being search
    pattern (str): pattern to look for in text

    Returns:
    (list): positions of pattern in text (in ascending order)
    """
    print("TEXT: {} PATTERN: {}".format(text, pattern))
    LEN_TEXT = len(text)
    LEN_PATTERN = len(pattern)
    occurences = []

    if LEN_TEXT < LEN_PATTERN:
        return []

    for i in range(LEN_TEXT - LEN_PATTERN + 1):
        j = 0
        # Check for pattern for current i        
        while(j < LEN_PATTERN):
            if(text[i+j] != pattern[j]):
                break
            j += 1
    
        if(j == LEN_PATTERN):
            occurences.append(i)

    return occurences


def find_KMP(text: str, pattern: str):
    """
    Knuth-Morris-Pratt algorithm

    Parameters:
    text (str): text being search
    pattern (str): pattern to look for in text

    Returns:
    (list): positions of pattern in text (in ascending order)
    """
    print("TEXT: {} PATTERN: {}".format(text, pattern))
    occurences = []

    LEN_TEXT = len(text)
    LEN_PATTERN = len(pattern)

    # longest prefix suffix 
    lps = np.zeros(LEN_PATTERN, dtype=np.int32)
    compute_lps(pattern, LEN_PATTERN, lps)
    
    idx_text = 0
    idx_pattern = 0
    while idx_text < LEN_TEXT:
        if pattern[idx_pattern] == text[idx_text]:
            idx_text += 1
            idx_pattern += 1
        
        if idx_pattern == LEN_PATTERN:
            occurences.append(idx_text - idx_pattern)
            idx_pattern = lps[idx_pattern - 1]
        elif(idx_text < LEN_TEXT) and (pattern[idx_pattern] != text[idx_text]):
            if idx_pattern != 0:
                idx_pattern = lps[idx_pattern - 1]
            else:
                idx_text += 1

    return occurences

def compute_lps(pattern: str, len_pattern: int, lps: list):
    len_prev_lps = 0

    lps[0] = 0
    i = 1

    while i < len_pattern:
        if pattern[i] == pattern[len_prev_lps]:
            len_prev_lps += 1
            lps[i] = len_prev_lps
            i += 1
        else:
            if len_prev_lps != 0:
                len_prev_lps = lps[len_prev_lps - 1]
            else:
                lps[i] = 0
                i += 1



def find_KR(text: str, pattern: str):
    """
    Karp-Rabin algorithm

    Parameters:
    text (str): text being search
    pattern (str): pattern to look for in text

    Returns:
    (list): positions of pattern in text (in ascending order)
    """
    print("TEXT: {} PATTERN: {}".format(text, pattern))
    occurences = []

    # M -> LEN_PATTERN
    # N -> LEN_TEXT
    # p -> hash_pattern
    # t -> hash_str
    LEN_POSSIBLE_CHARS = 256 # number of characters in extended ASCII (8-bit)
    PRIME_NUMBER = 257
    LEN_TEXT = len(text)
    LEN_PATTERN = len(pattern)
    H = LEN_POSSIBLE_CHARS ** (LEN_PATTERN - 1) % PRIME_NUMBER
    # H = 1
    # for _ in range(LEN_PATTERN):
    #     H = (H * LEN_POSSIBLE_CHARS) % PRIME_NUMBER
    
    hash_text_window = 0
    hash_pattern = 0
    
    # Calculate hash values of pattern and first window
    for i in range(LEN_PATTERN - 1):
        hash_pattern = (LEN_POSSIBLE_CHARS * hash_pattern + ord(pattern[i])) % PRIME_NUMBER
        hash_text_window = (LEN_POSSIBLE_CHARS * hash_text_window + ord(text[i])) % PRIME_NUMBER
    
    # Search for pattern
    # SOMETHING DOESNT WORK HERE!

    for i in range(LEN_TEXT - LEN_PATTERN + 1):
        print("hash pattern: {} hash text window: {}". format(hash_pattern, hash_text_window))
        if hash_pattern == hash_text_window:
            print("insisde hash comparision")
            chars_found = 0
            for j in range(LEN_PATTERN):
                if(text[i+j] != pattern[j]):
                    break
                chars_found += 1
            
            if chars_found == LEN_PATTERN:
                occurences.append(i)
    
        # Calculate hash values for next window
        if i < LEN_TEXT - LEN_PATTERN:
            hash_text_window = (LEN_POSSIBLE_CHARS * (hash_text_window - ord(text[i]) * H) +
                ord(text[i + LEN_PATTERN])) % PRIME_NUMBER

            if hash_text_window < 0:
                hash_text_window += PRIME_NUMBER

    return occurences

    # TEXT: abcdabcdab abc PATTERN: abc