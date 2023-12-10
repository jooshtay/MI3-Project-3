# MI3-Project-3
## Contents:

### Project Description
We are exploring LinkedIn job posting descriptions and analyzing what are key
qualitative factors that differentiate postings with a higher quantity of applications from a
lower quantity. We hypothesize that job postings that have a higher number of applicants
will be more detailed in summary and more descriptive in adjectives. We will be using
three different methods of keyword extraction as our text analysis.

### What you will find in this repo: 
Each section header will direct you to the respective folder.
1. A section containg our source code and how to use and install it: SRC. Within it, you will find three different rmd files that performs three different methods of analysis. Each file contains code for cleaning 
the same data. The methods are as follows:
- RAKE (Rapid Automatic Keyword Extraction): looks for keywords by looking to a sequence of words and excludes irrelevant words. 
- Phrases: extracts common phrases of the text.
- Textrank: Textrank is an algorithm within the textrank R package. The algorithm lets us to summarize text data while extracting keywords.


2. A section containing our source data: DATA.

3. A section containing key figures from our analysis: FIGURES.

4. A reference section containing all acknolwedgments and references.

## [SRC Section](https://github.com/bridaviss/ProjectM1/tree/main/SRC):

### [Installing/Building Our Code](https://github.com/bridaviss/ProjectM1/tree/main/SRC/Code%20Installation%20%26%20Cleaning):
The 'Data Cleaning for RAKE and Phrases.Rmd' is the data cleaning code for the phrases extraction **and** RAKE method. The data cleaning for these two files are the same, so 
the cleaning code is included as one file for each of the two methods. Once you have this data cleaning code, you can head on down to the Usage of Our Code section and download either the phrases extraction or RAKE method files, and perform the analysis. 

The data cleaning for the co-occurrence frequency method is slightly different: the data cleaning is included in one file. You do not need to download a separate file to clean the 
co-occurrence frequency data, it is already apart of the main file you will find below in the Usage of Our Code section. 


### [Usage of Our Code](https://github.com/bridaviss/ProjectM1/tree/main/SRC):
1. The goal of this analysis was to provide the audience with key qualitative factors that may differientiate Linkedin job postings that had a higher quantity of applications from a lower quantity of applications.
   - To do this, we performed three analyses:
       1. Phrases Extraction
            - Click here for the [code](https://github.com/bridaviss/ProjectM1/blob/main/SRC/LinkedInPhrasesAnalysis.Rmd) 
              
       3. Co-occurence Frequency
           - Click here for the [code](https://github.com/bridaviss/ProjectM1/blob/main/SRC/CooccurrenceFrequency.Rmd)
            
       5. Rapid Automatic Keyword Extraction
            - Click here for the [code](https://github.com/bridaviss/ProjectM1/blob/main/SRC/RAKE_method_code_.Rmd)
              
   



## [DATA Section](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings):
- You can download the data set here: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings or click the section header
- We are using the job_postings.csv 


## [FIGURES Section](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES):

### This is still a work in progress.

### Table of Contents:
1. [Phrases Extraction](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/Phrases%20Method%20Figures):
   - Key Takeaways: In both low and high application datasets, certain key phrases were consistently prominent, including "equal opportunity employer," "equal employment opportunity," "verbal communication skills," "affirmative action employer," "high school diploma," and "microsoft office suite." These phrases appear to be commonly emphasized in job postings regardless of application quantity. Additionally, the high applications dataset highlighted phrases like "5 years of experience" and "subject matter expert," suggesting a greater emphasis on specific qualifications and expertise in job postings that attract a larger number of applicants.
2. [Co-occurence Frequency](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/Co-occurence%20Frequency):
   - Key Takeaways: This analysis examined the relationship between words that frequently appeared in the same sentence by looking at the top thirty words that had the highest frequency occurence rating. When doing this analysis and comparing our datasets of lower vs. higher quantity of applications, we found that there was a lot of similarity within the two graphs. However for job postings that had a higher quantity of applications, there was a larger numbers of words that appeared near "team", "experience", and "skill" and the strength of these associations were stronger. 
3. [Rapid Automatic Keyword Extraction](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/RAKE%20Method%20Figures):
   - Key Takeways: This method of analysis gives individual words and phrases scores based on their co-occurence with other words and the frequency of which they show up in the text. There were not major differences when comparing the "low" and "high" subsets of data. The phrases and words that had a good combinaiton of rake and frequency values did not seem to differ between the two subsets. 

## REFERENCES Section:
1. A. Kon, “Linkedin Job Postings - 2023,” Kaggle, para. 1, Sept. 2023. [Online]. Available: https://www.kaggle.com/datasets/arshkon/linkedin-job-postings. [Accessed Sept. 15, 2023].
2. “An Overview of Keyword Extraction Techniques,” R-bloggers, para. 3, April 2018. [Online]. Available: https://www.r-bloggers.com/2018/04/an-overview-of-keyword-extraction-techniques/. [Accessed Sept. 15, 2023].
3. “udpipe: Tokenization, Parts of Speech Tagging, Lemmatization and Dependency Parsing with the 'UDPipe' 'NLP' Toolkit,” The R-Project for Statistical Computing, [Online]. Available:https://CRAN.R-project.org/package=udpipe. [Accessed Sept. 16, 2023].
4. “textrank: Summarize Text by Ranking Sentences and Finding Keywords,”The R-Project for Statistical Computing, [Online]. Available:https://CRAN.R-project.org/package=textrank. [Accessed Sept. 16, 2023].

