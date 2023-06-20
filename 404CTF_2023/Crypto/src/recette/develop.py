
sentence = "2i1s4i1s15d1o49i1o4d1o3i1o15d1o22d1o20d1o19i1o7d1o5d1o2i1o55i1o1d1o19d1o17d1o18d1o29i1o12i1o26i1o8d1o59d1o27i1o6d1o17i1o12d1o7d1o5i1o1d1o2d1o12i1o9d1o26d1o"

import re

# Use regular expression to match digits (\d+) and non-digits (\D+)
pattern = re.compile(r"(\d+|\D+)")

# Use the findall() method to find all matches in the string
matches = pattern.findall(sentence)

# Print the matches
print(matches)

result = ""

for i in range(len(matches)):
    # if i is a number
    if matches[i].isdigit():
        # Take the following character and repeat it i times
        result += matches[i + 1] * int(matches[i])
    else:
        pass

print(result)