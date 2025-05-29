# Unification and resolution in predicate logic

# Function to check if two predicates can be unified
def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():  # x is a variable
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():  # y is a variable
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

# Function to unify a variable with a term
def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Apply substitution (for displaying resolved result)
def substitute(theta, expr):
    return [theta.get(arg, arg) for arg in expr]

# Function to apply resolution rule
def resolution(kb, query):
    for clause in kb:
        premise, conclusion = clause
        theta = unify(premise, query, {})
        if theta is not None:
            new_query = substitute(theta, conclusion)
            if all(arg not in new_query for arg in theta):  # base case
                return True
            else:
                return resolution(kb, new_query)
    return False

# Knowledge base (Implications): Human(x) → Mortal(x)
knowledge_base = [
    [["Human", "x"], ["Mortal", "x"]]
]

# Fact: Human(John)
fact = ["Human", "John"]

# Query: Is John Mortal?
query = ["Mortal", "John"]

# Add fact to knowledge base
knowledge_base.insert(0, [fact, []])  # fact with no conclusion (known truth)

# Apply resolution
if resolution(knowledge_base, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
