#funkcja rysujaca graf, przyjmuje liste z listami
# nalezy zainsatalowac biblioteke Graphviz 2.38 i dodac .../Graphviz 2.38/bin
# do zmiennych srodowiskowych
from graphviz import Digraph
import os

def draw_graph(data):
	graph = Digraph(comment='Program Dependences Diagram')
	graph.attr('node', shape='box', style='filled', fillcolor='lightblue')

	for x in data:
		vertex1 = x[0] + "\n" + str(x[1])
		vertex2 = x[2] + "\n" + str(x[3])
		edge = str(x[4])
		graph.edge(vertex1, vertex2, edge)

	graph.attr(fontsize='20')
	graph.view()


