from collections import Counter
def most_common_characters(s):
    counter = Counter(s)
    most_common = counter.most_common()
    most_common_sorted = sorted(most_common, key=lambda x: (-x[1], x[0]))
    for char, count in most_common_sorted[:3]:
        print(char, count)
s = "aabbbccde"
most_common_characters(s)
