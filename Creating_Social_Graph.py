import itertools
from nltk import sent_tokenize
import nltk
nltk.download('punkt')
import urllib.request 
import json
import networkx as nx
import matplotlib.pyplot as plt


def cooccurrence(text, cast):
    """
    Takes as input text, a dict of chapter {headings: text},
    and cast, a comma separated list of character names.
    Returns a dictionary of cooccurrence counts for each
    possible pair.
    """
    possible_pairs = list(itertools.combinations(cast, 2))
    cooccurring = dict.fromkeys(possible_pairs, 0)
    for title, chapter in text['chapters'].items():
        for sent in sent_tokenize(chapter):
            for pair in possible_pairs:
                if pair[0] in sent and pair[1] in sent:
                    cooccurring[pair] += 1
    return cooccurring

url = 'https://s3.amazonaws.com/ddl-data-lake/oz.json'
data = urllib.request.urlopen(url).read().decode('utf-8-sig')

text = json.loads(data)
cast = text['cast']

G = nx.Graph()
G.name = "The Social Network of Oz"

pairs = cooccurrence(text, cast)
for pair, wgt in pairs.items():
    if wgt > 0:
        G.add_edge(pair[0], pair[1], weight=wgt)

# Make Dorothy the center
D = nx.ego_graph(G, "Dorothy")
edges, weights = zip(*nx.get_edge_attributes(D, "weight").items())

# Push nodes away that are less related to Dorothy
pos = nx.spring_layout(D, k=.5, iterations=40)
nx.draw(D, pos, node_color="gold", node_size=50, edgelist=edges, width=1, edge_color="orange", with_labels=True, font_size=12)

plt.savefig('social_graph.jpg')
plt.show()