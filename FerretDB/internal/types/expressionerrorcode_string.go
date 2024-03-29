// Code generated by "stringer -linecomment -type ExpressionErrorCode"; DO NOT EDIT.

package types

import "strconv"

func _() {
	// An "invalid array index" compiler error signifies that the constant values have changed.
	// Re-run the stringer command to generate them again.
	var x [1]struct{}
	_ = x[ErrNotFieldPath-1]
	_ = x[ErrEmptyFieldPath-2]
	_ = x[ErrInvalidFieldPath-3]
	_ = x[ErrUndefinedVariable-4]
	_ = x[ErrEmptyVariable-5]
}

const _ExpressionErrorCode_name = "ErrNotFieldPathErrEmptyFieldPathErrInvalidFieldPathErrUndefinedVariableErrEmptyVariable"

var _ExpressionErrorCode_index = [...]uint8{0, 15, 32, 51, 71, 87}

func (i ExpressionErrorCode) String() string {
	i -= 1
	if i < 0 || i >= ExpressionErrorCode(len(_ExpressionErrorCode_index)-1) {
		return "ExpressionErrorCode(" + strconv.FormatInt(int64(i+1), 10) + ")"
	}
	return _ExpressionErrorCode_name[_ExpressionErrorCode_index[i]:_ExpressionErrorCode_index[i+1]]
}
