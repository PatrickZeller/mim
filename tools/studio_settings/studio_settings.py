import os
import sys

from PySide2 import QtCore, QtWidgets, QtGui

from mim import style
from mim import core
from mim import resources

class StudioSettings(QtWidgets.QDialog):
    """Studio Settings interface"""

    def __init__(self, parent=None):
        super(StudioSettings, self).__init__(parent)
        self.setWindowTitle("Studio Settings")
        icon = QtGui.QIcon(resources.get_mim_icon_filepath())
        self.setWindowIcon(icon)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.resize(536, 422)
        
        # setup layout
        self.vl = QtWidgets.QVBoxLayout(self)
        self.vl.setObjectName("vl")
        self.add_menu("studio", "Studio", self.vl)
        self.add_menu("project", "Project", self.vl)
        self.add_menu("apps", "Applications", self.get_menu_layout("studio"))


    def get_menu_layout(self, name):
        """gets the vertical layout object of the menu
        
        Parms:
            name (string): name of the menu

        Returns:
            vl (QtWidgets.QVBoxLayout)
        """
        vl = self.findChild(QtWidgets.QVBoxLayout, "{}_vl".format(name))
        return vl

    def add_menu(self, name, label, root):
        """creats menu widgets for ui
        
        Parms:
            name (string): name of the object
            label (string): label of the menu
            root (QtWidgets.QLayout): object the menu should be added to
        """
        menu = QtWidgets.QCheckBox(label)
        menu.setObjectName(name)
        menu.setChecked(True)
        menu.stateChanged.connect(lambda: self.collapse_menu(name))
        groupbox = QtWidgets.QGroupBox()
        groupbox.setObjectName("{}_gb".format(name))
        groupbox.vl = QtWidgets.QVBoxLayout(groupbox)
        groupbox.vl.setObjectName("{}_vl".format(name))

        root.addWidget(menu)
        root.addWidget(groupbox)
    
    def collapse_menu(self, name):
        """collapeses menu item if open
        
        Parms:
            name (string): the name of the menu that should be collpsed
        """
        menu = self.findChild(QtWidgets.QCheckBox, name)
        groupbox = self.findChild(QtWidgets.QGroupBox, "{}_gb".format(name))
        if menu.checkState():
            groupbox.show()
        else:
            groupbox.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    launcher_instance = StudioSettings()
    launcher_instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()