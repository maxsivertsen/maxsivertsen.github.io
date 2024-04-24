---
layout: post
title: 'Jekyll and GitHub Pages Tricks'
categories: jekyll

---

## What's this blog post for?

This post primarily serves to provide an insight into some specific kinks that needed to be resolved in establishing this blog-site.

### Topic overview:
- 
<h2 id="latex">
### Incoporating latex
</h2>
I wanted to include some functions written in Latex, and it's surprisingly easy. Here is how it is done.

- From root, in the _layouts/ folder, go to the layout file for your posts (in my case this is _layout/post.html)

- Inside of post.html file, add the following
```
<script
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
  type="text/javascript">
</script> ```

- Finally, in your actual blog post (under _posts/2024-04-22-example-post.html) enclose your Latex writing with {% raw %} and {% endraw %}
```
{% raw %}
1) $$ f(x)=(log(array × 0.005 + 1 + 1e6)) $$
{% endraw %}
```
