## @ModifyConstant
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/ModifyConstant.html)

Allows to replace a constant value like - `20`, `true`, `PlayerClass`, `40.0f`, `"Hello"`. The annotated method returns new value of the constant and takes the old one as an argument. It can also optionally take the target method arguments by adding them at the end of the argument list. Must be placed in a [@Mixin](mixin.md) class.

**Warning:** `boolean` values should be modified using the `int` type, where `true` is `1`, and `false` is `0`

Example: modify every `20` to `200` in method `target()`
```java
@ModifyConstant(method="target(III)V", constant=@Constant(intValue=20))
private static int modify( int oldValue, int a, int b, int c ) {
	// a, b, c are the args of the 'void target(int a, int b, int c)'
	return 200;
}
```

Learn more about the constant annotation: [@Constant](constant.md).

#### Other Properties
By default mixin will ignore if the modification actually applies or not, those options can be used to force the mixin to throw an exception if the number of injection is not within a specified range.

* **require** - Minimum required number of injections, default: -1 (ignore)
* **allow** - Maximum allowed number of injections, default: -1 (ignore)


