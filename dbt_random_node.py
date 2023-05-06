import pprint


class RandomNode:
    def __init__(self, manifest, config):
        self.manifest = manifest
        self.config = config

    def ls(self):
        return pprint.pformat(self.manifest) + pprint.pformat(self.config)

    def run(self):
        return self.ls()
