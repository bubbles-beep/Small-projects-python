import wikipedia as wiki

#print all suggestions of your input
print(wiki.search("Python"))

#check if wikipedia will suggest us python if we make misspelling
print(wiki.suggest("Pyth"))

#how to get the summary of an article
print(wiki.summary("Python"))

#how to change a language from english
wiki.set_lang("pl")
print(wiki.summary("Python"))

#how to get only the title of article
print(p.title)

#how to get the url of the article
print(p.url)

#how to scrape full article
print(p.content)

#how to get images from article
print(p.images)

#how to get all referals used in the article
print(p.links)
