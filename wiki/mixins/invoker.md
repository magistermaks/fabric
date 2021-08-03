## @Invoker
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/gen/Invoker.html)

Used for calling private methods and constructors in target classes. has the same name, return value, and arguments as the private method to be invoked. May be placed in a Accessor Mixin - a special mixin defined as interface. Must be placed in a [@Mixin](mixin.md) class. See also: [@Accessor](accessor.md).

The Invoker annotation takes one (optional) argument - the name of the method to access (or the full method signature), if this argument is omitted the name will be taken from the annotated method.

#### Accessor Mixin
Example:
```java
@Mixin(TargetClass.class)
public interface TargetAccessor {

	// This example shows an invoker for 
	// method 'private void method()'

	@Invoker("method")
	void method();
	// calling this will invoke 'TargetClass.method()'

}
```

Using the invoker:
```java
((TargetAccessor) targetClassObject).method();
```

#### Classical Mixin
Example:
```java
@Mixin(TargetClass.class)
public class TargetMixin {
	
	// This example shows an invoker for 
	// method 'private void method()'
	
	@Invoker("method")
	void method() {
		// this is an unreachable statement
		// but must be used if the method is not abstract
		throw new AssertionError(); 
	}

}
```

Note that an invoker defined like that may not be accessed from outside the mixin class without [The Duck Interface](mixin.md).

