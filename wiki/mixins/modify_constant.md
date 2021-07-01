## @ModifyConstant
[Back](mixins.md)

Allows to replace a constant value like - `20`, `true`, `PlayerClass`, `40.0f`, `"Hello"`. Marked methods returns new value of the conststant and takes the old one as an argument. Must be placed in a [@Mixin](mixin.md) class.

**Warning:** bool values should be modified using the `int` type, where `true` is `1`, and `false` is `0`

Example: modify every `20` to `200` in method `target()`
```java
@ModifyConstant(method="target()V", constant = @Constant(intValue=20))
private static int modify( int oldValue ) {
	return 200;
}
```

the full usage is documented here: [@Constant](constant.md).

#### Other Properties
By default mixin will ignore if the modeficatiation actually applies or not, those options can be used to force the mixin to throw an exception if the number of injection is not within a specified range.

* **require** - Minimum required number of injections, default: -1 (ignore)
* **allow** - Maximum allowed number of injections, default: -1 (ignore)


