import PyPDF2 as p
from PyDictionary import PyDictionary
dictionary = PyDictionary()

news_article = False
research_article = False

pdf = p.PdfReader(open('2302.02718.pdf', 'rb'), strict = False)
numPages = len(pdf.pages)
p.PdfWriter().remove_images()

text = ''

for i in range(numPages):
    
    pageobj = pdf.pages[i]
    new_text = pageobj.extract_text()
    text+=new_text 

if (text.find("Abstract\n") != -1):
    research_article = True 
else :
    news_article = True


print(research_article)
print(news_article)

title = ''

if research_article:
    split = text.partition("Abstract")
    split2 = split.split(" ")
    for i in range(len(split2)):
        if  dictionary.meaning(split2[i],True) is None:
            break
        else: 
            title += split2[i]
    #split = text.partition("\n")
    #title = split[0]
    print(title)

if news_article: 
    split1 = text.partition('M')
    split2 = split1[2].partition("\n")
    title = split2[0]
    print(title)





""" file = open("text.txt", 'w', encoding="utf-8")
title = ''
for i in range(numPages) :
    pageobj = pdf.pages[i]
    text = pageobj.extract_text()
    file.writelines(text)
file.close()

file = open("text.txt", 'r', encoding="utf-8")
firstLine = file.readline()

for i in range(15):


file.close()
split1 = firstLine.split("M")
title = split1[1]
print(title) """


    






