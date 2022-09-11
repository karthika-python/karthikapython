class stringconcept():

   def reversefunction(self,text):
       name = ""
       for rev in text:     #rev=k a r t h i k a
           name = rev + name # name=k+,name=a+k(ak),name=r+ak(rak),name=t+rak....
       print("Original string is :", text)
       print("Reverse string is :", name)
       return (name)

   def reverseword(self):
       original= input("Enter the statement ?")
       reverseword= input("Enter word to reverse:")
       reversed=self.reversefunction(reverseword)
       #print(reversed)
       change=original.replace(reverseword,reversed)
       print("The change word is :",change)








obj=stringconcept()
obj.reversefunction("karthika")
obj.reverseword()


    '''def reversefunction(self):
        name=[1,5,8,5]
        name.reverse()
        #print("Original string is :", text)
        print("Reverse string is :", name)'''






