## @Constant
[Back](mixins.md)

Used to select a constant, for usage see: [@ModifyConstant](modify_constant.md)

As comparisons with zero and false values are optimized by the compiler special enums to match them are provided:

**Note:** All those enums expect `x` to be on the right-hand side, if that is not the case use the inverse.

| Name | Description |
| --- | --- |
| LESS_THAN_ZERO | `x < 0` |
| LESS_THAN_OR_EQUAL_TO_ZERO | `x <= 0` |
| GREATER_THAN_OR_EQUAL_TO_ZERO | `x >= 0` |
| GREATER_THAN_ZERO | `x > 0` |

To match other constant values use those selectors:

| Name | Description |
| --- | --- |
| @Constant(intValue=value) | Select integer `value` |
| @Constant(floatValue=value) | Select float `value` |
| @Constant(longValue=value) | Select long `value` |
| @Constant(doubleValue=value) | Select double `value` |
| @Constant(stringValue=value) | Select string `value` |
| @Constant(classValue=value) | Select class `value` |
| @Constant(nullValue=true) | Select null |
