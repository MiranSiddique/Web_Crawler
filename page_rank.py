import networkx as nx

def calculate_pagerank(links_graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    graph = nx.DiGraph()
    
    # Add edges to the graph
    for src, targets in links_graph.items():
        if isinstance(targets, list):
            for target in targets:
                graph.add_edge(src, target)
        elif isinstance(targets, float):
            print(f"Warning: Skipping page {src} as the 'links' value is a float instead of a list.")
        else:
            print(f"Warning: Unexpected data type for 'links' value of page {src}: {type(targets)}")
    
    # Compute PageRank
    pagerank = nx.pagerank(graph, alpha=damping_factor, max_iter=max_iterations, tol=tolerance)
    return pagerank
