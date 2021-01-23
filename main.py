class main:
    def __init__(self):
        pass

    def draw(self):
        print("Welcome to Friend_Tracker_2.0")
        print("-----------------------------")
        print("Type in read if you want to read a profile,\nand write if you want to add something to the profile,\nor type in help if you need help. Type in exit if you want ot exit.\n\nNOTE: The profile files are in the Data folder.")
        self.A = input(">>> ")
        if "ead" in self.A:
            self.readF()
        elif "rite" in self.A:
            self.writeF()
        elif "el" in self.A:
            self.help()
        elif "exit" in self.A:
            exit()
        else:
            print("Not correspondingly...")
            self.draw()

    def readF(self):
        self.name = input("Name: ")
        self.f = "Data/" + self.name + ".txt"
        with open(self.f, "r") as f:
            print(f.read())
            f.close()

        self.A = input("Go back? y: ")
        if "y" in self.A:
            self.draw()

    def writeF(self):
        global f
        self.name = input("Name: ")
        self.f = "Data/" + self.name + ".txt"
        self.item = input("Item: ")
        self.deff = input("Definition: ")

        with open(self.f, "a") as f:

            f.write(self.item + " : " + self.deff + "\n")
            f.close()

        self.A = input("Do you want to write more? y/n: ")
        if "y" in self.A:
            self.writeFM("yes")
        else:
            self.draw()

    def writeFM(self, y):
        while y:
            self.item = input("Item: ")
            self.deff = input("Definition: ")

            with open(self.f, "a") as f:
                f.write(self.item + " : " + self.deff + "\n")
                f.close()

            self.A = input("Do you want to write more? y/n: ")

            if "y" in self.A:
                self.writeFM(y)
            else:
                self.draw()

    def help(self):
        print("If you type in read it will ask you to type in the profile or persons name (Name of the file) like this: if i typed in write and i put in Fred to make a new profile, then i will type in Fred when i deside to read the file. If you wrote write it will ask you the persons name, after you have type in the name, type into the Item and write like there name or age or something like that but dont write the other part like this name is Fred, dont do that just type in name or something and then press enter, after you press enter it will ask you for definition and that is where you will type in the persons name like Fred or the age like 15, lastly it will ask do you want to write more. NOTE: If you type in the name wrong it will make another profile for that name! Make  sure you type in the name correctly before you press enter.")
        self.A = input("Go back? y: ")
        if "y" in self.A:
            self.draw()


if __name__ == "__main__":
    app = main()
    app.draw()
