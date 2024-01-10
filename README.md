A bare minimum extension library with the sole aim of providing a dot plot (aka strip plot/dot chart)

Abuses plt.scatter() or sns.scatterplot() to generate a dot plot (aka strip plot/dot chart)

> A dot plot, also known as a strip plot or dot chart, is a simple form of data visualization that consists of data points plotted as dots on a graph with an x- and y-axis.

Designed to work with `matplotlib` and `seaborn` (optionally)

Hijacks the existing `pyplot.scatter()` class

# installation

```text
pip install dotplotlib
```

# usage

Let's say you have data like this. Each row represents a mushroom. 

```text
          size   rating
--------------------------
0            4        2
1            5        7
2            3        7
3            3        3
4            6        5
5            4        3
6            6        8
7            8        9
```

```python
from dotplotlib import dotplot

x, y = dotplot.create(x=mushroom['size'])
plt.scatter(x, y)
```

Works with dates along the x-axis too, as seen here. The dots represent each support ticket arriving each day, and their colour intensity represents how quickly they were responded to. 

```python
from dotplotlib import dotplot

x, y = dotplot.create(x=mushroom['size'], color_by=mushroom['rating'])
plt.scatter(x, y)
```