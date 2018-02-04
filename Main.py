import TOI as toi
import BBC as bbc

keys = raw_input("Enter Tags\n").split(" ")


#print "News containg " +keys+ " is"


for j in range(len(keys)) :
    
    #to store the news we are getting from Times Of India
    str = []

    print "News contaning " +keys[j]+ " is:\n"

    #printing the news recieved from Times Of India
    print "News from Times Of India\n"

    #to get the news from Times Of India
    str = toi.get_news(str,keys[j])

    for i in str:

        print i

    str = []

    print "News From CNN\n"

    str = bbc.get_news(str,keys[j])

    for i in str:
        print i
    print "\n"
