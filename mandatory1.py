import os
import sys
import subprocess
import json
import glob

#import urllib
from urllib.request import urlopen
from urllib.error import HTTPError

listPyElec = []
listReadme = []
listReqReadme = []


#gets data (json) from api and saves it in text file
def get_data_api():
    try:
       res = urlopen('https://api.github.com/orgs/python-elective-1-spring-2019/repos?per_page=100')
       dataPyElec = json.loads(res.read().decode('utf-8'))
       #print(dataPyElec)

       txtApi1 = open("manApi1.txt",'w+')

       for element in json.dumps(dataPyElec, indent=2):
           txtApi1.write(element)

    except HTTPError as err:
       print(err)
    except Exception as err:
        print(err)

#open the file manApi1.txt and inserts the clones in a list
def insert_to_list():
    try:
       textFile = open('manApi1.txt', 'r')    
       templist = []

       for line in textFile.readlines():
           templist.append(line)

       for element in templist:
           if 'clone' in element:
               listPyElec.append(element[18:-3])
         
       #print(listPyElec[8])
       print(listPyElec)
       #sys.exit()
    except FileNotFoundError:
       print('file not found')
    except Exception as err:
        print(err)

#gets subdirectories
def get_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

#clones repos from listPyElec
def git_clone_repos():
    
    if os.path.exists('./git_clone_Mandatory') == False:
      
      os.mkdir('git_clone_Mandatory')
      os.chdir('git_clone_Mandatory')

      for index in range(len(listPyElec)):
          #print(listPyElec[index])
          subprocess.run(['git','clone', listPyElec[index]])
    else:  
       #os.chdir('git_clone_Mandatory')
       for pathDir in get_subdirectories('./git_clone_Mandatory'):
          #os.chdir('git_clone_Mandatory')
          #print(pathDir)
          #os.chdir('')
          #os.chdir(pathDir)
          subprocess.run(['git','pull', pathDir])
          #os.chdir('..')

#get the readme file and puts the '## Required reading'-part in list
def traverse_and_get_readme():

    for name in glob.glob('*/*/*.md'):
        try:
            with open(name, 'r') as file:
                strInFile = file.read()
                #print(strInFile)
                strInFile = strInFile[strInFile.find('## Required reading'):strInFile.find('## Sup')]
                #print(strInFile)
                listReadme.append(strInFile[strInFile.find('## Required reading'):strInFile.find('### Sup')])
        except IOError:
            print('error')
    
    #print(listReadme)

#write and order the '## Required reading'-part in to file   
def write_required_reading_md():
    
    #1. make txt file and insert every list from listReadme into file  
    file = open('temp.txt', 'w')
    for var in listReadme:
        file.write(var.rstrip('\n'))
    
    #2. read form file and insert line to list
    file = open('temp.txt', 'r')
    templist = []
    for element in file.readlines():
        templist.append(element.rstrip('\n'))
    
    #3. remove and then add to require part to list
    listReqReadme.append('## Required reading')
    for line in templist:
        line = line.replace('## Required reading' , '')
        #line = line.replace('* [', '')
        
        listReqReadme.append(line)
        #print('new:' + line)
    
    #4. sort and no double
    resultList = sorted(listReqReadme)
    resultList = list(dict.fromkeys(resultList))

    #5.make a direcktory to the readme.md
    os.mkdir('git_repo')
    os.chdir('git_repo')
    file = open('Required_reading.md', 'w')

    #6. uppercase and insert to Required_reading.md
    for index in range(len(resultList)):
        resultList[index] = resultList[index].replace(resultList[index][:4] , resultList[index][:4].upper())
        file.write(resultList[index]+ '\n')
        #print(resultList[index])
       
    #print(listReadme)
    
#push to github
def push_to_git():
    #another way write to github
    #subprocess.run(['git', 'init'])
    #make every sbuprocess wait (queue/one at the time) 
    if os.path.exists('./git_repo') == False:
        pipe = subprocess.Popen('git init', shell=True)
        pipe.wait()

        pipe = subprocess.Popen('git remote add origin https://github.com/ultracake/pythonMan1.git', shell=True)
        pipe.wait()
        
        pipe = subprocess.Popen('git add Required_reading.md', shell=True)
        pipe.wait()

        pipe = subprocess.Popen('git commit -m "test"', shell=True)
        pipe.wait()

        pipe = subprocess.Popen('git push -u origin master', shell=True)
        pipe.wait()

        print('the subprocess´s is done')
    else:
        print('can´t do, already exist')

def main():
    get_data_api()
    insert_to_list()
    git_clone_repos()
    traverse_and_get_readme()
    write_required_reading_md()
    push_to_git()

    print(listReqReadme)

if __name__ == '__main__':
  main()