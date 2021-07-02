## @Pseudo
[Back](mixins.md)

When you want to mixin into a class that may not exist at runtime (e.g. into other mods) this annotation can be added to a mixin class, then no error would be raied if the target class is not found. 

**Warning:** Don't use `@Pseudo` on mixins that target obfuscated classes (e.g. Minecraft's code) if done incorrectly will cause problems that are only manifest themselves outside of development environment.

Example:
```java
@Pseudo
@Mixin(TargetClass.class)
class MixinClass {

	// ...

}
```
