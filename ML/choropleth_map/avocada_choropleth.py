#https://towardsdatascience.com/mapping-avocado-prices-in-python-with-geopandas-geopy-and-matplotlib-c7e0ef08bc26

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from descartes.patch import PolygonPatch


#imoporting the avacado dataset
data = pd.read_csv('/home/antarix/Desktop/naive bayes/avocado.csv', index_col ='Date')
print(data)
print(data.columns)
#we drop most of the column and keep price and region
columns_to_drop = ['Unnamed: 0','4046', '4225', '4770',
       'Total Bags', 'Small Bags', 'Large Bags', 'XLarge Bags', 'type']
avo_df = data.drop(columns_to_drop, axis = 1)
print(avo_df.head)

#finding the unique regions
regions = avo_df['region'].unique()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(regions)


#get average price per region
group_by_region = avo_df.groupby(by=['region'])
avo_df_avg = group_by_region.mean()
print(avo_df_avg)
avo_df_avg = avo_df_avg.drop(['year'], axis = 1)
print(avo_df_avg)




from geopy.geocoders import Bing
from geopy.extra.rate_limiter import RateLimiter
geolocator = Bing(api_key='AtJCFBgH4SRed5lqZKT7yVF5AwPwdsEgWIwbhqZig7Ca_TTX504eHsGw46HYnoiA', timeout=30)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)
regions_dict = geolocator.geocode("Albany")
#print("regions_dictregions_dictregions_dict:", regions_dict)
regions_dict = {i : geolocator.geocode(i) for i in regions}
print(regions_dict)

#lets get the co-ordinates of the regions
#pandas has the cordinates of all the regions
regions_df = pd.DataFrame(regions_dict)
regions_df_melted = regions_df.iloc[1:2,:].melt()
regions_df_melted.columns = ['region', 'co-ordinates']

merged_df = pd.merge(avo_df_avg, regions_df_melted, left_on='region', right_on='region')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(merged_df)

'''Our next step is to bring this all together and create a GeoPandas GeoDataFrame
 which contains our average price for each region, plus the geographic information
  we need to plot each are on our map. To do that we first need to create a column for
   latitude and one for longitude (GeoPandas, very reasonably, wants to have that information
    to create its ‘geometry’ column, which is its way of storing the geodata).'''

merged_df[['latitude', 'longitude']] = pd.DataFrame(merged_df['co-ordinates'].tolist(), index=merged_df.index)
print (merged_df)

avo_gdf = gpd.GeoDataFrame(merged_df, geometry=gpd.points_from_xy(merged_df.longitude, merged_df.latitude))
print(avo_gdf)

#now plot avo_gdf
# import matplotlib.pyplot as plt
# avo_gdf.plot()
# plt.show()


from shapely.geometry import Point, Polygon
usa = gpd.read_file('/home/antarix/Downloads/cb_2018_us_county_500k/cb_2018_us_county_500k.shp')
# import matplotlib.pyplot as plt
# usa.plot()
# plt.show()



to_drop = ['Midsouth', 'Northeast', 'Plains', 'SouthCentral', 'Southeast', 'TotalUS', 'West','Commonwealth of the Northern Mariana Islands', 'United States Virgin Islands', 'Hawaii', 'Alaska', 'Guam', 'Puerto Rico', 'American Samoa']
for index, row in usa.iterrows():
    if row['NAME'] in to_drop :
        usa.drop(index, inplace=True)
print("**********************************************************")
print(usa)
# import matplotlib.pyplot as plt
# usa.plot()
# plt.show()


crs = {'init': 'epsg:4326'}
avo_gdf = gpd.GeoDataFrame(merged_df, crs=crs)
usa_gdf = gpd.GeoDataFrame(usa, crs=crs)


from mpl_toolkits.axes_grid1 import make_axes_locatable
# This is a function to allow us to make the legend pretty
fig, ax = plt.subplots(figsize = (20,16))
plt.title('Avocado Prices by region in the United States', fontsize=26, fontfamily='serif')
#this part makes the legend the same size as our map, for prettiness
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
usa.boundary.plot(ax=ax, color='DarkSlateBlue')
# using the boundary method here to get the outlines of the states, an aesthetic decision
avo_gdf.plot(cmap='Greens', column='AveragePrice', legend=True, ax=ax, s=2000, alpha=0.7, cax=cax)
# this saves a copy of the viz as a jpg so we can easily share it with our friends on twitter!
plt.savefig('/home/antarix/Desktop/naive bayes/avocado_price.jpg', format='jpg')