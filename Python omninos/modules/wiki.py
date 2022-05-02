"""import wikipedia
result = wikipedia.summary("India", sentences = 2)
print(result)"""

'''import wikipedia
result=wikipedia.search("anju", results=10)
print(result)'''
import wikipedia
 
# setting language to hindi
wikipedia.set_lang("hi")
 
# printing the summary
print(wikipedia.summary("rajasthan"))