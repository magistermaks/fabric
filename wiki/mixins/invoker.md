## @Invoker
[Back](mixins.md)

Used for calling private methods and constructors in target classes. has the same name, return value, and arguments as the private method to be invoked. Must be placed in a Accessor Mixin - special mixin defined as interface. See also: [@Accessor](accessor.md).

Example:
```java
@Mixin(TargetClass.class)
public interface TargetAccessor {

	@Invoker
	void method();
	// calling this will invoke 'TargetClass.method()'

}
```

Using the invoker:
```java
((TargetAccessor) targetClassObject).method();
```
