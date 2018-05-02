def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start = text.find(begin) + len(begin)  if begin in text else None
    stop = text.find(end)  if end in text else None 
    return text[start:stop]



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers('No [b]hi', '[b]', '[/b]'))
    print(between_markers('No[/b] hi', '[b]', '[/b]'))
    print(between_markers('No hi', '[b]', '[/b]'))
    print(between_markers('No <hi>', '>', '<'))
    print(between_markers("Never send a human to do a machine's job.","Never","do"))
## 
##
##    # These "asserts" are used for self-checking and not for testing
##    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
##    assert between_markers("<head><title>My new site</title></head>",
##                           "<title>", "</title>") == "My new site", "HTML"
##    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
##    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
##    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
##    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
