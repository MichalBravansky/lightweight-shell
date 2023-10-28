grammar Shell;

// Parsing rules
commandLine: pipeline EOF;
pipeline: simpleCommand (PIPE simpleCommand)* ;
simpleCommand: command (redirection)* ;
command: COMMAND (ARGUMENT)* ;
redirection: (REDIRECT_OUT | APPEND_OUT | REDIRECT_IN) ARGUMENT ;

// Lexical rules
COMMAND: [a-zA-Z]+ ;
ARGUMENT: [^\\s]+ ;
PIPE: '|' ;
REDIRECT_OUT: '>' ;
APPEND_OUT: '>>' ;
REDIRECT_IN: '<' ;
WS: [ \t\r\n]+ -> skip ;  // skip whitespaces