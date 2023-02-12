import PyPDF2 as p
import nlp as n
import os
#import numpy as nump



def read_and_interpret_pdf(pdf):
    print(pdf)
    news_article = False
    research_article = False
    #pdf = os.path.dirname(os.path.abspath(pdf))
    pdfreader = p.PdfReader(open(pdf, 'rb'), strict = False)
    numPages = len(pdfreader.pages)
    p.PdfWriter().remove_images()

    text = ''

    for i in range(numPages):
        
        pageobj = pdfreader.pages[i]
        new_text = pageobj.extract_text()
        text+=new_text 

    if (text.find("Abstract\n") != -1):
        research_article = True 
    else :
        news_article = True


    print(research_article)
    print(news_article)

    title = ''
    summary = ''
    topic = ''
    if research_article:
        split = text.partition("Abstract\n")
        split2 = split[0].split(" ")
        split3 = split[2].partition("Introduction\n")
        summary = split3[0]
        
        title = n.get_title(split[0])
        split = title.partition("\n")
        title = split[0]
        topic = n.classify_research(title)
        print(title)
        print(topic)
        print(summary)

    if news_article: 
        split1 = text.partition('M')
        split2 = split1[2].partition("\n")
        title = split2[0]
        print(title)
        topic = n.classify_article(title)
        print(topic)
        summary = n.summarize(text)
        print(summary)

    return [title, summary, topic]



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


        






