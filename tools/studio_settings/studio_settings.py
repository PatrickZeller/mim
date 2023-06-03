import os
import sys

from PySide2 import QtCore, QtWidgets, QtGui

from mim import style
from mim import core
from mim import resources

class pathWidget(QtWidgets.QWidget):
    """defines a path widget for settings"""
    def __init__(self, label, parent=None):
        super(pathWidget, self).__init__(parent)
        self.setObjectName(label)
        
        self.label = QtWidgets.QLabel(label)
        self.label.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))

        self.hl = QtWidgets.QHBoxLayout()
        self.hl.setContentsMargins(0,0,0,0)
        self.setLayout(self.hl)
        self.hl.addWidget(self.label)

        self.w = QtWidgets.QWidget()
        self.paths = QtWidgets.QVBoxLayout()
        self.paths.setContentsMargins(0,0,0,0)
        self.w.setLayout(self.paths)
        self.hl.addWidget(self.w)
        self.add_parm("Linux:")
        self.add_parm("Mac:")
        self.add_parm("Windows:")
        self.hl.addWidget(self.w)
    
    def add_parm(self, name):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        widget.setLayout(layout)
        label = QtWidgets.QLabel(name)
        label.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        label.setMinimumWidth(75)
        path = QtWidgets.QLineEdit()
        path.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        layout.addWidget(label)
        layout.addWidget(path)
        self.paths.addWidget(widget)
        pass

    

class StudioSettings(QtWidgets.QDialog):
    """Studio Settings interface"""

    def __init__(self, parent=None):
        super(StudioSettings, self).__init__(parent)
        self.setWindowTitle("Studio Settings")
        icon = QtGui.QIcon(resources.get_mim_icon_filepath())
        self.setWindowIcon(icon)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        self.resize(900, 1000)
        
        # setup layout
        self.base = QtWidgets.QVBoxLayout(self)
        self.base.setAlignment(QtCore.Qt.AlignRight)
        self.sa = QtWidgets.QScrollArea()
        self.sa.setWidgetResizable(True)
        self.sa.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.widget = QtWidgets.QWidget()
        self.vl = QtWidgets.QVBoxLayout()
        self.vl.setObjectName("vl")
        self.vl.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vl.setAlignment(QtCore.Qt.AlignTop)
        self.widget.setLayout(self.vl)
        self.sa.setWidget(self.widget)
        self.base.addWidget(self.sa)

        # setup default menus
        self.add_menu("studio", "Studio", self.vl)
        self.add_menu("project", "Project", self.vl)

        self.add_menu("general", "General", self.get_menu_layout("studio"))
        # add applications menu to studio
        self.add_menu("apps", "Applications", self.get_menu_layout("studio"))
        apps = self.get_menu_layout("apps")
        self.app_add_btn = QtWidgets.QPushButton("Add App")
        apps.addWidget(self.app_add_btn)
        self.app_add_btn.clicked.connect(self.add_new_app)
        self.app_add_btn.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))


        self.add_menu("plugins", "Plugins", self.get_menu_layout("studio"))
        
        self.add_menu("prj_apps", "Applications", self.get_menu_layout("project"))
        self.add_menu("prj_plugins", "Plugins", self.get_menu_layout("project"))
        self.add_menu("prj_general", "General", self.get_menu_layout("project"))

        # add save button
        self.save = QtWidgets.QPushButton("Save")
        self.base.addWidget(self.save)

    def add_new_app(self):
        """add new application to menu"""
        apps = self.get_menu_layout("apps")
        index = apps.count()
        names = []
        for i in range(index):
            w = apps.itemAt(i).widget()
            if isinstance(w, QtWidgets.QCheckBox):
                names.append(w.objectName())
        counter = 1
        name = "app%d"%(counter)
        while name in names:
            name = "app%d"%(counter)
            counter += 1
        self.add_menu(name, name.capitalize(), apps)
        new_app_layout = self.get_menu_layout(name)
        new_app_layout.addWidget(self.add_parm("Icon"))
        new_app_layout.addWidget(self.add_multiline_parm("Environment"))

        #add version button
        version_add_btn = QtWidgets.QPushButton("Add Version")
        version_add_btn.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        version_add_btn.clicked.connect(lambda: self.add_new_version(new_app_layout))
        new_app_layout.addWidget(version_add_btn)

    def add_new_version(self, root):
        """adds version menu to app"""
        index = root.count()
        o_n = root.objectName().split("_")[0]
        names = []
        for i in range(index):
            w = root.itemAt(i).widget()
            if isinstance(w, QtWidgets.QCheckBox):
                names.append(w.objectName())
        counter = 1
        name = "%s_version%d"%(o_n, counter)
        while name in names:
            name = "%s_version%d"%(o_n, counter)
            counter += 1        
        self.add_menu(name, name.replace(o_n + "_", "").capitalize(), root)
        new_version_layout = self.get_menu_layout(name)
        new_version_layout.addWidget(pathWidget("Executeable"))
        new_version_layout.addWidget(self.create_seperator())
        new_version_layout.addWidget(self.add_parm("Args"))
        new_version_layout.addWidget(self.create_seperator())
        new_version_layout.addWidget(pathWidget("Install_Args"))
        new_version_layout.addWidget(self.create_seperator())
        new_version_layout.addWidget(pathWidget("Install"))
        new_version_layout.addWidget(self.create_seperator())
        new_version_layout.addWidget(self.add_multiline_parm("Environment"))

    def create_seperator(self):
        separator = QtWidgets.QFrame()
        separator.Shape(QtWidgets.QFrame.HLine)
        separator.setSizePolicy(QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.Expanding)
        separator.setLineWidth(3)
        return separator


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
        menu.setFont(QtGui.QFont("Nunito ExtraLight", 9, QtGui.QFont.Bold))
        menu.stateChanged.connect(lambda: self.collapse_menu(name))
        menu.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        menu.setMinimumHeight(28)
        menu.setMaximumHeight(28)
        groupbox = QtWidgets.QGroupBox()
        groupbox.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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

    def add_parm(self, name):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        widget.setLayout(layout)
        label = QtWidgets.QLabel(name)
        label.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        label.setMinimumWidth(85)
        path = QtWidgets.QLineEdit()
        path.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        layout.addWidget(label)
        layout.addWidget(path)
        return widget
    
    def add_multiline_parm(self, name):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        widget.setLayout(layout)
        label = QtWidgets.QLabel(name)
        label.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        label.setMinimumWidth(85)
        env = QtWidgets.QTextEdit()
        env.setText("""{}""")
        env.setMaximumHeight(100)
        env.setFont(QtGui.QFont("Nunito ExtraLight", 8, QtGui.QFont.Normal))
        layout.addWidget(label)
        layout.addWidget(env)
        return widget


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    launcher_instance = StudioSettings()
    launcher_instance.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()