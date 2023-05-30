import os
import sqlite3
import os
import sys
from core import lib
from mim import PACKAGE_DIR

# lib.prep_db("C:/Users/patri/Documents/test_studio/studio.db")

class Settings:
    """This thing creates the settings for mim"""

    def init(self):
        self.config = os.path.join(PACKAGE_DIR, "config.json")
        self.studio = self.get_studio()

    def get_studio(self):
        """returns the studio config location"""
        self.data = lib.get_json(self.config) # get json file data from application location
        if "NOT_SET" in self.data.keys():
            self.not_set = True
            studio_location = ""
        else:
            self.not_set = False
            studio_location = self.data["STUDIO"][sys.platform] # Linux = Linux, Mac = Darwin, Windows = Windows
        return studio_location
    
    def set_studio_location(self, studio_paths):
        """sets studio location path
        
        Parms:
            studio_location (dict): {Linux:"", Darwin:"", Windows:""}
        """
        lib.write_json(self.config, studio_paths)
        self.get_studio() # updates the class with the new values
