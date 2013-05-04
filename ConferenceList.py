"""This is the code for creating the conference/journal
author list and the conference keywords list

Input: Conference.csv, Journal.csv, Paper.csv, PaperAuthor.csv

Output: ConJou_Authors.csv
    format:
         Conference/Journal ID, author ID

        ConJou_Keywords.csv
    format:
         Conference/Journal ID, distinguished keywords  

Author: Yifan Li
Version: 0.0.1

"""

import csv as csv

#Read the 'Paper.csv' file
Paper_object =csv.reader(open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\Paper.csv','rb'))
header = Paper_object.next() #Skip the first line as it is a header
Paper = [] #Creat a variable called 'Paper'
for row in Paper_object: #Skip through each row in the csv file
    Paper.append(row)#adding each row to the data variable
a = len(Paper)
print "The size of Paper is %d"%a


#Read the 'PaperAuthor.csv' file
PA_object =csv.reader(open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\PaperAuthor.csv','rb'))
header = PA_object.next() #Skip the first line as it is a header
PA = [] #Creat a variable called 'Paper'
for row in PA_object: #Skip through each row in the csv file
    PA.append(row)#adding each row to the data variable
	
print "The size of PA is %d"%len(PA)

#Make the paper list for each conference
Conference = [[a] for a in range(5223)] #5222 is the number of conferences, 0 represents not a conference
Journal = [[a] for a in range(22229)] #22228 is the number of Journals,0 represents not a journal
for paper in Paper:
	Conference[int(paper[3])].append(int(paper[0]))
	Journal[int(paper[4])].append(int(paper[0]))
#Make a keyword paper list
Paper_Key=[[a] for a in range(2259022)] #2259021 is the number of papers, 0 represent not a paper

for p in Paper:
	Paper_Key[int(p[0])].append(p[5])
	
	
#Make the author list for each paper
Paper_Author = [[a] for a in range(2259022)] #2259021 is the number of papers, 0 represent not a paper

for pa in PA:
	Paper_Author[int(pa[0])].append(int(pa[1]))
print len(Paper_Author)	

del Conference[0]
del Journal[0]

#Make the Author list
Conference_Author = [[a] for a in range(5223)]
Journal_Author = [[a] for a in range(22229)]

for Conf in Conference:
	ConfID = Conf[0]
	for paperID in Conf[1:(len(Conf) - 1)]:
		paper = Paper_Author[paperID]
		Conference_Author[ConfID].extend(paper[1:(len(paper) - 1)])

for Jou in Journal:
	JouID = Jou[0]
	for paperID in Jou[1:(len(Jou) - 1)]:
		paper = Paper_Author[paperID]
		Journal_Author[JouID].extend(paper[1:(len(paper) - 1)])

#Make the keyword list
Conference_Keyword = [[a] for a in range(5223)]
Journal_Keyword = [[a] for a in range(22229)]

for Conf in Conference:
	ConfID = Conf[0]
	for paperID in Conf[1:(len(Conf) - 1)]:
		paper = Paper_Key[paperID]    
		Conference_Keyword[ConfID].append(paper[1])

for Jou in Journal:
	JouID = Jou[0]
	for paperID in Jou[1:(len(Jou) - 1)]:
		paper = Paper_Key[paperID]
		Journal_Keyword[JouID].append(paper[1])
with open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\ConferenceAuthor.csv','wb') as csvfile:
	write_file_object = csv.writer(csvfile)
	for t in Conference_Author:
		write_file_object.writerow(t)

with open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\JournalAuthor.csv','wb') as csvfile:
	write_file_object = csv.writer(csvfile)
	for t in Journal_Author:
		write_file_object.writerow(t)

with open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\ConferenceKeyword.csv','wb') as csvfile:
	write_file_object = csv.writer(csvfile)
	for t in Conference_Keyword:
		write_file_object.writerow(t)	
		
with open('C:\Users\Eagles2F\Desktop\DionyBuddy\data\dataRev2\JournalKeyword.csv','wb') as csvfile:
	write_file_object = csv.writer(csvfile)
	for t in Journal_Keyword:
		write_file_object.writerow(t)	
print "Success!"