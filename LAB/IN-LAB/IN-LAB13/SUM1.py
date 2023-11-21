# Define the initial facts and rules
facts = {"Plant('Mango')", "Eating('Mango')", "Seed('Sprouts')","Fruit('Mango')","Human('Mango')"}
rules = [("Seed(A)==>Plant(A)", 1), ("Plant(A)==>Fruit(A)", 1), ("Plant(A),Eating(A)==>Human(A)", 1)]

# Define the inference engine function
def forward_chaining(facts, rules):
    inferred_facts = set(facts)
    while True:
        new_facts = set()
        for rule, count in rules:
            antecedents, consequent = rule.split("==>")
            antecedents = antecedents.strip("()").split(",")
            antecedents = [fact.strip() for fact in antecedents]
            consequent = consequent.strip()
            if all([fact in inferred_facts for fact in antecedents]):
                new_facts.add(consequent)
                if count == 2:
                    new_facts.add(rule)
        if not new_facts:
            break
        inferred_facts |= new_facts
    return inferred_facts

# Apply the inference engine to the given facts and rules
inferred_facts = forward_chaining(facts, rules)

# Print the inferred facts
print("Inferred facts:")
for fact in inferred_facts:
    print(fact)
