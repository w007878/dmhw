# Homework for Data Mining Course in SYSU

This course is named as 'Data Mining', given by Prof. Zheng Wei-shi. This is a half-term course without final exam. The task of it is to build three big projects. This repo is used to handle all of them.

## Homework 1 -- SDH

An implement to the algorithm ``Supervised Discrete Hashing``, according to [this paper, CPVR2015](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Shen_Supervised_Discrete_Hashing_2015_CVPR_paper.pdf)

Wrote in ``MATLAB``

nothing original, nothing special

## Homework 2 -- Dictionary

#### Background 

This homework asks me to do some arbitrary project with PageRank algorithm or its improvements. Prof. Zheng recommended to measure importance of academic thesis. 

Another good usage of PageRank is to rank importance of users in a social network. This application may be widely used in the many modern websites. I do not think it is something really funny -- at least others may do it much better than me.

However, in order to avoid conflict of implementing same idea with other classmates, I decided to measure  frequency of English words in a specific dictionary. Only *noun*, *adjective*, *adverb* and *verb* words will be counted or the top words in the result list may be 'meaningless' as the consequence of too many reference of *preposition* and *article*, etc.

#### Acknowledge

I choose the online edition of ``Longman Dictionary of Contemporary English, 6th Edition``. I do not have any copyright of this dictionary. I only use the dictionary for study and research instead any commerical activity. So anybody who use my code can only use it for Data Mining study also. 

The offical homepage of the dictionary is [HERE](http://global.longmandictionaries.com). Please pay for it if you really need it.

#### Detail

I found it is very difficult to get all the existing words in the dictionary. However, if some words is not referenced by any other words, the rank value of it should be very low, in that situation the result would have a obvious change if we ignore these words.

We only concern about the words referenced by others frequently. To get start, I download 4000 IELTS academy words from [this website](https://www.examword.com/ielts-list/4000-academic-word-1?la=en), and then apply a BFS algorithm to it.

I use ``scrapy`` and ``R`` to get and clean the data. PageRank is used to measure the importantance of them.

I save the result in ``hw2-dictionary/result``, you can get it if you are interested in. 

## Homework 3 -- Music

#### Background

I am asked to implement a cluster algorithm to slove any problem I want. My first idea is to divide users of [Steam](store.steampowered.com) into differnent groups by the games they play. 

（To be continued）
