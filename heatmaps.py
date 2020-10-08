import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Import data from CSV File, supply path as str
data_raw = np.genfromtxt('/home/clemens/Downloads/HT_pos.csv', delimiter=',', skip_header=1)


#Gets ME or DE data from raw data and turns it into 4x4 numpy array, works with a copy of original, uncomment the one you need

ME_data = np.transpose(np.delete(data_raw, [0, 1, 3], 1)).reshape((4,4))
#DE_data = np.transpose(np.delete(data_raw, [0, 1, 2], 1)).reshape((4,4))


#Creates seaborn heatmap, CHANGE INPUT DATA (first entry) AND CMAP (ME_data - Blues, DE_data - hot_r)
ax = sns.heatmap(ME_data, vmin = 0, vmax= 1, cmap= 'Blues', annot = True, annot_kws = {"color": 'black'}, xticklabels = False, yticklabels= False, fmt="0.4f", square = True)

#Creates outline of heatmap
for _, spine in ax.spines.items():
    spine.set_visible(True)


plt.tight_layout()
plt.show()
