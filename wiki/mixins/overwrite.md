## @Overwrite
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/Overwrite.html)

Replaces a method of the same name, arguments and return type. Must be placed in a [@Mixin](mixin.md) class.

**Warning:** This way of modifying a method conflicts with every other mod also modifying the same method so it shouldn't be used when not absolutely necessary.

Example:
```java
@Overwrite
public void target( int arg ) {
	// this will replace 'target' method in the target class
}
```

