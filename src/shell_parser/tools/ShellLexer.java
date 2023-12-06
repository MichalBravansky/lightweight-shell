// Generated from Shell.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ShellLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, REDIRECTION_OVERWRITE=3, REDIRECTION_APPEND=4, REDIRECTION_READ=5, 
		UNQUOTED_ARG=6, SINGLE_QUOTED_ARG=7, DOUBLE_QUOTED_ARG=8, BACKQUOTED_ARG=9, 
		WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "REDIRECTION_OVERWRITE", "REDIRECTION_APPEND", "REDIRECTION_READ", 
			"UNQUOTED_ARG", "SINGLE_QUOTED_ARG", "DOUBLE_QUOTED_ARG", "BACKQUOTED_ARG", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'|'", "'>'", "'>>'", "'<'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "REDIRECTION_OVERWRITE", "REDIRECTION_APPEND", "REDIRECTION_READ", 
			"UNQUOTED_ARG", "SINGLE_QUOTED_ARG", "DOUBLE_QUOTED_ARG", "BACKQUOTED_ARG", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public ShellLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Shell.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\nJ\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0004\u0005\"\b\u0005\u000b"+
		"\u0005\f\u0005#\u0001\u0006\u0001\u0006\u0004\u0006(\b\u0006\u000b\u0006"+
		"\f\u0006)\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0004\u00072\b\u0007\u000b\u0007\f\u00073\u0001\u0007\u0005"+
		"\u00077\b\u0007\n\u0007\f\u0007:\t\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0004\b@\b\b\u000b\b\f\bA\u0001\b\u0001\b\u0001\t\u0004\tG"+
		"\b\t\u000b\t\f\tH\u0000\u0000\n\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0001\u0000"+
		"\u0005\b\u0000\t\n  \"\"\'\';<>>``||\u0002\u0000\n\n\'\'\u0003\u0000\n"+
		"\n\"\"``\u0002\u0000\n\n``\u0002\u0000\t\t  Q\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0001\u0015\u0001\u0000\u0000\u0000"+
		"\u0003\u0017\u0001\u0000\u0000\u0000\u0005\u0019\u0001\u0000\u0000\u0000"+
		"\u0007\u001b\u0001\u0000\u0000\u0000\t\u001e\u0001\u0000\u0000\u0000\u000b"+
		"!\u0001\u0000\u0000\u0000\r%\u0001\u0000\u0000\u0000\u000f-\u0001\u0000"+
		"\u0000\u0000\u0011=\u0001\u0000\u0000\u0000\u0013F\u0001\u0000\u0000\u0000"+
		"\u0015\u0016\u0005;\u0000\u0000\u0016\u0002\u0001\u0000\u0000\u0000\u0017"+
		"\u0018\u0005|\u0000\u0000\u0018\u0004\u0001\u0000\u0000\u0000\u0019\u001a"+
		"\u0005>\u0000\u0000\u001a\u0006\u0001\u0000\u0000\u0000\u001b\u001c\u0005"+
		">\u0000\u0000\u001c\u001d\u0005>\u0000\u0000\u001d\b\u0001\u0000\u0000"+
		"\u0000\u001e\u001f\u0005<\u0000\u0000\u001f\n\u0001\u0000\u0000\u0000"+
		" \"\b\u0000\u0000\u0000! \u0001\u0000\u0000\u0000\"#\u0001\u0000\u0000"+
		"\u0000#!\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\f\u0001\u0000"+
		"\u0000\u0000%\'\u0005\'\u0000\u0000&(\b\u0001\u0000\u0000\'&\u0001\u0000"+
		"\u0000\u0000()\u0001\u0000\u0000\u0000)\'\u0001\u0000\u0000\u0000)*\u0001"+
		"\u0000\u0000\u0000*+\u0001\u0000\u0000\u0000+,\u0005\'\u0000\u0000,\u000e"+
		"\u0001\u0000\u0000\u0000-8\u0005\"\u0000\u0000.2\b\u0002\u0000\u0000/"+
		"0\u0005\\\u0000\u000002\u0005\"\u0000\u00001.\u0001\u0000\u0000\u0000"+
		"1/\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000031\u0001\u0000\u0000"+
		"\u000034\u0001\u0000\u0000\u000047\u0001\u0000\u0000\u000057\u0003\u0011"+
		"\b\u000061\u0001\u0000\u0000\u000065\u0001\u0000\u0000\u00007:\u0001\u0000"+
		"\u0000\u000086\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009;\u0001"+
		"\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000;<\u0005\"\u0000\u0000<\u0010"+
		"\u0001\u0000\u0000\u0000=?\u0005`\u0000\u0000>@\b\u0003\u0000\u0000?>"+
		"\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A?\u0001\u0000\u0000"+
		"\u0000AB\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CD\u0005`\u0000"+
		"\u0000D\u0012\u0001\u0000\u0000\u0000EG\u0007\u0004\u0000\u0000FE\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000"+
		"HI\u0001\u0000\u0000\u0000I\u0014\u0001\u0000\u0000\u0000\t\u0000#)13"+
		"68AH\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}