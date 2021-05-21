
def studyVar(var):
    print(f'The variable is: \' {var}')
    print(f"The variable type is: {type(var)}")
    print(f"The variable id is: {id(var)}")


studyVar(1)
studyVar(1.7)
studyVar(True)
studyVar("ciao")
l0 = [8, 9]
l1 = [1, 2]
studyVar(l0)
studyVar(l1)
