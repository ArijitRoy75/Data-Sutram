import math
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
coords=pd.read_excel('heatmap_buy_20.xlsx').iloc[1:].values
lons = coords[:,0].tolist()
lats = coords[:,1].tolist()
weights=coords[:,2].tolist()
fig = plt.figure(figsize=(13, 13))
m = Basemap(projection='mill',
            llcrnrlon=88.1,
            llcrnrlat=22.1,
            urcrnrlon=88.8,
            urcrnrlat=22.9,
            resolution = 'f')
m.drawmapboundary(fill_color='white')
m.drawcoastlines(color='black')
w=[]
for i in weights:    
    a=math.sqrt(i)
    w.append(a)
m.scatter(lons, lats, latlon=True,c=w, cmap='RdBu_r', alpha=0.8)
plt.colorbar(label="SquareRoot(Weights)")
plt.title(label="Weight Variation Heatmap on Basemap")
plt.show()
