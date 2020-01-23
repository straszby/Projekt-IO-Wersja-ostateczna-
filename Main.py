import os

from Reader import *
from Graph_service import *
from DrawGraph import *
#from Export import exportXML
from File import File


def main():
    ROOT_DIR = os.path.abspath(os.curdir)
    dirs = find_file(ROOT_DIR)
    file_table = []

    for file in dirs:
        x = parse_file(file)
        file_table.append(File(x.name, x.size, x.dependencies, x.functions))

    draw_graph(build_modules_graph_structure(file_table))

if __name__ == '__main__':
   main()