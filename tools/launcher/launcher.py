import os
import sys

from PySide2 import QtCore, QtWidgets, QtGui

# from widgets import project_item

from . import launcher_ui
from mim import style
from mim import core
from mim import resources
import mim.version


class Launcher(QtWidgets.QDialog):
    """Launcher interface"""

    def __init__(self, parent=None):
        super(Launcher, self).__init__(parent)

        self.ui = launcher_ui.Ui_launcher()
        self.ui.setupUi(self)
        # self.setStyleSheet(style.get_main_style())
        self.setWindowTitle("Launcher")
        icon = QtGui.QIcon(resources.get_mim_icon_filepath())
        self.setWindowIcon(icon)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)

        # Allow minimize
        self.setWindowFlags(
            QtCore.Qt.Window
            | QtCore.Qt.CustomizeWindowHint
            | QtCore.Qt.WindowTitleHint
            | QtCore.Qt.WindowMinimizeButtonHint
            | QtCore.Qt.WindowCloseButtonHint
        )
        self.setFocus()

    def update_toolbox(self):
        pass

    def set_project(self):
        pass

    def search(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    launcher_instance = Launcher()
    launcher_instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
