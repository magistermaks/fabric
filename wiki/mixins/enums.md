## Modifying Enums
[Back](mixins.md)

This article shows how to use mixins to modify enum classes, all shown modifications will target this example enum:
```java
enum TargetEnum {
	RED(255, 0, 0),
	GREEN(0, 255, 0),
	BLUE(0, 0, 255);

	public final byte r, g, b;
	
	TargetEnum(int r, int g, int b) {
		this.r = (byte) r;
		this.g = (byte) g;
		this.b = (byte) b;
	}
}
```

#### Modify Values
**TODO**

#### Adding Values
To add a value to a mixin use a [@Inject](inject.md) to add the new value in static constructor and a [@Invoker](invoker.md) to be able to call the private constructor.

Example:
```java
@Mixin(TargetEnum.class)
abstract class TargetEnumMixin {

	// access the private constructor
	// the first two args (name and id) are added to enum constructors by java
	// if you are using McDev plugin add @SuppressWarnings("InvokerTarget")
	@Invoker("<init>(Ljava/lang/String;IIII)")
	private static TargetEnum init(String name, int id, int r, int g, int b) {
		throw new AssertionError(); // unreachable statement
	}
	
	// synthetic field, find the name in bytecode
	// if you are using McDev plugin add @SuppressWarnings("ShadowTarget")
	@Shadow
	@Final
	@Mutable
	private static TargetEnum[] field_1234;
	
	// add new property from the static constructor
	// if you are using McDev plugin add @SuppressWarnings("UnresolvedMixinReference")
	@Inject(method="<clinit>", at=@At("TAIL"))
	private static void clinit(CallbackInfo ci) {
		ArrayList<TargetEnum> values =  new ArrayList<>(Arrays.asList(field_1234);
		TargetEnum last = values.get(values.size() - 1);
		
		// add new value
		values.add( init("PINK", last.ordinal() + 1, 255, 192, 203) );
		
		field_1234 = values.toArray(new TargetEnum[0]);
	}

}
```

Now (optionally) create a new class for ease-of-use of the new enum value:
```java
class ExtendedTargetEnum {
	public static TargetEnum PINK = TargetEnum.valueOf("PINK");
}
```

Accessing the new value:
```java
ExtendedTargetEnum.PINK;
TargetEnum.valueOf("PINK");
TargetEnum.values(); // get all values; including PINK
```

> This article is based on the great [Gist](https://gist.github.com/LlamaLad7/0b553d5ae04e4eb44d3a1e8558be9151) by `LlamaLad7`
