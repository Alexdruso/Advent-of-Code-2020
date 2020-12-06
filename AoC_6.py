f = open("input6.txt", "r")

customDeclarations = f.read()

customDeclaration = set()
count = 0
for answers in customDeclarations.splitlines():
    if answers == "":
        count = count + len(customDeclaration)
        customDeclaration = set()
        continue
    customDeclaration = customDeclaration.union(set(list(answers)))

count = count + len(customDeclaration)
print('The sum of the unique positive answers for each group is: {}'.format(count))

customDeclaration = set(customDeclarations.splitlines()[0])
count = 0
for index in range(len(customDeclarations.splitlines())):
    if customDeclarations.splitlines()[index] == "":
        count = count + len(customDeclaration)
        customDeclaration = set(customDeclarations.splitlines()[index+1])
        continue
    customDeclaration = customDeclaration.intersection(set(customDeclarations.splitlines()[index]))

count = count + len(customDeclaration)
print('The sum of the unique positive answers for in common among the group is: {}'.format(count))