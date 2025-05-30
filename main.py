from googlesearch import search
a = ("Welcome to Search Engine powered by Google")
a = a.center(40)
print(a)
while True :
  search_term = input("Enter your search term(type exit() for quit): \n")
  if (search_term == "exit()"):
   break
  for url in search (search_term,num=10,stop=10,pause=2):
    print(url)
