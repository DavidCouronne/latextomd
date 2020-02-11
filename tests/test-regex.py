import re

regex = r"\\begin{exercice}(\[(?P<block_title>.*?)\])?(\[(?P<block_bareme>.*?)\])?"

test_str = "\\begin{exercice}[titre][2]"

matches = re.finditer(regex, test_str, re.MULTILINE)

titre = ""
bareme = ""

for matchNum, match in enumerate(matches, start=1):
    titre = match.group(2)
    if match.group(4):
        bareme = f"{match.group(4)} points"
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    print ("{group}".format(groupNum = 2,group = match.group(2)))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

print(titre)
print(bareme)
