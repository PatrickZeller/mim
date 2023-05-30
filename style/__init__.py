import os
from PySide2 import QtCore, QtGui

STYLE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_style(*args):
    """ Serves to simple resources access

    :param *args: should contain *subfolder* names and *filename* of
                  resource from resources folder
    :type *args: list
    """
    return os.path.normpath(os.path.join(STYLE_DIR, *args))
        
def get_main_style():
    """loads css file for mim style
    
    Returns:
        string utf-8 of the css file
    """
    rc = QtCore.QFile(get_style("main.css"))
    rc.open(QtCore.QFile.ReadOnly)
    content = rc.readAll().data()
    load_font()
    return str(content, "utf-8")


def load_font():
    """Load and register fonts into Qt application."""
    fonts_dirpath = os.path.join(STYLE_DIR, "fonts")
    font_dirs = []
    font_dirs.append(os.path.join(fonts_dirpath))
    for font_dir in font_dirs:
        for filename in os.listdir(font_dir):
            if os.path.splitext(filename)[1] not in [".ttf"]:
                continue
            full_path = os.path.join(font_dir, filename)
            font_id = QtGui.QFontDatabase.addApplicationFont(full_path)
            QtGui.QFontDatabase.applicationFontFamilies(
                font_id
            )
