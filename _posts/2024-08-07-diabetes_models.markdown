---
layout: post
title: Simple Linear Regression Models
categories: ml, ai
---

How do different models stack up against one another when performing on a high-dimensional dataset with a continuous target variable?

<details>
  <summary>An overview of this shallow dive</summary>

A dataset provided by sk-learn is used to evaluate the performance across a handful of introductory machine learning models. The dataset consists of 442 observations and 10 predictor features, and a target variable. K-Fold cross-validation is employed to provide a more robust evaluation of model performance, however it is necessary to note that it does not return a singular model. In situations with smaller datasets, this can test against random variation in the data split (training/testing).

</details>

<h2> Regression Model Types </h2>

To predict a continuous variable, a selection of 6 popular introductory regression models are considered and their performances evaluted; these models are linear regression (lr), random forest (rf), ridge regression (ridge), lasso regression (lasso), partial least squares regression (plsr), and support vector regression (svr).

<h2> Data Preprocessing and Expectations </h2>

For the sake of reproducibility, it is necessary to set a random_state whenever required. This is done in the code (link to code-repo at the bottom). To ensure consistency across models, the data has been standardized in the data pipeline. This was done using sklearn's StandardScaler(). For all model hyperparameters, default values were taken. While methods exist to determine the best hyperparameter for most of the models used here, these have been overlooked with respect to time. However, these can be determine by plotting RMSE vs hyperparameter values, for example. A future entry will detail this topic further. The data was split 80/20 train-test. An additional 5-fold cross-validation approach is applied to the training data. Results from model performances are given in the results section.

As for model expectations, given that this is a continuous dataset, if the data has discernable patterns, then it can be expected that the linear models will pick up on these to some extent. If there is a relatively simple linear relationship between a specific feature and the target variable, we would then expect the linear models to perform in a comparative manner. However, not all models are made equal, as concepts like multicollinearity make clear. While plsr, ridge -, and lasso regression are relatively well-equipped for this challenge, the basic linear model will struggle if this is present. By default, svr is not primed for multicollinearity, although regularization (ridge) can be implemented to help offset the penalty suffered. For rf, on account of it being an ensemble model, it offers a robust approach and is unlikely to be impacted by multicolinearity.

<h2> Results </h2>

<p align="center">
  <img src="/assets/blog_posts/aug24_diabetes/r2_table.png" alt="Diabetes Model Performances">
</p>

The model performances can be seen in the table. The model names are given on the left, while their R2 values of model performance are given in columns R2, CV R2, and CV Internal R2. The R2 column represents model accuracy for a model built using the training data and evaluated on testing data. The same goes for CV R2, however the models are created using 5-fold cross-validation, allowing for more thorough development. CV Internal R2 is the R2 of a model when averaging each of the folds R2 performances from the pipeline.

It becomes apparent from the R2 values (most reliable) that linear models perform best on this dataset, suggesting a linear relationship in the data is to be had. Additionally, the CV R2 and CV Internal R2 both demonstrate extremely similar R2 values. This is likely indicative of similar model performances converging across multiple folds, pointing again towards the linear relationship of the data. Both random forest and SVR performed relatively poorly. As these models are more adept at detecting non-linear relationships, it suggests that non-linearities may be present, which would further support the belief that the data is linear in nature.

<p align="center">
  <img src="/assets/blog_posts/aug24_diabetes/diabetes_model_graph.png" alt="Diabetes Graph">
</p>


While the information in the graph is difficult to discern, it is clear that the SVR predictions are more consistently false in the same manner. The remaining visualizations of model performances do not allow for a definite statement to be made beyond a more closely grouped set of predictions. And yes, choosing the right color scheme here was poorly done. Next time though!

Thanks for reading!

<h3> Code Availability </h3>

The code used for this project can be seen and used in full on my GitHub page.
https://github.com/maxsivertsen/diabetes_regression_models/tree/main