## @Redirect
[Back](mixins.md)

Redirects (replaces) the selected point (a method call, field access, or object construction). Must be placed in a [@Mixin](mixin.md) class.

The marked method takes the object on which the call was made as the first argument and method args as the subsequent args, and returns the same type as the replaced call. When a field is being redirected only the first argument is present, while the return type is the type of the field.

**Warning:** This way of modifying a method conflicts with every other mod that also applies the same redirect so it shouldn't be used when not absolutely necessary.

Learn how to select methods/fields in this article [@At](at.md).

Example: Redirecting method call
```java
@Redirect(method="target()V", at=@At(value="INVOKE", target="Lnet/example/Example;method(II)I"))
private int redirect(Example self, int x, int y) {
    return x * y;
}
```

Modification:
```patch
public void target() {
+	int i = redirect(someObject, 6, 9);
-	int i = someObject.method(6, 9);
}
```

Example: Redirecting field access
```java
@Redirect(method="target()V", at=@At(value = "FIELD", target="Lnet/example/Example;someField:I"))
private int redirect(Example self) {
	return 300;
}
```

Modification:
```patch
public void target() {
+	int i = redirect(someObject);
-	int i = someObject.someField;
}
```
