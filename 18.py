INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = "INTEGER", "PLUS", "MINUS", "*", "/", "(", ")", "EOF"


#Followed the tutorial at https://ruslanspivak.com/lsbasi-part1/ to write an interpreter.  Fun!

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token(%s, %s)" % (self.type, repr(self.value))

class Lexer():
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")
            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")
            if self.current_char == "*":
                self.advance()
                return Token(MUL, "*")
            if self.current_char == "/":
                self.advance()
                return Token(DIV, "/")
            if self.current_char == "(":
                self.advance()
                return Token(LPAREN, "(")
            if self.current_char == ")":
                self.advance()
                return Token(RPAREN, ")")
            
            self.error()
        return Token(EOF, None)

class Interpreter():
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self): #precedence 2
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self): #precedence 1
        result = self.factor()
        return result

    def expr(self): #precedence 0
        result = self.term()

        while self.current_token.type in (PLUS, MINUS, MUL, DIV):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
            elif token.type == MUL:
                self.eat(MUL)
                result *= self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result //= self.term()
        return result

#Addition has higher precedence than multiplication
class Interpreter2(Interpreter):
    def term(self): #precedence 1
        result = self.factor()
        while self.current_token.type in (PLUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.factor()
        return result

    def expr(self): #precendence 0
        result = self.term()

        while self.current_token.type in (MINUS, MUL, DIV):
            token = self.current_token
            if token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
            elif token.type == MUL:
                self.eat(MUL)
                result *= self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result //= self.term()
        return result


l = Lexer("1 + 2 * 3 + 4 * 5 + 6")
i = Interpreter(l)
print(i.expr())

l = Lexer("1 + 2 * 3 + 4 * 5 + 6")
i = Interpreter2(l)
print(i.expr())


input = []
with open("18.txt") as f:
    input = [x.strip() for x in f.readlines()]

def part1():
    result = 0
    for i in input:
        lex = Lexer(i)
        interp = Interpreter(lex)
        r = interp.expr()
        result += r
    return result

def part2():
    result = 0
    for i in input:
        lex = Lexer(i)
        interp = Interpreter2(lex)
        r = interp.expr()
        result += r
    return result

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
