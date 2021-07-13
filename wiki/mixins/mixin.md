## @Mixin
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Mixin.html)

The mixin class must be marked by a `@Mixin` annotation ...

```java
@Mixin(ClassToBeMixedInto.class)
class MixinClass {
	
}
```

... and placed in `modid.mixin.json`, in 'mixin' if the mixin should applied on both server and client, or in 'server'/'client' to apply the mixin on only one side. "package" should point to the package where the mixins are located.

```patch
{
	"required": true,
+	"package": "net.example.mixin",
	"minVersion": "0.8",
	"compatibilityLevel": "JAVA_16",
	"mixins": [
+		"MixinClass"
	],
	"client": [
		
	],
	"server": [

	]
	"injectors": {
		"defaultRequire": 1
	}
}
```

If you are trying to mixin into private class, or a class that doesn't exist at the compile time use `target` property to pass the class as a string: `@Mixin(target = "net/example/Example")`. _If the target class may be missing at the runtime remember to use [@Pseudo](pseudo.md) annotation._

#### Using `this`
To reference the target class with `this` and keep the compiler happy, we have to cast the mixin's `this` to a object (as the compiler wrongly thinks that `this` refers to `MixinClass`) and then to `TargetClass`.

```java
@Mixix(TargetClass.class) {

	private method() {
		((TargetClass) (Object) this).somePublicMethodOfTargetClass();
	}

}
```

#### Extending
Let's imagine a situation where the target class `TargetClass` extends a `SomeClass` class, and you want to 'inject' an over**ride** of one of the non-final methods from `SomeClass` into `TargetClass`, how could you accomplish this?

```java
class SomeClass {
	public void method() {
		System.out.print("foo!");
	}
}

class TargetClass extends SomeClass {
	// empty
}

@Mixin(TargetClass.class)
class TargetClassMixin {
	public void method() {
		System.out.print("foo!");
	}
}
```

This example shows exactly that, mixins inject **all** methods placed in their body into the target class, you can even make your mixin abstract and extend the `SomeClass` so that you can use the java's `@Override` annotation.

But sometime this can cause problems, what if you just want to write some private helper method or field that is used only by the code in you mixin and you don't want it being injected into the target class? (it could then conflict with a similar helper method injected there by some other mod) You can use the [@Unique](unique.md) annotation, it won't stop them being inject, but it ensures that the method names never conflict.

If you want to actually add a public method to the target class that would be accessible from the outside of the mixin class, don't use [@Unique](unique.md) but simply add a prefix to the method or field name e.g. `mymod_someMethod()` and use the Duck Interface to access it.

#### The 'Duck' Interface
Is an interface that the mixin implements and that is used as a proxy to access methods added to the target class by a mixin.

Example:
```java
interface TargetMixinDuck {
	public example_addedMethod();
}

@Mixin(TargetClass.class) 
class TargetMixin implements TargetMixinDuck {

	// implements TargetMixinDuck in the eyes of the compiler
	public example_addedMethod() {
		// method added to the target class
	}

}

// Usage:
((TargetMixinDuck) targetClassObject).example_addedMethod(); 
// call 'example_addedMethod' method added to 'TargetClass'
```

#### Inheritance
Mixins can also be used to "inject" some class into target class' inheritance tree.

Example:
```java
class TargetClass {
	// empty
}

@Mixin(TargetClass.class)
class TargetClassMixin implements SomeInterface {
	// implement all methods from SomeInterface 
}
```

After the presented mixin is applied `TargetClass` will implement `SomeInterface` so that `targetClass instanceof SomeInterface == true`.

#### Priority
@Mixin annotation can take additional parameter - `priority` which dictates how mixin should apply the changes if multiple mixins are applied to the same class. The default value of `priority` is `1000`, **lower value** indicates **higher** priority.

This example uses the `inject` and `at` annotation, learn more here: [@Inject](inject.md), [@At](at.md).

Example:
```java
@Mixin(value=TargetClass.class, priority=1000 /* default value */)
class MixinA {

	@Inject(method="target()V", at=@At("HEAD"))
	public void injection(CallbackInfo info) {
		System.out.println("MixinA");
	}
}
```

```java
@Mixin(value=TargetClass.class, priority=500)
class MixinB {

	@Inject(method="target()V", at=@At("HEAD"))
	public void injection(CallbackInfo info) {
		System.out.println("MixinB");
	}
}
```

Modification:
```patch
class TargetClass {

	public void target() {
+		System.out.println("MixinB");
+		System.out.println("MixinA");
	}

}
```
