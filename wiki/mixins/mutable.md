## @Mutable
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Mutable.html)

It allows for modifying a shadowed final field. See: [@Shadow](shadow.md), [@Final](final.md) for reference.

Example:
```java
@Mixin(TargetClass.class)
public abstract class TargetMixin {

	@Final
	@Mutable
	@Shadow
	private int field; 
	// allows using and modifying final 'field' from TargetClass
	// note the absence of 'final' keyword in the definition.

}
```
