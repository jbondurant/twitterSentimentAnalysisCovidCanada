import numpy as np
import matplotlib.pyplot as plt

from cycler import cycler

# code taken from https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html

category_names = ['Negative', 'Neutral',
                  'Positive']

#line_styles = ['-', '--', ':']
hatches = ['xxx', '...', '***']

#we should really rename the labels to reflect a short name for each topic
#i.e. replacing topic 6 with other
results = {
    'Topic 1': [35.555555555555557, 55.55555555555556, 8.888888888888889],
    'Topic 2': [23.404255319148937, 75, 1.5957446808510637],
    'Topic 3': [68.90756302521008, 29.411764705882354, 1.680672268907563],
    'Topic 4': [15.311004784688995, 66.98564593301436, 17.703349282296652],
    'Topic 5': [15.675675675675677, 80, 4.3243243243243246],
    'Topic 6': [28.346456692913385, 61.81102362204725, 9.84251968503937],
}


def survey(results, category_names):

    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))



    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    #jt removed ax.xaxis.set_visible(False)
    ax.set_xlim(0, 100)

    for i, (colname, color, hatch) in enumerate(zip(category_names, category_colors, hatches)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths


        rects2 = ax.barh(labels, widths, left=starts, height=0.8, color= 'r', alpha=0.0, align = 'edge')

        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color='w', hatch=hatch, edgecolor='black')

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects2, label_type='center', color='black', fmt='%.1f', padding = -3, fontsize = 'small')

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='large')

    return fig, ax


survey(results, category_names)
plt.show()