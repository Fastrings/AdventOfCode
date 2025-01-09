import networkx as nx

def extract_from_file() -> list[str]:
    with open("Day 23\\input.txt") as file:
        return [line.strip() for line in file]

def find_triangles(network_map: list[str]) -> int:
    g = nx.parse_edgelist(network_map, delimiter='-')
    triangles = set()

    for node in g:
        neighbors = set(g[node])
        for neighbor in neighbors: # iterates through each neighbor of each neighbor of original node
            common_neighbors = neighbors & set(g[neighbor]) # finds the ones that are in common -> these are triangles
            for cn in common_neighbors:
                triangle = tuple(sorted([node, neighbor, cn]))
                if any(label.startswith('t') for label in triangle):
                    triangles.add(triangle)
    
    return len(triangles)

def find_password(network_map: list[str]) -> int:
    g = nx.parse_edgelist(network_map, delimiter='-')
    cliques = list(nx.find_cliques(g))
    max_clique = max(cliques, key=len)

    return ','.join(sorted(max_clique))

if __name__ == '__main__':
    connections = extract_from_file()
    print("Number of groups of 3 computers where at least 1 starts with the letter 't': ", find_triangles(connections))
    print("Password to enter the LAN party: ", find_password(connections))