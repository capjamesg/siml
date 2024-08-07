from lark import Discard, Lark, Token, Transformer
from lark import Tree, Token
from lark.exceptions import UnexpectedCharacters, UnexpectedToken
from lark.visitors import Interpreter

grammar = """
entries: entry+

entry: term ", " page (see_also)? (subentry)*

term: string
page: NUMBER | NUMBER "-" NUMBER
see_also: "See also: " term
subentry: INDENT term ", " page EOL

string: /[a-zA-Z0-9' ]+/
NEW_LINE: "\\n"
INDENT: "\\t" | "    "
DOT: "."
NUMBER: /[0-9]+/(".")?
EOL: "\\n"
%import common.WS

%ignore NEW_LINE
%ignore INDENT
%ignore WS
"""

def token_to_string(tree):
    if isinstance(tree, Tree):
        return token_to_string(tree.children[0])

    return tree.value


def token_to_number(token):
    if len(token.children) == 1:
        return {"start": token.children[0], "end": token.children[0]}
    else:
        return {"start": token.children[0], "end": token.children[1]}


class SpaceTransformer(Transformer):
    def WS(self, tok: Token):
        return Discard

    def NEW_LINE(self, tok: Token):
        return Discard

    def INDENT(self, tok: Token):
        return Discard

    def NUMBER(self, tok: Token):
        if tok.value.endswith("."):
            return int(tok.value[:-1])

        return int(tok.value)


class ConstructIndex(Interpreter):
    def __init__(self):
        self.index = {}

    def __call__(self, tree):
        self.visit(tree)
        return self.index

    def string(self, token):
        return token_to_string(token)

    def visit(self, item):
        if not isinstance(item, Tree):
            return item
        
        # added here to be explicit that the item is a tree
        tree = item

        for child in tree.children:
            self.visit(child)

        if tree.data == "string":
            return self.string(tree.children[0])

        if tree.data == "entry":
            term = token_to_string(tree.children[0])
            page = token_to_number(tree.children[1])

            if term not in self.index:
                self.index[term] = {}

            if len(tree.children) > 2:
                see_also = token_to_string(tree.children[2])
                self.index[term]["see also"] = see_also

            if len(tree.children) > 3:
                subentries = {}
                for subentry in tree.children[3:]:
                    subentry = self.visit(subentry)
                    subentries[subentry["term"]] = subentry["page"]

                self.index[term]["page"] = page
                self.index[term]["subentries"] = subentries
            else:
                self.index[term]["page"] = page

        elif tree.data == "subentry":
            term = token_to_string(tree.children[0])
            page = token_to_number(tree.children[1])
            return {"term": term, "page": page}


def evaluate(text):
    try:
        parsed = Lark(grammar, start="entries").parse(text)
    except (UnexpectedCharacters, UnexpectedToken) as e:
        print(e)
        return

    try:
        parsed = SpaceTransformer().transform(parsed)
    except Exception as e:
        print("There was an error cleaning the data types in the index.")
        print(e)
        return

    try:
        evaluated = ConstructIndex()(parsed)
    except Exception as e:
        print("There was an error constructing the index.")
        print(e)
        return

    return evaluated

def read_file(file_name):
    with open(file_name) as f:
        text = f.read().strip()

    return text