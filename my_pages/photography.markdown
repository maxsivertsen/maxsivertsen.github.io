---
layout: photography
title: Photography
permalink: /photography/
---

<style>
    h1 {
        text-align: center;
    }


<style>
  .image-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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

<h1> Nature </h1>

<div class="image-grid">
    {% for photo in site.data.nature_photos %}
        <div class="grid-item">
            <img src="{{ '/assets/photography/nature/' | append: photo}}" alt="{{ photo }}" loading = "lazy" />
        </div>
    {% endfor %}
</div>


<h1> Urban </h1>

<div class="image-grid">
    {% for photo in site.data.urban_photos %}
        <div class="grid-item">
            <img src="{{ '/assets/photography/urban/' | append: photo}}" alt="{{ photo }}" loading = "lazy" />
        </div>
    {% endfor %}
</div>

<h1> Winter </h1>