import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string: str):
    nodes = parse_nodes(i_s)

    if not nodes:
        if input_string=='(;)': return SgfTree()
        else: raise ValueError("Invalid input")
    parent = nodes.pop(0)

    main_pattern = re.compile(r'(?P<key>[A-Z]+)(?P<values>(\[\w+\])+)+')
    
    p_match = [m.group('key') for m in main_pattern.finditer(parent)]
    v_match = [m.group('values') for m in main_pattern.finditer(parent)]

    props = {p:parse_values(v) for (p,v) in zip(p_match,v_match)}
    childs = [SgfTree(properties={m.group('key'):parse_values(m.group('values')) for m in main_pattern.finditer(node)}) for node in nodes]

    return SgfTree(properties=props,children=childs)

def parse_nodes(sgf_string: str):
    return [m.group(0) for m in re.finditer(r'([A-Z]+(\[\w\])+)+',sgf_string)]

def parse_values(values):
    return [v.group(0) for v in re.finditer(r'\w+',values)]