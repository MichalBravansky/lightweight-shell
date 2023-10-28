grammar Shell;

// Parser rules
commands: commandLine ;
commandLine: command (pipe command)* ;
command: COMMAND arg* (redirection)? ;
pipe: '|';
redirection: ('>' | '>>' | '<') FILE ;
arg: ARG | QUOTED_ARG | commandArg ;
commandArg: COMMAND ;

// Lexer rules
COMMAND: [a-zA-Z_][a-zA-Z_0-9]* ;
ARG: ~[ |<>"]+ ;
QUOTED_ARG: '"' (~["])* '"' ;
FILE: ~[ |<>]+ ;
WS: [ \t\n\r]+ -> skip ;