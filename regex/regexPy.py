# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

import re

# print(dir(re))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

findall = re.findall("ain", txt)
print(findall)

split = re.split("\s", txt, 1)
print(split)

# txt = re.sub("\s", "👍 ", txt, 1)
sub = re.sub("\s", "👍 ", txt, 1)
print(sub)
