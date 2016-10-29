#!/usr/bin/python
import sys

class Pdb:
    def __init__(self):
        self.id = [] #id number 
        self.res = [] #residuum
        self.name = [] #aminoacids names
        self.position_x = []
        self.position_y = []
        self.position_z = []
    
    def read(self):
        handler = open('2kyv.pdb', 'r+')
        self.file = handler.readlines()
        for i in self.file:
            if i[0:6].strip() == "ATOM":
                index = i[7:11]
                self.id.append(index)
                ###################
                residuum = i[23:26]
                self.res.append(residuum)
                ###################
                name = i[17:20]
                self.name.append(name)
                ###################
                position_x = i[31:38]
                self.position_x.append(position_x)
                ###################
                position_y = i[39:46]
                self.position_y.append(position_y)
                ###################
                position_z = i[47:54]
                self.position_z.append(position_z)
        print "The PDB file has been read"

    def renumber_id(self):
        index = 0 
        for i in self.id:
            self.id[index] = index + 1
            print self.id[index]
            index = index + 1
        print "In file there is ",index," atoms"

    def renumber_res(self):
        index = 0
        self.name[index - 1] = " "
        self.res[index - 1] = 0

        for i in self.res:
            if self.name[index] == self.name[index - 1]: #If two aminoacids are the same
                self.res[index] = int(self.res[index - 1]) #they have equal residuum
            else:
                if int(self.res[index]) < int(self.res[index - 1]): #if residuum starts from 1
                    if int(self.res[index]) == int(self.res[-1]): #index is on the last value in list
                        self.res[index] = int(self.res[index - 1]) #assign to this value previous value
                    else:
                        self.res[index] = 1             
                else:
                    self.res[index] = int(self.res[index - 1]) + 1 #complete with the missing residuum number
            print int(self.res[index])
            index = index + 1
        print "Renumbered"

    def discontinuities_spaces(self):
        index = 0
        for i in self.res:#Badamy roznice miedzy dwoma kolejnymi residuuami
            if int(self.res[index]) - int(self.res[index - 1]) > 1:
                print "\nBeginning of the structure:" + self.res[index-1] + " residuum," + " index: " + str(self.id[index-1])
                print "Missing residuum:"
                for j in range (int(self.res[index-1])+1, int(self.res[index])):
                    print j
            index = index + 1
        
    def find_by_res(self):
        choice = input("Enter residuum number: \n")
        index = 0
        print "Id  AA  Res  Pos X   Pos Y   Pos Z\n"
        for i in self.res: # i = ..., 51, 51, 51, 51, 52, 52, ...
            if (int(i) == choice):
                print self.id[index], self.name[index], self.res[index], self.position_x[index], self.position_y[index], self.position_z[index]
            index = index + 1

    def iteration(self):
        iter_ob_x = iter(self.position_x)
        iter_ob_y = iter(self.position_y)
        iter_ob_z = iter(self.position_z)
        iter_index = iter(self.id)
        
        while True:
            try:
                element_x = next(iter_ob_x)
                element_y = next(iter_ob_y)
                element_z = next(iter_ob_z)
                element_i = next(iter_index)
                print "ID:",element_i,"X:",element_x,"Y:",element_y,"Z:",element_z
            except StopIteration:
                break

def main():
    obj = Pdb()
    while True:
        choice = input(
        """
        Menu:

        1   Read PDB file
        2   Renumbering indexes
        3   Renumbering residuum
        4   Find a particular atom with residuum
        5   Iterate over atom coordinates
        6   Show discontinuities spaces in residuum
        0   End the program

        """)
    num = int(choice)

    if num == 0:
        break
    elif num == 1:
        obj.read()
    elif num == 2:
        obj.renumber_id()
    elif num == 3:
        obj.renumber_res()
    elif num == 4:
        obj.find_by_res()
    elif num == 5:
        obj.iteration()
    elif num == 6:
        obj.discontinuities_spaces()
    
if __name__ == '__main__':
    main()