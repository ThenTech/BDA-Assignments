from dblp_parser import run_parser_strategy, IItemStrategy, AuthorStrategyYearGraphs
import sys
import os

import snap

DATAFULL = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp.xml"
DATASNAP = "G:/_temp/UHasselt/BigDataAnalysis/DBLP/dblp50000.xml"
DATAFULL = "C:/Apps/Github/BDA-Assignments/DBLP/dblp.xml"
DATASNAP = "C:/Apps/Github/BDA-Assignments/DBLP/dblp50000.xml"

# DATAFULL = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp.xml"
# DATASNAP = "C:/Users/Cedric/Google Drive (cedric.mingneau@student.uhasselt.be)/BDA persoonlijk/oefeningen/dblp50000.xml"

DATA = DATASNAP


def safe_file_name(name, include=tuple()):
    removechars = ('\\', '/', '*', '?', ':', '"', '|', '<', '>')
    return "".join(c for c in name if c not in removechars or c in include).strip()


class GraphMiner:
    def __init__(self, data_path, filter_key=""):
        self.data_path  = data_path
        self.filter_key = filter_key

        self.author_data = None  # {year: AuthorGraph}

    class Graph:
        def __init__(self, year=-1):
            self.G = snap.PUNGraph.New()
            self.year = year

            self.last_id   = -1
            self.intstore  = {}
            self.itemstore = snap.TIntStrH()

        def AddItem(self, item):
            if not self.has_author(item):
                self.last_id += 1
                self.intstore[item] = self.last_id
                self.itemstore.AddDat(self.last_id, item)

                self.G.AddNode(self.intstore[item])

        def AddConnection(self, item1, item2):
            self.AddItem(item1)
            self.AddItem(item2)
            self.G.AddEdge(self.intstore[item1], self.intstore[item2])

        def get_author_from_id(self, idx):
            return self.itemstore.GetDatWithDefault(idx, "?")

        def has_author(self, name):
            return name in self.intstore

        def get_id_from_author(self, name):
            return self.intstore.get(name, -1)

        def get_node_from_id(self, idx):
            return self.G.GetNI(idx) if self.itemstore.IsKey(idx) else None

        def get_node_from_name(self, name):
            idx = self.get_id_from_author(name)
            return self.G.GetNI(idx) if idx > -1 else None

        def Nodes(self):
            return self.G.Nodes()

        def Edges(self):
            return self.G.Edges()

        def EdgesByNode(self):
            for n in self.Nodes():
                for idx in n.GetOutEdges():
                    yield idx

        @staticmethod
        def __print(txt, outfile=None):
            if outfile:
                outfile.write('\n'.join(txt) + '\n')
            else:
                map(print, txt)

        def print_max_connected(self, outfile=None):
            # Max connected nodes
            MxWcc = snap.GetMxWcc(self.G)

            self.__print((
                "    Max wcc nodes {0}, edges {1}".format(MxWcc.GetNodes(), MxWcc.GetEdges()),
                "      => {0}".format(", ".join(map(lambda n: self.get_author_from_id(n.GetId()) or "?", MxWcc.Nodes())))
            ), outfile)

        def print_rank(self, top_x=10, outfile=None):
            # PageRank: importance of nodes
            PRankH = snap.TIntFltH()
            snap.GetPageRank(self.G, PRankH)
            top_ranks = list(sorted(PRankH, key=lambda v: PRankH[v], reverse=True))[0:top_x]

            self.__print((
                "    Top {0} authors: (by pagerank and edge ratio)\n      {1}"\
                    .format(top_x,
                            "\n      ".join("{1:2.0f}% {0}".format(self.get_author_from_id(i), PRankH[i]*100) \
                                                for i in top_ranks)),
            ), outfile)

        def print_centrality(self, top_x=10, outfile=None):
            Nodes = snap.TIntFltH()
            Edges = snap.TIntPrFltH()
            snap.GetBetweennessCentr(self.G, Nodes, Edges, 1.0)
            top_central = list(sorted(Nodes, key=lambda v: Nodes[v], reverse=True))[0:top_x]

            self.__print((
                "    Top {0} central authors: (by centrality)\n      {1}"
                    .format(top_x,
                            "\n      ".join("{1:4f} {0}".format(self.get_author_from_id(i), Nodes[i]) \
                                                for i in top_central)),
            ), outfile)

        def print_communities(self, outfile=None):
            # Community detection
            CmtyV = snap.TCnComV()
            modularity = snap.CommunityCNM(self.G, CmtyV)

            self.__print(
                ("    Communities:",)
              + tuple("      {0:2d}: ".format(i) + ", ".join(map(self.get_author_from_id, Cmty)) \
                         for i, Cmty in enumerate(CmtyV))
            #   + ("     The modularity of the network is {0}".format(modularity),)
            , outfile)

        def print_cores(self, k=3):
            Core3 = snap.GetKCore(self.G, 3)

            # TODO ?

        def print_node_stats(self, top_x=10, outfile=None):
            self.print_max_connected(outfile=outfile)
            self.print_rank(top_x=top_x, outfile=outfile)
            self.print_centrality(top_x=top_x, outfile=outfile)
            self.print_communities(outfile=outfile)

        def dump(self, name="dump{0}.graph"):
            if not self.G: return

            with snap.TFOut(name.format(self.year)) as out:
                self.G.Save(out)
                out.Flush()

        def export(self, name="export{0}.png", title="Graph for {0}"):
            # Draw to image
            try:
                snap.DrawGViz(self.G, snap.gvlCirco,
                              name.format(self.year),
                              title.format(self.year),
                              self.itemstore)
            except Exception as e:
                print("WARNING: Graph.export - {0}".format(e))

    def prepare(self):
        print("Start parsing {0}...".format(self.data_path))

        strat = run_parser_strategy(self.data_path,
                                    AuthorStrategyYearGraphs(GraphMiner.Graph, self.filter_key))
        strat.stop()
        strat.process_others()

        self.author_data = strat.get_data()

        print ("Found authors for {0} years in \"{1}\":"\
                .format(len(self.author_data), self.filter_key))

        for year, g in sorted(self.author_data.items()):
            print("  {0}: {1: 3} authors".format(year, g.G.GetNodes()))
            # g.print_node_stats()

        self.export_graphs()

    def __make_dir(self, _path):
        _path = _path.format(safe_file_name(self.filter_key) + "_{0}")
        base_dir = os.path.dirname(_path)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        return _path

    def dump_graphs(self, year=-1, name="./dump/{0}.graph"):
        name = self.__make_dir(name)

        if year < 0:
            for year, g in self.author_data.items():
                g.dump(name)
        elif year in self.author_data:
            self.author_data[year].dump(name)

    def export_graphs(self, year=-1, name="./visualise/{0}.png"):
        name = self.__make_dir(name)

        if year < 0:
            for year, g in self.author_data.items():
                g.export(name)
        elif year in self.author_data:
            self.author_data[year].export(name)

    def plot_year(self, year, top_x=10):
        merged_graph = None
        years = ""
        info = ""

        if isinstance(year, tuple):
            for y in range(year[0], year[1]):
                if y in self.author_data:
                    if not merged_graph:
                        merged_graph = self.author_data[y]
                    else:
                        G = self.author_data[y]
                        for edge in G.Edges():
                            item1, item2 = map(G.get_author_from_id, (edge.GetSrcNId(), edge.GetDstNId()))
                            merged_graph.AddConnection(item1, item2)

            years = "{0}-{1}".format(year[0], year[1])

            info = "Plotting top {0} authors for years {1} ({2} authors)..."\
                        .format(top_x, years, merged_graph.G.GetNodes() if merged_graph else "?")
            print(info)
        else:
            merged_graph = self.author_data[year] if year in self.author_data else None
            years = str(year)

            info = "Plotting top {0} items for year {1} ({2} authors)..."\
                        .format(top_x, years, merged_graph.G.GetNodes() if merged_graph else "?")
            print(info)

        if not merged_graph:
            print("  No such year!")
            return

        outfile = self.__make_dir("./visualise/interval_{0}").format(years)

        with open(outfile + ".txt", "w") as ofile:
            ofile.write(info + "\n")
            merged_graph.print_node_stats(top_x=top_x, outfile=ofile)
        merged_graph.export(outfile + ".png", "Graph for period " + years)

    def plot_interval_years(self, year_from=0, year_to=3000, delta=5, offset=3, top_x=10):
        for year in range(year_from, year_to+1, offset):
            if year in self.author_data:
                last_year = min(year + delta, year_to+1)
                while last_year not in self.author_data:
                    last_year -= 1

                self.plot_year((year, last_year), top_x=top_x)


if __name__ == "__main__":
    data_path, pub_key = DATA, "conf/pods"

    argc = len(sys.argv)
    if argc != 3:
        print("No args given! Expected file path.")
        # sys.exit()
    else:
        _, data_path, pub_key = sys.argv

    g = GraphMiner(data_path, pub_key)
    g.prepare()
    g.plot_interval_years(year_from=1990)
    g.plot_year((2006, 2016))
