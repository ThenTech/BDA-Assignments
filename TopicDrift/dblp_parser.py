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

        self.item_callback.start_item(tag)

    # Call when an elements ends
    def endElement(self, tag):
        # if self.CurrentData == "author":
        #     # print ("author:", self.author)
        #     self.item_callback.update_item(self.author)
        if self.CurrentData == "title":
            # print ("title:", self.title)
            self.item_callback.update_item(self.title)
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


class TitleStrategyWords(IItemStrategy):
    TAG  = "title"
    TAG2 = "year"

    def __init__(self, ignore_words=None, ignore_chars="", translate_words=None, show_progress=True):
        self.ignore           = ignore_words or []
        self.ignore_chars     = ignore_chars or ""
        self.ignore_translate = { ord(c): None for c in self.ignore_chars }
        self.word_translate   = translate_words or {}
        self.titles           = {}

        self.tag          = ""
        self.current_item = []
        self.current_year = -1

        self.progress = progress(total=1,
                                 desc="  Aggregating titles...",
                                 ncols=79, ascii=True) \
                    if show_progress else None

    def __del__(self):
        self.stop()

    def stop(self):
        if self.progress:
            self.progress.close()

    def start_item(self, tag):
        self.tag = tag

    def update_item(self, value):
        if self.tag == self.TAG:
            self.current_item.extend(value.lower().split(" "))
        elif self.tag == self.TAG2:
            self.current_year = int(value)

    def end_item(self, tag):
        if ((self.tag == self.TAG and self.tag != tag) or (self.tag == self.TAG2 and self.tag != tag)) \
          and self.current_item and self.current_year > 1900:
            # Clean title
            cleaned = []

            for word in self.current_item:
                # Remove chars
                word = word.translate(self.ignore_translate).strip()

                # Translate
                if word in self.word_translate:
                    word = self.word_translate[word]

                if word and word not in self.ignore:
                    cleaned.append(word)

            if self.current_year not in self.titles:
                self.titles[self.current_year] = []

            # self.titles[self.current_year].append(tuple(cleaned))
            self.titles[self.current_year].append(" ".join(cleaned))

            self.current_item = []
            self.current_year = -1

            if self.progress:
                self.progress.update()

    def get_data(self):
        return self.titles


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
