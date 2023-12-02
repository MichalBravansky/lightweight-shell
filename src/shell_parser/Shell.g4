grammar Shell;

// Parser rules
sequence : commands (sequenceOp commands)* sequenceOp? EOF ;
commands : command (pipe command)* ;
command : WS* (redirection WS*)* argument (WS* atom)* WS* ;
commandSubstitution : BACKQUOTED_ARG ;
sequenceOp : SEQUENCE_OP ;
pipe : '|';
args : argument* ;
atom : redirection | argument ;
redirection : redirectionType WS* argument ;
argument : ( quotedArg | UNQUOTED_ARG )+ ;
quotedArg : SINGLE_QUOTED_ARG | DOUBLE_QUOTED_ARG | BACKQUOTED_ARG ;

// Lexer rules
SEQUENCE_OP: ';';

// Complex quote lexer rules
redirectionType: REDIRECTION_OVERWRITE | REDIRECTION_APPEND | REDIRECTION_READ;

REDIRECTION_OVERWRITE: '>';
REDIRECTION_APPEND: '>>';
REDIRECTION_READ: '<';

UNQUOTED_ARG : (~[ '"`|;<>\n\t])+ ;
SINGLE_QUOTED_ARG : '\'' (~['\n])+ '\'' ;
DOUBLE_QUOTED_ARG : '"' (((~[`"\n]) | '\\"')+ | BACKQUOTED_ARG)* '"';
BACKQUOTED_ARG : '`' (~[`\n])+ '`' ;

WS : [ \t]+ ;