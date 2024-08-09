---
layout: photography
title: Photography
permalink: /photography/
---


<h1>Photos</h1>


<style>
  .image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
  }
  .grid-item {
    border: 1px solid #ddd;
    padding: 5px;
  }
  .grid-item img {
    width: 100%;
    height: auto;
    display: block;
  }
</style>

<div class="image-grid">
    {% assign photos = "Additional-normalizations.jpeg,'histogram_Dynamic World Normalization [30, 50].png','histogram_Linear Normalization.png',loon_picture_gray.jpeg,baseline_histogram.jpeg,'histogram_Dynamic World Normalization [30, 70].png',Histogrammeinebnung.png,Dynamic-world-normalization.jpeg,'histogram_Gaussian Normalization.png','histogram_Norm2 Normalization.png','histogram_Baseline Comparisons.png','histogram_Histogram Equalization.png',loon_picture_bird.jpeg
| split "," %}
    {% for photo in photos %}
        <div class="grid-item">
            <img src="{{ '/assets/imgs/' | append: photo}}" alt="{{ photo }}" />
        </div>
    {% endfor %}
</div>
