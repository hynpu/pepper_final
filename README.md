# pepper_final

# Hand gesture capture using OPENCV

https://gogul.dev/software/hand-gesture-recognition-p1

Run the buildDataSet.py file to capture hand gesture from a webcam. Each run will generate 100 .png files for training.

I have used opencv for taking a running average of the background for 30 frames and then use that running average to detect the hand that has to be introduced after the background has been properly recognized.

I had found a very useful article on foreground mask by Gogul09 and i have pretty much used his code for background ellimination with a few changes in order to suit my cause.

He has written an awesome article on the problem and you can read it up here.

# Train the dataset

https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#sphx-glr-beginner-blitz-neural-networks-tutorial-py

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
