## @Inject
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/Inject.html)

Injects code into the target method at the specified position. Must be placed in a [@Mixin](mixin.md) class.

#### Return Type
The method to be injected takes one more argument than the target that depend on the return type of target method - `CallbackInfo` if target returns void or `CallbackInfoReturnable<T>` otherwise - where `T` is the return type.

Example: injecting into `int target( int a, int b )` method
```java
@Inject(method="target(II)I", at=@At("INVOKE"))
private void injected( int a, int b, CallbackInfoReturnable<Integer> info ) {
	// code to be injected into target
}
```

The `at` parameter of the `@Inject` annotation specifies where the code will be injected in the target, learn more about it here: [@At](at.md). But the following table describes a few of the options: 

| Name | Description |
| --- | --- |
| HEAD | Top of the method |
| RETURN | Before every return statement |
| INVOKE | At a method call |
| TAIL | Before the final return statement |

#### Injecting Into Constructors
Will only work for `@At("TAIL")` and `@At("RETURN")`, the return value of constructors is of type `void` so `CallbackInfo` should be used - not `CallbackInfoReturnable<T>`.

Example:
```java
@Inject(method="<init>()V", at=@At("RETURN"))
private void init(CallbackInfo info) {
	// inject into a constructor
}
```

#### Cancellable Injections
The injection can be cancelled when a `cancellable=true` parameter is added to the `@Inject` annotation.

Example:
```java
@Inject(method="target()V", at=@At("INVOKE"), cancellable=true)
private void injected( CallbackInfo info ) {
	if( something ) {
	
		// cancel the taget method, this
		// works similary to calling return in the target
		info.cancel();
		
		// if 'info' is of type 'CallbackInfoReturnable' the
		// method can be canceled with 'info.setReturnValue( value )'
		
	}
}
```

#### Capture Locals
Local variables from the target method can captured by specifying `locals` parameters in the `@Inject` annotation. Remember to select a point after the local is defined.

Example:
```java
@Inject(method="target(II)I", at=@At(value="INVOKE_ASSIGN", ordinal=0), locals=LocalCapture.CAPTURE_FAILSOFT)
private void injected( int a, int b, CallbackInfoReturnable<Integer> info, int sth ) {
	// this code will capture local varible 'sth' from target method
	System.out.print(sth);
}
```

| Name | Description |
| --- | --- |
| `NO_CAPTURE` | The default value, don't capture any locals |
| `CAPTURE_FAILSOFT` | Print a warning and skips the injection if the expected locals don't match with the target |
| `CAPTURE_FAILHARD` | Fail if the calculated locals are different from the expected values |
| `CAPTURE_FAILEXCEPTION` | Throws an exception if the method is called and expected locals don't match with the target |
| `PRINT` | This will print available locals and signatures to the log |

This will result in a following injection:
```patch
int target( int a, int b ) {
	int sth = method(a, b);
+	System.out.print(sth);
}
```
