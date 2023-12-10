# MI3-Project-3
## Contents:

### Project Description
In this project, we are exploring whether we can extract relevant features of images of Boston.

### What you will find in this repo: 
Each section header will direct you to the respective folder.
1. A section containng our source code and how to use and install it: SRC. Within it, you will find three different rmd files that performs three different methods of analysis. Each file contains code for cleaning 
the same data. The methods are as follows:
- RAKE (Rapid Automatic Keyword Extraction): looks for keywords by looking to a sequence of words and excludes irrelevant words. 
- Phrases: extracts common phrases of the text.
- Textrank: Textrank is an algorithm within the textrank R package. The algorithm lets us to summarize text data while extracting keywords.


2. A section containing how to access our source data: DATA.

3. A section containing key figures from our analysis: FIGURES.

4. A reference section containing all acknolwedgments and references.

## [SRC Section](https://github.com/bridaviss/ProjectM1/tree/main/SRC):

### [Installing/Building/ Usage of Our Code](https://github.com/bridaviss/ProjectM1/tree/main/SRC/Code%20Installation%20%26%20Cleaning):
The code to install, build, and use the code are all the same.

The code you will walk you through how to preprocess the images and then use the ORB algorithm to detect and match the relevant features of the images. 


## [DATA Section](https://www.mapillary.com/dataset/places):
- You can download the data set here: https://www.mapillary.com/dataset/places or click the section header
- You may need to create an account to access the image data.
- We are using the second zip file: msls_images_vol_1.zip


## [FIGURES Section](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES):
- Within this section you will find key plots.
- 

### Table of Contents:
1. [Phrases Extraction](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/Phrases%20Method%20Figures):
   - Key Takeaways: In both low and high application datasets, certain key phrases were consistently prominent, including "equal opportunity employer," "equal employment opportunity," "verbal communication skills," "affirmative action employer," "high school diploma," and "microsoft office suite." These phrases appear to be commonly emphasized in job postings regardless of application quantity. Additionally, the high applications dataset highlighted phrases like "5 years of experience" and "subject matter expert," suggesting a greater emphasis on specific qualifications and expertise in job postings that attract a larger number of applicants.
2. [Co-occurence Frequency](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/Co-occurence%20Frequency):
   - Key Takeaways: This analysis examined the relationship between words that frequently appeared in the same sentence by looking at the top thirty words that had the highest frequency occurence rating. When doing this analysis and comparing our datasets of lower vs. higher quantity of applications, we found that there was a lot of similarity within the two graphs. However for job postings that had a higher quantity of applications, there was a larger numbers of words that appeared near "team", "experience", and "skill" and the strength of these associations were stronger. 
3. [Rapid Automatic Keyword Extraction](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES/RAKE%20Method%20Figures):
   - Key Takeways: This method of analysis gives individual words and phrases scores based on their co-occurence with other words and the frequency of which they show up in the text. There were not major differences when comparing the "low" and "high" subsets of data. The phrases and words that had a good combinaiton of rake and frequency values did not seem to differ between the two subsets. 

## REFERENCES Section:
1. J. Geralds, “Sega Ends Production of Dreamcast,” vnunet.com, para. 2, Jan. 31, 2007. [Online]. Available: http://nli.vnunet.com/news/1116995. [Accessed Sept. 12, 2007].
2. B. Javaheri, “Getting Started with OpenCV,” domino.ai, Feb. 25, 2023. [Online] Avaialble: https://domino.ai/blog/getting-started-with-open-cv. [Accessed Oct 8, 2023].
3. D. Tyagi, “Introduction to ORB (Oriented FAST and Rotated BRIEF),” medium.com, Jan. 1, 2019 [Online]. Available: https://medium.com/@deepanshut041/introduction-to-orb-oriented-fast-and-rotated-brief-4220e8ec40cf. [Accessed Nov. 3, 2023].
4. Z. Zeng, J. Zhang, X. Wang, Y. Chen, and C. Zhu, “Place Recognition: An Overview of Vision Perspective,” Applied Sciences, vol. 8, no. 11, p. 2257, Nov. 2018, doi: 10.3390/app8112257.
5. @infoaryan, “Feature matching using ORB algorithm in Python-OpenCV,” www.geeksforgeeks.org, Jan, 03, 2023. [Online]. Available: https://www.geeksforgeeks.org/feature-matching-using-orb-algorithm-in-python-opencv/. [Accessed Nov. 3, 2023].
6. o	M. Curry, “Image Recognition Applied To City Photos” [Online]. Available: https://www.currymichael.com/city.[Accessed Oct. 16, 2023].





