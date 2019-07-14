#defining function for list normalisation
def normalize_list(lis):
    max_value = max(lis)
    min_value = min(lis)
    for i in range(0, len(lis)):
        lis[i] = (lis[i] - min_value) / (max_value - min_value)
    return lis

#importing required libraries
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

#reading the excel sheet 
coords=pd.read_excel('heatmap_buy_20.xlsx').iloc[1:].values
#converting the columns of the datframes into lists
lons = coords[:,0].tolist()
lats = coords[:,1].tolist()
weights=coords[:,2].tolist()

#creating a miller basemap object with lower left coordinate as(88.1 East,22.1 North), and upper right coordinate as (88.8 East,22.9 North)
fig = plt.figure(figsize=(13, 13))
m = Basemap(projection='mill',
            llcrnrlon=88.1,
            llcrnrlat=22.1,
            urcrnrlon=88.8,
            urcrnrlat=22.9,
            resolution = 'f')
m.drawmapboundary(fill_color='white')
m.drawcoastlines(color='black')

#normalizing weights
w=normalize_list(weights)

#creating a scatterplot heatmap
m.scatter(lons, lats, latlon=True,c=w, cmap='RdBu_r', alpha=0.8)
plt.colorbar(label="Normalised Weights")
plt.title(label="Weight Variation Heatmap on Basemap")
plt.show()
