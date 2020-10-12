import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import data from CSV File, CHANGE PATH
data_raw = np.genfromtxt('D:/g/Downloads/HT_pos.csv', delimiter=',', skip_header=1)

#Uncomment apropriate Filename for the heatmap to be saved under

#filename = 'ME_heatmap'
filename = 'DE_heatmap'


#Gets ME or DE data from raw data and turns it into 4x4 numpy array, works with a copy of original, sets color (col) variable for heatmap

if filename == 'ME_heatmap':
    data = ME_data = np.transpose(np.delete(data_raw, [0, 1, 3], 1)).reshape((4,4))
    col = 'Blues'
else:
    data = DE_data = np.transpose(np.delete(data_raw, [0, 1, 2], 1)).reshape((4,4))
    col = 'hot_r'


#Creates seaborn heatmap
ax = sns.heatmap(data, vmin = 0, vmax= 1, cmap= f'{col}', annot = True, annot_kws = {"color": 'black'}, xticklabels = False, yticklabels= False, fmt="0.4f", square = True)

#Creates outline of heatmap
for _, spine in ax.spines.items():
    spine.set_visible(True)


#save output to specified File (CHANGE PATH), tightlayout cuts the whitespaces around
plt.savefig(f'C:/Python Projects/heatmaps/{filename}.png', dpi=1200)
plt.tight_layout()
plt.show()
