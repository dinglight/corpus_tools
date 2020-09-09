"""count the every char in the input file
Usage:
    python char_frequency.py input_file.txt
"""

import sys
import codecs

def char_frequency(file_path):
    """count very char in the input file.
    Args:
      file_path: input file
    return:
      a dictionary of char and count
    """
    char_count_dict = dict()
    with codecs.open(file_path, encoding='utf-8-sig') as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            # jump over empty line
            if not line:
                continue

            word = line.split()[0]
            for char in word:
                keys = char_count_dict.keys()
                if char in keys:
                    char_count_dict[char] += 1
                else:
                    char_count_dict[char] = 1
    return char_count_dict

if __name__ == '__main__':
    print(sys.argv[1])
    print(char_frequency(sys.argv[1]))
