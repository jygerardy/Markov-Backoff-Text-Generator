doc = ['This is your first text', 'and here is your second text.']
# For better results, use large corpora
mark = markov(doc, 2, 2)
mark.generate_markov_text('type a sentence that has at least n_grams words', size=300)
