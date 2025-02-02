[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/daterange.png?raw=true)

A `matplotlib` extension library for making tree dot plots, strip plots or dot charts in Python (`seaborn` compatible)

### Installation

```text
pip install dotplotlib
```

### Usage

###### Example 1: Simple Dot Chart

`.dotchart` returns `x` and `y` lists that can be inputted straight into `matplotlib` or `seaborn` [scatterplots](https://www.w3schools.com/python/matplotlib_scatter.asp). 

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

###### Example 2: Dot Chart with Color Mapping

Pass the data you would like to color by to the `color_by=` argument. 

Returns an extra list `c` that should be passed into the `c=` parameter if using `matplotlib` or `hue=` if using `seaborn`. 

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

###### Example 3: Using `make_dotchart` to plot in one step

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

###### Example 4: Plotting in a Jupyter Notebook

If plotting inline, use the default `.dotchart()` to obtain `x` and `y` lists, and then adjust as necessary with one of the following: 

```python
plt.figure(figsize=(12,6))  # or
plt.figure().set_figwidth(12) # or
plt.figure().set_figheight(12)
```

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/jupyter.png?raw=true)

<br>

---

### Themes

![](https://github.com/jl33-ai/dotplotlib/blob/main/demos/gallery.png?raw=true)

---

### Feature set

- Generate strip plots/dot charts by exploiting `matplotlib/seaborn` scatterplots
- Supports any cmap color profile
- The data can be automatically sorted for better visualization, especially when using color mapping.
- Accepts both list and pandas.Series as input data.
- Set custom labels, titles, and dot sizes for your charts.
- Works with Jupyter Notebook

---

### Contributing

Anyone is welcome to raise a PR!

[contributors-shield]: https://img.shields.io/github/contributors/jl33-ai/dotplotlib.svg?style=for-the-badge
[contributors-url]: https://github.com/jl33-ai/dotplotlib/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jl33-ai/dotplotlib.svg?style=for-the-badge
[forks-url]: https://github.com/jl33-ai/dotplotlib/network/members
[stars-shield]: https://img.shields.io/github/stars/jl33-ai/dotplotlib.svg?style=for-the-badge
[stars-url]: https://github.com/jl33-ai/dotplotlib/stargazers
[issues-shield]: https://img.shields.io/github/issues/jl33-ai/dotplotlib.svg?style=for-the-badge
[issues-url]: https://github.com/jl33-ai/dotplotlib/issues
[license-shield]: https://img.shields.io/github/license/jl33-ai/dotplotlib.svg?style=for-the-badge
[license-url]: https://github.com/jl33-ai/dotplotlib/blob/master/LICENSE.txt
