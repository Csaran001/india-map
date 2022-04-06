from bokeh.models import GeoJSONDataSource
from urllib.request import urlopen
import json

from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper
from bokeh.palettes import Viridis256
from bokeh.plotting import figure
from bokeh.io import output_file, show
import matplotlib.pyplot as plt
from bokeh.io import show, output_notebook

%matplotlib 
output_notebook()


with urlopen("https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson") as response:
    geojson = json.load(response)

for i in range(len(geojson['features'])):
  geojson['features'][i]['properties']['Color'] = ['antiquewnite','aqua', 'aquamarine','azure','beige', 'bisque', 'black', 'blanchedalmond','blue', 'blueviolet ', 'brown', 'burlywood','cadetblue' , 'chartreuse','chocolate', 'coral','cornflowerblue', 'cornsilk','crimson', 'cyan', 'darkblue','darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', ' darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange'][i%26]



cmap = LinearColorMapper(palette=Viridis256)

TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

geo_source = GeoJSONDataSource(geojson=json.dumps(geojson))

p = figure(title='India', tools=TOOLS, x_axis_location=None, y_axis_location=None, width=800, height=800)
p.grid.grid_line_color = None

p.patches('xs', 'ys', fill_alpha=0.7, line_color='black', fill_color='Color', line_width=0.1, source=geo_source)

hover = p.select_one(HoverTool)
hover.point_policy = 'follow_mouse'
hover.tooltips = [('State:', '@NAME_1')]

show(p)