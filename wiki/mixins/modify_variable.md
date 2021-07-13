## @ModifyVariable
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/ModifyVariable.html)

Modifies local variable at the selected point. The annotated takes a single argument - the old value and returns the new value. It can also optionally take the target method arguments by adding them at the end of the argument list. Must be placed in a [@Mixin](mixin.md) class.

Example:
```java
@ModifyVariable(method="target()V", at=@At(value="INVOKE_ASSIGN", target="Lnet/example/Example;foo()I"))
private int modify( int old ) {
	return 42;
}
```

Modification:
```patch
private void target() {
	int i = foo();
+	i = modify(i);
}
```

If the local variable to be modified cannot be deduced by the mixin (for example when there are multiple locals of the same type) the `index` property can be used to specify exactly which variable should be modified. The index is one-based and includes method arguments.
