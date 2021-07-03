## @Accessor
[Back](mixins.md)

Used for setting or getting a private field in a target class. Must be placed in a Accessor Mixin - special mixin defined as interface. See also: [@Invoker](invoker.md).

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
