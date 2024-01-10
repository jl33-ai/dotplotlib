import pandas as pd
import warnings

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

    recommended_ymax = int(max(seenCount.values())*1.5)
    warning_msg = f"For better visibility, try configuring your plot with the following line: plt.ylim = [{0}, {recommended_ymax}]. Fine tune appropriately."
    warnings.warn(str(warning_msg))

    if color_by is not None:
        return x_out, y, color_out
    else:
        return x_out, y