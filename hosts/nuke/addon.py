import os
from mim.core import host

NUKE_HOST_DIR = os.path.dirname(os.path.abspath(__file__))


class NukeHost(host):
    """ nuke host application class """

    def environments(self):
        """sets up environments for nuke"""
        plugins = self.settings["plugins"]
        
        plugin_paths = [
            os.path.join(os.environ["TOOLS"], "plugins", i) for i in plugins if "NeatVideo" in i
        ]
        ofx = ";".join(plugin_paths)
        os.environ["OFX_PLUGIN_PATH"] = ofx
        os.environ['NUKE_TEMP_DIR'] = os.path.join(os.environ['TEMP'], self.name)
        os.environ["NUKE_PATH"] = os.path.join(
            os.environ["CONFIG"], self.name, self.version[:-4]
        )

    def get_workfile_extensions(self):
        """returns list of strings with the possible file extentions of this host 
        
        Returns:
            list
        """
        return [".nk"]
    
    def set_exec(self):
        self.executable = "Nuke" + self.version[:4] + ".exe"
        pass

    def install(self):
        """installs host on system"""

        if os.path.splitext(self.install_file)[1] == "zip":
            self.zip_install()
        else:
            self.custom_install()

        start = time.time()
        finished = str(round(time.time() - start))
        print("install time %s seconds" % finished)
        print("%s is installed" % self.host)
        pass
