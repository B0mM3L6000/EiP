















#####################################
#sauce foooter:

from random import randint
try:
    #Create an Encoder object
    enc = Encoder()
    # Create two strings
    st1 = "Lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat voluptua"
    st2 = "At vero eos at accusam sit justo duo dolores et ea rebum Stet clita kasd gubergren no sea takimata sanctus est Lorem ipsum"
    # set the dictionary
    enc.updateEncoding(st1,st2)
    # create a random sentence from words of the first sentence
    bagOfWords = str.split(st1)
    st3 = ""
    for i in range(19):
        st3 += bagOfWords[randint(0,len(bagOfWords)-1)]+" "
    st3 += bagOfWords[1]
    # encode the random sentence
    st4 = enc.encode(st3)
    # decode it
    st5 = enc.decode(st4)
    # print the random sentence
    print("#Encode String:",st3)
    # print the encoded sentence
    print("#Decode String:",st4)
    # print the decoded sentence
    print("#Result:",st5)
    # in this case: if the random and the decoded sentence are equal, the test is passed
    if(str.split(st3) == str.split(st5)):
        print("correct")
    else:
        print("Encoding or Decoding incorrect")
        print("Line #Encode String: and Line #Result: should be equal")
except:
    print("Some names or functions do not work correctly or are wrongly named")
