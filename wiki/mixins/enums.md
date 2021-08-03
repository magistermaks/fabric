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

#### Adding Values
To add a value to a mixin [@Inject](inject.md) into static constructor, add use an [@Invoker](invoker.md) to be able to call the private constructor of the `enum`.

Example:
```java
@Mixin(TargetEnum.class)
abstract class TargetEnumMixin {

	// access the private constructor
	// the first two args (name and id) are added to enum constructors by java
	// if you are using McDev plugin add @SuppressWarnings("InvokerTarget")
	@Invoker("<init>")
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
	// static blocks are merged into the target class (at the end)
	static {
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

#### Replace Values
This can be done quite similarly to adding custom values. An [@Invoker](invoker.md) for the private constructor will still be needed, but instead of an injection into the static constructor, an [@Redirect](redirect.md) will be used.

Example:
```java
@Mixin(TargetEnum.class)
abstract class TargetEnumMixin {

	// access the private constructor
	// the first two args (name and id) are added to enum constructors by java
	// if you are using McDev plugin add @SuppressWarnings("InvokerTarget")
	@Invoker("<init>")
	private static TargetEnum init(String name, int id, int r, int g, int b) {
		throw new AssertionError(); // unreachable statement
	}
	
	// replace the property creation in static constructor
	// if you are using McDev plugin add @SuppressWarnings("UnresolvedMixinReference")
	@Redirect(
		method = "<clinit>()V",
		at = @At(
			value = "NEW",
			ordinal = 0, // this will correspond to the index of the enum value to replace
			target = "Lpath/to/TargetEnum;<init>(Ljava/lang/String;IBBB)Lpath/to/TargetEnum;" // enum constructor
		)
	)
	private static TargetEnum clinit(String name, int id, int r, int g, int b) {
		// generally it's advised to leave the 'name' at its original value
		return init("ORANGE", id, 255, 165, 0); // replace RED with ORANGE
	}

}
```

Accessing the new `ORANGE` value:
```java
TargetEnum.RED;
TargetEnum.valueOf("ORANGE");
TargetEnum.values(); // get all values; including ORANGE

// Warning!
// this will break if the internal name of the field is changed
// so it's adviced to leave it unmodified (but then TargetEnum.valueOf("ORANGE") won't work)
TargetEnum.valueOf("RED");
```

> This article is based on the great [Gist](https://gist.github.com/LlamaLad7/0b553d5ae04e4eb44d3a1e8558be9151) by `LlamaLad7`
