#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""rerange the left 95% words sequence by hamming distance in order to get the
maximum compress ratio
refer https://www.lingholic.com/how-many-words-do-i-need-to-know/
Usage: python rerange_words src_word_list.txt rerangeed_word_list.txt
"""

import sys
import codecs

def hamming_distance(str1, str2):
    """calculate the hamming distance of two strings."""
    # ensure length of str1 >= str2
    if len(str2) > len(str1):
        str1, str2 = str2, str1
    # distance is difference in length + differing chars
    distance = len(str1) - len(str2)
    for index, value in enumerate(str2):
        if value != str1[index]:
            distance += 1

    return distance

def get_min_distance_word(word_list, src_word):
    """Returns the min distance word from the word_list."""
    dst_word = ''
    min_distance = sys.maxsize
    for word in word_list:
        distance = hamming_distance(src_word, word)
        if min_distance > distance:
            min_distance = distance
            dst_word = word
        if min_distance == 1:
            break
    return dst_word

def sort_by_hamming(word_list):
    """Sort the word_list by the hamming distance."""
    result = []
    src_word = ''

    while len(word_list) > 0:
        dst_word = get_min_distance_word(word_list, src_word)
        src_word = dst_word
        word_list.remove(dst_word)
        result.append(src_word)

    return result

def rerange(raw_file, out_file):
    """Split word list to two parts: the top5 and left.
       Do resort the left words with hamming distance.
       Merge the two parts and write to the out file."""
    word_list = []
    for line in codecs.open(raw_file, encoding='utf-8-sig').readlines():
        word = line.rstrip().split()[0]
        word_list.append(word)

    word_count = len(word_list)
    top5_count = int(word_count*0.05)
    if top5_count > 5000:
        top5_count = 5000
    top5_list = word_list[:top5_count]
    left_list = word_list[top5_count:]

    result = top5_list
    result += sort_by_hamming(left_list)

    # ourput
    with codecs.open(out_file, 'w') as out:
        for word in result:
            out.write("%s\n" % word.encode('utf-8'))

if __name__ == '__main__':
    import time
    start = time.time()
    rerange(sys.argv[1], sys.argv[2])
    end = time.time()
    print (end-start)
