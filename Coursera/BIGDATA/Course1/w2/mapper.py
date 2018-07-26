import sys
import re
for line in sys.stdin:
    article_id, content = line.split("\t",1)
    #words = content.split()
    words = re.split("\W+", content)
    for word in words:
        print(word, 1,sep = "\t")

