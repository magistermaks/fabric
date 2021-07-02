## @ModifyVariable
[Back](mixins.md)

Modifies local variable at the selected point. Marked method takes a single argument - the old value and returns the new value. Must be placed in a [@Mixin](mixin.md) class.

Example:
```java
@ModifyVariable(method="target()V", at=@At(value="INVOKE_ASSIGN", target="Lnet/example/Example;foo()I"))
private int modify( int in ) {
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

If the local variable to be modified cannot be deduced by the mixin (for example when there are multiple locals of the same type) the `index` propery can be used to specify exacly which variable should be modified. The index is one-based and includes method arguments.
