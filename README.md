![](/demos/daterange.svg)

Great things come in tiny packages. A bare minimum extension library with the sole aim of providing a dot plot (aka strip plot/dot chart)
- Designed to work with `matplotlib` and `seaborn` 
- Hijacks `plt.scatter` or `sns.scatterplot` (optionally) to generate a dot plot. 

# installation

```text
pip install dotplotlib
```

# usage

First, import the package.

```python
from dotplotlib import dotchart
```

Then generate `x, y` data. Pass in just the column containing the unit that would go on the x-axis. 

```python
x, y = dotplot(x=data['size'])
```

And that's all! Now you simply plot it as a `scatter` or `scatterplot`.

```python
import matplotlib.pyplot as plt
plt.scatter(x)
plt.show()
```

# preset themes

Instead of just giving you `x, y` data to make the plot yourself, `make_dotplot()` actually generates the plot. 

### `custom:lavender`

![](/demos/lavender.svg)

### `cmap`

Any cmap value supported by matplotlib ([see here](https://matplotlib.org/stable/users/explain/colors/colormaps.html)) will work when passed into `theme='viridis'`.

**viridis**

![](/demos/default.svg)

**gnuplot**

![](/demos/gnuplot.svg)

# full worked example

Let's say you have data like this. Each row represents a mushroom. It is loaded into a `pandas.DataFrame` object called `data`

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
x, y, c = dotchart(data['size'], color_by=data['rating'])

plt.scatter(x, y, c=c, cmap='viridis')  
plt.colorbar()  
plt.xlabel('Size')
plt.ylabel('Number')
plt.title('Mushroom Size Count Colored by Rating')
plt.show()
```


