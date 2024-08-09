---
layout: photography
title: Nature, Urban, Winter, Forests, Mountains...
permalink: /photography/urban
---

<style>
    h1 {
        text-align: center;
    }
</style>


<style>
  .image-grid {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
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

<h1> Urban </h1>

<div class="image-grid">
    {% for photo in site.data.urban_photos %}
        <div class="grid-item">
            <img src="{{ '/assets/photography/urban/' | append: photo}}" alt="{{ photo }}" loading = "lazy" />
        </div>
    {% endfor %}
</div>