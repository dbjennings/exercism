def is_isogram(string: str) -> bool:
    """
    Function: Determines if a word or phrase is an isogram.
    Note: In this case, spaces/hyphens can appear multiple times

         Parameters:
            string (str): The word/phrase being tested

        Returns:
            bool: True if string is an isogram

    Definitions:
        isogram - a word or phrase that has no repeating letters
    """
    
    stripped = string.lower().replace('-','').replace(' ','')
    return len(set(stripped)) == len(stripped)
