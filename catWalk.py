#https://app.codesignal.com/arcade/python-arcade/slithering-in-strings/GH7QauS4xyHin5YLm
#Remove multiple white spaces with single white space and remove trailing spaces.
#highlight: how to use regular expression to replace, re.sub
#strip: to remove trailing spaces 
def catWalk(code):
    #return code.strip()
    return re.sub(r'\s+',' ',code).strip(' ')  