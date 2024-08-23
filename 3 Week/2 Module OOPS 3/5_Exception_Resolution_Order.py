""" 
CASE - 1
            --> Given a piece of code that can throw any of several different exceptions, and one needs to account for all of the potential exceptions that could be raised without creating duplicate code or long, meandering code passages. 
            
            --> If you can handle different exceptions all using a single block of code, they can be grouped together in a tuple
"""

# url = "https://google.com"
# try:
#     client_obj.get_url(url)
# except (URLError, ValueError, SocketTimeout):
#     client_obj.remove_url(url)

""" 
CASE - 2            
            --> If something specific needs to be done for one of the exceptions amont the list, seperate it out into a new except block and perform the required operation there.
"""

# url = "https://google.com"
# try:
#     client_obj.get_url(url)
# except (URLError, ValueError):
#     client_obj.remove_url(url)
# except SocketTimeout:
#     client_obj.handle_url_timeout(url)


# try:
#     f = open("handle.txt")
# except (FileNotFoundError, PermissionError) as e:
#     ...
""" Except statement can be re-written as in the code given below. This works because OSError is a base class that's common to both the FileNotFoundError and PermissionError exceptions"""
# try:
#     f = open("hii.txt")
# except OSError:
#     ...


""" 
CASE - 3            
            --> The e variable holds an instance of the raised OSError. This is useful if the exception has to be invested further, such as processing it based on the valur of the additional status code. The except clauses are checked in the order listed and the first match executes.
"""
# try:
#     f = open("hii.txt")
# except OSError as e:
#     if e.errno == errno.ENOENT:
#         logger.error("File not found")
#     elif e.errno == errno.EACCES:
#         logger.error("Permission Denied")
#     else:
#         logger.error("Unexpected error ", e.errno)


""" 
CASE - 4            
            --> Here the except FileNotFoundError clause doens't execute because the OSError is more general, matches the FileNotFoundError exception, and was listed first.
"""
try:
    f = open("missing")
except OSError:
    print("It failed")
except FileNotFoundError:
    print("The file was missing.")

# FileNotFoundError is the subclass of OSError
