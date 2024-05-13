import os
import sys
import subprocess
import time


from core.project import Project
from core.settings import Settings
from core import lib


class Host:
    """creates a host object"""

    def init(self, name, version):
        """initializes host calss

        Parms:
            name (string): name of host
            version (string): version tag of host application
        """
        self.host_name = name
        self.version = version
        self.host = "{}_{}".format(self.host_name, self.version)
        self.tools = Settings().studio
        self.set_exec()

    def set_exec(self):
        pass

    def load_settings(self):
        """collects settings for given host application"""
        self.install_file = "some/path"
        self.root = "some/path"
        pass

    def set_version(self, version):
        """sets host version

        Parms:
            version (string): version tag of host application
        """
        self.version = version

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

    def zip_install(self):
        """zip file extraction"""
        lib.unzip_with_progress(self.install_file, self.root)
        pass

    def custom_install(self, args):
        """custom install function
        
        Parms:
            args (string): space seperated list of command line arguments for the installer
        """
        _args = [self.install_file]
        _args.append(args.split(" "))
        cmd = " ".join(_args)
        os.system(cmd)

    def get_workfile_extensions(self):
        return [".mim"]        

    def launch(self):
        """launches the host application"""
        pass

    def exists(self):
        """checkes if the host exists on the client

        Returns:
            True if host exists
            False if not
        """
        app_path = os.path.join(self.tools, self.host)
        return os.path.isdir(app_path)

    def get_icon(self):
        pass

    def environments(self):
        """sets the environments for the host"""
        pass

    def cli(self):
        """starts the host in headless mode"""
        pass
