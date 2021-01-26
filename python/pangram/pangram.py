def is_pangram(sentence):

    '''
    Determines if a given sentence is a pangram.
    Pangram - a sentence or phrase that contains all letters of a given
              language
    '''

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if not letter in sentence.lower():
            return False
    
    return True
