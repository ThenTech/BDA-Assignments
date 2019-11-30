from dblp_parser import run_parser_strategy, IItemStrategy, TitleStrategyWords
import sys
import os
import math

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.stem import PorterStemmer

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from collections import Counter

from pyLDAvis import sklearn as sklearn_lda
import pyLDAvis


DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
DATAFULL = "C:/Apps/Github/BDA-Assignments/DBLP/dblp.xml"
DATASNAP = "C:/Apps/Github/BDA-Assignments/DBLP/dblp50000.xml"

# DATAFULL = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp.xml"
# DATASNAP = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp50000.xml"

DATA = DATAFULL


def safe_file_name(name, include=tuple()):
    removechars = ('\\', '/', '*', '?', ':', '"', '|', '<', '>')
    return "".join(c for c in name if c not in removechars or c in include).strip()


class Clusterer:
    IGNORE_WORDS = [
        "data", "database", "databas", "novel", "using", "approach", "base", "new",
        "proceed", "use", "fast", "through",
        "the", "a", "an", "at", "to", "with", "from", "by", "your", "via", "you",
        "and", "of", "on", "no", "for", "in", "is", "und", "der", "für", "von",
    ]
    IGNORE_CHARS = ".,:-'\"!?@#$/\\"
    TRANSLATE_WORDS = {
        "optimising" : "optimise",
        "optimizing" : "optimise",
        "behaviors"  : "behaviours",
    }

    def __init__(self, data_path, pub_key="", k=10, seed=None, show_plot=True, save_plot=True, save_visualisation=True):
        self.data_path  = data_path
        self.k          = max(1, k)
        self.iterations = 10
        self.seed       = seed
        self.publication_key = pub_key.lower()
        self.stemmer    = PorterStemmer()

        self.show_plot = show_plot
        self.save_plot = save_plot
        self.save_visualisation = save_visualisation

        self.output_prefix = "./visualisation/"

        if not os.path.exists(data_path):
            raise Exception("[Clusterer] No such file: {}".format(data_path))

        self.documents = {}  # {year: [[title 1 words], [title 2 words] ...] }

    def prepare(self):
        print("Start parsing {0}...".format(self.data_path))

        strat = run_parser_strategy(self.data_path,
                                    TitleStrategyWords(self.publication_key,
                                                       self.IGNORE_WORDS, self.IGNORE_CHARS, self.TRANSLATE_WORDS,
                                                       self.stemmer))
        strat.stop()

        self.documents = strat.get_data()

        print ("Found titles for {0} years, to find {1} clusters/topics in {2}.\n"\
                .format(len(self.documents), self.k, self.publication_key if self.publication_key else "any"))

    def plot_year(self, year, top_x = 10):
        data = []

        if isinstance(year, tuple):
            for y in range(year[0], year[1]):
                if y in self.documents:
                    data.extend(self.documents[y])

            print("Plotting top {0} items for years {1}-{2} ({3} publications)..."\
                .format(top_x, year[0], year[1], len(data) if len(data) > 0 else "no"))
        else:
            data = self.documents[year] if year in self.documents else []

            print("Plotting top {0} items for year {1} ({2} publications)..."\
                    .format(top_x, year, len(data) if len(data) > 0 else "no"))

            if year not in self.documents:
                print("  No such year!")
                return

        if len(data) < 3:
            print("  Too little data!")
            return

        try:
            counts = CountVectorizer(max_df=0.96, min_df=2, stop_words="english")
            fitted = counts.fit_transform(data)
            vocabulary = counts.get_feature_names()

            LDA = LatentDirichletAllocation(n_components=self.k, random_state=self.seed, n_jobs=4, max_iter=self.iterations)
            LDA.fit(fitted) # Fit with same data, no training data available...
            lda_transformed = LDA.transform(fitted)
        except Exception as e:
            print("  {0}".format(e))
            return

        # Normalise?
        lda_components = LDA.components_ / LDA.components_.sum(axis=1)[:, np.newaxis]

        all_words = {}

        # Count how many docs/titles are assigned to each of the self.k topics
        doc_topics = lda_transformed.argmax(axis=1)
        total_docs_in_topic = Counter(doc_topics)

        output = self.output_prefix + "{0}_k{1}/".format(safe_file_name(self.publication_key) if self.publication_key else "any", self.k)
        if not os.path.exists(output):
            os.makedirs(output)

        out_info = "cat={0}_year={1}_k={2}".format(safe_file_name(self.publication_key) if self.publication_key else "any",
                                                   year, self.k)
        plt.figure(num="Plot for " + out_info, dpi=200)
        plt.suptitle("Clusters for {0} field ({1} publications) in {2}" \
                        .format(self.publication_key if self.publication_key else "any",
                                len(data), year),
                     fontsize=14)
        plt_rows, plt_cols = 3, math.ceil(self.k / 2)
        plt_shape = (plt_rows, plt_cols)

        for i, topic in enumerate(lda_components):
            words = {}
            topic_score = lda_transformed[0][i]

            # Get scores for each word
            for (word_idx, word_score) in zip(topic.argsort()[-top_x:], sorted(topic)[-top_x:]):
                score = topic_score * word_score
                word = vocabulary[word_idx]

                words[word] = score

                if word not in all_words:
                    all_words[word] = word_score
                else:
                    all_words[word] += word_score

            # Create cloud
            wordcloud = WordCloud(background_color="white", width=400, height=250).generate_from_frequencies(words)

            # Print from high to low score
            words = map(lambda x: x[0], sorted(words.items(), key=lambda kv: kv[1], reverse=True))
            # words = sorted(words.keys())
            print("  Topic {0} ({1} titles): {2}".format(i+1, total_docs_in_topic[i], ", ".join(words)))

            plt.subplot2grid(plt_shape, (i // plt_cols, i % plt_cols), rowspan=1, colspan=1)
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.title("Cluster {0}".format(i+1), fontsize=8)
            plt.axis("off")

        # Create cloud for all of year
        wordcloud = WordCloud(background_color="white", width=2500, height=720).generate_from_frequencies(all_words)
        plt.subplot2grid(plt_shape, (plt_rows-1, 0), rowspan=1, colspan=plt_cols)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.title("All words")
        plt.axis("off")
        plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.88, wspace=0.15, hspace=0.20)

        if self.save_plot:
            plt.savefig(output + "plot_{0}.png".format(out_info), dpi=200)
        if self.show_plot:
            plt.show()

        if self.save_visualisation:
            LDAvis_prepared = sklearn_lda.prepare(LDA, fitted, counts)
            pyLDAvis.save_html(LDAvis_prepared, output + "ldavis_{0}.html".format(out_info))


    def plot_single_years(self, year_from = 0, year_to = 3000, top_x = 10):
        for year in range(year_from, year_to+1):
            if year in self.documents:
                self.plot_year(year, top_x=top_x)

    def plot_interval_years(self, year_from = 0, year_to = 3000, delta = 10, offset = 8, top_x = 10):
        for year in range(year_from, year_to+1, offset):
            if year in self.documents:
                last_year = min(year + delta, year_to+1)
                while last_year not in self.documents:
                    last_year -= 1

                self.plot_year((year, last_year), top_x=top_x)



if __name__ == "__main__":
    data_path, pub_key, cluster_amount = DATA, "", 5

    argc = len(sys.argv)
    if argc != 4:
        print("No args given! Expected file path, pub_key and cluster_amount.")
        # sys.exit()
    else:
        _, data_path, pub_key, cluster_amount = sys.argv
        pub_key = "" if "any" in pub_key else pub_key.lower()
        cluster_amount = int(cluster_amount)

    c = Clusterer(data_path, pub_key=pub_key, k=cluster_amount, seed=1746077,
                  show_plot=False, save_plot=True, save_visualisation=True)

    c.prepare()
    # c.plot_year(2000)
    # c.plot_single_years(year_from=1990, year_to=2010)
    c.plot_interval_years(year_from=1990)
