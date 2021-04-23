[*Hand Gesture Recognition using Python and OpenCV*](https://gogul.dev/software/hand-gesture-recognition-p1)
# Introduction

Gesture recognition has been a very interesting problem in Computer Vision community for a long time. This is particularly due to the fact that segmentation of foreground object from a cluttered background is a challenging problem in real-time. The most obvious reason is because of the semantic gap involved when a human looks at an image and a computer looking at the same image. Humans can easily figure out what’s in an image but for a computer, images are just 3-dimensional matrices. It is because of this, computer vision problems remains a challenge. Look at the image below.

This image describes the semantic segmentation problem where the objective is to find different regions in an image and tag its corresponding labels. In this case, “sky”, “person”, “tree” and “grass”. A quick Google search will give you the necessary links to learn more about this research topic. As this is a very difficult problem to solve, we will restrict our focus to nicely segment one foreground object from a live video sequence.

# Problem statement

We are going to recognize hand gestures from a video sequence. To recognize these gestures from a live video sequence, we first need to take out the hand region alone removing all the unwanted portions in the video sequence. After segmenting the hand region, we then count the fingers shown in the video sequence to instruct a robot based on the finger count. Thus, the entire problem could be solved using 2 simple steps -

Find and segment the hand region from the video sequence.
Count the number of fingers from the segmented hand region in the video sequence.
How are we going to achieve this? To understand hand-gesture recognition in depth, I have decided to make this tutorial into two parts based on the above two steps.

The first part will be discussed in this tutorial with code. Let’s get started!

