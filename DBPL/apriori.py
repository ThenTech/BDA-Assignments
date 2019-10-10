from dblp_parser import run_parser_strategy, IItemStrategy, AuthorStrategyFrequency, AuthorStrategySets, AuthorStrategyNTupleFrequency
from itertools import chain
import sys
import os
import time

DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"

# DATAFULL = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp.xml"
# DATASNAP = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp50000.xml"

DATA = DATAFULL


def dump_list_to_file(li, key_lut, fname):
    if not key_lut:
        with open(fname, 'w') as fp:
            for i in li:
                fp.write("{0}\n".format(i))
    else:
        with open(fname, 'w') as fp:
            for i in li:
                keys = (i[0],) if isinstance(i[0], int) else i[0]
                keys = tuple(map(lambda x: key_lut[x], keys))
                fp.write("{0}: {1}\n".format(keys, i[1]))


def apriori_test():
    """For debug comparison only."""
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

    dump_list_to_file(["{} :\n  {}".format(k, "\n  ".join("{}".format(x) for x in v)) for k, v in itemsets.items()], {}, "apr_test_itemsets.txt")
    dump_list_to_file(rules, {}, "apr_test_rules.txt")


class Apriori:
    def __init__(self, data_path, support_threshold = 15):
        self.data_path         = data_path
        self.support_threshold = max(1, support_threshold)

        if not os.path.exists(data_path):
            raise Exception("[Apriori] No such file: {}".format(data_path))

        self.pass_counter = 1
        self.total_items  = 0
        self.key_to_index = {}  # To translat from name to idx -> improve memory consumption
        self.index_to_key = []  # For printing original names

    def __filter_dict(self, d):
        n_thresholded = {}

        for k, v in d.items():
            if v >= self.support_threshold:
                n_thresholded[k] = v

        return n_thresholded

    def __next_pass(self, authors_thesholded):
        print("Start pass {}...".format(self.pass_counter))

        if self.pass_counter == 1:
            # First pass gets unique frequencies

            strat = run_parser_strategy(self.data_path, AuthorStrategyFrequency(show_progress=True))
            # freqs -> strat.get_data()  ==> { author: freq }

            strat.stop()
            amount_n_tuples  = len(strat.get_data())
            self.total_items = strat.total_items

            print("  Caching singles LUT...")
            self.key_to_index = { k: i for i, k in enumerate(strat.get_data().keys()) }
            self.index_to_key = list(strat.get_data().keys())

            simplified_keys_dict = {}
            for k, v in strat.get_data().items():
                simplified_keys_dict[self.key_to_index[k]] = v
            strat.authors = simplified_keys_dict

            print("  Created {} {}-tuples.".format(amount_n_tuples, self.pass_counter))
        else:
            # N-pass gets n-tuple frequencies

            n_supported_uniques = authors_thesholded.keys()
            if self.pass_counter > 2:
                # Chain used keys from previous pass to single unique list, keeping order
                n_supported_uniques = dict.fromkeys(chain(*n_supported_uniques))

            # Previously, combinations were created here, but this needed too much memory.
            # Now only the supported uniques from the previous pass are aggregated, and hashed
            # into a dictionary for O(1) lookup.
            # Combinations are now made when reading a basket.

            print("  {} supported uniques from previous pass to find tuples.".format(len(n_supported_uniques)))

            strat = run_parser_strategy(self.data_path,
                                        AuthorStrategyNTupleFrequency(n_supported_uniques, self.key_to_index, self.pass_counter,
                                                                      prev_size=self.total_items))
            strat.stop()

            print("  Created {} {}-tuples.".format(len(strat.get_data()), self.pass_counter))

        dump_list_to_file(strat.get_data().items(), self.index_to_key, "pass_{}-tuples_freqs.txt".format(self.pass_counter))

        # Filter on support threshold
        n_thresholded = self.__filter_dict(strat.get_data())

        del strat  # Explicit delete
        print("  {} {}-tuples >= support {}.".format(len(n_thresholded), self.pass_counter, self.support_threshold))

        dump_list_to_file(n_thresholded.items(), self.index_to_key, "pass_{}-tuples_freqs_support.txt".format(self.pass_counter))

        self.pass_counter += 1
        return n_thresholded

    def start(self):
        """Run passes over the data xml."""
        print("> Run with \"{}\" and support {}".format(self.data_path, self.support_threshold))

        n_thresholded = {}

        start = time.perf_counter()

        while True:
            n_thresholded = self.__next_pass(n_thresholded)
            if len(n_thresholded) < 2:
                # If there are no or only one n-tuple, no new (n+1)-tuples can be created
                break

        end = time.perf_counter() - start
        minutes, seconds = int(end // 60), end % 60

        print("\n> Completed {0} passes in {1:02d}:{2:06.3f}".format(self.pass_counter, minutes, seconds))


if __name__ == "__main__":
    data_path, support_threshold = DATA, 15

    argc = len(sys.argv)
    if argc < 3:
        print("No args given! Expected file path and support_threshold.")
        # sys.exit()
    else:
        data_path, support_threshold = sys.argv
        support_threshold = int(support_threshold)

    # apriori_test()
    Apriori(data_path, support_threshold).start()
