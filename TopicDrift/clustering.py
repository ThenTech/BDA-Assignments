from dblp_parser import run_parser_strategy, IItemStrategy, TitleStrategyWords
import sys
import os
import time

import scipy.cluster as cl
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
DATASNAP = "C:/Apps/Github/BDA-Assignments/DBLP/dblp50000.xml"

# DATAFULL = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp.xml"
# DATASNAP = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp50000.xml"

DATA = DATASNAP


class Clusterer:
    IGNORE_WORDS = [
        "data", "database", "novel", "using", "approach", "based", "new",
        "proceedings", "use", "fast",
        "the", "a", "an",
        "and", "of", "on", "for", "in", "is", "und", "der",
    ]
    IGNORE_CHARS = ".,:-'\"!@#$"
    TRANSLATE_WORDS = {
        "algorithms": "algorithm",
        "technologies": "technology",
        "systems": "system",
        "models": "model",
        "methods": "method",
        "programs": "program",
        "designs": "design",
        "images": "image",
        "networks": "network",
        "applications": "application",
        "databases": "database",
        "problems": "problem",
        "generations": "generation",
        "estimations": "estimation",
    }

    def __init__(self, data_path, k=10, seed=None):
        self.data_path  = data_path
        self.k          = max(1, k)
        self.iterations = 10
        self.seed       = seed

        if not os.path.exists(data_path):
            raise Exception("[Clusterer] No such file: {}".format(data_path))

        self.documents = {}  # {year: [[title 1 words], [title 2 words] ...] }

    def start(self):
        print("Start parsing {0}...".format(self.data_path))

        strat = run_parser_strategy(self.data_path,
                                    TitleStrategyWords(self.IGNORE_WORDS, self.IGNORE_CHARS, self.TRANSLATE_WORDS))
        strat.stop()

        self.documents = strat.get_data()

        print ("Found titles for {0} years, to find {1} clusters/topics.\n".format(len(self.documents), self.k))

    def plot_year(self, year, top_x = 10):
        print("Plotting top {0} items for year {1}...".format(top_x, year))

        if year not in self.documents:
            print("  No such year!")
            return

        data = self.documents[year]

        counts = CountVectorizer(max_df=0.85, min_df=2, stop_words='english')
        fitted = counts.fit_transform(data)

        LDA = LatentDirichletAllocation(n_components=self.k, random_state=self.seed)
        LDA.fit(fitted)

        for i, topic in enumerate(LDA.components_):
            topic_top_rank = sorted(counts.get_feature_names()[i] for i in topic.argsort()[-top_x:])
            print("  Topic {1}: {2}".format(top_x, i+1, ", ".join(topic_top_rank)))


if __name__ == "__main__":
    data_path, cluster_amount = DATA, 5

    argc = len(sys.argv)
    if argc != 3:
        print("No args given! Expected file path and cluster_amount.")
        # sys.exit()
    else:
        _, data_path, cluster_amount = sys.argv
        cluster_amount = int(cluster_amount)

    c = Clusterer(data_path, cluster_amount, seed=1746077)

    c.start()
    c.plot_year(2000)
    c.plot_year(2001)
