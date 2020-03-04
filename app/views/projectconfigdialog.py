import sys
sys.path.append("../..")
from managers.eventconfigmanager import EventConfigManager

from .dirconfigwidget import DirConfigWidget
from .teamconfigwidget import TeamConfigWidget
from .eventconfigwidget import EventConfigWidget
from .vectorconfigwidget import VectorConfigWidget

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

class ProjectConfigDialog(QDialog): 
    def __init__(self, parent):
        super(ProjectConfigDialog, self).__init__(parent)
        self.eventConfigManager = EventConfigManager()
        self.initUI()

    def initUI(self): 
        self.resize(850,600)
        self.teamConfig = TeamConfigWidget(parent=self, eventManager=self.eventConfigManager)
        self.dirConfig = DirConfigWidget(parent=self, eventManager=self.eventConfigManager)
        self.eventConfig = EventConfigWidget(parent=self, eventManager=self.eventConfigManager)
        self.vectorConfig = VectorConfigWidget(parent=self, eventManager=self.eventConfigManager)
        
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamConfig)
        self.stack.addWidget(self.dirConfig)
        self.stack.addWidget(self.eventConfig)
        self.stack.addWidget(self.vectorConfig)

        self.viewList = QListWidget()
        self.viewList.insertItem(0, "Team Configuration")
        self.viewList.insertItem(1, "Directory Configuration")
        self.viewList.insertItem(2, "Event Configuration")
        self.viewList.insertItem(3, "Vector Configuration")
        self.viewList.currentRowChanged.connect(lambda i : self.stack.setCurrentIndex(i))

        self.startNewProject = QPushButton("Start New Project")
        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)

        newProjectControlContainer = QHBoxLayout()
        newProjectControlContainer.addItem(hSpacer)
        newProjectControlContainer.addWidget(self.startNewProject)

        viewContainer = QHBoxLayout()
        viewContainer.addWidget(self.viewList, 30)
        viewContainer.addWidget(self.stack, 60)

        mainContainer = QVBoxLayout(self)
        mainContainer.addLayout(viewContainer)
        mainContainer.addLayout(newProjectControlContainer)

        self.setLayout(mainContainer)
        self.exec_()

