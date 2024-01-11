import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

Y_SCALE=1.25

def dotchart(x, color_by=None, reverse=False):
    """
    Generates x, y coordinates for a dot chart from an array-like input and sorts the data to facilitate color mapping.
    OPTIONAL: color_by specifies the data column which controls the colors of the datapoints

    Parameters:
    - x: List or pandas.Series containing data points for the x-axis.
    - color_by (optional): List or pandas.Series to color the datapoints by. Pass as argument to c= (matplotlib) or hue= (seaborn). 
    - reverse (optional): Boolean to indicate if the color map should be reversed. 

    Returns:
    - Tuple of two or three lists (x_out, y, [color_out]):
      'x_out' contains elements of 'x' in the original or sorted order,
      'y' contains the occurrence count for each corresponding x value,
      'color_out' (optional) is returned if color_by is provided, containing
      the color_by column to pass to matplotlib or seaborn.
    """
    if not isinstance(x, (list, pd.Series)):
        raise ValueError("Input x must be a list or a pandas Series")
    
    if color_by is not None:
        if not isinstance(color_by, (list, pd.Series)):
            raise ValueError("Input color_by must be a list or a pandas Series (or None)")
        if len(x) != len(color_by):
            raise ValueError("Inputs x and color_by must be data of the same length")

        df = pd.DataFrame({'x': x, 'color_by': color_by})
        df.sort_values(by='color_by', ascending=not reverse, inplace=True)
        x = df['x']
        color_out = df['color_by']

    seenCount = {}
    x_out, y = [], []

    for value in x:
        seenCount[value] = seenCount.get(value, 0) + 1
        x_out.append(value)
        y.append(seenCount[value])

    recommended_ymax = int(max(seenCount.values())*Y_SCALE)
    warning_msg = f"\n If your plot is oddly shaped, try: \n 1. Adjust the window size with your cursor \n 2. Add the following line: plt.ylim = [{0}, {recommended_ymax}], and fine tune appropriately."
    warnings.simplefilter('always', UserWarning)
    warnings.warn(warning_msg)

    if color_by is not None:
        return x_out, y, color_out
    else:
        return x_out, y
    
def make_dotchart(x, 
                  color_by=None, 
                  reverse=False, 
                  theme=None, 
                  colorbar=True, 
                  xlabel='x', 
                  ylabel='y', 
                  title='Dot Chart', 
                  dot_size=50):
    """
    Creates a dot chart with customizable themes, labels, and color mapping.

    This function generates a scatter plot based on the provided 'x' values. 
    If 'color_by' is specified, points will be colored based on these values. 
    The function offers several themes and customization options including labels, 
    title, and the presence of a color bar.

    Parameters:
    - x (list or pandas.Series): Data points for the x-axis.
    - color_by (list or pandas.Series, optional): Data points used for color mapping. Default is None.
    - reverse (bool, optional): If True, reverses the color mapping order. Default is False.
    - theme (str, optional): The theme of the plot. Options are 'custom:lavender'. You map specify any cmap supported by matplotlib.
    - colorbar (bool, optional): If True, includes a color bar in the plot. Default is True.
    - xlabel (str, optional): Label for the x-axis. Default is 'x'.
    - ylabel (str, optional): Label for the y-axis. Default is 'y'.
    - title (str, optional): Title of the plot. Default is 'Dot Chart'.
    - dot_size (int, optional): Size of the dots in the scatter plot. Default is 50.

    Raises:
    - ValueError: If 'x' or 'color_by' are not lists or pandas.Series, or if they are of different lengths.

    Examples:
    - Basic usage:
      >>> make_dotchart([1, 2, 3, 4], color_by=[10, 20, 30, 40], theme='default')
    
    - Customized usage:
      >>> make_dotchart([1, 2, 3, 4], color_by=[10, 20, 30, 40], xlabel='Custom X', ylabel='Custom Y', title='Custom Title', dot_size=100)
    """
    if color_by is None: 
        if theme is not None:
            warnings.warn("Colour theme was specified but cannot be applied, since no 'color_by' data was given.")
        x, y = dotchart(x)
        recommended_ymax = int(max(y)*Y_SCALE)
        plt.scatter(x, y, s=dot_size)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.ylim([0, recommended_ymax])
        plt.show()
    
    else:
        x, y, c = dotchart(x, color_by=color_by, reverse=reverse)
        recommended_ymax = int(max(y)*Y_SCALE)
        match theme:
            case 'custom:lavender':
                sns.set(rc={'axes.facecolor': 'lavender'})  
                ax = sns.scatterplot(x=x, y=y, hue=c, s=dot_size, legend="full", palette="RdYlGn")
                ax.grid(False)  
                ax.get_legend().remove()
                ax.set_xlabel(xlabel)
                ax.set_ylabel(ylabel)
                ax.set_title(title)
                plt.ylim([0, recommended_ymax])

                if colorbar:
                    scale_legend = plt.Normalize(c.min(), c.max())
                    color_map = plt.cm.ScalarMappable(cmap="RdYlGn", norm=scale_legend)
                    color_map.set_array([])
                    plt.colorbar(color_map, ax=ax)

                plt.show()

            case _:
                try: 
                    plt.scatter(x, y, c=c, cmap=theme, s=dot_size)
                except ValueError as e: 
                    print(f"The theme '{theme}' is unsupported by dotplotlib, and is not a valid cmap.")
                    print(e)
                    return
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.ylim([0, recommended_ymax])

                if colorbar:
                    plt.colorbar()

                plt.show()