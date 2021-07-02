## @Mixin
[Back](mixins.md)

The mixin class must be marked by a `@Mixin` adnotation ...

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

#### Priority
@Mixin adnotation can take aditional parameter - `priority` which dictates how mixin should apply the changes if multiple mixins are applied to the same class. The defult value of `priority` is `1000`, **lower value** indicates **higher** priority.

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
