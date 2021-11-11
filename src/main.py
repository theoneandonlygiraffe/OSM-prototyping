


if __name__ == '__main__':
    import osmnx as ox
    import matplotlib.pyplot as plt
    import geopandas as gp
    import networkx as nx
    import pandas as pd


    # get some data
    place = "49.49671,8.47955"
    distance=4000
    buildings = ox.geometries_from_address(place,{"building":True}, dist=distance)
 
    streets = ox.graph_from_address(place,dist=distance, network_type="drive")
    rails = ox.graph_from_address(place,dist=distance, custom_filter='["railway"~"rail"]')
    graph =nx.compose(streets,rails)

    

    colors= ['w' if 'highway' in d else 'r' for _, _, _, d in graph.edges(keys=True, data=True)]
    fig, ax = ox.plot_graph(graph,show=False,edge_color=colors)

    #landuse.plot(column='landuse', ax=ax)
    #buildings.plot(ax=ax, color='None',lw=1, alpha=1)


    buildings.plot(ax=ax)

    #ax.axis('off')
    plt.show()
    #fig.show()