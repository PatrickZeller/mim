import os
import json
import sqlite3
from zipfile import ZipFile


def unzip_with_progress(src, dst):
    """unzips zipfile with progess printed

    Parms:
        src (string): path to zip file
        dst (string): path to extract to

    Returns:
        True if successfull
        False if unzip was not possible
    """
    if os.path.splitext(src)[1] == "zip":
        zf = ZipFile(src)
        uncompress_size = sum((file.file_size for file in zf.infolist()))
        extracted_size = 0
        prog = 0
        for file in zf.infolist():
            extracted_size += file.file_size
            progress = extracted_size * 100 / uncompress_size
            if prog != round(progress):
                print("{}%".format(round(progress)))
            prog = round(progress)
            zf.extract(file, dst)
        return True
    else:
        return False


def write_json(file, data):
    """writes json file with provided data
    
    Parms:
        file (string): file location for the output
        data (dict): your data
    """
    with open(file, "w") as w_data:
        json.dump(data, w_data, indent=2)
    

def get_json(file):
    """gets data from json file

    Parms:
        file (string): path to json file

    Returns:
        data (dict): data read from the json file
    """
    data = {}
    if os.path.isfile(file):
        with open(file) as content:
            data.update(json.load(content))
        return data
    else:
        return {}


def make_folder(path):
    """Creates folder for directory if not presant

    Parms:
        path (string): Directory or Location you want to create

    Returns:
        True if dir was created
        False if dir allready exists
    """
    if not os.path.isdir(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
        return True
    else:
        return False


def prep_db(location):
    """Creates a Sqlite3 Database with desired table layout.

    Layout:
    status table
    project table
    type table
    action tabel

    Parms:
        location (string): location of the database file
    """
    db = location
    make_folder(db)

    if not os.path.isfile(db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        # initialize db

        # create team table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS team (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        team_name TEXT,
                        icon TEXT
                        )"""
        )

        # create team table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS team (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        team_name TEXT,
                        icon TEXT
                        )"""
        )

        # create recent_project_list table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS recent_project_list (
                        id INTEGER PRIMARY KEY AUTOINCREMENT
                        )"""
        )

        # create recent_projects table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS recent_projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        list_id INTEGER,
                        project_id INTEGER,
                        FOREIGN KEY (list_id) REFERENCES recent_project_list(id),
                        FOREIGN KEY (project_id) REFERENCES projects(id)
                        )"""
        )

        # create users table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        image BLOB,
                        settings TEXT,
                        tag TEXT,
                        birthday REAL,
                        status INTEGER,
                        recent_projects INTEGER,
                        team INTEGER,
                        _meta_ BLOB,
                        FOREIGN KEY (status) REFERENCES user_status(id),
                        FOREIGN KEY (recent_projects) REFERENCES recent_project_list(id),
                        FOREIGN KEY (team) REFERENCES team(id)
                        )"""
        )

        # create user_status table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS user_status (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        status_type TEXT,
                        icon TEXT
                        )"""
        )

        # create setting_type table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS setting_type (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        type TEXT
                        )"""
        )

        # create setting table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS setting (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        setting_name TEXT,
                        _meta_ BLOB
                        )"""
        )
        # create setting_values table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS setting_values (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        setting_name TEXT,
                        setting_label TEXT,
                        setting INTEGER,
                        setting_value TEXT,
                        setting_type INTEGER,
                        _meta_ BLOB,
                        FOREIGN KEY (setting) REFERENCES setting(id),
                        FOREIGN KEY (setting_type) REFERENCES setting(id)
                        )"""
        )
        # create plugins table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS plugins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        plugin_name TEXT,
                        plugin_label TEXT,
                        plugin_icon TEXT,
                        plugin_env TEXT
                        )"""
        )
        # create plugin_versions table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS plugin_versions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        version_name TEXT,
                        version_label TEXT,
                        plugin INTEGER,
                        hosts INTEGER,
                        version_exec TEXT,
                        version_install TEXT,
                        version_args TEXT,
                        version_env TEXT,
                        _meta_ BLOB,
                        FOREIGN KEY (plugin) REFERENCES plugins(id),
                        FOREIGN KEY (hosts) REFERENCES host_list(id)
                        )"""
        )
        # create host_list table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS host_list (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        host_list_name TEXT
                        )"""
        )
        # create plugin_host table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS plugin_host (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        host_list_id INTEGER,
                        host_id INTEGER,
                        FOREIGN KEY (host_list_id) REFERENCES host_list(id),
                        FOREIGN KEY (host_id) REFERENCES app_version(id)
                        )"""
        )
        # create app_versions table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS app_versions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        version_name TEXT,
                        version_label TEXT,
                        app INTEGER,
                        version_exec TEXT,
                        version_args TEXT,
                        version_install TEXT,
                        version_install_args TEXT,
                        version_env TEXT,
                        _meta_ BLOB,
                        FOREIGN KEY (app) REFERENCES applications(id)
                        )"""
        )
        # create applications table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS applications (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        app_name TEXT,
                        app_label TEXT,
                        app_icon TEXT,
                        app_env TEXT
                        )"""
        )
        # create config table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS config (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        config_name TEXT,
                        _meta_ BLOB
                        )"""
        )
        # create config_settings table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS config_settings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        config_id INTEGER,
                        app_id INTEGER,
                        plugin_id INTEGER,
                        setting_id INTEGER,
                        FOREIGN KEY (config_id) REFERENCES config(id),
                        FOREIGN KEY (app_id) REFERENCES app_version(id),
                        FOREIGN KEY (plugin_id) REFERENCES plugin_version(id),
                        FOREIGN KEY (setting_id) REFERENCES setting_values(id)
                        )"""
        )
        # create project_status table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS project_status (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        status_type TEXT,
                        icon TEXT
                        )"""
        )

        # create projects table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS projects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        project_name TEXT,
                        image BLOB,
                        _meta_ BLOB,
                        status_id INTEGER,
                        config_id INTEGER,
                        FOREIGN KEY (status_id) REFERENCES project_status(id),
                        FOREIGN KEY (config_id) REFERENCES config(id)
                        )"""
        )

        # create type table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS type(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        action_type TEXT
                        )"""
        )

        # create action table
        cur.execute(
            """CREATE TABLE IF NOT EXISTS action (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        info INTEGER,
                        date REAL,
                        project_id INTEGER,
                        type_id INTEGER,
                        _meta_ BLOB,
                        FOREIGN KEY (project_id) REFERENCES projects(id),
                        FOREIGN KEY (type_id) REFERENCES type(id)
                        )"""
        )

        con.commit()
        con.close()

class mim_path:
    """simple thing that gives you paths for all os's"""

    def init(self):
        self.mac = None
        self.windows = None
        self.linux = None

    def set_windows(self, path):
        """sets the path for windows
        
        Parms:
            path (string): path for windows
        """
        self.windows = path

    def set_mac(self, path):
        """sets the path for mac
        
        Parms:
            path (string): path for mac
        """
        self.mac = path

    def set_linux(self, path):
        """sets the path for linux
        
        Parms:
            path (string): path for linux
        """
        self.mac = path

    def set_all(self, data):
        """sets all paths in one go
        
        Parms:
            data (dict): {Linux:"", Darwin:"", Windows:""}
        """
        self.set_linux(data["Linux"])
        self.set_mac(data["Darwin"])
        self.set_windows(data["Windows"])

    def get_all(self):
        """returns all paths in a dict to be used for other things
        
        Returns:
            paths (dict): {Linux:"", Darwin:"", Windows:""}
        """
        paths = {"Linux": self.linux, "Darwin": self.mac, "Windows": self.windows}
        return paths