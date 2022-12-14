ps axf | grep dump | awk '{print "kill " $1}' | sh
