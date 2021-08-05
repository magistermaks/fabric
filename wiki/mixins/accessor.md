## @Accessor
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/gen/Accessor.html) 

Used for setting or getting a private field in a target class. May be placed in a Accessor Mixin - a special mixin defined as interface. Must be placed in a [@Mixin](mixin.md) class. See also: [@Invoker](invoker.md).

#### Accessor Mixin
Example:
```java
@Mixin(TargetClass.class)
public interface TargetAccessor {
	
	// This example shows an accessor for 
	// field 'private int field;' defined in 'TargetClass'
	
	@Accessor("field")
	int getField();

	@Accessor("field")
	void setField(int value);

}
```

Using the accessor:
```java
((TargetAccessor) targetClassObject).getField(); // get
((TargetAccessor) targetClassObject).setField(value); // set
```

#### Classical Mixin
Example:
```java
@Mixin(TargetClass.class)
public class TargetMixin {
	
	// This example shows an accessor for 
	// field 'private int field;' defined in 'TargetClass'
	
	@Accessor("field")
	int getField();

	@Accessor("field")
	void setField(int value);

}
```

Note that an accessor defined like that may not be accessed from outside the mixin class without [The Duck Interface](mixin.md).

