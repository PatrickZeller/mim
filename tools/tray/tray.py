import os
import sys
import subprocess

from PySide2 import QtWidgets, QtGui, QtCore

from mim import resources
from mim.resources import icons
import mim.version
from mim import style
from tools.launcher import launcher
from tools.studio_settings import studio_settings

class mim_tray(QtWidgets.QSystemTrayIcon):
    """
    CREATE A SYSTEM TRAY ICON CLASS AND ADD MENU
    """
    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        self.setToolTip("MIM VFX Pipeline tools \nVersion: {}".format(mim.version.__version__))
        self.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # menu start
        menu = QtWidgets.QMenu(parent)

        # add launcher
        open_app = menu.addAction("Launcher")
        open_app.triggered.connect(self.open_launcher)
        # open_app.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # add browser
        open_browser = menu.addAction("Browser")
        open_browser.triggered.connect(self.open_browser)
        # open_browser.setVisible(False)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # add publisher
        open_publisher = menu.addAction("Publisher")
        open_publisher.triggered.connect(self.open_publisher)
        # open_publisher.setVisible(False)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # add deliver
        open_deliver = menu.addAction("Deliver Tool")
        open_deliver.triggered.connect(self.open_deliver)
        # open_publisher.setVisible(False)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        menu.addSeparator()

        # add settings
        open_settings = menu.addAction("Settings")
        open_settings.triggered.connect(self.open_settings)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # add manager
        open_manager = menu.addAction("Manager")
        open_manager.triggered.connect(self.open_manager)
        # open_manager.setVisible(False)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        # add studio
        open_studio = menu.addAction("Studio Settings")
        open_studio.triggered.connect(self.open_studio)
        # open_studio.setVisible(False)
        # open_cal.setIcon(QtGui.QIcon(resources.get_mim_icon_filepath()))

        menu.addSeparator()

        # add exit button
        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())

        menu.addSeparator()
        self.menu = menu
        self.setContextMenu(menu)
        self.activated.connect(self.onTrayIconActivated)


    def onTrayIconActivated(self, reason):
        """
        This function will trigger function on click or double click
        Parms:
            reason: Qt thing do not know
        """
        if reason == self.DoubleClick:
            self.open_launcher()
        if reason == self.Trigger:
            current_mouse_cursor = QtGui.QCursor.pos()
            offset = QtCore.QPoint(0, self.menu.sizeHint().height())
            self.menu.move(current_mouse_cursor - offset)
            self.menu.show()

    def open_launcher(self):
        """
        this function will open launcher
        """
        self.launcher_instance = launcher.Launcher()
        self.launcher_instance.show()

    def open_settings(self):
        """
        this function will open settings
        """
        os.system('calc')

    def open_browser(self):
        """
        this function will open browser
        """
        self.launcher_instance = launcher.Launcher()
        self.launcher_instance.show()

    def open_publisher(self):
        """
        this function will open publisher
        """
        self.launcher_instance = launcher.Launcher()
        self.launcher_instance.show()

    def open_deliver(self):
        """
        this function will open deliver tool
        """
        self.launcher_instance = launcher.Launcher()
        self.launcher_instance.show()

    def open_manager(self):
        """
        this function will open manager
        """
        self.launcher_instance = launcher.Launcher()
        self.launcher_instance.show()

    def open_studio(self):
        """
        this function will open studio settings
        """
        self.studio_settings_instance = studio_settings.StudioSettings()
        self.studio_settings_instance.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style.get_main_style())
    app.setStyle("Fusion")
    app.setFont(QtGui.QFont("Nunito ExtraLight", 11, QtGui.QFont.Bold))
    app.setQuitOnLastWindowClosed(False)
    tray_icon = mim_tray()
    tray_icon.show()
    tray_icon.showMessage('MIM', 'Tray is now available')
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()