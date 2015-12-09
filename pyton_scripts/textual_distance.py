#!/usr/bin/python

import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer

# connect to the database 
connection = psycopg2.connect(host='localhost', port='5432', database='comment_classification', user='evermal', password= '')
cursor = connection.cursor()

cursor.execute("select commenttext from processed_comment where classification = 'DESIGN'")
processed_comment_list = cursor.fetchall()

formatted_comment_list = []
for processed_comment in processed_comment_list:
    formatted_comment = " ".join(processed_comment[0].lower().replace('\n','').replace('\r\n', '').replace('\r', '').replace('\t', '').replace('//','').replace('/**','').replace('*/','').replace('/*','').replace('*','').replace(',','').replace(':','').replace('...','').replace(';','').split())
    formatted_comment_list.append(formatted_comment)

# print formatted_comment_list



# documents = [open(f) for f in text_files]
# tfidf = TfidfVectorizer().fit_transform(documents)
# # no need to normalize, since Vectorizer will return normalized tf-idf
# pairwise_similarity = tfidf * tfidf.T

vect = TfidfVectorizer(min_df=1)
X = vect.fit_transform(formatted_comment_list)
# tfidf = vect.fit_transform(formatted_comment_list)

# .A transforms a sparse matrix to a dense one, for the purpose of printing it. .T means transpose
# print (tfidf * tfidf.T).A

# print X
print X.mean(axis=0)


# array([[ 1.        ,  0.25082859,  0.39482963,  0.        ],
#        [ 0.25082859,  1.        ,  0.22057609,  0.        ],
#        [ 0.39482963,  0.22057609,  1.        ,  0.26264139],
#        [ 0.        ,  0.        ,  0.26264139,  1.        ]])

# import os
# import sys


# import re


# # password = sys.argv[1]


# # getting training dataset numbers
# technical_debt_regex = 'hack|retarded|at\sa\sloss|stupid|remove\sthis\scode|ugly|take\scare|something.s\sgone\swrong|nuke|is\sproblematic|may\scause\sproblem|hacky|unknown\swhy\swe\sever\sexperience\sthis|treat\sthis\sas\sa\ssoft\serror|silly|workaround\sfor\sbug|kludge|fixme|this\sisn.t\squite\sright|trial\sand\serror|give\sup|this\sis\swrong|hang\sour\sheads\sin\sshame|temporary\ssolution|causes\sissue|something\sbad\sis\sgoing\son|cause\sfor\sissue|this\sdoesn.t\slook\sright|is\sthis\snext\sline\ssafe|this\sindicates\sa\smore\sfundamental\sproblem|temporary\scrutch|this\scan\sbe\sa\smess|this\sisn.t\svery\ssolid|this\sis\stemporary\sand\swill\sgo\saway|is\sthis\sline\sreally\ssafe|there\sis\sa\sproblem|some\sfatal\serror|something\sserious\sis\swrong|don.t\suse\sthis|get\srid\sof\sthis|doubt\sthat\sthis\swould\swork|this\sis\sbs|give\sup\sand\sgo\saway|risk\sof\sthis\sblowing\sup|just\sabandon\sit|prolly\sa\sbug|probably\sa\sbug|hope\severything\swill\swork|toss\sit|barf|something\sbad\shappened|fix\sthis\scrap|yuck|certainly\sbuggy|remove\sme\sbefore\sproduction|you\scan\sbe\sunhappy\snow|this\sis\suncool|bail\sout|it\sdoesn.t\swork\syet|crap|inconsistency|abandon\sall\shope|kaboom'


# connection = None



# cursor.execute("select distinct(projectname) from comment_class order by 1")
# test_projects = cursor.fetchall()


# for test_project_result in test_projects:
#     test_project = test_project_result[0]
#     print "Analyzing project :" + test_project
#     td_counter = 0 
#     false_positive = 0
#     true_positive = 0
#     true_negative = 0
#     false_negative = 0
#     recall = 0.000
#     precision = 0.000
#     f1measure = 0.000


#     cursor.execute("select a.commenttext, a.classification from processed_comment a , comment_class b where a.commentclassid= b.id and a.classification in ('IMPLEMENTATION', 'WITHOUT_CLASSIFICATION','BUG_FIX_COMMENT') and b.projectname like '%"+test_project+"%'")
#     # cursor.execute("select a.commenttext, a.classification from processed_comment a , comment_class b where a.commentclassid= b.id and b.projectname like '%"+test_project+"%'")
#     comments = cursor.fetchall()
#     for comment in comments:
#         match = re.search(technical_debt_regex, comment[0])
#         if match:
#             td_counter = td_counter + 1
#             if comment[1] == 'WITHOUT_CLASSIFICATION' or comment[1] == 'BUG_FIX_COMMENT':
#                 false_positive = false_positive + 1
#             else:
#                 true_positive = true_positive + 1
#         else:
#             if comment[1] == 'WITHOUT_CLASSIFICATION' or comment[1] == 'BUG_FIX_COMMENT':
#                 true_negative = true_negative + 1
#             else:
#                 false_negative = false_negative + 1

#     recall = float(true_positive) / float((true_positive + false_negative))
#     precision = float(true_positive) / float((true_positive + false_positive))
#     # f1measure = ((precision * recall) / (precision + recall)) * 2
#     print 'Precision:  ' + str(precision)
#     print 'Recall:     '    + str(recall)
#     # print 'F1 measure: ' +str(f1measure)

#     print 'Total td found: '+str(td_counter)
#     print 'True positives: '+str(true_positive)
#     print 'True negatives: '+str(true_negative)
#     print 'False positives: '+str(false_positive)
#     print 'False negatives: '+str(false_negative)

                

#     