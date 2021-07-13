## @Pseudo
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Pseudo.html)

When you want to mixin into a class that may not exist at runtime (e.g. into other mods) this annotation can be added to a mixin class, then no error would be raised if the target class is not found. 

**Warning:** Don't use `@Pseudo` on mixins that target obfuscated classes (e.g. Minecraft's code) if done incorrectly that will cause problems that are only visible outside of development environment.

Example:
```java
@Pseudo
@Mixin(TargetClass.class)
class MixinClass {

	// ...

}
```
