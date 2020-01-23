import Function


class File(object):
    def __init__(self, name, size, dependencies=None, functions=None):
        if dependencies is None:
            dependencies = []
        if functions is None:
            functions = []
        self.name = name
        self.size = size
        self.dependencies = dependencies
        self.functions = functions

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def add_functions(self, function):
        self.functions.append(function)

    def __str__(self):
        return "file name: {} \nsize: {} \ndependencies: {}\n".format(self.name, self.size, self.dependencies)

