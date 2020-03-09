import sys
sys.path.append("../..")

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QListWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy

from managers.eventconfigmanager import EventConfigManager

from app.widgets.dirconfigwidget import DirConfigWidget
from app.widgets.teamconfigwidget import TeamConfigWidget
from app.widgets.eventconfigwidget import EventConfigWidget
from app.widgets.vectorconfigwidget import VectorConfigWidget

class ProjectConfigDialog(QDialog): 
    def __init__(self, parent):
        super(ProjectConfigDialog, self).__init__(parent)
        self.eventConfigManager = EventConfigManager.get_instance()
        self.parent = parent
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
        self.startNewProject.clicked.connect(self.start)
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
        self.show()

    def start(self):
        # TODO: Verify that all configuration is correctly setup
        self.parent.updateView(2)
        self.done(0)

