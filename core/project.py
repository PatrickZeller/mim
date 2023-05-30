import sqlite3
import os
import time
import re

from shutil import copytree, rmtree, copyfile

from core.settings import Settings
from core import lib


class Project:
    """This class holds all infos for a project

    Function
    """

    def init(self, name, config=None):
        """constructs the project class with the given arguments

        Parms:
            name (string): name of the project
            config (dict): dict of project settings. defaults to None
        """
        self.studio = Settings().studio
        self.db = os.path.join(self.studio, "projects.db")
        self.set_name(name)
        if config == None:
            config = Settings().studio
        self.set_config(config)

    def get_db(self):
        """Opens the database connection

        Returns: sqlite3 connection
        """
        self.prep_db()
        con = sqlite3.connect(self.db)
        return con

    def get_projects(self):
        """Gets all projects from the database

        Returns: list of all projects
        """
        con = self.get_db()
        cur = con.cursor()
        cur.execute("SELECT project_name FROM project")
        items = cur.fetchall()
        if items is not None:
            projects = [i[0] for i in items]
        else:
            projects = []
        return projects

    def prep_db(self):
        """Creates a Sqlite3 Database with desired table layout.

        Layout:
        status table
        project table
        type table
        action tabel
        """
        lib.prep_db(self.db)

    def find(self, pattern, filter={}):
        """Gets all projects from the database that match the patern

        Parms:
            pattern (string): pattern to search for
            filter (dict): filters the search // not implemented

        Returns: list of all matching projects
        """
        con = self.get_db()
        cur = con.cursor()
        cur.execute(
            "SELECT project_name FROM project WHERE project_name LIKE '%{pattern}%'".format(
                pattern
            )
        )
        items = cur.fetchall()
        if items is not None:
            projects = [i[0] for i in items]
        else:
            projects = []
        return projects

    def validate_name(self):
        """validates project name

        Returns:
            True if name is safe
            False if name is not safe
        """
        name = self.name
        safe = True
        if " " in name:
            safe = False
        if name in self.get_projects():
            safe = False
        return safe

    def set_name(self, name):
        """adds project name to project instance

        Parms:
            name (string): name of the project
        """
        self.name = name

    def set_config(self, config):
        """adds config information to the project

        Parms:
            config (dict): dict of all project config settings
        """
        self.config = config

    def set_image(self, image):
        """adds image to project instance

        Parms:
            image (string): path to thumbnail image
        """
        self.image = image

    def create(self):
        """creates project with spesified name

        Returns:
            True when project was created
            False if it failed to create the project
        """
        if self.validate_name():
            return True
        else:
            return False

    def activate(self):
        """activates current project"""
        pass

    def deactivate(self):
        """deactivates current project"""
        pass

    def revive(self):
        """revives current project"""
        pass

    def archive(self):
        """archives current project"""
        pass

    def get_data(self):
        self.find(self.name())
        pass

    @classmethod
    def from_path(cls, path):
        """loads a project from the path given
        this is used in the migrate function

        Parms:
            path (string): the path to the projects root location
        """
        name = os.path.basename(path)
        config_dir = os.path.join(path, ".config")
        config_file = os.path.join(config_dir, "config.json")
        if os.path.isfile(config_file):
            config = lib.get_json(config_file)
            return cls(name, config) # type: ignore
        else:
            return cls(name) # type: ignore
