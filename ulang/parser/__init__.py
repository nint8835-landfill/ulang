from importlib.resources import read_text

from lark import Lark, Tree

PARSER = Lark(read_text("ulang.parser", "ulang.lark"))


def parse(source: str) -> Tree:
    return PARSER.parse(source)
