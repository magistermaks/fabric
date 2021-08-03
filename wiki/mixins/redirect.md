## @Redirect
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/Redirect.html)

Redirects (replaces) the selected point (a method call, field access, or object construction). Must be placed in a [@Mixin](mixin.md) class.

**Warning:** This way of modifying a method conflicts with every other mod that also applies the same redirect so it shouldn't be used when not absolutely necessary.

When redirecting a static field/method or a constructor use static handler method.
Learn how to select methods/fields/new calls in this article [@At](at.md).

#### Method Redirect
The marked method takes the object on which the call was made as the first argument (or not if the replaced method was static), method args as the subsequent args, and returns the same type as the replaced call.

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

#### Field Redirect
Can either target field write or read. When targeting field write the method must return `void` and take the object on in which the field is located as the first argument (or not if the replaced field was static) and take the value that was intended to be written as the second argument. When targeting field read method must return value of the same type a the redirected field, and take the object on in which the field is located as the first argument (or not if the replaced field was static).

to specify what filed operation exactly to target use the `opcode` @At argument:
| Opcode | Description |
| ------ | ---------- |
| `GETSTATIC` | static field read |
| `PUTSTATIC` | static field write |
| `GETFIELD` | non-static field read |
| `PUTFIELD` | non-static field write |
| Default | target any of the above |

Example: Redirecting non-static field read access
```java
@Redirect(method="target()V", at=@At(value="FIELD", opcode=Opcodes.GETFIELD target="Lnet/example/Example;someField:I"))
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

#### Constructor Redirect
Targets object construction, takes the values passed to the constructor as the arguments.

Example: Constructor redirect
```java
@Redirect(method="target()V", at=@At(value="NEW", target="Lnet/example/Example;<init>(III)Lnet/example/Example;"))
private static Example redirect(int a, int b, int c) {
	return new Example(1, 2, 3);
}
```

Modification:
```patch
public void target() {
+	Example e = redirect(4, 2, 0);
-	Example e = new Example(4, 2, 0);
}
```

#### `instanceof` Redirect
**FIXME** this is untested!

Redirect can also be used to replace the java's `instanceof` check the signature of the handler method is one of:
* `boolean redirect(Object object, Class clazz)` - `instanceof` redirect
* `Class redirect(Object object, Class clazz)` - class redirect

Example: `instanceof` redirect
```java
@Redirect(method="target()V", at=@At(value="CONSTANT", args="classValue=Lpath/to/Example;"))
private static boolean redirect(Object object, Class clazz) {
	return false;
}
```

Modification:
```patch
public void target() {
+	boolean b = redirect(obj, Example.class);
-	boolean b = obj instanceof Example;
}
```
