// Generated from Shell.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShellParser}.
 */
public interface ShellListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShellParser#shell}.
	 * @param ctx the parse tree
	 */
	void enterShell(ShellParser.ShellContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#shell}.
	 * @param ctx the parse tree
	 */
	void exitShell(ShellParser.ShellContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#sequence}.
	 * @param ctx the parse tree
	 */
	void enterSequence(ShellParser.SequenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#sequence}.
	 * @param ctx the parse tree
	 */
	void exitSequence(ShellParser.SequenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void enterPipe(ShellParser.PipeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#pipe}.
	 * @param ctx the parse tree
	 */
	void exitPipe(ShellParser.PipeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#command}.
	 * @param ctx the parse tree
	 */
	void enterCommand(ShellParser.CommandContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#command}.
	 * @param ctx the parse tree
	 */
	void exitCommand(ShellParser.CommandContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(ShellParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(ShellParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(ShellParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(ShellParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void enterRedirection(ShellParser.RedirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#redirection}.
	 * @param ctx the parse tree
	 */
	void exitRedirection(ShellParser.RedirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(ShellParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(ShellParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#quotedArg}.
	 * @param ctx the parse tree
	 */
	void enterQuotedArg(ShellParser.QuotedArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#quotedArg}.
	 * @param ctx the parse tree
	 */
	void exitQuotedArg(ShellParser.QuotedArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShellParser#redirectionType}.
	 * @param ctx the parse tree
	 */
	void enterRedirectionType(ShellParser.RedirectionTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShellParser#redirectionType}.
	 * @param ctx the parse tree
	 */
	void exitRedirectionType(ShellParser.RedirectionTypeContext ctx);
}