from dblp_parser import run_parser_strategy, IItemStrategy, AuthorStrategyFrequency, AuthorStrategySets, AuthorStrategyNTupleFrequency
from itertools import combinations

DATAFULL = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp.xml"
# DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
DATASNAP = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp50000.xml"

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


    # basket_n = len(strat.get_data())
    # fraction = int(0.001 * basket_n)
    # strat.authors = {k: v for (k, v) in list(strat.get_data().items())[:fraction] }


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
    pass_ctr = 2
    if (len(authors_thesholded) > 0):
        n_thresholded = do_pass_n(pass_ctr, support_threshold, authors_thesholded)
        pass_ctr += 1
        while (len(n_thresholded) > 0):
            do_pass_n(pass_ctr, support_threshold, n_thresholded)
            pass_ctr += 1


def do_pass_n(n, support_threshold, authors_thesholded):
    print("Start pass {}...".format(n))

    author_combinations = combinations(authors_thesholded.keys(), 2)

    author_pairs = { k: 0 for k in author_combinations }
    amount_n_tuples = len(author_pairs)

    print("Created {} pairs.".format(amount_n_tuples))

    print("Find pairs in itemsets...")
    strat = run_parser_strategy(DATA, AuthorStrategyNTupleFrequency(author_pairs, n))

    dump_list_to_file(strat.get_data().items(), "pass_2_pair_freqs.txt")

    n_thresholded = {}
    for k, v in strat.get_data().items():
        if v >= support_threshold:
            n_thresholded[k] = v

    print("{} pairs >= support {}.".format(len(n_thresholded), support_threshold))

    dump_list_to_file(n_thresholded.items(), "pass_2_pair_freqs_support.txt")

    return n_thresholded

if __name__ == "__main__":
    print("Start")

    # apriori_test()
    apriori_implement()
