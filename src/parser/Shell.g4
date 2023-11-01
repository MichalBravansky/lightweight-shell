grammar Shell;

// Parser rules
commands: command (pipe command)* ;
command: COMMAND arg* (redirection)? ;
pipe: '|';
redirection: ('>' | '>>' | '<') FILE ;
arg: UNQUOTED_ARG | quotedArg | commandArg ;
commandArg: COMMAND ;

// Incorporating complex quote rules
quotedArg: SINGLE_QUOTED_ARG | DOUBLE_QUOTED_ARG | BACKQUOTED_ARG ;

// Lexer rules
COMMAND: [a-zA-Z_][a-zA-Z_0-9]* ;

// Complex quote lexer rules
UNQUOTED_ARG: (~[ ;<>|"'`\n\t])+ ;
SINGLE_QUOTED_ARG: '\'' (~[\n'])+ '\'' ;
DOUBLE_QUOTED_ARG: '"' (BACKQUOTED_ARG | ((~[`\n"]) | '\\"')+)* '"';
BACKQUOTED_ARG: '`' (~[\n`])+ '`' ;

FILE: ~[ |<>]+ ;
WS: [ \t\n\r]+ -> skip ;