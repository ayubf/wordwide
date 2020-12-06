#!python

# Imported Libraries

#Search functions inside the file
from bs4 import BeautifulSoup

#Gets the webpage
import requests

#Decorations, stylizing and rich text
from rich import print


#Source for defenitions
dictionary = 'https://www.merriam-webster.com/dictionary/'

#Argument Support
import argparse
import sys

#Functions

def main():
    def dictSearch():

        #Uses dictionary url and adds the word the user searches for at the end, then parses it
        req = requests.get(dictionary+sys.argv[2])
        soup = BeautifulSoup(req.content, 'lxml')
    
        extr = ': '

        #The class of the elements that holds the defenition
        defs = soup.find(class_='dtText')
        if defs is None:
            defs = soup.find(class_='un')
            if defs is None:
                print("Sorry that's not available(use -h for help)")
                return 0
        else: 
            defs = soup.find(class_='dtText').text
    
        #Cleans the extra bits we dont need
        if extr in defs:
            defs = defs.replace(extr, '')
    
        word = '[bold bright_blue]'+sys.argv[2]+'[/bold bright_blue]: '
        defs = defs
        print(word,defs)


    def wotDay():
        #Similar to dictSearch but searches the same url everytime, but the page changes every day
        req= requests.get('https://www.merriam-webster.com/word-of-the-day')
        soup = BeautifulSoup(req.content,'lxml')

        #Word name
        wotd = soup.find('h1').text

        #Word defenition
        wotdDef = soup.find('p').text

        #Clean-up if statements
        if '1' in wotdDef:
            wotdDef = wotdDef.replace('1', '')
        if ':' in wotdDef:
            wotdDef = wotdDef.replace(':','')

        #Puts the word and the definition togehter
        wotdForm = wotd+':'+wotdDef
    
        print(wotdForm)


    def help():
        #Prints the help/information page
        print('''
    
        [blue] ----  [bold blue]Wordwide Quick Search[/bold blue]  ----[/]

                    Version 1.0
                    Ayub Farah
                     Python 3

        [blue]------------------------------------[/]

        [bold red]Command Index[/bold red]:
        [red]-h[/]: displays this page
        [red]-d {word} [/]: Searches for the defention of {word}
        [red]-w[/] : displays the word of the day

        [blue]------------------------------------[/]
        [bold green]
        Dev Note:[/bold green]
        Simple cli tool to help me with quick searches. 
        I'm planning to add more functionality in the future.
        If you have anything to tell me(ie, comments, questions, concerns, 
        suggestions, bugs/issues) my reddit is u/slushieslurp

        [blue]------------------------------------[/]

        [bold purple]Links[/bold purple]:
        [purple]Repo[/]: https://github.com/ayubf/wordwide
        [purple]Python.org[/]: https://www.python.org/

        [blue]------------------------------------[/]

        [bold magenta]Libraries[/bold magenta]:
        [magenta]BeautifulSoup4[/]:https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        [magenta]Rich[/]:https://rich.readthedocs.io/en/latest/introduction.html
        [magenta]Requests[/]:https://requests.readthedocs.io/en/master/ 

     
        [blue]------------------------------------[/]

        [bold cyan1]Release Notes[/bold cyan1]:
        [cyan2](Full Release Notes:https://github.com/ayubf/wordwide/blob/main/releases.txt)[/]

        - [cyan1]1.0[/]
        . Definiton search added
        . Word of the day feature added

      
        [blue]------------------------------------[/]
        
            [italic yellow]Thank you for downloading![/italic yellow]

                    - Ayub
        ''')


    if '-d' in sys.argv[1]:
        dictSearch()
    if '-h' in sys.argv[1]:
        help()
    if '-w' in sys.argv[1]:
        wotDay()