![](/demos/daterange.png)

*Great things come in tiny packages*. A bare minimum extension library with the sole aim of providing a dot plot (aka strip plot/dot chart)
- Designed to work with `matplotlib` and `seaborn`.
- Provides a simple yet powerful interface for visualizing data distributions, frequencies and categories.

# installation

```text
pip install dotplotlib
```

# basic usage

`dotplotlib` can be used to generate dot charts with minimal code. Here are some basic examples

### Example 1: Simple Dot Chart

`.dotchart` returns `x` and `y` lists that can be inputted straight into `matplotlib` or `seaborn` scatterplots. 

```python
from dotplotlib import dotchart
import matplotlib.pyplot as plt

# Data preparation
data = {'size': [1, 2, 3, 4, 5, 6]}

# Generate dot chart data
x, y = dotchart(data['size'])

# Plot
plt.scatter(x, y)
plt.show()
```

### Example 2: Dot Chart with Color Mapping

Returns an extra `c` list that should be passed into the `c=` parameter if using `matplotlib` or `hue=` if using `seaborn`. 

```python
from dotplotlib import dotchart
import matplotlib.pyplot as plt

# Data preparation
data = {'size': [1, 2, 3, 4, 5, 6], 'rating': [3, 2, 5, 4, 3, 6]}

# Generate dot chart data with color mapping
x, y, c = dotchart(data['size'], color_by=data['rating'])

# Plot with color mapping
plt.scatter(x, y, c=c, cmap='viridis')
plt.colorbar()
plt.xlabel('Size')
plt.ylabel('Number')
plt.title('Mushroom Size Count Colored by Rating')
plt.show()
```

### Example 3: Using `make_dotchart` for Simplified Plotting

Instead of just giving you `x, y` data to make the plot yourself, `make_dotplot()` actually generates the plot. 

```python
from dotplotlib import make_dotchart

# Data preparation
test_df = {'size': [1, 2, 3, 4, 5, 6], 'rating': [3, 2, 5, 4, 3, 6]}

# Create a dot chart with additional customization
make_dotchart(test_df['size'], color_by=test_df['rating'], dot_size=40, theme='gnuplot2')
```

---

# preset themes

### `custom:lavender`

![](/demos/lavender.png)

### `cmap`

Any cmap value supported by matplotlib ([see here](https://matplotlib.org/stable/users/explain/colors/colormaps.html)) will work when passed into `theme='viridis'`.

**viridis:**

![](/demos/default.png)

**gnuplot:**

![](/demos/gnuplot.png)

---

# features

- generate strip plots/dot charts by exploiting `matplotlib/seaborn` scatterplots
- supports any cmap color profile
- the data can be automatically sorted for better visualization, especially when using color mapping.
- accepts both list and pandas.Series as input data.
- set custom labels, titles, and dot sizes for your charts.

# credit