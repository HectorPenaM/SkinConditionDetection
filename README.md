# SkinConditionDetection
CNN-based solution to detect skin conditions from images

## Problem Statement

The accurate and timely diagnosis of skin conditions poses a significant challenge in LATAM countries, particularly in smaller towns and villages, due to reliance on traditional subjective methods and limited access to dermatological doctors. These factors contribute to delays in treatment, increasing the risk of complications for patients.

## Objective & Solutions

The goal of this project is to develop a system able to give users a primary diagnosis of skin conditions found on their skin:
 <br/>

1. Users will supply images of areas of their skin that show the condition.
2. The system will be able to identify the condition based on the images supplied by the user.
3. Once a condition has been identified, the system will give the user instructions on how to treat the identified ailment.
This solution is planned to be deployed through a web application.
<br/>
<br/>
It is important to clarify that the results supplied by the proposed system are not meant to be a substitute to a proper medical diagnosis. 
<br/>
<br/>

![Project Architecture](/img/project_architecture.png 'Project Architecture')
<br/>
## Implementation Techniques In Brief

Given that images containing skin conditions will be used, it is first necessary to apply various filters and extract fundamental features from each one. This approach aims to achieve greater completeness when training the data.
<br/>
<br/>
A CNN will be trained by splitting the data into training, testing, and validation groups. Clearly, it will be necessary to adjust the hyperparameters to find the optimal configuration. The model will then provide a diagnosis of the identified disease or indicate 'healthy,' depending on the case.
<br/>
<br/>
Afterwards, the results obtained after Hyperparameter Tuning of our model will be compared with different models to analyze which one performs with the best metrics. In the end, we will choose the best model to further enhance its performance.

