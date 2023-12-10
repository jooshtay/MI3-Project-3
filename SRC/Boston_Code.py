#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 02:04:15 2023

@author: joshuataylor
"""

# Import necessary libraries
import cv2
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load in the images
boston_imgs = '/Users/joshuataylor/Desktop/UVA /Fall 2023/DS 4002/Project 2 - Boston/bost_test'

# Create an ORB object 
orb = cv2.ORB_create()

# Create a matcher object - this will be used to match the features from the training
# and testing images
match_ob = cv2.BFMatcher( cv2.NORM_HAMMING , crossCheck=True )

# Create an empty dictionary to store data frames for each angle of rotation
# We're running the ORB analysis multiple times on the images when they are rotated to 
# different degrees. 
rotation_data_frames = {}

# We are going to use a for loop that will run through all the steps laid out in the analysis
# plan. I will label them as such.
for img in os.listdir( boston_imgs ):
    
    if img.endswith(('.jpg', '.jpeg', '.png')): 
        
        image_path = os.path.join( boston_imgs, img )
        
        image = cv2.imread( image_path )
        
        image_rgb = cv2.cvtColor( image , cv2.COLOR_BGR2RGB ) # Step: 1 convert
                                                              # images from BGR to RGB
        
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY) # Step 1: convert img to grayscale

        # Loop through each rotation angle
        for rotation_angle in [ 5 , 10 , 15 , 20 , 25 , 30 ]:
            
            # Step 2: Building our test images
            
            # Fnding the center of the image, that's the point from where we will rotate 
            # the image
            test_image = cv2.pyrDown( image_rgb )
            
            num_rows, num_cols = test_image.shape[ : 2 ]
            
            rotation_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), rotation_angle, 1)
            
            test_image = cv2.warpAffine( test_image , rotation_matrix , ( num_cols, num_rows ) )
            
            test_gray = cv2.cvtColor(test_image, cv2.COLOR_RGB2GRAY ) 
            

            # Step 3: Detect the relevant features (keypoints + descriptors)
            train_keypoints, train_descriptor = orb.detectAndCompute( image_gray , None )
            test_keypoints, test_descriptor = orb.detectAndCompute( test_gray , None )

            # Step 4: Match the features
            matches = match_ob.match(train_descriptor, test_descriptor)

            # Sort by the shortest ,best matching, features
            matches = sorted(matches, key = lambda x: x.distance)

            # Create a data frame for rotation angles if not already created
            if rotation_angle not in rotation_data_frames:
                rotation_data_frames[rotation_angle] = pd.DataFrame(columns=['Image', 'Hamming Distance'])

            # Add the hamming distances to the data frame
            data = {'Image': img, 'Hamming Distance': [ match.distance for match in matches ] } 
            rotation_data_frames[ rotation_angle ] = rotation_data_frames[ rotation_angle ].append( pd.DataFrame( data ), ignore_index = True )

# Print or use the data frames for analysis
for rotation_angle, data_frame in rotation_data_frames.items():
    print(f"Data Frame for Rotation Angle {rotation_angle}:\n", data_frame)
    

# Create an empty dictionary store five-number summaries for each rotation angle
five_number_summaries = {}

# Loop through each rotation angle and compute the five-number summary
for rotation_angle, data_frame in rotation_data_frames.items():
    
    summary = data_frame[ 'Hamming Distance' ].describe(percentiles=[ 0.25 , 0.5 , 0.75 ] )
    
    five_number_summaries[ rotation_angle ] = {
        
        'Minimum': summary[ 'min' ],
        
        'Lower Hinge': summary[ '25%' ],
        
        'Median': summary[ '50%' ],
        
        'Upper Hinge': summary[ '75%' ],
        
        'Maximum': summary[ 'max' ]
    }

# Print or use the five-number summaries for analysis
for rotation_angle, summary in five_number_summaries.items():
   
    print(f"Rotation Angle: {rotation_angle}")
   
    print(f"Minimum: {summary['Minimum']}")
   
    print(f"Lower Hinge: {summary['Lower Hinge']}")
   
    print(f"Median: {summary['Median']}")
   
    print(f"Upper Hinge: {summary['Upper Hinge']}")
   
    print(f"Maximum: {summary['Maximum']}\n")
    

# Combine all dfs into one to make it easier to plot
results = pd.concat(rotation_data_frames.values(), keys = rotation_data_frames.keys(), names = [ 'Rotation Angle' ] )

# Set a custom color palette
colors = sns.color_palette("husl", len(rotation_data_frames))

# Create final graphic
plt.figure(figsize=( 12 , 8 ) )

sns.boxplot( x ='Rotation Angle', y = 'Hamming Distance', data = results , palette = colors, showfliers = False )

plt.title( 'Hamming Distances for Different Rotation Angles' )

plt.show()




    
    
    
    
    
    
    
