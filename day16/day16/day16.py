# AOC 2022 Day 16

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day16" / "day16"

class Node:
    def __init__(self, name):
        self.name = name
        self.flow = 0
        self.tunnels = []
        self.cost = {}
        self.visited = False


def parse(lines):
    nodes = {}
    for line in lines:
        node_name = line[6:8]
        flow = int(line[line.index("=")+1:line.index(";")])

        # Add or update this node
        if node_name in nodes.keys():
            nodes[node_name].flow = flow

        else:
            node = Node(node_name)
            node.flow = flow
            nodes[node_name] = node

        # Is there more than one connection
        if line[line.index("valve")+5] == "s":
            # There are, process them all
            for tunnel_name in line[line.index("valve")+6:].strip().split(", "):
                if tunnel_name not in nodes.keys():
                    tunnel = Node(tunnel_name)
                    nodes[tunnel_name] = tunnel

                nodes[node_name].tunnels.append(tunnel)
                nodes[node_name].cost[tunnel_name] = 1

        else:
            # Only one connection
            tunnel_name = line[line.index("valve")+6:]
            if tunnel_name not in nodes.keys():
                tunnel = Node(tunnel_name)
                nodes[tunnel_name] = tunnel

            nodes[node_name].tunnels.append(tunnel)
            nodes[node_name].cost[tunnel_name] = 1

    return nodes["AA"]
            
def find_flow(fr, to, current_flow, steps):
    # Are there any steps left?
    if steps == 0:
        return current_flow

    current_flow += current_flow

    # Have we visited this node already?
    if not to.visited:
        to.visited = True

        # Is there flow here?
        if to.flow > 0:
            # Add it and reduce the steps
            steps -= 1
            current_flow += to.flow

    # Recursively check the everything from here
    for node in to.tunnels:
        current_flow += find_flow(to, node, current_flow, steps-1)

    return current_flow
       

def part1(lines):
    valves = parse(lines)
    max_flow = 0

    valves.visited = True

    # Look at each path from "AA" to see what the max flow is
    for node in valves.tunnels:
        flow = find_flow(valves, node, 0, 29)
        max_flow = max(flow, max_flow)

    return max_flow

def part2(lines):
    pass

if __name__ == "__main__":

    # with open(root_path / "input", "r") as f:
    with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print(f"Part 1: Answer: {part1(lines)}")
    print(f"Part 2: Answer: {part2(lines)}")
