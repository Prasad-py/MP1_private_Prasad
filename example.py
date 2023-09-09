# import metapy

# def tokens_lowercase(doc):
#     #Write a token stream that tokenizes with ICUTokenizer (use the argument "suppress_tags=True"), 
#     #lowercases, removes words with less than 2 and more than 5  characters
#     #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
#     '''Place your code here'''
    
#     #leave the rest of the code as is
#     tok.set_content(doc.content())
#     tokens, counts = [], []
#     for token, count in trigrams.items():
#         counts.append(count)
#         tokens.append(token)
#     return tokens


# if __name__ == '__main__':
#     doc = metapy.index.Document()
#     doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")
#     print(doc.content()) #you can access the document string with .content()
#     tokens = tokens_lowercase(doc)
#     print(tokens)


import metapy

def tokens_lowercase(doc):
    # Replace the comment below with a brief description of what this function does.
    '''
    This function tokenizes the input document using the ICUTokenizer with the argument "suppress_tags=True,"
    converts tokens to lowercase, removes words with less than 2 and more than 5 characters, performs stemming,
    and generates trigrams.
    '''

    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    tok = metapy.analyzers.LowercaseFilter(tok)
    tok = metapy.analyzers.LengthFilter(tok, min=2, max=5)
    tok = metapy.analyzers.Porter2Filter(tok)
    ana = metapy.analyzers.NGramWordAnalyzer(3, tok)
    trigrams = ana.analyze(doc)

    #leave the rest of the code as is
    tok.set_content(doc.content())
    tokens, counts = [], []
    for token, count in trigrams.items():
        counts.append(count)
        tokens.append(token)
    return tokens
    
if __name__ == '__main__':
    doc = metapy.index.Document()
    doc.content("I said that I can't believe that it only costs $19.95! I could only find it for more than $30 before.")
    
    # Replace the comment below with an explanation of what the following code block does.
    '''
    This code block prints the original content of the document and then calls the tokens_lowercase function
    to tokenize, lowercase, filter, stem, and generate trigrams from the content. It then prints the resulting tokens.
    '''
    
    print("Original Document Content:")
    print(doc.content())
    
    tokens = tokens_lowercase(doc)
    
    print("\nProcessed Tokens:")
    print(tokens)
