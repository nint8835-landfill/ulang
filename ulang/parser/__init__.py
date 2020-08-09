from importlib.resources import read_text

from lark import Lark, Tree

from .transformer import LanguageTransformer

PARSER = Lark(read_text("ulang.parser", "ulang.lark"))


def parse(source: str) -> Tree:
    return LanguageTransformer().transform(PARSER.parse(source))
