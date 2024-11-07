from os.path import dirname, join

from polyglot_piranha import execute_piranha, PiranhaArguments, Rule, RuleGraph, OutgoingEdges

# Create Piranha arguments
piranha_arguments = PiranhaArguments(
    language = "java",
    path_to_configurations =  "./java/configurations",
    paths_to_codebase = ["./java/examples"],
)


# Execute Piranha and print the transformed code
piranha_summary = execute_piranha(piranha_arguments)

