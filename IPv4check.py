import re

def is_valid_IP(strng):

    chk = re.split('\.', strng)

    if len(chk) != 4:
        return False
    
    for i in range(len(chk)):
        if not str.isnumeric(chk[i]):
            return False
        chk2 = str(chk[i])
        if chk2[0] == '0' and len(chk2) > 1:
            return False
        
    nStrng = list(map(int, chk))
    
    for j in range(len(nStrng)):
        if 255 - nStrng[j] < 0:
            return False
        
    return True

#   Did this one after a long hiatus, felt satisfied with my answer up until I saw someone import socket
# and use that library for a very simple straightforward check. Everyone feels clever until someone does it
# simpler, faster, or cleaner. Fun things were learned though! Turns out, you -can't- subscript a specific 
# index on a string of numbers from a list of strings because those numbers in those indexes are considered 
# integers and -not- characters like I assumed. Overall, became more familiar with string manipulation in
# Python and the quirks of the language. Pretty happy about that.