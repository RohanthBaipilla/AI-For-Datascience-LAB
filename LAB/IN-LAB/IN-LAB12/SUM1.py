# Define the initial facts and rules
facts = {
    ("animal", "hen"),
    ("eating", "hen"),
    ("egg", "chick")
}

rules = [
    (("egg", "A"), ("animal", "A")),
    (("animal", "A"), ("food", "A")),
    (("animal", "A"), ("eating", "A"), ("human", "A"))
]

# Initialize the working memory with the initial facts
working_memory = set(facts)

# Iterate over the rules until no new facts can be inferred
while True:
    new_facts = set()
    for rule in rules:
        # Check if all the premises of the rule are in the working memory
        if all(premise in working_memory for premise in rule[:-1]):
            # Add the conclusion to the set of new facts
            new_facts.add(rule[-1])
    # If no new facts were inferred, stop iterating
    if not new_facts:
        break
    # Add the new facts to the working memory
    working_memory.update(new_facts)

# Print the inferred facts
print(list(working_memory))
