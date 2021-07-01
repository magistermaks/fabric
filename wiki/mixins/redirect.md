## @Redirect
[Back](mixins.md)

Replaces a method call. Must be placed in a [@Mixin](mixin.md) class.

**Warning:** This way of modifying a method conflicts with every other mod that also applies the same redirect so it shouldn't be used when not absolutely necessary.

Example:
```java
@Redirect(method="target()V", at=@At(value="INVOKE", target="Lnet/example/Example;method(II)I"))
private int redirect(Example self, int x, int y) {
    return x * y;
}
```

```patch
public void target() {
+	int i = redirect(this, 6, 9);
-	int i = this.method(6, 9);
}
```
