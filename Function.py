class Function(object):
    def __init__(self, name, functions=None):
        if functions is None:
            functions = []
        self.name = name
        self.functions = functions

    def add_functions_names(self, function_name):
        self.functions.append(function_name)

    def __str__(self):
        return "Name: {} \nFunctions names: {}".format(self.name, self.functions)
