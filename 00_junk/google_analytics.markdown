---
layout: post
title: Data Engineer
categories: data science, data engineering
---

<h1> What is google analytics? </h1>

Marketing funnel : acquisition is awareness, engagement is when they interact, and monetization is when they make a purchase. Each one of them evaluates what the users actions are, relative to the market funnel funnel. For a company, they might have a website and want to know where the users originated from. For example, what potential advertisement medium led the potential customer to the website. Then, the company would continue to work down the market funnel and evaluate different website features to determine the different values of various website features relative to user interaction. Finally, at the end of the funnel there is the actual purchase of a product or service, this then would be the monetization of the newly acquired consumer. An additional step would be the retention of this consumer.

<h2> How is google analytics set up? </h2>

To capture user information (aka events), applications will require the use of the Firebase SDK. Alternatively, websites will require a tag of code.

Using google analytics requires an account. It is best practice to have one account for each company. The account will have different properties, each representing different flows of information. For example, a logistics company may have two different properties, one to manage out-going delivery, and another for incoming warehouse delivery. These would each be further broken down into data streams based on device type: web data, android app, or iOS app. Drawing the three components into one, there will be an account with properties, which will be further broken down into data streams. It should be noted here that Google Analytics 360 is an enterprise level service, and offers additional features.

<h3> Implementing tags </h3>

At the heart of event capturing lie tags. These are snippets of JavaScript that allow our platform to record events. Using the recommended 'Tag Manager' enables the easy central oversight, implementation, and management of tags from the 'Tag Manager' in the accounts management overview. This requires the inclusion of two instances of code in the website/application, one in the head, and the other in the body.