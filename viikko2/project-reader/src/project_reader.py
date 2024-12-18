from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        config = toml.loads(content)
        mesta = config['tool']['poetry']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(mesta['name'], mesta['description'], mesta['license'], mesta['authors'], mesta['dependencies'], mesta['group']['dev']['dependencies'])
