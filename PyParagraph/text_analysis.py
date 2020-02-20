import re
import os

textfile = os.path.join(".", "paragraph_1.txt")

wordCount = 0
sentenceCount = 0
AvgwordsLength = 0
AvgsentenceLength = 0
with open(textfile, "r") as data:
    dataread = data.read()
    wordslist = dataread.split()
    letterTotal = 0
    for word in wordslist:
        for char in word:
            if char in "abcdefghijklmnsopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
                letterTotal += 1
    AvgwordsLength += letterTotal / len(wordslist)
    wordCount += len(wordslist)
    sentencelist = re.split("(?<=[.!?]) +", dataread)
    sentenceCount = len(sentencelist)
    AvgsentenceLength = len(wordslist) / len(sentencelist)

print("Paragraph Analysis")
print("------------------")
print("Approximate Word Count: " + str(wordCount))
print("Approximate Sentence Count: " + str(sentenceCount))
print("Average Letter Count Per Word: " + str(AvgwordsLength))
print("Average Sentence Length: " + str(AvgsentenceLength))