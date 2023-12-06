grammar Shell;

// Parser rules
shell: command | pipe | sequence EOF ;
sequence : (command | pipe) ';' (command | pipe | sequence)? EOF ;
pipe : command '|' command | command '|' pipe;
command : WS* (redirection WS*)* argument (WS* atom)* WS* ;
arguments : (WS* argument)* WS* ;

atom : redirection | argument ;

redirection : redirectionType WS* argument ;

argument : ( quotedArg | UNQUOTED_ARG )+ ;
quotedArg : SINGLE_QUOTED_ARG | DOUBLE_QUOTED_ARG | BACKQUOTED_ARG ;

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