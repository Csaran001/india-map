import pandas as pd
!pip install geopandas
import geopandas as gpd
import matplotlib.pyplot as plt

fp = (r'india-polygon.shp')
map_df = gpd.read_file(fp)
map_df.head() #check the head of the file

data_df = pd.read_excel(r'data_ecxel.xlsx')
data_df.rename(columns={'Name of State / UT': 'st_nm'},inplace=True)
data_df.head() #check the head of the file

merged= map_df.merge(data_df, on = 'st_nm', how = 'left')
merged.head()

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('Indian States', fontdict={'fontsize': '25', 'fontweight' : '10'})

merged.plot(column='Total Confirmed cases',cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0', legend=True,markersize=[39.739192, -104.990337])