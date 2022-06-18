from typing import Iterable
from rule import Rule


class MarkovAlgorithm:
    def __init__(self, rules: Iterable[Rule]):
        assert len(rules) > 0
        self.rules = rules
    
    def __str__(self):
        return "\n".join(f"{i+1}. {rule}" for i, rule in enumerate(self.rules))
    
    def run(self, user_input):
        running = True
        while running:
            matches = (rule for rule in self.rules if rule.lhs in user_input)
            
            try:
                rule = next(matches)
                replaced = user_input.replace(rule.lhs, rule.rhs, 1)
                running = not rule.final

                print(f"Rule {self.rules.index(rule)+1}: {user_input} -> {replaced}")
                user_input = replaced
            except StopIteration:
                running = False
        
        return user_input
