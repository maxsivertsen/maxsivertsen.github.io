---
layout: post
title: Visualizing normalization techniques of simple arrays
categories: ml, ai, preprocessing, pre-processing, tech, computer-vision
---

Neural networks (NN) are powerful tools for making predictions. Before a NN can predict, however, it requires training. For the purpose of an example, we have a NN that predicts dog, cat, or other from a given image. For training, the model is provided with data from which is can learn to detect patterns in the image. This will allow it to predict and classify (hopefully accurately) new images that it has never seen before.

One important aspect of training the model is pre-processing. Imagine being a simple NN model for a moment and having to learn to identify cats, dogs, and others. You probably would be able to identify the pictures pretty quickly after seeing a few defining features between cats and dogs, but what happens if those provided images are particularly blurry? Suddenly, you are only seeing the pattern of four legs, a head, and a tail. This could lead to confusion regarding the learning of patterns, potentially to the extent that even other 4-legged creatures like horses would falsely be classified as cat or dog. So what steps can be taken to avoid this problem?

Normalization techniques are one approach, and while the abstraction will pick up here, we will try and keep it as simple as possible.

Let us start with a gray-scale image and what it really is. The image consists of a raster of pixels, and each pixel will have an attached value. These pixels can be represented using a histogram that will show us the distribution of pixel values in the image.
[insert image here]  [insert image histogram here]

With this in mind, what are the possible results of applying different normalization techniques to a simple array of values? Using three separate distributions as baseline comparisons, we evaluate both linear and non-linear transformations to our baseline arrays.
[normal dist, right skew, left skew]
![Baseline Histograms](max-website/_data/_assets/images/normalization_distributions/histogram_Baseline Comparisons.png)
test1
[!Baseline Histograms](_assets/images/normalization_distributions/histogram_Baseline Comparisons.png)
test2
[!Baseline Histograms](/home/empathyforgiveness/max_website/max-website/_data/_assets/images/normalization_distributions/histogram_Baseline Comparisons.png)
test3

The first approach is commonly referred to as the min-max normalization and serves to scale the array values to a specific range, in this case 0 and 1.

here is what it does, how it changes stuff etc.

[insert image]