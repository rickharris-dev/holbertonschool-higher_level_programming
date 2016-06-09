import sys

''' Prints the action or prints error '''
if len(sys.argv) < 2:
    print "Please enter an action"
elif sys.argv[1] == "create":
    print "create"
elif sys.argv[1] == "print":
    print "print"
elif sys.argv[1] == "insert":
    print "insert"
elif sys.argv[1] == "delete":
    print "delete"
else:
    print "Undefined action " + sys.argv[1]
