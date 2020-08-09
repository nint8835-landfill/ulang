from typing import List


class Expression:
    def evaluate(self):
        raise NotImplementedError()


class LiteralExpression(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class FunctionExpression(Expression):
    def __init__(self, name: str, parameters: List[str], children: List[Expression]):
        self.name = name
        self.parameters = parameters
        self.children = children

    def evaluate(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"""Function {self.name}
    Parameters: {self.parameters}
    Body: {self.children}"""


class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def evaluate(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"Variable {self.name}"

    __repr__ = __str__
