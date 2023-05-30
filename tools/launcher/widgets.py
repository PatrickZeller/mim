import os

from PySide2 import QtCore, QtWidgets, QtGui

import project_simple_ui
"""
class project_item(QtWidgets.QDialog):
    def __init__(self, project):
        super(project_item, self).__init__()
        ## dress the widget
        self.ui = project_simple_ui.Ui_Form()
        self.ui.setupUi(self)
        self.project = project
        self.prj_path = os.path.join(os.environ["PROJECTS"], self.project)
        self.ui.edit.hide()

        # connect functions
        self.ui.open.pressed.connect(self.prj_open)
        self.ui.info.pressed.connect(self.prj_info)
        self.ui.output.pressed.connect(self.prj_output)

        ## add user faceing info
        image_loc = os.path.join(
            os.environ["PROJECTS"], self.project, ".config", ".image.jpg"
        )
        if os.path.exists(image_loc):
            pixmap = QtGui.QPixmap(image_loc)
        else:
            pixmap = QtGui.QPixmap("resources/standin/prj.png")
        self.ui.image.setPixmap(pixmap)
        self.ui.name.setFont(QtGui.QFont("Nunito", 10))
        try:
            prj = studio.Project.from_name(project)
            status = prj.get()["status"]
            if status == "active":
                self.ui.status.setStyleSheet("QLabel{ color: rgb(233, 215, 0);}")
            elif status == "revived":
                self.ui.status.setStyleSheet("QLabel{ color: rgb(212, 212, 212);}")
            elif status == "inactive":
                self.ui.status.setStyleSheet("QLabel{ color: rgb(176, 28, 59);}")
        except:
            status = "archived"
        self.ui.status.setText(status)
        self.ui.name.setText(project)

    def prj_info(self):
        prj = studio.Project.from_name(self.project)
        prj.environment()
        message = "<br>".join([k + ": " + str(i) for k, i in prj.data.items()])
        info.make_info(message)

    def prj_output(self):
        prj = studio.Project.from_name(self.project)
        prj.environment()
        message = "<br>".join([k + ": " + str(i) for k, i in prj.data.items()])
        info.make_info(message, "output")

    def prj_open(self):
        command = "explorer " + '"' + self.prj_path.replace("/", "\\") + '"'
        Popen(command, close_fds=True, creationflags=CREATE_NEW_CONSOLE)

    def mouseMoveEvent(self, event):
        # drag=QtGui.QDrag(self)
        # MimeData=QtCore.QMimeData()
        # comps = ["file:///{}".format(self.prj_path.replace("/", "\\"))]
        # MimeData.setUrls(comps)
        # drag.setMimeData(MimeData)
        # drag.exec_(QtCore.Qt.CopyAction)
        pass

    def dragEnterEvent(self, event):
        # if event.mimeData().hasText():
        #     event.setDropAction(QtCore.Qt.CopyAction)
        #     event.accept()
        #     event.ignore()
        # else:
        #     event.ignore()
        event.ignore()

"""

class app_button(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(app_button, self).__init__(parent)