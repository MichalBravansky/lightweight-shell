import antlr4
from ShellLexer import ShellLexer
from ShellParser import ShellParser
#from ShellVisitorImpl import ShellVisitorImpl

def main():
    while True:
        try:
            user_input = input("shell> ")
            if user_input in ["exit", "quit"]:
                break
            input_stream = antlr4.InputStream(user_input)
            lexer = ShellLexer(input_stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = ShellParser(token_stream)
            tree = parser.commandLine()
            print(tree)
            #visitor = ShellVisitorImpl()
            #visitor.visit(tree)
        except KeyboardInterrupt:
            print()  # Print a newline before exiting
        except EOFError:
            break  # Exit on Ctrl-D
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()