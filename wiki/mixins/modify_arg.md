## @ModifyArg
[Back](mixins.md)

Modifies argument in method invocation. Learn how to select a method with [@At](at.md) annotation. The `index` property can be used to specify zero-base index of the argument to be modified (if the target method has more than one argument). The modification method takes either only one argument - the old value, or all arguments given to target method. Must be placed in a [@Mixin](mixin.md) class. To modify multiple arguments see: [@ModifyArgs](modify_args.md).

Example:
```java
@ModifyArg(method="target()V", at=@At(value="INVOKE", target="Lnet/example/Example;method(III)V"), index=0)
private int modify( int a /* or: int a, int b, int c */ ) {
	return 42;
}
```

Modification:
```patch
private void target() {
+	int a = 1;
+	int b = 2;
+	int c = 3;
+	a = modify(a);
+	method(a, b, c);
-	method(1, 2, 3);
}
```
