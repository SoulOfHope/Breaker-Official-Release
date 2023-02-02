from sly import Lexer, Parser
import os
import time
import sys
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
def refreshvar():
    if os.path.exists("var1.txt"):
        os.remove("var1.txt")
        open("var1.txt",'x')
    else:
        open("var1.txt",'x')
    if os.path.exists("var2.txt"):
        os.remove("var2.txt")
        open("var2.txt",'x')
    else:
        open("var2.txt",'x')
    if os.path.exists("var3.txt"):
        os.remove("var3.txt")
        open("var3.txt",'x')
    else:
        open("var3.txt",'x')
    if os.path.exists("var4.txt"):
        os.remove("var4.txt")
        open("var4.txt",'x')
    else:
        open("var4.txt",'x')
    if os.path.exists("var5.txt"):
        os.remove("var5.txt")
        open("var5.txt",'x')
    else:
        open("var5.txt",'x')
    if os.path.exists("var6.txt"):
        os.remove("var6.txt")
        open("var6.txt",'x')
    else:
        open("var6.txt",'x')
    if os.path.exists("var7.txt"):
        os.remove("var7.txt")
        open("var7.txt",'x')
    else:
        open("var7.txt",'x')
    if os.path.exists("var8.txt"):
        os.remove("var8.txt")
        open("var8.txt",'x')
    else:
        open("var8.txt",'x')
    if os.path.exists("var9.txt"):
        os.remove("var9.txt")
        open("var9.txt",'x')
    else:
        open("var9.txt",'x')
    if os.path.exists("var0.txt"):
        os.remove("var0.txt")
        open("var0.txt",'x')
    else:
        open("var0.txt",'x')
if os.path.exists("main.br"):
    refreshvar()
    print('Breaker has loaded.')
    view = input('Would you like to use the console or the interpreter? ')
    os.system('clear')
else:
    print('Downloading Breaker')
    print('Parsing files')
    print('Loading...')
    open('main.br', 'x')
    print('Breaker has loaded. Please Edit the main.br root file')
    exit(0x80)

if __name__ == '__main__':
    while True:
        view = view.lower()
        if view == 'console':
            class BRLexerConsole(Lexer):
                tokens = {
        RETURN, HELP, CALL, FILE, INFO, ERASE, REFRESH, CLEAR
    }

                RETURN = 'return'
                HELP = 'help'
                CALL = 'call'
                FILE = r'f..*'
                INFO = 'sysinfo'
                ERASE = 'erase'
                REFRESH = 'refresh'
                CLEAR = 'clear'

                ignore = (r' ()' '')
                ignore_tab = r'\t.*'
                ignore_comment = r'\#.*'
                ignore_newline = r'\n+'

                # Error handling rule
                def error(self, t):
                    enablePrint()
                    print("Illegal character '%s'" % t.value[0])
                    self.index += 1
                    blockPrint()


            class BRParserConsole(Parser):
                # Get the token list from the lexer (required)
                tokens = BRLexerConsole.tokens

                @_('CLEAR')
                def statement(self, t):
                    os.system('clear')
                    blockPrint()

                @_('ERASE')
                def statement(self, t):
                    enablePrint()
                    delete = input(
            'Are you sure you want to erase your breaker file? (This will delete Breaker, Please use all capitals YES or NO to confirm): '
        )
                    if delete == 'YES':
                        print('Erasing main.br')
                        time.sleep(5)
                        os.remove('main.br')
                        print('Breaker is now uninstalling...')
                        time.sleep(10)
                        f = open('main.py', 'r+')
                        f.truncate(0)
                        f.write(
                r'''def pack():
    with open('breaker.install','r') as firstfile, open('main.py','r+') as secondfile:
      
    # read content from first file
        for line in firstfile:
               
             # append content to second file
             secondfile.write(line)
pack()
'''
            )

                @_('RETURN')
                def statement(self, t):
                    enablePrint()
                    print('Returned with exit code:0')
                    exit(0)

                @_('REFRESH')
                def statement(self, t):
                    enablePrint()
                    refreshvar()
                    os.remove('main.br')
                    f=open("main.br", 'x')
                    f.close()
                    os.system('clear')
                    blockPrint()
                
                @_('INFO')
                def statement(self, t):
                    enablePrint()
                    print('''
Breaker Shell/Language

Full Official Release v1.3.8

Current Channel: Official (Verified)

Last Update: 26 Jan 2023

Dev: OrionOreo
''')
                    blockPrint()
                    return 'END OF INFO'

                @_('CALL FILE')
                def statement(self, t):
                    enablePrint()
                    file = t.FILE[2:] + '.txt'
                    if os.path.exists(file):
                        f = open(file, 'r')
                        return f.read()
                    else:
                        return 'PATH ERROR: file', file, 'was not found.'
    
                @_('HELP')
                def statement(self, t):
                    enablePrint()
                    print('''
Welcome to the console help!

return = Exits Breaker
              
help = Opens this message
              
call f. = Call a variable file
            
sysinfo = Loads the system information
              
erase = Erases breaker for reinstallation

refresh = Reloads all variables and Main.br

clear = Clear the console
''')
                    blockPrint()
                    return 'End of help'

            consolelexer = BRLexerConsole()
            consoleparser = BRParserConsole()
            try:
                enablePrint()
                text = input('Breaker > ')
                while text:
                    result = consoleparser.parse(consolelexer.tokenize(text))
                    print(result)
                    break
            except EOFError:
                break
        elif view == 'interpreter':
            class BRLexer(Lexer):
                tokens = {
        SAY, SET, ASSIGN, RETURN, NUM, CALL, COPY, TO, COMMENT
    }

                SAY = r'say.*'
                SET = 'set'
                ASSIGN = r'=.*'
                RETURN = 'return'
                NUM = r'[0-9]'
                CALL = 'call'
                COPY = r'copy [0-9]'
                TO = r'to [0-9]'
                COMMENT = r'#/.*'
                

                ignore = (r' ()' '')
                ignore_tab = r'\t.*'
                ignore_newline = r'\n+'

                # Error handling rule
                def error(self, t):
                    print("Illegal character '%s'" % t.value[0])
                    exit(0)
                
            class BRParser(Parser):
                # Get the token list from the lexer (required)
                tokens = BRLexer.tokens
                
                @_('COMMENT')
                def statement(self, t):
                    blockPrint()

                @_('SAY')
                def statement(self, t):
                    enablePrint()
                    return t.SAY[4:]

                @_('RETURN')
                def statement(self, t):
                    exit(0)

                @_('SET NUM ASSIGN')
                def statement(self, t):
                    file = ('var' + t.NUM[0] + '.txt')
                    f = open(file, 'r+')
                    wf = t.ASSIGN[1:]
                    wf = str(wf)
                    f.truncate(0)
                    f.write(wf)
                    blockPrint()
                    return 'Overwritten successfully'

                @_('CALL NUM')
                def statement(self, t):
                    enablePrint()
                    file = 'var' + t.NUM[0] + '.txt'
                    if os.path.exists(file):
                        f = open(file, 'r')
                        return f.read()
                    else:
                        return 'PATH ERROR: file', file, 'was not found.'

                @_('COPY TO')
                def statement(self,t):
                    enablePrint()
                    filec = 'var' + t.COPY[5] + '.txt'
                    if os.path.exists(filec):
                        cf = open(filec, 'r')
                        copy=cf.read()
                        filep = 'var' + t.TO[3] + '.txt'
                        if os.path.exists(filep):
                            pf = open(filep, 'w')
                            pf.write(copy)
                            blockPrint()
                        else:
                            return "Your program is missing data. Please use the console to reload"
                    else:
                        return 'PATH ERROR: file', filec, 'was not found.'
                       
            lexer = BRLexer()
            parser = BRParser()
            try:
                f = open("main.br", "r")
                text = f.readline()
                while text:
                    result = parser.parse(lexer.tokenize(text))
                    print(result)
                    text = f.readline()
                break
            except EOFError:
                break