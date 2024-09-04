from tkinter import filedialog
import json

def writeJsonFile(data:dict)->None:
    print('Do you want to save Json file? [Y/N]')
    answer = input()
    if answer == 'y' or answer == 'Y':
        saveFile = filedialog.asksaveasfile(filetypes=[('Json File','*.json'),('All Files','*.*')],defaultextension=[('Json File','*.json'),])
        saveFile.writelines(json.dumps(data,indent=4))
        saveFile.close()
        print('Your Json file is sucessfully created')
 

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

if __name__ == '__main__':
    csvFiles = []
    print('Welcome to the configuration files generator')
    print('Do you want to add a csv file? [Y/N]')
    answer = input()
    if answer == 'Y' or answer == 'y':
        PathCsv = filedialog.askopenfilename(title='Selecionar archivo',filetypes=[("CSV","*.csv*"),("Todos los archivos","*.*")])
        csvFiles.append(PathCsv)
    elif answer == 'N' or answer == 'n':
        exit()
    while answer == 'Y' or answer == 'y':
        print('Do you want to add another csv file? [Y/N]')
        answer = input()
        if answer == 'Y' or answer == 'y':
            PathCsv = filedialog.askopenfilename(title='Selecionar archivo',filetypes=[("CSV","*.csv*"),("Todos los archivos","*.*")])
            csvFiles.append(PathCsv)
        else:
            break
    createJsonFile(csvFiles)
    print('Touch whatever key to exit')
    _ = input()
