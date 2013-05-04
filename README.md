Conference_Cluster_Preprocessing
================================
这段python代码是用来将KDDCUP2013最原始的数据初步聚合的。

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

PS: conference里面的author会有重复的情况，请根据需要自行排除。
