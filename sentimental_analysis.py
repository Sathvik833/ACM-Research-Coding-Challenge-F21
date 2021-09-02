#Import libraries
from textblob import TextBlob
from nltk.tokenize import sent_tokenize

#Open the file for reading
file = open('C:/Users/12628/Documents/SA/input', 'r')

#Create empty string
temp = ''

#Read the file and append the lines from the file to the string and then close the file
for x in file:
    temp += x.split('\n')[0] + ' '
file.close()

#Create a extra list to contain the filtered lines
filtered_lines = []

#Tokenize the list in order to form sentences accurately
tokenized_list = sent_tokenize(temp)

#Get rid of any junk characters that sentences contain
temp = ''
for x in tokenized_list:
    count = 0
    temp_2 = ''
    for z in x.split(' '):
        count += 1
        for i in z:
            if i.isalnum():
                temp += i
        temp_2 += temp
        if count != len(x.split(' ')):
            temp_2 += ' '
        temp = ''
    filtered_lines.append(temp_2)

#Evaluate the total score of the sentimental analysis from the scale of -1 to 1
#Also evaluate the sentimental anaylsis score of each line too
total_score = 0
SA_score = []
Individual_line_scores = {}
for x in filtered_lines:
    text = TextBlob(x)
    sentiment_score = text.sentiment.polarity
    Individual_line_scores[x] = sentiment_score
    total_score += sentiment_score

#Print individual line scores
for x in Individual_line_scores:
    print(Individual_line_scores[x])

print()
#Print total score
print(total_score/(len(Individual_line_scores)))