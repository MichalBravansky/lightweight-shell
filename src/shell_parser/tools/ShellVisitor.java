// Generated from Shell.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ShellParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ShellVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ShellParser#shell}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShell(ShellParser.ShellContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#sequence}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSequence(ShellParser.SequenceContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#pipe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPipe(ShellParser.PipeContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#command}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommand(ShellParser.CommandContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#arguments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArguments(ShellParser.ArgumentsContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(ShellParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#redirection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirection(ShellParser.RedirectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(ShellParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#quotedArg}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitQuotedArg(ShellParser.QuotedArgContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShellParser#redirectionType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRedirectionType(ShellParser.RedirectionTypeContext ctx);
}