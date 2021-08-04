## @Constant
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/Constant.html)

Used to select a constant, for usage see: [@ModifyConstant](modify_constant.md).

As comparisons with zero and false values are optimized by the compiler special enums to match them are provided:

**Note:** All those enums expect `x` to be on the left-hand side, if that is not the case use the inverse.

| Name | Description |
| --- | --- |
| LESS_THAN_ZERO | `x < 0` |
| LESS_THAN_OR_EQUAL_TO_ZERO | `x <= 0` |
| GREATER_THAN_OR_EQUAL_TO_ZERO | `x >= 0` |
| GREATER_THAN_ZERO | `x > 0` |

To match other constant values use those selectors:

| Name | Description |
| --- | --- |
| `@Constant(intValue=value)` | Select integer `value` |
| `@Constant(floatValue=value)` | Select float `value` |
| `@Constant(longValue=value)` | Select long `value` |
| `@Constant(doubleValue=value)` | Select double `value` |
| `@Constant(stringValue=value)` | Select string `value` |
| `@Constant(classValue=value)` | Select class `value` |
| `@Constant(nullValue=true)` | Select `null` |

`ordinal` property can be used to specify the index of the desired constant. default value is -1, allowing multiple constants to be selected.

Learn how to select a constant value with the @At selector here: [@At](at.md).
