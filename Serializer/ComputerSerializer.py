#ComputerSerializer made by Kevin Sugar for HeyJobs GmbH
#Last changed 21.02.2020

import configparser
import datetime

config = configparser.ConfigParser()
config.read("config.ini")


def GetModel():
    global Model
    Model = input("Please enter the TYPE of device (WIN/MAC): ")
    Model = Model.upper()
    
    if Model in ("MAC","IOS","OSX"):
        print("Model is MAC")
        Model = "MAC"

    if Model in ("WIN","PC"):
        print("Model is WIN")
        Model = "WIN"
    
    if Model not in ("MAC", "WIN"):
        print("MODEL IS NOT WIN OR MAC! PLEASE CHECK INPUT!")
        GetModel()
    

def GetYear():
    global Year
    Year = input("Please enter the YEAR of the device: ")
    if int(Year) > datetime.datetime.now().year:
        print("CAN'T USE YEAR THAT IS IN THE FUTURE!")
        GetYear()
    if int(Year) < 2010:
        OldYear = input("Are you sure that you want to use " + Year + " as the Year? (Y/N): ")
        if OldYear.upper() in ("Y","YES","JA","J"):
            pass
        if OldYear.upper() in ("N","NO","N","NEIN"):
            GetYear()


def GetID():
    global ID
    global Model
    
    if Model in ("MAC","mac","Mac"):
        ID = config["DEFAULT"].getint("MACNUMBER")        

    if Model in ("WIN","win","Win","PC","pc"):
        ID = config["DEFAULT"].getint("WINNUMBER")
    
    ID = ID+1
   

def GenerateName():
    global Model
    print("The generated Computername is: ")
    print("{}{}HJ{:0>3}".format(Model,Year,ID))
    EndScript()


def EndScript():
    global Model
    End = input("Please copy the generated name, if you want to change the Year type \"YEAR\", if you want to quit type \"END\": ")
    End = End.upper()
    if End in ("YEAR"):
        GetYear()
        GetID()
        GenerateName()

    if End in ("END"):
        if Model in ("MAC"):
            config.set("DEFAULT", "MACNUMBER", str(ID))
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        if Model in ("WIN"):
            config.set("DEFAULT", "WINNUMBER", str(ID))
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        AskEnd = input("Press enter to exit the application or type \"R\" to restart... \n")
        if AskEnd.upper() == "R":
            print(AskEnd)
            Start()
        

def Start():
    GetModel()
    GetYear()
    GetID()
    GenerateName()     

if __name__ == "__main__":
    Start()
    
    
