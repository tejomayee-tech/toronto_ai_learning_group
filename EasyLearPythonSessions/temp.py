paragraph = """A story is a narrative account of related events, whether true or fictional, 
told to entertain, educate, or preserve culture. Stories can be shared through words, images, 
or performance and can range from a brief anecdote to the plot of a novel. The term can also refer to a report, 
a rumor, or even a falsehood, notes Dictionary.com and Merriam-Webster."""



sentenses = paragraph.split(".")
for sentense in sentenses:
    print(sentense.lstrip()+".")