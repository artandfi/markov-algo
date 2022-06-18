import re


class Rule:
    def __init__(self, rule: str):
        assert "->" in rule
        lhs, rhs = re.sub(r"\s+", "", rule).replace("_", "").split("->")

        self.final = rhs[0] == "."
        rhs = rhs[1:] if self.final else rhs
        
        self.lhs, self.rhs = lhs, rhs
    
    def __eq__(self, other):
        return (
            isinstance(other, Rule)
            and self.lhs == other.lhs
            and self.rhs == other.rhs
            and self.final == other.final
        )

    def __str__(self):
        return f"{self.lhs} -> {'.' if self.final else ''}{self.rhs}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__str__()}')"
