![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/daterange.png?raw=true)

*Great things come in tiny packages*. A bare minimum extension library for creating tree dot plots, strip plots or dot charts w/ matplotlib or seaborn in Python
- Designed to work with `matplotlib` and `seaborn` in Python
- Fully customizable

# installation

```text
pip install dotplotlib
```

# basic usage

`dotplotlib` can be used to generate dot charts with minimal code. Here are some basic examples:

<br>

### Example 1: Simple Dot Chart

`.dotchart` returns `x` and `y` lists that can be inputted straight into `matplotlib` or `seaborn` scatterplots. 

```python
from dotplotlib import dotchart
import matplotlib.pyplot as plt

data = {'size': [1, 2, 2, 3, 3, 3, 4]}

# Generate dot chart data
x, y = dotchart(data['size'])

# Plot
plt.scatter(x, y)
plt.show()
```

### Example 2: Dot Chart with Color Mapping

Pass the data you would like to color by with the `color_by=` argument. 

Returns an extra `c` list that should be passed into the `c=` parameter if using `matplotlib` or `hue=` if using `seaborn`. 

```python
from dotplotlib import dotchart
import matplotlib.pyplot as plt

data = {'size': [1, 2, 2, 3, 3, 3, 4], 'rating': [3, 2, 5, 4, 3, 6, 4]}

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

Instead of just giving you `x, y` lists to make the plot yourself, `make_dotplot()` actually generates the plot. 

```python
from dotplotlib import make_dotchart

df = {'size': [1, 2, 2, 3, 3, 3, 4], 'rating': [3, 2, 5, 4, 3, 6, 7]}

# Create a dot chart with optional arguments (only the first one is mandatory)
make_dotchart(df['size'], 
                  color_by=df['rating'], # list to color by
                  reverse=False, # inverts the color mapping
                  theme='gnuplot2', # scroll down to see all themes
                  colorbar=True, 
                  xlabel='Sizes', 
                  ylabel='Size Count', 
                  title='Mushroom Sizes Colored by Rating', 
                  dot_size=40):
```

### Example 4: If plotting in a Jupyter Notebook

If plotting inline, use the default `.dotchart()` to obtain `x` and `y` lists, and then adjust as necessary with one of the following: 

- `plt.figure(figsize=(12,6))` 
- `plt.figure().set_figwidth(12)`
- `plt.figure().set_figheight(12)`


---

# preset themes

### `custom:lavender`

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/lavender.png?raw=true)

### `cmap`

Any cmap value supported by matplotlib ([see here](https://matplotlib.org/stable/users/explain/colors/colormaps.html)) will work when passed into `theme='viridis'`.

**viridis:**

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/default.png?raw=true)

**gnuplot:**

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/gnuplot.png?raw=true)

---

# features

- generate strip plots/dot charts by exploiting `matplotlib/seaborn` scatterplots
- supports any cmap color profile
- the data can be automatically sorted for better visualization, especially when using color mapping.
- accepts both list and pandas.Series as input data.
- set custom labels, titles, and dot sizes for your charts.
- works with Jupyter Notebook

# attribution

- [pjarzabek](https://github.com/Pjarzabek/DotPlotPython/blob/master/How%20to%20create%20dot%20plots%20in%20Python.ipynb)
- m3
- ddlegal

# feature requests

- apply to become a contributor (pls help)
- open an issue on our GitHub repository
- email me: justinkhlee27\[at\]gmail.com
