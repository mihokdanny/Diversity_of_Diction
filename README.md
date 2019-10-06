# Diversity of Diction

This project compares the vocabularies of representative works from three groups of creative writing.  Using tools such as Python and Beautiful Soup, we were able to answer the questions:

* Which form of creative writing appears to have the broadest vocabulary?

* What are the most commonly used words among creative writing groups?  Authors?

# Getting Started / Prerequisites

# Sampling Data

The three groups of creative writing chosen for comparison were: Songwriters, Poets, and Journalists.  From these, we selected five of the most successful authors, and five of their works.


![images/artists_pic.jpg](images/artists_pic.jpg)


After selecting a sample of works, we set off to obtain the text for analysis.  This involved a process known as "web scraping."  We identified websites containing the text of the works that we were searching for, and utilized tools such as Beautiful Soup, Python, Urllib, and Requests to scrape the webpages and parse the HTML.


![images/song_url_structure.PNG](images/song_url_structure.PNG)

![images/song_scraping_snip.PNG](images/song_scraping_snip.PNG)


# Data Cleaning/Processing

With the text now at our disposal, we could make a plan to clean the text and extract our target data.  Below is a representation of how we used tools like RegEx to convert the blocks of text into a Python list of "regular expressions," NLTK's list of "stop words" to remove words that we considered unuseful, and NLP tasks such as converting all text to lowercase to combine otherwise identical words.  Note* This is an appropriate time to apply stemming and lemmatization.

![images/process_snip1.PNG](images/process_snip1.PNG)
![images/process_snip2.PNG](images/process_snip2.PNG)
![images/process_snip3.PNG](images/process_snip3.PNG)

The data was then loaded into a sqlite database.

# Analysis / Answering Our Questions

The process detailed above produces an organized data set that can be manipulated by the programming language of your choice for the purposes of analysis and visualization.

Using Python, pandas, and the graphing tool provided by ObservableHQ, we were able to create visualizations to display the answers to our questions.

1) Which form of creative writing appears to have the broadest vocabulary?

2) What are the most commonly used words among creative writing groups?  Authors?

![images/common_words_legend.PNG](images/common_words_legend.PNG)

![images/NLP_common_words.PNG](images/NLP_common_words.PNG)

Note that the circle size represents the frequency of a word’s usage in a work.  Words may appear more than once, as each bubble shown only represents one word per work.

![images/NLP_words_tree_more.PNG](images/NLP_words_tree_more.PNG)

# Additional Visualizations

We wondered: would a higher word count necessarily result in a decrease in the ratio of unique words out of the total?  That is, in writings where choruses are common (songs and poetry), would a higher word count simply mean that the work is more repetitive?
Surprisingly, looking at the graph below we see that songs appear to become MORE repetitive as total lyrics decrease!

![images/poets_vs_songwriters_unique_ratio.png](images/poets_vs_songwriters_unique_ratio.png)

What is the most commonly used word across all groups?  Can you guess?

![images/top_word_pie_chart.PNG](images/top_word_pie_chart.PNG)