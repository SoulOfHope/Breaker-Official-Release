import os
import sys
from sly import Lexer, Parser

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def run_file(runfile):
    variables = {}
    class BRLexer(Lexer):
        tokens = {
            SAY, SET, ASSIGN, NUM, CALL, COPY, TO, COMMENT
        }

        SAY = r'say.*'
        SET = 'set'
        ASSIGN = r'=.*'
        NUM = r'\d+'
        CALL = 'call'
        COPY = r'copy'
        TO = r'to'
        COMMENT = '#/.*'

        ignore = r' ()''""'
        ignore_newline = r'\n'
        ignore_tab = r'\t'

        # Error handling rule
        def error(self, t):
            enablePrint()
            print("Unknown Character '%s'" % t.value[0])
            self.index += 1
            blockPrint()

    class BRParser(Parser):
        # Get the token list from the lexer (required)
        tokens = BRLexer.tokens

        @_('COMMENT')
        def statement(self, t):
            blockPrint()
            return True

        @_('SAY')
        def statement(self, t):
            enablePrint()
            return t.SAY[4:]

        @_('SET NUM ASSIGN')
        def statement(self, t):
            var_id = 'var' + t.NUM[0]
            value = t.ASSIGN[1:]
            variables[var_id] = value
            blockPrint()
            return True

        @_('CALL NUM')
        def statement(self, t):
            enablePrint()
            var_id = 'var' + t.NUM[0]
            if var_id in variables:
                return variables[var_id].strip(' ').strip('"')
            else:
                return 'ERROR: Variable not found'

        @_('COPY NUM TO NUM')
        def statement(self, t):
            enablePrint()
            src_id = 'var' + t.NUM0[0]
            dst_id = 'var' + t.NUM1[0]
            if src_id in variables:
                variables[dst_id] = variables[src_id]
                blockPrint()
                return True
            else:
                return 'ERROR: Source variable not found'

    lexer = BRLexer()
    parser = BRParser()
    try:
        with open(runfile, 'r') as f:
            text = f.readline()
            while text:
                result = parser.parse(lexer.tokenize(text))
                print(result)
                text = f.readline()
    except EOFError:
        pass
    except Exception as e:
        print('ERROR:', e)

def run_console():
    class BRLexerConsole(Lexer):
        tokens = {
            RETURN, HELP, FILE, INFO, CLEAR, RUN
        }

        RETURN = 'return'
        HELP = 'help'
        FILE = r'[A-Za-z0-9_.]+\.br'
        INFO = 'info'
        CLEAR = 'clear'
        RUN = 'run'

        ignore = r' ()'
        ignore_newline = r'\n'
        ignore_tab = r'\t'

    class BRParserConsole(Parser):
        tokens = BRLexerConsole.tokens

        @_('CLEAR')
        def statement(self, t):
            os.system('clear')

        @_('RETURN')
        def statement(self, t):
            sys.exit(0)

        @_('HELP')
        def statement(self, t):
            enablePrint()
            print('''
Commands:

return = Exits Breaker

help = Opens this message

info = Loads the system information

clear = Clear the console

run = Runs interpreter on a file
''')
            return 'End of help'

        @_('INFO')
        def statement(self, t):
            enablePrint()
            print('''
Breaker Shell/Language

Full Official Release v1.3.81

Current Channel: Official (Stable)

Last Update: 11 Feb 2023

Dev: OrionOreo
''')
            return 'END OF INFO'

        @_('RUN FILE')
        def statement(self, t):
            enablePrint()
            runfile = t.FILE
            if os.path.exists(runfile):
                run_file(runfile)
                blockPrint()
            else:
                return 'PATH ERROR: file', runfile, 'was not found. (Was extension valid (.br)?)'

    consolelexer = BRLexerConsole()
    consoleparser = BRParserConsole()
    try:
        text = input('Breaker > ')
        while text:
            result = consoleparser.parse(consolelexer.tokenize(text))
            print(result)
            enablePrint()
            text = input('Breaker > ')
    except EOFError:
        pass

if __name__ == '__main__':
    run_console()
