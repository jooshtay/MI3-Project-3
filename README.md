# MI3-Project-3
## Contents:

### Project Description
In this project, we are exploring whether we can extract relevant features of images of Boston.

### What you will find in this repo: 
Each section header will direct you to the respective folder.
1. A section containng our source code and how to use and install it: SRC. Within it, you will find the primary code file.
The steps are as follows:
- Preprocess the images 
- Build the testing and training images
- Detect the features of both sets of images by applying the ORB algorithm to them
- Match the features found in the testing and training images 


2. A section containing how to access our source data: DATA.

3. A section containing key figures from our analysis: FIGURES.

4. A reference section containing all acknolwedgments and references.

## [SRC Section](https://github.com/jooshtay/MI3-Project-3/tree/main/SRC):

### [Installing/Building/Usage of Our Code](https://github.com/jooshtay/MI3-Project-3/tree/main/SRC):
The code to install, build, and use the code are all the same.

The code you will walk you through how to preprocess the images and then use the ORB algorithm to detect and match the relevant features of the images. 


## [DATA Section](https://www.mapillary.com/dataset/places):
- You can download the data set here: https://www.mapillary.com/dataset/places or click the section header
- You may need to create an account to access the image data.
- We are using the second zip file: msls_images_vol_1.zip


## [FIGURES Section](https://github.com/bridaviss/ProjectM1/tree/main/FIGURES):
- Within this section you will find key plots.

### Table of Contents:
1. [Common Image Sizes]():
   - Key Takeaways: This reinforces that no such image resizing was needed for our images. The ORB algorithm did not require that we resize our images. It was imporant to see though because if our downsampling (reducing the size and blurring the image) had different effects across different image sizes, then we could have dropped uncommon image sizes or resized some of the images.
2. [How well did ORB do?]():
   - Key Takeaways: The y-axis represents all of the hamming distance matches between relevant features. The x-axis represents how much the test image was rotated. It does not appear that rotating has a significant impact on the first quartile of matches, in other words, the best 25% of matched features were matched regardless of how much the image was rotated. There must be a large amount of features in the training data that are fairly obvious under different circumstances.

## REFERENCES Section:
1. B. Javaheri, “Getting Started with OpenCV,” domino.ai, Feb. 25, 2023. [Online] Avaialble: https://domino.ai/blog/getting-started-with-open-cv. [Accessed Oct 8, 2023].
2.  D. Tyagi, “Introduction to ORB (Oriented FAST and Rotated BRIEF),” medium.com, Jan. 1, 2019 [Online]. Available: https://medium.com/@deepanshut041/introduction-to-orb-oriented-fast-and-rotated-brief-4220e8ec40cf. [Accessed Nov. 3, 2023].
3. Z. Zeng, J. Zhang, X. Wang, Y. Chen, and C. Zhu, “Place Recognition: An Overview of Vision Perspective,” Applied Sciences, vol. 8, no. 11, p. 2257, Nov. 2018, doi: 10.3390/app8112257.
4. @infoaryan, “Feature matching using ORB algorithm in Python-OpenCV,” www.geeksforgeeks.org, Jan, 03, 2023. [Online]. Available: https://www.geeksforgeeks.org/feature-matching-using-orb-algorithm-in-python-opencv/. [Accessed Nov. 3, 2023].






