from dataConnections.resources.base import ResourceNameExistsException


class ConnectionHandler:
    def __init__(self):
        self.resources = dict()

    def add_resource(self, resource):
        if self.resources.get(resource.name):
            raise ResourceNameExistsException()

        self.resources[resource.name] = resource
        self.__dict__.update({resource.name: resource})

    def __getitem__(self, key):
        return self.resources[key]