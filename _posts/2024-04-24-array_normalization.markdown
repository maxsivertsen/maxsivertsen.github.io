---
layout: post
title: Visualizing normalization techniques of simple arrays
categories: ml, ai
---

Neural networks (NN) are powerful tools for making predictions. Before a NN can predict, however, it requires training. For the purpose of an example, we have a NN that predicts dog, cat, or other from a given image. For training, the model is provided with data from which is can learn to detect patterns in the image. This will allow it to predict and classify (hopefully accurately) new images that it has never seen before.

### Concretization example
One important aspect of training the model is pre-processing. Imagine being a simple NN model for a moment and having to learn to identify cats, dogs, and others. You probably would be able to identify the pictures pretty quickly after seeing a few defining features between cats and dogs, but what happens if those provided images are particularly blurry? Suddenly, you are only seeing the pattern of four legs, a head, and a tail. This could lead to confusion regarding the learning of patterns, potentially to the extent that even other 4-legged creatures like horses would falsely be classified as cat or dog. So what steps can be taken to avoid this problem?

Normalization techniques are one approach, and while the abstraction will pick up here, we will try and keep it as simple as possible.

### Abstraction
Let us start with a gray-scale image and what it really is. The image consists of a raster of pixels, and each pixel will have an attached value. These pixels can be represented using a histogram that will show us the distribution of pixel values in the image.
[insert image here]  [insert image histogram here]

With this in mind, what are the possible results of applying different normalization techniques to a simple array of values? Using three separate distributions as baseline comparisons, we evaluate both linear and non-linear transformations to our baseline arrays.

![Baseline Histograms](/assets/imgs/histogram_Baseline Comparisons.png)

## Linear Normalization

### The Equation:
{% raw %}
$$ val_{\text{out}} ​= (val_{\text{in}}​−c) × ((d−c) / (b−a​)) + a $$
{% endraw %}



### Variables:
- `b` and `a` determine the new range of the array (scaling)
- `d` and `c` are the maximum and minimum values of the array
- `X` represents each item in the array

### Idea:
Linear normalization will rescale an array to predetermined parameters, typically with bounds [0, 1].

### Application:
If the array is not already bound at [0, 1], this is the first step. Use the normalization equation above to achieve this. Then, apply the same equation on the recently transformed array, but set the variables `c` and `d` to the 1st and 99th percentile values. The aim is to reduce the influence of extreme outliers.

### Result:
In a long tailed right-skewed distribution, applying the min-max normalization method with 1st and 99th percentile values should shift the value distribution towards 0. The reason being, outlier variables above 99th percentile will likely be ‘cut-off’, as in if the value of an array [1:100] at position 100 was 10000, that value would be reassigned a value of 99, thus greatly reducing its pull on the distribution.

![Linear Normalization](/assets/imgs/histogram_Linear Normalization.png)

---

## Dynamic World Normalization

### The DW Equation:
{% raw %}

1) $$ f(x)=(log(array × 0.005 + 1 + 1e6)) $$

2) $$ g(x)= (f(x)−lower\_percentile​) / (upper\_percentile−lower\_percentile) $$

3) $$ array\_dw\_normalized ​= (1) / ( 1 + exp(−g(x) × 2)​ ) $$

{% endraw %}

### Idea:
1) First we apply a log transform to the array, this helps compress the dynamic range of values (particularly useful when dealing with wide-ranged, heavy-tailed distributions). We include the epsilon value (1e6) to avoid encountering log(0) and ensure stability.
2) Apply normalization using percentile values [30, 50] and [30, 70]. This will disregard extreme outliers.
3) The sigmoid function will transform the values to a range of [0, 1].

### Application:
Pass the array into \( f(x) \) and determine the percentiles for \( g(x) \) – we elected to use both [30, 50] and [30, 70]. Then apply the sigmoid transform (step 3).


### Result:
This method will compress the range of array values and make use of all of the array values present. As a simple example, imagine an array with range [0, 100], but with only 20 unique values. If we compress this using DW normalization, we could rescale the image in step 2 to [30, 50]. This would result is a more even distribution across all available pixel values. In turn, that can result in more pronounced differentiations between values.

![Dynamic World 3050](/assets/imgs/histogram_Dynamic World Normalization [30, 50].png)
![Dynamic World 3070](/assets/imgs/histogram_Dynamic World Normalization [30, 70].png)


---

## Histogram Equalization

### The Equation:
{% raw %}

\[ O(i) = \text{round}\left(\left(\frac{(M \times N) - \text{min\_CDF}}{\text{CDF}(I(i)) - \text{min\_CDF}}\right) \times (L - 1)\right) \]
$$ \nabla_\boldsymbol{x} J(\boldsymbol{x}) $$

{% endraw %}
### Idea:
[Histogram Equalization](https://en.wikipedia.org/wiki/Histogram_equalization)
![Histogram Equalization Img](/assets/imgs/Histogrammeinebnung.png)
<figcaption>Histogram equalization visualized, credit: By Zefram - Own work, Public Domain, https://commons.wikimedia.org/w/index.php?curid=668605</figcaption>

### Application:
Histogram equalization will take an initial distribution of values in an array and reassign them such that each unique value in the array’s range has the same frequency

### Result:
The result should be a more uniform distribution of values relative to the initial distribution.

![Histogram Equalization](/assets/imgs/histogram_Histogram Equalization.png)

---


---

## Gaussian Normalization (Standardization, Z-score)

### The Equation:
{% raw %}

$$ \[ z = \frac{(x - \mu)}{\text{sd}} \] $$

{% endraw %}

### Variables:
- `x`: array
- `mu`: mean
- `sd`: standard deviation

### Idea:
This technique is also known as Z-score normalization. It simply rescales the array by shifting it and standardizing it to have a mean of 0 and sd of 1.

### Application:
{% raw %}

$$ \[ z = \frac{(\text{array}_X - \mu)}{\text{sd}} \] $$

{% endraw %}

### Result:
For normal distribution, this method can improve the Gaussian characteristics of the array’s values. However, in the case of skewed data, this technique will exacerbate the skewed characteristics of the dataset.

![Gaussian Norm](/assets/imgs/histogram_Gaussian Normalization.png)

---

## Norm2 Normalization

### The Equation:
{% raw %}

\begin{verbatim}
\begin{lstlisting}[language=Python]
def z_score_normalization(x):
    mean = np.mean(x)
    std_dev = np.std(x)
    normalized_x = (x - mean) / std_dev
    return normalized_x
\end{lstlisting}
\end{verbatim}

{% raw %}

### Variables:

### Idea:
L2 Normalization will rescale an array using the magnitude of the vector (the magnitude is the denominator in the equation)

### Application:
A simple example would be an array [1,3,5]. Simply square each value, then apply the square root (\sqrt{35}) and divide each value by \sqrt{35}.

### Result:
Because this technique does not actually alter the distribution or proportional distance between values, it only will yield a change in the range of the array (compression of the range).

![Norm2 Norm](/assets/imgs/histogram_Norm2 Normalization.png)

## Image normalization - visualized

Using the following image we will investigate how the spread of pixel values changes with different normalization methods.

![Color Loon](/assets/imgs/loon_picture_bird.jpeg)

The first step requires converting the image to gray scale. The original image is an RGB image, meaning that is has 3 channels. To simplify the process we select the green channel since it has a better balance between between brightness and contrast than either red or blue.

![Gray Loon](/assets/imgs/loon_picture_gray.jpeg)

Next it is necessary to establish a baseline histogram for comparative purposes regarding the visualization of changes of different normalization methods.

![Gray Loon Histogram](/assets/imgs/baseline_histogram.jpeg)

The following demonstrates changes in the distribution of pixel values after applying the aforementioned normalization (transformation) techniques.

![Normalization Methods](/assets/imgs/Additional-normalizations.jpeg)

![Dynamic World Normalization](/assets/imgs/Dynamic-world-normalization.jpeg)