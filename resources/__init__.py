import os

RESOURCES_DIR = os.path.dirname(os.path.abspath(__file__))


def get_resource(*args):
    """ Serves to simple resources access

    :param *args: should contain *subfolder* names and *filename* of
                  resource from resources folder
    :type *args: list
    """
    return os.path.normpath(os.path.join(RESOURCES_DIR, *args))


def get_liberation_font_path(bold=False, italic=False):
    font_name = "LiberationSans"
    suffix = ""
    if bold:
        suffix += "Bold"
    if italic:
        suffix += "Italic"

    if not suffix:
        suffix = "Regular"

    filename = "{}-{}.ttf".format(font_name, suffix)
    font_path = get_resource("fonts", font_name, filename)
    return font_path


def get_mim_icon_filepath():
    return get_resource("icons", "hub_icon.png")