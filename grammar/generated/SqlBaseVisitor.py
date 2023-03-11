# Generated from SqlBase.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlBaseParser import SqlBaseParser
else:
    from SqlBaseParser import SqlBaseParser

# This class defines a complete generic visitor for a parse tree produced by SqlBaseParser.

class SqlBaseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SqlBaseParser#singleStatement.
    def visitSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#singleExpression.
    def visitSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#singleTableIdentifier.
    def visitSingleTableIdentifier(self, ctx:SqlBaseParser.SingleTableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#singleMultipartIdentifier.
    def visitSingleMultipartIdentifier(self, ctx:SqlBaseParser.SingleMultipartIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#singleFunctionIdentifier.
    def visitSingleFunctionIdentifier(self, ctx:SqlBaseParser.SingleFunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#singleDataType.
    def visitSingleDataType(self, ctx:SqlBaseParser.SingleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#statementDefault.
    def visitStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#dmlStatement.
    def visitDmlStatement(self, ctx:SqlBaseParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#query.
    def visitQuery(self, ctx:SqlBaseParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#namespace.
    def visitNamespace(self, ctx:SqlBaseParser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#ctes.
    def visitCtes(self, ctx:SqlBaseParser.CtesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#namedQuery.
    def visitNamedQuery(self, ctx:SqlBaseParser.NamedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#constantList.
    def visitConstantList(self, ctx:SqlBaseParser.ConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#nestedConstantList.
    def visitNestedConstantList(self, ctx:SqlBaseParser.NestedConstantListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#resource.
    def visitResource(self, ctx:SqlBaseParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#queryOrganization.
    def visitQueryOrganization(self, ctx:SqlBaseParser.QueryOrganizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#queryTermDefault.
    def visitQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#setOperation.
    def visitSetOperation(self, ctx:SqlBaseParser.SetOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def visitQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#fromStmt.
    def visitFromStmt(self, ctx:SqlBaseParser.FromStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#table.
    def visitTable(self, ctx:SqlBaseParser.TableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#subquery.
    def visitSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#sortItem.
    def visitSortItem(self, ctx:SqlBaseParser.SortItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#fromStatement.
    def visitFromStatement(self, ctx:SqlBaseParser.FromStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#fromStatementBody.
    def visitFromStatementBody(self, ctx:SqlBaseParser.FromStatementBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#regularQuerySpecification.
    def visitRegularQuerySpecification(self, ctx:SqlBaseParser.RegularQuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#selectClause.
    def visitSelectClause(self, ctx:SqlBaseParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#assignmentList.
    def visitAssignmentList(self, ctx:SqlBaseParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#assignment.
    def visitAssignment(self, ctx:SqlBaseParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#whereClause.
    def visitWhereClause(self, ctx:SqlBaseParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#havingClause.
    def visitHavingClause(self, ctx:SqlBaseParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#fromClause.
    def visitFromClause(self, ctx:SqlBaseParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#aggregationClause.
    def visitAggregationClause(self, ctx:SqlBaseParser.AggregationClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#groupingSet.
    def visitGroupingSet(self, ctx:SqlBaseParser.GroupingSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#lateralView.
    def visitLateralView(self, ctx:SqlBaseParser.LateralViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#setQuantifier.
    def visitSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#relation.
    def visitRelation(self, ctx:SqlBaseParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#joinRelation.
    def visitJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#joinType.
    def visitJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#joinCriteria.
    def visitJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#identifierList.
    def visitIdentifierList(self, ctx:SqlBaseParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#identifierSeq.
    def visitIdentifierSeq(self, ctx:SqlBaseParser.IdentifierSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#orderedIdentifierList.
    def visitOrderedIdentifierList(self, ctx:SqlBaseParser.OrderedIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#orderedIdentifier.
    def visitOrderedIdentifier(self, ctx:SqlBaseParser.OrderedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#tableName.
    def visitTableName(self, ctx:SqlBaseParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#aliasedQuery.
    def visitAliasedQuery(self, ctx:SqlBaseParser.AliasedQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#aliasedRelation.
    def visitAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#tableValuedFunction.
    def visitTableValuedFunction(self, ctx:SqlBaseParser.TableValuedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#functionTable.
    def visitFunctionTable(self, ctx:SqlBaseParser.FunctionTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#tableAlias.
    def visitTableAlias(self, ctx:SqlBaseParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#multipartIdentifierList.
    def visitMultipartIdentifierList(self, ctx:SqlBaseParser.MultipartIdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#multipartIdentifier.
    def visitMultipartIdentifier(self, ctx:SqlBaseParser.MultipartIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#tableIdentifier.
    def visitTableIdentifier(self, ctx:SqlBaseParser.TableIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#functionIdentifier.
    def visitFunctionIdentifier(self, ctx:SqlBaseParser.FunctionIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#namedExpression.
    def visitNamedExpression(self, ctx:SqlBaseParser.NamedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#namedExpressionSeq.
    def visitNamedExpressionSeq(self, ctx:SqlBaseParser.NamedExpressionSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#expression.
    def visitExpression(self, ctx:SqlBaseParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#logicalNot.
    def visitLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#predicated.
    def visitPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#exists.
    def visitExists(self, ctx:SqlBaseParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#logicalBinary.
    def visitLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#predicate.
    def visitPredicate(self, ctx:SqlBaseParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def visitValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#comparison.
    def visitComparison(self, ctx:SqlBaseParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#arithmeticBinary.
    def visitArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#arithmeticUnary.
    def visitArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#struct.
    def visitStruct(self, ctx:SqlBaseParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#dereference.
    def visitDereference(self, ctx:SqlBaseParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#simpleCase.
    def visitSimpleCase(self, ctx:SqlBaseParser.SimpleCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#columnReference.
    def visitColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#rowConstructor.
    def visitRowConstructor(self, ctx:SqlBaseParser.RowConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#last.
    def visitLast(self, ctx:SqlBaseParser.LastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#star.
    def visitStar(self, ctx:SqlBaseParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#overlay.
    def visitOverlay(self, ctx:SqlBaseParser.OverlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#subscript.
    def visitSubscript(self, ctx:SqlBaseParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#subqueryExpression.
    def visitSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#substring.
    def visitSubstring(self, ctx:SqlBaseParser.SubstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#currentDatetime.
    def visitCurrentDatetime(self, ctx:SqlBaseParser.CurrentDatetimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#cast.
    def visitCast(self, ctx:SqlBaseParser.CastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#constantDefault.
    def visitConstantDefault(self, ctx:SqlBaseParser.ConstantDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#lambda.
    def visitLambda(self, ctx:SqlBaseParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:SqlBaseParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#extract.
    def visitExtract(self, ctx:SqlBaseParser.ExtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#trim.
    def visitTrim(self, ctx:SqlBaseParser.TrimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#functionCall.
    def visitFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#searchedCase.
    def visitSearchedCase(self, ctx:SqlBaseParser.SearchedCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#position.
    def visitPosition(self, ctx:SqlBaseParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#first.
    def visitFirst(self, ctx:SqlBaseParser.FirstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#nullLiteral.
    def visitNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:SqlBaseParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#typeConstructor.
    def visitTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#numericLiteral.
    def visitNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#stringLiteral.
    def visitStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#arithmeticOperator.
    def visitArithmeticOperator(self, ctx:SqlBaseParser.ArithmeticOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#predicateOperator.
    def visitPredicateOperator(self, ctx:SqlBaseParser.PredicateOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#booleanValue.
    def visitBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#interval.
    def visitInterval(self, ctx:SqlBaseParser.IntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#errorCapturingMultiUnitsInterval.
    def visitErrorCapturingMultiUnitsInterval(self, ctx:SqlBaseParser.ErrorCapturingMultiUnitsIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#multiUnitsInterval.
    def visitMultiUnitsInterval(self, ctx:SqlBaseParser.MultiUnitsIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#errorCapturingUnitToUnitInterval.
    def visitErrorCapturingUnitToUnitInterval(self, ctx:SqlBaseParser.ErrorCapturingUnitToUnitIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#unitToUnitInterval.
    def visitUnitToUnitInterval(self, ctx:SqlBaseParser.UnitToUnitIntervalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#intervalValue.
    def visitIntervalValue(self, ctx:SqlBaseParser.IntervalValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#intervalUnit.
    def visitIntervalUnit(self, ctx:SqlBaseParser.IntervalUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#complexDataType.
    def visitComplexDataType(self, ctx:SqlBaseParser.ComplexDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#primitiveDataType.
    def visitPrimitiveDataType(self, ctx:SqlBaseParser.PrimitiveDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#complexColTypeList.
    def visitComplexColTypeList(self, ctx:SqlBaseParser.ComplexColTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#complexColType.
    def visitComplexColType(self, ctx:SqlBaseParser.ComplexColTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#whenClause.
    def visitWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#windowClause.
    def visitWindowClause(self, ctx:SqlBaseParser.WindowClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#namedWindow.
    def visitNamedWindow(self, ctx:SqlBaseParser.NamedWindowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#windowRef.
    def visitWindowRef(self, ctx:SqlBaseParser.WindowRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#windowDef.
    def visitWindowDef(self, ctx:SqlBaseParser.WindowDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#windowFrame.
    def visitWindowFrame(self, ctx:SqlBaseParser.WindowFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#frameBound.
    def visitFrameBound(self, ctx:SqlBaseParser.FrameBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:SqlBaseParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#functionName.
    def visitFunctionName(self, ctx:SqlBaseParser.FunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#qualifiedName.
    def visitQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#errorCapturingIdentifier.
    def visitErrorCapturingIdentifier(self, ctx:SqlBaseParser.ErrorCapturingIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#errorIdent.
    def visitErrorIdent(self, ctx:SqlBaseParser.ErrorIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#realIdent.
    def visitRealIdent(self, ctx:SqlBaseParser.RealIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#identifier.
    def visitIdentifier(self, ctx:SqlBaseParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def visitUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#quotedIdentifierAlternative.
    def visitQuotedIdentifierAlternative(self, ctx:SqlBaseParser.QuotedIdentifierAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#quotedIdentifier.
    def visitQuotedIdentifier(self, ctx:SqlBaseParser.QuotedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#exponentLiteral.
    def visitExponentLiteral(self, ctx:SqlBaseParser.ExponentLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#legacyDecimalLiteral.
    def visitLegacyDecimalLiteral(self, ctx:SqlBaseParser.LegacyDecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#bigIntLiteral.
    def visitBigIntLiteral(self, ctx:SqlBaseParser.BigIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#smallIntLiteral.
    def visitSmallIntLiteral(self, ctx:SqlBaseParser.SmallIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#tinyIntLiteral.
    def visitTinyIntLiteral(self, ctx:SqlBaseParser.TinyIntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#doubleLiteral.
    def visitDoubleLiteral(self, ctx:SqlBaseParser.DoubleLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#bigDecimalLiteral.
    def visitBigDecimalLiteral(self, ctx:SqlBaseParser.BigDecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#ansiNonReserved.
    def visitAnsiNonReserved(self, ctx:SqlBaseParser.AnsiNonReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#strictNonReserved.
    def visitStrictNonReserved(self, ctx:SqlBaseParser.StrictNonReservedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SqlBaseParser#nonReserved.
    def visitNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        return self.visitChildren(ctx)



del SqlBaseParser