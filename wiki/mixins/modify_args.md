## @ModifyArgs
[Back](mixins.md)

Modifies multiple argument in method invocation. Select the target method with [@At](at.md) annotation. Marked method takes a single `Args` argument and returns `void`. After the `Args` argument it can also optionally take target method arguments. Must be placed in a [@Mixin](mixin.md) class. To modify a single argument see: [@ModifyArg](modify_arg.md).

Example:
```java
@ModifyArgs(target="target(F)V", at=@At(value="INVOKE", target="Lnet/example/Example;method(III)V"))
private void modifyArgs(Args args, float f) {
	// the 'float f' is an optional target's ('void target(float f)') method argument.
	
	args.set(0, 42);
	args.set(1, args.get(1) * 2);
	// third argument is left unmodified
}
```
