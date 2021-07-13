## @Shadow
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Shadow.html)

Allows accessing method or field from the target class, to used it, mark field or method of the same name, type, and access specifier.

Example:
```java
@Mixin(TargetClass.class)
public abstract class TargetMixin {

	@Shadow
	private int field; 
	// allows using 'field' from TargetClass

	@Shadow
	public abstract void method(); 
	// allows calling 'method' from TargetClass
	// as this method must be abstract, the mixin class must be also be abstract
	
}
```

When shadowing a final field or method use [@Final](final.md) annotation.
