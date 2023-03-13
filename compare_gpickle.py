import os
import networkx as nx
import argparse

parser = argparse.ArgumentParser(description='Compare two folders containing .gpickle files')
parser.add_argument('folder1', metavar='folder1_path', type=str, help='Path to the first folder')
parser.add_argument('folder2', metavar='folder2_path', type=str, help='Path to the second folder')
args = parser.parse_args()

# iterate through the files in each folder
for file1, file2 in zip(os.listdir(args.folder1), os.listdir(args.folder2)):
    # check if both files have the same name
    if file1 == file2:
        # load the .gpickle files into networkx graphs
        graph1 = nx.read_gpickle(os.path.join(args.folder1, file1))
        graph2 = nx.read_gpickle(os.path.join(args.folder2, file2))
        # compare the graphs
        if nx.utils.misc.graphs_equal(graph1, graph2):
            print(f"{file1} and {file2} are equal")
        else:
            print(f"{file1} and {file2} are not equal")
    else:
        print(f"{file1} and {file2} do not have the same name")
