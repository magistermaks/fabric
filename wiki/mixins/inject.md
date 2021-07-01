## @Inject
[Back](mixins.md)

Injects code into the target method at the specified position. Must be placed in a [@Mixin](mixin.md) class.

#### Return Type
The method to be injected takes one more argument than the target that depend on the return type of target method - `CallbackInfo` if target returns void or `CallbackInfoReturnable<T>` oterwise where `T` is the return type.

Example: injecting into `int target( int a, int b )` method
```java
@Inject(method="target(II)V", at=@At("INVOKE"))
private void injected( int a, int b, CallbackInfoReturnable<Integer> info ) {
	// code to be injected into target
}
```

The `at` parameter of the `@Inject` adnotation specifies where the code will be injected in the target, learn more about it here: [@At](at.md). But the following table describes a few of the options: 

| Name | Description |
| --- | --- |
| HEAD | Top of the method |
| RETURN | Before every return statement |
| INVOKE | At a method call |
| TAIL |  Before the final return statement  |

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
The injection can be cancelled when a `cancellable=true` paramter is added to the `@Inject` adnotation.

Example:
```java
@Inject(method="target()V", at=@At("INVOKE"), cancellable=true)
private void injected( CallbackInfo info ) {
	if( something ) {
	
		// cancel the taget method, this
		// works similary to calling return in the target
		info.cancel();
		
		// if `info` is of type `CallbackInfoReturnable` the
		// method can be canceled with `info.setReturnValue( value )`
		
	}
}
```

#### Capture Locals

**TODO**
