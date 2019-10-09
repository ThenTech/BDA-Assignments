from dblp_parser import run_parser_strategy, IItemStrategy, AuthorStrategyFrequency, AuthorStrategySets
from itertools import combinations
import threading
from tqdm import tqdm as progress

DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
# DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
DATASNAP = "C:/Apps/Github/BDA-Assignments/DBLP/dblp50000.xml"

DATA = DATASNAP

"""
Pass 1
    - Vertaal tabel: [author,    id]
    - Count tabel  : [id    , count]

        => dict {author: count}?

Pass 2
    - Only use authors count >= support_threshold
    - Make combinations of
"""

def dump_list_to_file(li, fname):
    with open(fname, 'w') as fp:
        for i in li:
            fp.write("{0}\n".format(i))

def apriori_test():
    from efficient_apriori import apriori

    strat = run_parser_strategy(DATA, AuthorStrategySets())


    basket_n = len(strat.get_data())
    fraction = int(0.001 * basket_n)
    baskets  = list(strat.get_data().keys())[:fraction]

    print("Baskets:", basket_n)
    print("Pick {} items...".format(fraction))

    itemsets, rules = apriori(baskets,
                              min_support=20/basket_n, min_confidence=1.0,
                              verbosity = 1)

    dump_list_to_file(["{} :\n  {}".format(k, "\n  ".join("{}".format(x) for x in v)) for k, v in itemsets.items()], "apr_test_itemsets.txt")
    dump_list_to_file(rules, "apr_test_rules.txt")


def apriori_implement(support_threshold = 12):
    ####################
    # ----- Pass 1 -----
    print("Start pass 1...")

    strat = run_parser_strategy(DATA, AuthorStrategyFrequency())
    # freqs -> strat.get_data()  ==> { author: freq }

    n_authors = len(strat.get_data())
    print("Found freqs for {} authors.".format(n_authors))

    # Adjust for support
    authors_thesholded = {}

    for k, v in strat.get_data().items():
        if v >= support_threshold:
            authors_thesholded[k] = v

    del strat
    strat = None

    dump_list_to_file(authors_thesholded.items(), "pass_1_single_freqs.txt")
    print("{} authors >= support {}.".format(len(authors_thesholded), support_threshold))


    ####################
    # ----- Pass 2 -----
    print("Start pass 2...")

    author_combinations = combinations(authors_thesholded.keys(), 2)

    author_pairs = { k: 0 for k in author_combinations }
    amount_n_tuples = len(author_pairs)

    print("Created {} pairs.".format(amount_n_tuples))

    class AuthorStrategyPairFrequency(IItemStrategy):
        TAG = "author"

        def __init__(self, author_pairs):
            self.authors      = author_pairs
            self.tag          = ""
            self.current_item = []


            self.__keys = list(self.authors.keys())
            self.size   = len(self.__keys)
            self.progress = progress(total=amount_n_tuples,
                                     desc="Finding {}-tuples...".format(2),
                                     ncols=100, ascii=True)

        def __del__(self):
            self.progress.close()

        def __threaded_check(self):
            def check(start, end):
                start, end = int(start), int(end)
                for i in range(start, end):
                    key = self.__keys[i]
                    if all(t in self.current_item for t in key):
                            self.authors[key] += 1

            max_threads = 4
            threads = []

            for i in range(max_threads):
                threads.append(threading.Thread(target=check,
                                                args=(self.size * i / max_threads,
                                                      self.size * (i+1) / max_threads)))
                threads[i].start()

            for t in threads:
                t.join()

        def start_item(self, tag):
            self.tag = tag

        def update_item(self, author):
            if self.tag == self.TAG:
                self.current_item.append(author)

        def end_item(self, tag):
            if self.tag == self.TAG and self.tag != tag and self.current_item:
                if len(self.current_item) >= 2:

                    self.__threaded_check()
                    self.progress.update(1)

                    # for author_tuple in self.authors.keys():
                    #     if all(t in self.current_item for t in author_tuple):
                    #         self.authors[author_tuple] += 1

                self.current_item = []

        def get_data(self):
            return self.authors

    print("Find pairs in itemsets...")
    strat = run_parser_strategy(DATA, AuthorStrategyPairFrequency(author_pairs))

    dump_list_to_file(strat.get_data().items(), "pass_2_pair_freqs.txt")

    n_thresholded = {}
    for k, v in strat.get_data().items():
        if v >= support_threshold:
            n_thresholded[k] = v

    print("{} pairs >= support {}.".format(len(n_thresholded), support_threshold))

    dump_list_to_file(n_thresholded.items(), "pass_2_pair_freqs_support.txt")

if __name__ == "__main__":
    print("> Start with {}".format(DATA))

    # apriori_test()
    apriori_implement()
