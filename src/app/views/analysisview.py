import sys
sys.path.append("../..")
from managers.vectormanager import VectorManager

from app.views.graph.graphgenerator import GraphGenerator

from PyQt5.QtWidgets import QWidget, QDialog,QFrame, QGridLayout, QHBoxLayout, QVBoxLayout, QTableView,\
                            QTableWidget, QTabWidget, QListWidget, QListWidgetItem, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QAction

class AnalysisView(QWidget): 
    def __init__(self, parent=None): 
        super(QWidget, self).__init__(parent)
        self.vectorManager = VectorManager.get_instance()
        self.graphGenerator = GraphGenerator.get_instance()
        self.initUI()

    def initUI(self): 
        self.setupMainLayout()
        self.setLayout(self.mainLayout)

    def setupMainLayout(self): 
        #Log Entries table
        self.logEntriesTbl = QTableView()
        self.setupVectorTab()

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.logEntriesTbl, "Log Entries")
        self.tabWidget.addTab(self.vectorTab, "Vector View")

        # Defined Vectors list
        self.vectorWidget = QListWidget()

        self.workspace = QHBoxLayout()
        self.workspace.addWidget(self.vectorWidget, 10)
        self.workspace.addWidget(self.tabWidget,90)

        # Filtering and search
        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.search = QLineEdit()
        self.search.setFixedWidth(250)
        self.filterBox = QComboBox()

        # Container for tab/table controls 
        self.controls = QHBoxLayout()
        self.controls.addItem(hSpacer)
        self.controls.addWidget(self.search)
        self.controls.addWidget(self.filterBox)

        # Container for all workspace
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.controls)
        self.mainLayout.addLayout(self.workspace)

    def setupVectorTab(self): 
        self.graph = QWidget()
        self.graph.setLayout(QVBoxLayout())
        self.setupGraph()
        self.nodes = QTableView()

        self.vectorViews = QHBoxLayout()
        self.vectorViews.addWidget(self.nodes, 30)
        self.vectorViews.addWidget(self.graph, 70)

        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.orientationCb = QComboBox()
        self.unitsCb = QComboBox()
        self.interval = QLineEdit()

        # Graph controls such as orientation, interval units, interval
        self.graphContols = QHBoxLayout()
        self.graphContols.addItem(hSpacer)
        self.graphContols.addWidget(self.orientationCb)
        self.graphContols.addWidget(self.unitsCb)
        self.graphContols.addWidget(self.interval)

        self.container = QVBoxLayout()
        self.container.addLayout(self.graphContols)
        self.container.addLayout(self.vectorViews)

        self.vectorTab = QWidget()
        self.vectorTab.setLayout(self.container)

    def setupGraph(self): 
        graph = self.graph
        if len(self.vectors.get_vectors()) != 0: 
            self.graphGenerator.createGraphForVector()
        self.graphGenerator.build()
        qgv = self.graphGenerator.getGraph()
        graph.layout().addWidget(qgv)

    def nodeInvoked(self, node):
        d = QDialog(self)
        d.show()

    # TODO: Figure out why this breaks and does not update the list view. 
    def updateVectorList(self):
        vectors = self.vectorManager.get_vectors()
        for vector in vectors: 
            item = QListWidgetItem(vector.getName())
            self.vectorWidget.addItem(item)
    