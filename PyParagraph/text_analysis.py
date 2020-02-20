import re
import os

textfile = os.path.join(".", "example.txt")

wordCount = 0
sentenceCount = 0
wordsLength = {}
sentenceLength = {}
with open(textfile, "r") as data:
    dataread = data.read()
    wordslist = dataread.split()
    wordCount += len(wordslist)
    sentencelist = re.split("(?<=[.!?]) +", dataread)
    sentenceCount = len(sentencelist)
    