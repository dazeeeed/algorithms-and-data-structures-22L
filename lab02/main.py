import time
import sys
import codecs
import numpy as np

def load_textfile(filename: str):
    try:
        with codecs.open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
            return content
    except:
        print("Couldn't read the file!")
        sys.exit(1)


def bubble_sort(data):
    tmp_data = data
    for pass_nr in range(len(tmp_data)-1, 0, -1):
        for i in range(pass_nr):
            if tmp_data[i] > tmp_data[i+1]:
                tmp_data[i], tmp_data[i+1] = tmp_data[i+1], tmp_data[i]
    
    return tmp_data


def insertion_sort(data):
    tmp_data = data
    for i in range(1, len(tmp_data)):
        j=i-1
        next_element = tmp_data[i]
        while(tmp_data[j] > next_element and j >= 0):
            tmp_data[j+1] = tmp_data[j]
            j=j-1
        tmp_data[j+1] = next_element
        
    return tmp_data


def merge_sort(data):
    tmp_data = data
    if(len(tmp_data) > 1):
        mid_idx = len(tmp_data) // 2
        left_data = tmp_data[:mid_idx]
        right_data = tmp_data[mid_idx:]

        merge_sort(left_data)
        merge_sort(right_data)
        
        a, b, c = 0, 0, 0 
        while((a < len(left_data) and (b < len(right_data)))):
            if(left_data[a] < right_data[b]):
                tmp_data[c] = left_data[a]
                a += 1
            else:
                tmp_data[c] = right_data[b]
                b += 1
            c += 1

        while(a < len(left_data)):
            tmp_data[c] = left_data[a]
            a += 1
            c += 1
        
        while(b < len(right_data)):
            tmp_data[c] = right_data[b]
            b += 1
            c += 1 

    return tmp_data


def quick_sort(data):
    pass


def main():
    N = 10
    illegal_chars = "()'-:,.?!;—"
    
    content = load_textfile("pan-tadeusz.txt").lower()
    for char in illegal_chars:
        content = content.replace(char, "")
    content = np.array(content.split()[:N])


    test_table = [10,4,5,1,3]
    sorted_content = merge_sort(test_table)
    print(sorted_content)
    # print(test_table)

    


if __name__ == "__main__":
    main()