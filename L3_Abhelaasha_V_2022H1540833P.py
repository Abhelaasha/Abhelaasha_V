import httpimport #importing the package httpimport
url = "https://raw.githubusercontent.com/Abhelaasha/PFA_Assignment/main/" #github url for the corresponding hosted python module
with httpimport.remote_repo(url): #importing the repository for the given url
    import factorial as p #importing the necessary package into the program or application
    import circle as c #importing the necessray package into the programme
print("Given number ",4," ",p.fact(4))
print("Given radius ",7," ",c.area(7))
