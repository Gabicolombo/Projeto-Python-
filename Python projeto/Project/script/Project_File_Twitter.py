punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
outfile = open("resulting_data.csv", "w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
fileref = open(r"C:\Users\Gabriela\Documents\Python\Coursera\Project\project_twitter_data.csv")
lines = fileref.readlines()[1:]

def strip_punctuation(string):
    for c in range(len(string)):
        if string[c] in punctuation_chars:
            string = string.replace(string[c], ' ')
    string = string.replace(" ", "")
    return string

# lists of words to use
positive_words = []
pos_f = open(r"C:\Users\Gabriela\Documents\Python\Coursera\Project\positive_words.txt")
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        positive_words.append(lin.strip())


def get_pos(s):
    count = 0
    s = s.lower().split()
    for item in s:
        item = strip_punctuation(item)
        if item in positive_words:
            count +=1
    return count

negative_words = []
pos_f = open(r"C:\Users\Gabriela\Documents\Python\Coursera\Project\negative_words.txt")
for lin in pos_f:
    if lin[0] != ';' and lin[0] != '\n':
        negative_words.append(lin.strip())

def get_neg(s):
    count = 0
    s = s.lower().split()
    for item in s:
        item = strip_punctuation(item)
        if item in negative_words:
            count +=1
    return count


def writeInDataFile(outfile):
    for linesTD in lines:
        listTD = linesTD.strip().split(',')
        outfile.write(
            "{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]),
                                        (get_pos(listTD[0]) - get_neg(listTD[0]))))
        outfile.write("\n")


writeInDataFile(outfile)
fileref.close()
outfile.close()