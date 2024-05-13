import tkintermapview
import os

database_path = os.path.join("/Volumes/Crucial X6/tiles.db")



top_left_position = (53.25978985306654, -13.833764956711107)
bottom_right_position = (42.562587186536504, 8.578343030126733)
zoom_min = 0
zoom_max = 14
loader = tkintermapview.OfflineLoader(path=database_path,
                                      tile_server="http://tiles.openseamap.org/seamark//{z}/{x}/{y}.png")

loader.save_offline_tiles(top_left_position, bottom_right_position, zoom_min, zoom_max)

# You can call save_offline_tiles() multiple times and load multiple regions into the database.
# You can also pass a tile_server argument to the OfflineLoader and specify the server to use.
# This server needs to be then also set for the TkinterMapView when the database is used.
# You can load tiles of multiple servers in the database. Which one then will be used depends on
# which server is specified for the TkinterMapView.

# print all regions that were loaded in the database
loader.print_loaded_sections()
