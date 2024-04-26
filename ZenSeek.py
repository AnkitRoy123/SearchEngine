from googlesearch import search
a = ("Welcome to ZenSeek. It's create by Ankit Roy. This is a search engine.")
a = a.center(40)
print(a)
while True :
  search_term = input("Enter your search term: \n")
  for url in search (search_term,num=10,stop=10,pause=2):
    print(url)
