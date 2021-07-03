## @Unique
[Back](mixins.md)

This annotation ensures that the method and field names never conflict with anything in the target class or with any method or field added to the target class by other mixins. Can be added to the mixin class definition to make every method in that mixin unique. Lean more about it in the **Extending** section of the [@Mixin](mixin.md) article.

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
