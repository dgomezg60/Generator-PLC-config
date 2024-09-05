import easygui
import json

def writeJsonFile(data:dict)->None:
    print('Do you want to save Json file? [Y/N]')
    answer = input()
    if answer == 'y' or answer == 'Y':
        saveFile =easygui.filesavebox(default='*.json')
        if saveFile != None:
            file = open(saveFile,'w')
            file.writelines(json.dumps(data,indent=4))
            file.close()
            print('Your Json file is sucessfully created')
    elif answer == 'n' or answer == 'N':
        pass

def createJsonFile(PathsFiles:list[str])->None:
    Json = {}
    for PathFile in PathsFiles:
        file = open(PathFile,'r')
        filename = PathFile[PathFile.rfind('/'):]
        db =filename[filename.find('[')+1:filename.find(']')]
        ListOfData = []
        for line in file:
            line = line.replace('\n','')
            Data = {
                "Name": None,
                "DataType":None,
                "Offset": None
            }
            Words = line.split(',')
            for i in range(0,len(Data.keys())):
                Data[f'{list(Data.keys())[i]}'] = Words[i]
            ListOfData.append(Data)
        Json[f'{db}'] = ListOfData
    writeJsonFile(Json)

def addCsvFiles()->str:
    print('Do you want to add a csv file? [Y/N]')
    firstanswer = input()
    if firstanswer == 'Y' or firstanswer == 'y':
        PathCsv = easygui.fileopenbox(default='*.csv')
        if PathCsv != None:
            csvFiles.append(PathCsv)
    elif firstanswer == 'N' or firstanswer == 'n':
        return firstanswer
    answer = firstanswer
    while (answer == 'Y' or answer == 'y') and PathCsv !=None:
        print('Do you want to add another csv file? [Y/N]')
        answer = input()
        if answer == 'Y' or answer == 'y':
            PathCsv = easygui.fileopenbox(default='*.csv')
            if PathCsv != None:
                csvFiles.append(PathCsv)
        else:
            break
    if PathCsv == None:
        return 'N'
    createJsonFile(csvFiles)
    return firstanswer

if __name__ == '__main__':
    csvFiles = []
    print('Welcome to the json files generator')
    answer = addCsvFiles()
    while answer == 'Y' or answer == 'y':
        print('Do you want to do another json file?')
        answer = input()
        if answer == 'N' or answer == 'n':
            break
        elif answer == 'Y' or answer =='y':
            answer = addCsvFiles()
    print('Touch whatever key to exit')
    _ = input()