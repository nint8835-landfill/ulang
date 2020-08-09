from typing import List, Tuple, Union, cast

from lark import Token, Transformer

from .expression import (
    Expression,
    FunctionExpression,
    LiteralExpression,
    VariableExpression,
)


class LanguageTransformer(Transformer):
    def literal(self, item: Union[List[Token], Token]) -> LiteralExpression:
        if isinstance(item, list):
            item = item[0]
        if item.type == "SIGNED_NUMBER":
            return LiteralExpression(int(item.value))
        else:
            return LiteralExpression(item.value)

    def parameter_list(self, items: List[Token]) -> List[str]:
        return [token.value for token in items]

    def identifier(self, items: Tuple[Token]) -> VariableExpression:
        return VariableExpression(items[0].value)

    def function(
        self, items: List[Union[Token, List[str], Expression]]
    ) -> FunctionExpression:
        name, parameters, *children = items
        name = cast(Token, name)
        parameters = cast(List[str], parameters)
        return FunctionExpression(name.value, parameters, children)  # type: ignore  # No matter what I do, I can't manage to make mypy cast children to List[Expression] successfully # noqa
