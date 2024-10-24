class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

def create_rule(rule_string):
    # Convert rule string into AST (implement parsing logic)
    pass

def combine_rules(rules):
    # Combine multiple ASTs (rules) into a single AST
    pass

def evaluate_rule(ast, data):
    # Evaluate AST against the provided user data
    pass

# Test cases
rule1 = "age > 30 AND salary > 50000"
ast1 = create_rule(rule1)
data = {"age": 35, "salary": 60000}
result = evaluate_rule(ast1, data)
print(result)
