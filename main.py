from madlib import piranha_river

for required in piranha_river.required:
    piranha_river.inputs.append(input("Enter a %s: " % required))

print(piranha_river.story % tuple(piranha_river.inputs))

