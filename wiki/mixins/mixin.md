## @Mixin
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
