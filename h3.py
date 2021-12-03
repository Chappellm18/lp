# h3.py
import sys
import time   # sys needed to access cmd line args and sys.exit()


class Node:
    def __init__(self, type, right, left):
        self.type = type
        self.right = right
        self.left = left


class Token:
    def __init__(self, line, column, category, lexeme):
        self.line = line         # source program line number of the token
        self.column = column     # source program column in which token starts
        self.category = category  # category of the token
        self.lexeme = lexeme     # token in string form


# global variables
trace = False      # controls token trace
grade = True      # set to True to create output to be graded
source = ''        # receives entire source program
sourceindex = 0    # index into the source code in source
line = 0           # current line number
column = 0         # current column number
tokenslist = []    # list of tokens created by the tokenizer
tokenindex = -1    # index of current token in tokens
token = None       # current token
prevchar = '\n'    # '\n' in prevchar signals start of new line
blankline = True

co_names = []      # holds variable names
co_consts = []     # constants constants in binary form
co_code = []       # holds bytecode

symtab = []

# token categories that can start statements

# constants that represent token categories
EOF = 0      # end of file
PRINT = 1      # 'print' keyword
UNSIGNEDINT = 2      # unsigned integer
NAME = 3      # identifier that is not a keyword
ASSIGNOP = 4      # '=' assignment operator
LEFTPAREN = 5      # '('
RIGHTPAREN = 6      # ')'
PLUS = 7      # '+'
MINUS = 8      # '-'
TIMES = 9      # '*'
NEWLINE = 10     # end of line
ERROR = 11     # if not any of the above, then error
NEGATE = 12
INTEGER = 13
PROGRAM = 14

# displayable names for each token category
catnames = ['EOF', 'print', 'UNSIGNEDINT', 'NAME', 'ASSIGNOP',
            'LEFTPAREN', 'RIGHTPAREN', 'PLUS', 'MINUS',
            'TIMES', 'NEWLINE', 'ERROR']

# keywords and their token categories}
keywords = {'print': PRINT}

# one and two-character tokens and their token categories
smalltokens = {'=': ASSIGNOP, '(': LEFTPAREN, ')': RIGHTPAREN,
               '+': PLUS, '-': MINUS, '*': TIMES, '\n': NEWLINE, '': EOF}

# bytecode opcodes
UNARY_NEGATIVE = 11      # hex 0B
BINARY_MULTIPLY = 20      # hex 14
BINARY_ADD = 23      # hex 17
PRINT_ITEM = 71      # hex 47
PRINT_NEWLINE = 72      # hex 48
STORE_NAME = 90      # hex 5A
LOAD_CONST = 100     # hex 64
LOAD_NAME = 101     # hex 65

#################
# main function #
#################


def main():
    global source

    if len(sys.argv) == 2:
        try:
            infile = open(sys.argv[1], 'r')
            source = infile.read()   # read source code
        except IOError:
            print('Cannot read input file ' + sys.argv[1])
            sys.exit(1)
    else:
        print('Wrong number of command line arguments')
        print('Format: python h1.py <infile>')
        sys.exit(1)

    if source[-1] != '\n':
        source = source + '\n'

    if grade:
        print(time.strftime('%c') + '%34s' % 'Mitch Chappell')
        print('Interpreter = ' + sys.argv[0])
        print('Input file  = ' + sys.argv[1])

    if trace:
        print('------------------------------------------- Token trace')
        print('Line  Col Category       Lexeme\n')

    try:
        tokenizer()  # tokenize source code in source
        ast = parser()    # parse and compile

    # on an error, display an error message
    # token is the token object on which the error was detected
    except RuntimeError as emsg:
        # output slash n in place of newline
        lexeme = token.lexeme.replace('\n', '\\n')
        print('\nError on ' + "'" + lexeme + "'" + ' line ' +
              str(token.line) + ' column ' + str(token.column))
        print(emsg)         # message from RuntimeError object
        sys.exit(1)

    interpreter(ast)  # interpret the program

    if grade or trace:
        print('------------------------------------------- Program output')


####################
# tokenizer        #
####################


def tokenizer():
    global token
    curchar = ' '                       # prime curchar with space

    while True:
        # skip whitespace but not newlines
        while curchar != '\n' and curchar.isspace():
            curchar = getchar()  # get next char from source program

        # construct and initialize token
        token = Token(line, column, None, '')

        if curchar.isdigit():            # start of unsigned int?
            token.category = UNSIGNEDINT  # save category of token
            while True:
                token.lexeme += curchar    # append curchar to lexeme
                curchar = getchar()        # get next character
                if not curchar.isdigit():  # break if not a digit
                    break

        elif curchar.isalpha() or curchar == '_':   # start of name?
            while True:
                token.lexeme += curchar    # append curchar to lexeme
                curchar = getchar()        # get next character
                # break if not letter, '_', or digit
                if not (curchar.isalnum() or curchar == '_'):
                    break

            # determine if lexeme is a keyword or name of variable
            if token.lexeme in keywords:
                token.category = keywords[token.lexeme]
            else:
                token.category = NAME

        elif curchar in smalltokens:
            token.category = smalltokens[curchar]      # get category
            token.lexeme = curchar
            curchar = getchar()       # move to first char after the token

        else:
            token.category = ERROR    # invalid token
            token.lexeme = curchar    # save lexeme
            raise RuntimeError('Invalid token')

        tokenslist.append(token)     # append token to tokens list
        if trace:                    # display token if trace is True
            print("%3s %4s  %-14s %s" % (str(token.line),
                                         str(token.column), catnames[token.category], token.lexeme))

        if token.category == EOF:    # finished tokenizing?
            break

# getchar() gets next char from source and adjusts line and column


def getchar():
    global sourceindex, column, line, prevchar, blankline

    # check if starting a new line
    if prevchar == '\n':    # '\n' signals start of a new line
        line += 1            # increment line number
        column = 0           # reset column number
        blankline = True     # initialize blankline

    if sourceindex >= len(source):  # at end of source code?
        column = 1                   # set EOF column to 1
        prevchar = ''                # save current char for next call
        return ''                    # null str signals end of source

    c = source[sourceindex]  # get next char in the source program
    sourceindex += 1        # increment sourceindex to next character
    column += 1             # increment column number
    if not c.isspace():     # if c not whitespace then line not blank
        blankline = False    # indicate line not blank
    prevchar = c            # save current character

    # if at end of blank line, return space in place of '\n'
    if c == '\n' and blankline:
        return ' '
    else:
        return c             # return character to tokenizer()

####################
# parser functions #
####################
# advances to the next token in the list tokens


def advance():
    global token, tokenindex
    tokenindex += 1
    if tokenindex >= len(tokenslist):
        raise RuntimeError('Unexpected end of file')
    token = tokenslist[tokenindex]

# advances if current token is the expected token


def consume(expectedcat):
    if (token.category == expectedcat):
        advance()
    else:
        raise RuntimeError('Expecting ' + catnames[expectedcat])

# top level function of parser


def parser():
    if trace:
        print('------------------------------------------- Program Output')
    advance()
    return program()


def program():
    stmtlist = []
    while token.category in [NAME, PRINT]:
        stmtlist.append(stmt())
    if token.category != EOF:
        raise RuntimeError('Expecting EOF')
    return Node(PROGRAM, stmtlist, None)


def stmt():
    ast = simplestmt()
    consume(NEWLINE)
    return ast


def simplestmt():
    if token.category == NAME:
        return assignmentstmt()
    elif token.category == PRINT:
        return printstmt()
    else:
        raise RuntimeError('Expecting statement')


def assignmentstmt():
    lexeme = token.lexeme
    advance()
    consume(ASSIGNOP)
    node = Node(ASSIGNOP, lexeme, expr())
    return node


def printstmt():
    advance()
    consume(LEFTPAREN)
    expr()
    co_code.append(PRINT_ITEM)
    co_code.append(PRINT_NEWLINE)
    consume(RIGHTPAREN)


def expr():
    left = term()
    while token.category == PLUS:
        advance()
        right = term()
        node = Node(PLUS, left, right)
        left = node
    return left


def term():
    global sign
    sign = 1
    left = factor()
    while token.category == TIMES:
        advance()
        sign = 1
        right = factor()
        node = Node(TIMES, left, right)
        left = node
    return left


def factor():
    global sign
    if token.category == PLUS:
        advance()
        return factor()
    elif token.category == MINUS:
        sign = -sign
        advance()
        return factor()
    elif token.category == UNSIGNEDINT:
        node = Node(INTEGER, sign*int(token.lexeme), None)
        advance()
        return node
    elif token.category == NAME:
        node = Node(NAME, token.lexeme, None)
        advance()
        if sign == -1:
            node = Node(NEGATE, node, None)
        return node
    elif token.category == LEFTPAREN:
        advance()
        savesign = sign
        node = expr()
        if savesign == -1:
            node = Node(NEGATE, node, None)
        consume(RIGHTPAREN)
        return node
    else:
        raise RuntimeError('Expecting factor')

########################
# interpreter #
########################


def interpreter(ast):
    if (ast.left != None):
        for stmt in ast.left:
            if stmt.type == ASSIGNOP:
                symtab[stmt.left] = value(stmt.right)
            elif stmt.type == PRINT:
                print(value(stmt.left))
            else:
                raise RuntimeError('Expecting stmt')


def value(node):
    if node.type == INTEGER:
        return node.left
    elif node.type == NAME:
        return symtab[node.left]
    elif node.type == NEGATE:
        return -value(node.left)
    elif node.type == TIMES:
        return value(node.left) * value(node.right)
    elif node.type == PLUS:
        return value(node.left) + value(node.right)
    else:
        raise RuntimeError('Expecting value')


####################
# start of program #
####################
main()
if grade:
    # display interpreter's source code
    print('------------------------------------------- ' + sys.argv[0])
    print(open(sys.argv[0]).read())
