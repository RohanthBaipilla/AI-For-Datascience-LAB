def resolution(rules, statement):
    clauses = []
    for rule in rules:
        clauses.append(set(rule))

    neg_statement = set(["not " + s for s in statement])
    clauses.append(neg_statement)

    while True:
        new_clauses = set()
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])
                if set() in resolvents:
                    return True
                new_clauses.update(resolvents)
        if new_clauses.issubset(clauses):
            return False
        clauses = clauses.union(new_clauses)

def resolve(clause1, clause2):
    resolvents = set()
    for literal in clause1:
        if "not " + literal in clause2:
            new_clause1 = clause1.difference(set([literal]))
            new_clause2 = clause2.difference(set(["not " + literal]))
            resolvent = new_clause1.union(new_clause2)
            resolvents.add(resolvent)
    return resolvents

rules = [
    ["has_job", "has_income", "has_good_credit"],
    ["has_job", "has_income", "not has_bad_credit"],
    ["not has_job", "has_savings"],
    ["not has_income", "has_collateral"]
]

statement = ["has_job", "has_income", "not has_bad_credit"]

if resolution(rules, statement):
    print("This person is eligible for a loan.")
else:
    print("This person is not eligible for a loan.")
