## @Final
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Final.html)

Should be added to along with [@Shadow](shadow.md) if the shadowed field or method is final in the target class. The annotated filed or method **shouldn't** be than marked with java's `final` keyword. To modify shadowed final field marked with use [@Mutable](mutable.md).

Example:
```java
@Mixin(TargetClass.class)
public abstract class TargetMixin {

	@Final
	@Shadow
	private int field; 
	// allows using final 'field' from TargetClass
	// note the absence of 'final' keyword in the definition.

}
```
