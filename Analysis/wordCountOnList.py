import sys
import re

#Usage
# python wordCountOnList.py ./targetWords ./targetText

def main(listPath, textPath):
    wordList = open(listPath, "r").read().split("\n")[:-1]
    wordDict = {}
    for word in wordList:
        wordDict[word] = 0


    text = open(textPath, "r").read()
    textWordList = re.split('\W+', text)


    for word in textWordList:
        print(word)
        if word.lower() in wordList:
            wordDict[word.lower()] += 1

    print("Top 4 words found and number of occurances")
    top4 = sorted(wordDict.items(), key = lambda x:x[1])
    print(top4[-4:])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])