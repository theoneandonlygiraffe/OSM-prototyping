


if __name__ == '__main__':
    import osmnx as ox
    import matplotlib.pyplot as plt
    import geopandas as gp
    import networkx as nx
    import pandas as pd

    #from palettable.scientific.sequential import Dark2_7

    # get some data
    place = "49.3165, 8.4527"
    distance=4000
    buildings = ox.geometries_from_address(place,{"building":True}, dist=distance)
    landuse = ox.geometries_from_address(place,{"landuse":True}, dist=distance)
 
    #streets = ox.graph_from_address(place,dist=distance, network_type="drive")
    streets = ox.graph_from_address(place,dist=distance)
    #rails = ox.graph_from_address(place,dist=distance, custom_filter='["railway"~"rail"]')
    #graph =nx.compose(streets,rails)
    graph=streets
    
    
    #draw graph
    colors= [
    "r" if 'highway' in d and d['highway']=='motorway' 
    else "orange" if 'highway' in d and d['highway']=='trunk'
    else "yellow" if 'highway' in d and d['highway']=='primary'
    else "yellow" if 'highway' in d and d['highway']=='secondary'
    else "w" if 'highway' in d and d['highway']=='tertiary'
    else "w" if 'highway' in d and d['highway']=='unclassified'
    else "w" if 'highway' in d and d['highway']=='residential'
    else 'grey' if 'highway' in d 
    else 'blue' for _, _, _, d in graph.edges(keys=True, data=True)
    ]

    #colors=ox.plot.get_colors(cmap="Greys")
    fig, ax = ox.plot_graph(graph,show=False,edge_color=colors,node_size=0)

    #draw streets
    #fig, ax = ox.plot_figure_ground(point=(49.3165, 8.4527),dist=distance, dpi=40, save=False, show=True, close=False)

    #draw land and buildings
    #landuse.plot(column='landuse', ax=ax,cmap= "Greens_r")
    buildings.plot(ax=ax,color="cyan")
    #buildings.plot(ax=ax, color='None',lw=1, alpha=1)
    
    nodes, edges = ox.graph_to_gdfs(streets)
    print(edges)
    
    #ax.axis('off')
    plt.show()
    #fig.show()