import os
import shutil 
from pathlib import Path
bruh = os.listdir("C:/Users/6on/ngsi-summer-2024/Airport3/PassportImages")
bruh2 = os.listdir("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages")



def make_dir():
    for i in bruh:
        name = i.removesuffix(".png")
        if not Path("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages2/" + name).is_dir():
            os.mkdir("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages2/" + name)
        
        
def seperate():
    for i in bruh:
        name = i.removesuffix(".png")        
        for n in bruh2:
            # print(n.rsplit("_"))
            if int(n.rsplit("_")[0]) == int(name):
                if not Path("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages2/" + name + "/"+ n).is_file():
                    shutil.move("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages/" + n,"C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages2/" + name)
                else:
                    shutil.move("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages/" + n,"C:/Users/6on/ngsi-summer-2024/Airport3/Disacard")

                
                
        
def check_num():

    print(os.listdir("C:/Users/6on/ngsi-summer-2024/Airport3/PassportImages"))


def move_passport():
    for i in bruh2:
        if not i.__contains__("_"):
            if not Path("C:/Users/6on/ngsi-summer-2024/Airport3/PassportImages/"+i):
                shutil.move("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages/" + i, "C:/Users/6on/ngsi-summer-2024/Airport3/PassportImages")
            else:
                shutil.move("C:/Users/6on/ngsi-summer-2024/Airport3/AirportImages/" + i, "C:/Users/6on/ngsi-summer-2024/Airport3/Discard")
        

# move_passport()
# make_dir()
seperate()
# check_num()
