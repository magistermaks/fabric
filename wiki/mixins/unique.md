## @Unique
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Unique.html)

This annotation ensures that the method and field names never conflict with anything in the target class or with any method or field added to the target class by other mixins. Can be added to the mixin class definition to make every method in that mixin unique. Lean more about it in the **Extending** section of the [@Mixin](mixin.md) article. Don't use on non-private methods or fields.

If you want to actually add a public method to the target class that would be accessible from the outside of the mixin class, don't use [@Unique](unique.md) but simply add a prefix to the method or field name e.g. `mymod_someMethod()` and use the Duck Interface to access it. Learn more about it in the [@Mixin](mixin.md) article.

Example:
```java
@Mixin(TargetClass.class)
class TargetMixin {

	@Unique
	private void method(int i) {
		// some method used by the mixin
	}

}
```
