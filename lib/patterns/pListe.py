#!/usr/bin/python

class PListe(list):

    # Pour chaque entree ds arguments_attribut['name'], 
    # on cree un class_pattern determine par le pattern_matching
    def __init__(self, arguments_attribut, name_pattern):
        for i in arguments_attribut['name']:
            self.append(self.init_class_pattern(i, name_pattern, arguments_attribut))

    def init_class_pattern(self, name, name_pattern, arguments_attribut):
        arguments_attribut['name'] = name
        import_pattern = __import__('p' + name_pattern)
        class_pattern = getattr(import_pattern, 'P' + name_pattern)
        return class_pattern(arguments_attribut)
