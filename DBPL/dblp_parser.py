from xml import sax
from itertools import combinations
from tqdm import tqdm as progress

class IItemStrategy:
    TAG = ""

    def __init__(self):
        pass

    def start_item(self, *args):
        pass

    def update_item(self, *args):
        pass

    def end_item(self, *args):
        pass

    def get_data(self):
        return None

class DataHandler(sax.ContentHandler):
    TAGS = {
        'volume', 'book', 'editor', 'cite', 'i',
        'author', 'www', 'booktitle', 'note', 'series',
        'tt', 'inproceedings', 'crossref', 'address', 'number',
        'journal', 'publisher', 'url', 'ee', 'isbn', 'incollection',
        'title', 'cdrom', 'school', 'sup', 'phdthesis', 'proceedings',
        'article', 'sub', 'year', 'pages', 'dblp', 'month'
    }

    def __init__(self, author_callback=None):
        sax.ContentHandler.__init__(self)
        self.CurrentData = ""
        self.author      = ""
        self.title       = ""
        self.year        = ""
        self.school      = ""
        self.pages       = ""
        self.isbn        = ""
        self.ee          = ""

        self.author_callback = author_callback or IItemStrategy()

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.author_callback.end_item(tag)

        self.CurrentData = tag
        # attributes: mdate, key

        self.author_callback.start_item(tag)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "author":
            # print ("author:", self.author)
            self.author_callback.update_item(self.author)
        # elif self.CurrentData == "title":
        #     # print ("title:", self.title)
        #     pass
        # elif self.CurrentData == "year":
        #     # print ("Year:", self.year)
        #     pass
        # elif self.CurrentData == "school":
        #     # print ("school:", self.school)
        #     pass
        # elif self.CurrentData == "pages":
        #     # print ("pages:", self.pages)
        #     pass
        # elif self.CurrentData == "isbn":
        #     # print ("isbn:", self.isbn)
        #     pass
        # elif self.CurrentData == "ee":
        #     # print ("ee:", self.ee)
        #     pass
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        # elif self.CurrentData == "title":
        #     self.title = content
        # elif self.CurrentData == "year":
        #     self.year = content
        # elif self.CurrentData == "school":
        #     self.school = content
        # elif self.CurrentData == "pages":
        #     self.pages = content
        # elif self.CurrentData == "isbn":
        #     self.isbn = content
        # elif self.CurrentData == "ee":
        #     self.ee = content



class AuthorStrategyFrequency(IItemStrategy):
    TAG = "author"

    def __init__(self, show_progress=False):
        self.authors      = {}
        self.tag          = ""
        self.current_item = None
        self.total_items = 0

        self.progress = progress(total=1,
                                 desc="  Finding 1-tuples...",
                                 ncols=100, ascii=True) \
                            if show_progress else None

    def __del__(self):
        self.stop()

    def stop(self):
        if self.progress:
            self.progress.close()

    def start_item(self, tag):
        self.tag = tag

    def update_item(self, author):
        if self.tag == self.TAG:
            self.current_item = author

            if self.current_item in self.authors:
                self.authors[self.current_item] += 1
            else:
                self.authors[self.current_item] = 1

    def end_item(self, tag):
        if self.tag == self.TAG and self.tag != tag:
            self.total_items += 1
            if self.progress:
                self.progress.update()
        self.current_item = ""

    def get_data(self):
        return self.authors


class AuthorStrategySets(IItemStrategy):
    TAG = "author"

    def __init__(self):
        self.authors      = {}
        self.tag          = ""
        self.current_item = []

    def start_item(self, tag):
        self.tag = tag

    def update_item(self, author):
        if self.tag == self.TAG:
            self.current_item.append(author)

    def end_item(self, tag):
        if self.tag == self.TAG and self.tag != tag and self.current_item:
            self.current_item = tuple(sorted(self.current_item))

            if self.current_item in self.authors:
                self.authors[self.current_item] += 1
            else:
                self.authors[self.current_item] = 1

            self.current_item = []

    def get_data(self):
        return self.authors


class AuthorStrategyNTupleFrequency(IItemStrategy):
    TAG = "author"

    def __init__(self, n_supported_uniques, key_to_idx, tuple_size, prev_size=0):
        self.authors      = {}
        self.freq_authors = n_supported_uniques
        self.key_to_idx   = key_to_idx
        self.tuple_size   = tuple_size
        self.tag          = ""
        self.current_item = []

        self.progress = progress(total=prev_size or 1,
                                 desc="  Finding {}-tuples...".format(self.tuple_size),
                                 ncols=100, ascii=True)

    def __del__(self):
        self.stop()

    def stop(self):
        if self.progress:
            self.progress.close()

    def start_item(self, tag):
        self.tag = tag

    def update_item(self, author):
        if self.tag == self.TAG:
            idx = self.key_to_idx[author]

            # Only add single if it is within supported threshold, i.e in freq_authors
            if idx in self.freq_authors:
                self.current_item.append(idx)

    def end_item(self, tag):
        if self.tag == self.TAG and self.tag != tag:
            # Lazy combinations, only create combinations from current_items
            # Since these are already frequent, the combinations will be frequent as well
            if self.current_item and len(self.current_item) >= self.tuple_size:
                n_tuples = combinations(sorted(self.current_item), self.tuple_size)

                for t in n_tuples:
                    if t in self.authors:
                        self.authors[t] += 1
                    else:
                        self.authors[t] = 1

            self.current_item = []
            self.progress.update()

    def get_data(self):
        return self.authors


def run_parser_strategy(data, strat=AuthorStrategyFrequency()):
    xmlparser = sax.make_parser()

    xmlparser.setFeature(sax.handler.feature_namespaces, 0)
    xmlparser.setContentHandler(DataHandler(strat))

    xmlparser.parse(data)

    return strat


if __name__ == "__main__":
    DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
    # DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
    DATASNAP = "C:/Apps/Github/BDA-Assignments/DBLP/dblp50000.xml"

    DATA = DATASNAP


    author_strategy = AuthorStrategySets()

    run_parser_strategy(DATA, author_strategy)

    print("Authors:", len(author_strategy.get_data()))  # 2'347'426
    # print("Authors:", len(auteurs))  # 69'706

    c = 10
    for k, v in author_strategy.get_data().items():
        print ("{0:30s}: {1}".format("{}".format(k), v))
        c -= 1
        if c == 0: break
