import abc

class ResourceNameExistsException(Exception):
    pass


class BaseResource(abc.ABC):
    def __init__(self,name):
        self.name = name;
