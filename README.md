# pepper_final

There are following main components in the project

+ hand gesture capture suing OPENCV
+ build the hand gesture dataset, including 5 gestures (stop, left, right, flow, OK)
+ trian the dataset using pytorch on GOOGLE COLAB, which is a free online server which can easily and efficiently train your model
+ build the ROS package, which includes: 
  + hand gesture recognition node:
    + load the saved trained neural network weight parameters (trained on google colab), and there is an explanationn from this page https://stackoverflow.com/questions/64141188/how-to-load-checkpoints-across-different-versions-of-pytorch-1-3-1-and-1-6-x-u (This is not an ideal solution, but it works for transferring checkpoints from newer versions to older versions.) 
    + capture the hand gesture (realtim) using the webcam, and then save the hand gesture image to the neural network to get the gesture class (left, right, OK...)
    + publish the gesture to the ROS topic gesture_class
  + gesture class smooth node
    + the node runs 20 hz, and there is a gesture class list, which collects the **most recent** 10 gestures
    + in each execution, the node will collect the current gesture class given by the hand gesture recognition node, and also it will discard the oldest gesture
    + find the most common gesture in the gesture class list, so that we can avoid the "noise"
    + the threshold is 60%, which means the most common gesture will be at least 60% of the captured past 10 gestures; otherwise we will think the data collection is too noisy, and send "no move" to the PEPPER; if the most common gesture is more frequent than 60%, then we send the movement to PEPPER (left, right, no move, OK means started to collect man, and flow means whatever)
  + pepper control node:
    +

# Hand gesture capture using OPENCV

https://gogul.dev/software/hand-gesture-recognition-p1 (you can copy and rephrase the passage from the link)

Run the buildDataSet.py file to capture hand gesture from a webcam. Each run will generate 100 .png files for training.

I have used opencv for taking a running average of the background for 30 frames and then use that running average to detect the hand that has to be introduced after the background has been properly recognized.

I had found a very useful article on foreground mask by Gogul09 and i have pretty much used his code for background ellimination with a few changes in order to suit my cause.

He has written an awesome article on the problem and you can read it up here.

# Train the dataset

https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#sphx-glr-beginner-blitz-neural-networks-tutorial-py (rephrase the passage from this link)

Neural networks can be constructed using the torch.nn package.

Now that you had a glimpse of autograd, nn depends on autograd to define models and differentiate them. An nn.Module contains layers, and a method forward(input) that returns the output.

For example, look at this network that classifies digit images:

It is a simple feed-forward network. It takes the input, feeds it through several layers one after the other, and then finally gives the output.

A typical training procedure for a neural network is as follows:

1. Define the neural network that has some learnable parameters (or weights)
2. Iterate over a dataset of inputs
3. Process input through the network
4. Compute the loss (how far is the output from being correct)
5. Propagate gradients back into the network’s parameters
6. Update the weights of the network, typically using a simple update rule: *weight = weight - learning_rate * gradient*

the detailed code example can be found here:

https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html

# Smooth the gesture capture

https://github.com/hynpu/pepper_final/blob/main/src/ges_signal_proc.py

Run a smooth filter at the frequency of 20Hz. The algo will filter the most common appeared gesture from topic "gesture_class", and also consider if the appearance number of current gesture is greater than the threshold (which is 60% of the past 20 gestures). If so, output the gesture to the topic 'cur_gest', which will be used by PEPPER.

