

class Encoder:
    def __init__(self, encoding = {}):
        self.encoding = encoding

    def updateEncoding(self,string1,string2):
        list1 = str.split(string1)
        list2 = str.split(string2)
        self.encoding = {}
        for i in range(len(list1)):
            self.encoding[list1[i]] = list2[i]

    def encode(self, string):
        encodedstring = ""
        toencode = str.split(string)
        for i in range(len(toencode)):
            encodedstring += self.encoding[toencode[i]] + " "
        return encodedstring

    def decode(self, string):
        decodedic = {}
        for key in self.encoding:
            decodedic[self.encoding[key]] = key
        decodedstring = ""
        todecode = str.split(string)
        for i in range(len(todecode)):
            decodedstring += decodedic[todecode[i]] + " "
        return decodedstring



##################################
"""
29.5:

nein es gilt nicht, wenn z.B. das Dictionary für verschiedene schlüssel gleiche
Bedeutungen hat

z.B. dict erstellt mit den strings:
"haus baum welt"
"rot blau blau"

und übersetzt werden soll:
"baum welt haus"

dann erhält man am ende: "welt welt haus"


"""




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
