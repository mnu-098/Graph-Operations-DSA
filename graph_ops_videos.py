import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation

# ---------------- Base Graph ----------------
base_nodes = [1, 2, 3, 4]
base_edges = [(1, 2), (2, 3), (3, 4)]

def make_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

# Common draw function
def draw_graph(ax, G, highlight_nodes=[], highlight_edges=[], title=""):
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color="lightgreen", ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, width=2.5, edge_color="red", ax=ax)
    ax.set_title(title)

# ---------------- 1. Insert Vertex ----------------
def animate_insert_vertex():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        if frame == 0:
            G = make_graph(nodes, edges)
            draw_graph(ax, G, title="Before Insertion")
        else:
            G = make_graph(nodes + [5], edges)
            draw_graph(ax, G, highlight_nodes=[5], title="After Inserting Vertex 5")

    ani = animation.FuncAnimation(fig, update, frames=2, interval=1500, repeat=False)
    ani.save("graph_insert_vertex.gif", writer="pillow", fps=1)

# ---------------- 2. Delete Vertex ----------------
def animate_delete_vertex():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        if frame == 0:
            G = make_graph(nodes, edges)
            draw_graph(ax, G, title="Before Deletion")
        else:
            G = make_graph([n for n in nodes if n != 4], [(1,2),(2,3)])  # remove node 4
            draw_graph(ax, G, title="After Deleting Vertex 4")

    ani = animation.FuncAnimation(fig, update, frames=2, interval=1500, repeat=False)
    ani.save("graph_delete_vertex.gif", writer="pillow", fps=1)

# ---------------- 3. Add Edge ----------------
def animate_add_edge():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        if frame == 0:
            G = make_graph(nodes, edges)
            draw_graph(ax, G, title="Before Adding Edge")
        else:
            new_edges = edges + [(1,3)]
            G = make_graph(nodes, new_edges)
            draw_graph(ax, G, highlight_edges=[(1,3)], title="After Adding Edge (1,3)")

    ani = animation.FuncAnimation(fig, update, frames=2, interval=1500, repeat=False)
    ani.save("graph_add_edge.gif", writer="pillow", fps=1)

# ---------------- 4. Delete Edge ----------------
def animate_delete_edge():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        if frame == 0:
            G = make_graph(nodes, edges)
            draw_graph(ax, G, highlight_edges=[(2,3)], title="Before Deleting Edge (2,3)")
        else:
            new_edges = [(1,2),(3,4)]  # removed (2,3)
            G = make_graph(nodes, new_edges)
            draw_graph(ax, G, title="After Deleting Edge (2,3)")

    ani = animation.FuncAnimation(fig, update, frames=2, interval=1500, repeat=False)
    ani.save("graph_delete_edge.gif", writer="pillow", fps=1)

# ---------------- 5. Find Vertex ----------------
def animate_find_vertex():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        G = make_graph(nodes, edges)
        if frame == 0:
            draw_graph(ax, G, title="Searching for Vertex 3...")
        else:
            draw_graph(ax, G, highlight_nodes=[3], title="Vertex 3 Found!")

    ani = animation.FuncAnimation(fig, update, frames=2, interval=1500, repeat=False)
    ani.save("graph_find_vertex.gif", writer="pillow", fps=1)

# ---------------- 6. Traverse Graph (BFS) ----------------
def bfs_traversal(G, start):
    visited, queue = [], [start]
    order = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            order.append(node)
            queue.extend([n for n in G.neighbors(node) if n not in visited])
    return order

def animate_traverse_graph():
    nodes, edges = base_nodes.copy(), base_edges.copy()
    G = make_graph(nodes, edges)
    bfs_order = bfs_traversal(G, 1)
    fig, ax = plt.subplots(figsize=(5,4))

    def update(frame):
        ax.clear()
        highlighted = bfs_order[:frame+1]
        draw_graph(ax, G, highlight_nodes=highlighted, title=f"BFS Traversal Step {frame+1}")

    ani = animation.FuncAnimation(fig, update, frames=len(bfs_order), interval=1500, repeat=False)
    ani.save("graph_traverse_bfs.gif", writer="pillow", fps=1)

# ---------------- Run All ----------------
animate_insert_vertex()
animate_delete_vertex()
animate_add_edge()
animate_delete_edge()
animate_find_vertex()
animate_traverse_graph()

print("✅ All 6 graph operation GIFs generated successfully!")
