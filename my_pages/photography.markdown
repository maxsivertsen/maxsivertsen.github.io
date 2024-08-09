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

<h1> Mountains </h1>

<div class="image-grid">
    {% for photo in site.data.photos %}
        <div class="grid-item">
            <img src="{{ '/assets/photography/nature/' | append: photo}}" alt="{{ photo }}" loading = "lazy" />
        </div>
    {% endfor %}
</div>


<h1> Forest </h1>

<h1> Germany </h1>

<h1> Urban </h1>
