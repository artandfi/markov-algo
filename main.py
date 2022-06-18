"""CLI for Markov algorithm engine"""
from rule import Rule
from markov import MarkovAlgorithm


def main():
    print("--Markov algorithm engine by artandfi--")
    print("Input the rules for the algorithm or S to stop:")

    rules = []
    ask_rules = True
    
    while ask_rules:
        user_input = input()
        if user_input in "sS":
            if not rules:
                print("Provide at least one rule")
            else:
                ask_rules = False
        else:
            try:
                rule = Rule(user_input)
                rules.append(rule)
            except AssertionError:
                print("Invalid rule. Please try again")
    
    algorithm = MarkovAlgorithm(rules)
    print("--Rules--")
    print(algorithm)
    print("--------")
    user_input = input("Specify the input string: ")
    print("Running algorithm...")
    output = algorithm.run(user_input)
    print(f"Algorithm run finished with output {output}")


if __name__ == "__main__":
    main()
