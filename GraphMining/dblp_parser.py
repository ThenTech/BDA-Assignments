from xml import sax
from itertools import combinations
from tqdm import tqdm as progress

class IItemStrategy:
    TAG = ""

    def __init__(self):
        pass

    def set_attribute(self, *args):
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

    def __init__(self, item_callback=None):
        sax.ContentHandler.__init__(self)
        self.CurrentData = ""
        self.author      = ""
        self.title       = ""
        self.year        = ""
        self.school      = ""
        self.pages       = ""
        self.isbn        = ""
        self.ee          = ""

        self.item_callback = item_callback or IItemStrategy()

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.item_callback.end_item(tag)

        self.CurrentData = tag

        # attributes: mdate, key
        self.item_callback.set_attribute(attributes)

        self.item_callback.start_item(tag)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "author":
            # print ("author:", self.author)
            self.item_callback.update_item(self.author)
        # if self.CurrentData == "title":
        #     # print ("title:", self.title)
        #     self.item_callback.update_item(self.title)
        elif self.CurrentData == "year":
            # print ("Year:", self.year)
            self.item_callback.update_item(self.year)
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
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "year":
            self.year = content
        # elif self.CurrentData == "school":
        #     self.school = content
        # elif self.CurrentData == "pages":
        #     self.pages = content
        # elif self.CurrentData == "isbn":
        #     self.isbn = content
        # elif self.CurrentData == "ee":
        #     self.ee = content


class AuthorStrategyYearGraphs(IItemStrategy):
    TAG  = "author"
    TAG2 = "year"
    ATTR = "key"

    def __init__(self, graph_class=None, filter_key=None, show_progress=True):
        self.graph_class = graph_class
        self.filter_key  = filter_key

        self.authors = {}

        self.key          = False
        self.tag          = ""
        self.current_item = []
        self.current_year = -1

        self.progress = progress(total=1,
                                 desc="  Finding authors...",
                                 ncols=79, ascii=True) \
                            if show_progress else None

    def __del__(self):
        self.stop()

    def stop(self):
        if self.progress:
            self.progress.close()

    def set_attribute(self, attr):
        if self.filter_key and attr.getLength() == 2:
            self.key = self.filter_key in attr.get(self.ATTR, "").lower()

            if self.key:
                # Clear previous
                self.current_item = []
                self.current_year = -1

    def start_item(self, tag):
        self.tag = tag

    def update_item(self, value):
        if self.tag == self.TAG:
            self.current_item.append(value)
        elif self.tag == self.TAG2:
            self.current_year = int(value)

    def end_item(self, tag):
        if ((self.tag == self.TAG and self.tag != tag) or (self.tag == self.TAG2 and self.tag != tag)) \
          and self.current_item and self.current_year > 1900:
            if self.key:
                if self.current_year not in self.authors:
                    self.authors[self.current_year] = self.graph_class(self.current_year)

                # Add nodes and edges
                if len(self.current_item) > 1:
                    for a1, a2 in combinations(self.current_item, 2):
                        self.authors[self.current_year].AddConnection(a1, a2)
                        # self.authors[self.current_year].AddConnection(a2, a1)
                else:
                    self.authors[self.current_year].AddItem(self.current_item[0])

            self.current_item = []
            self.current_year = -1

            if self.progress:
                self.progress.update()

    def get_data(self):
        return self.authors


def run_parser_strategy(data, strat=None):
    xmlparser = sax.make_parser()

    xmlparser.setFeature(sax.handler.feature_namespaces, 0)
    xmlparser.setContentHandler(DataHandler(strat))

    xmlparser.parse(data)

    return strat
