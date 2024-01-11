Great things come in tiny packages. A bare minimum extension library with the sole aim of providing a dot plot (aka strip plot/dot chart)
- Designed to work with `matplotlib` and `seaborn` 
- Hijacks `plt.scatter` or `sns.scatterplot` (optionally) to generate a dot plot. 

# installation

```text
pip install dotplotlib
```

# usage

### fully customizable 

First, import the package.

```python
from dotplotlib import dotchart
```

Then generate `x, y` data. Pass in just the column containing the unit that would go on the x-axis. 

```python
x, y = dotplot(x=mushroom['size'])
```

And that's all! Now you simply plot it as a `scatter` or `scatterplot`.

```python
import matplotlib.pyplot as plt
```

# examples (1: basic matplotlib, 2: seaborn, 3: affinda)


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

plt.scatter(x, y)
```

### preset themes

1. `lavender`

2. `default` 

3. `console`


```python
from dotplotlib import dotplot

x, y, c = dotplot.create(x=mushroom['size'], color_by=mushroom['rating'])
```

# credits

- I got the formatting code from 