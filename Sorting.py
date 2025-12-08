from collections import Counter

s = "tree"
print(''.join(char * count for char, count in Counter(s).most_common()))
