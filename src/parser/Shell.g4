grammar Shell;

// Parser rules
sequence: commands (sequenceOp commands)* sequenceOp?;
commands: command (pipe command)* ;
command: COMMAND arg* (redirection)? ;
sequenceOp: SEQUENCE_OP ;
pipe: '|';
redirection: redirectionType arg ;
arg: UNQUOTED_ARG | quotedArg | commandArg ;
commandArg: COMMAND ;

// Incorporating complex quote rules
quotedArg: SINGLE_QUOTED_ARG | DOUBLE_QUOTED_ARG | BACKQUOTED_ARG ;

// Lexer rules
COMMAND: [a-zA-Z_][a-zA-Z_0-9]* ;
SEQUENCE_OP: ';';

// Complex quote lexer rules
redirectionType: (REDIRECTION_OVERWRITE | REDIRECTION_APPEND | REDIRECTION_READ);

REDIRECTION_OVERWRITE: '>';
REDIRECTION_APPEND: '>>';
REDIRECTION_READ: '<';

UNQUOTED_ARG: (~[ ;<>|"'`\n\t])+ ;
SINGLE_QUOTED_ARG: '\'' (~[\n'])+ '\'' ;
DOUBLE_QUOTED_ARG: '"' (BACKQUOTED_ARG | ((~[`\n"]) | '\\"')+)* '"';
BACKQUOTED_ARG: '`' (~[\n`])+ '`' ;


FILE: ~[ ;|<>]+ ;
WS: [ \t\n\r]+ -> skip ;

