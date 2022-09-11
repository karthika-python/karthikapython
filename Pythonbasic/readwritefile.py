class Textfile:
    '''def fileread(self):
        f = open("C:\\Users\\karth\\PycharmProjects\\pythonProject\\Karthika1\\textfile\\test1.txt")
        print(f.read())
        print(f.read(10))
        print(f.readline())
        print(f.readlines())
        iterate = f.readlines()
        for xc in iterate:
            print(xc)
        f.close()'''

    def filereadfindaword(self, matchstring):
        f = open("C:\\Users\\karth\\PycharmProjects\\pythonProject\\Karthika1\\textfile\\test1.txt")
        iterate = f.readlines()
        count = 0
        for xc in iterate:
            count += 1
            print(xc)
            '''setstore = re.split("\s", xc)
            # print(setstore)
            for eachvalu in setstore:
                # print(eachvalu)
                if (eachvalu == matchstring):
                    print("The given string is " + matchstring + " identified in line number : " + str(count))'''
        f.close()
obj = Textfile()
obj.filereadfindaword("third")