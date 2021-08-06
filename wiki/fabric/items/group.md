## Item Groups
[Back](../fabric.md)

Item Groups (aka Creative Tabs) can be easily created with the help of Fabric API:

```java
// call in the mod initilizer
public static final ItemGroup EXAMPLE_GROUP = FabricItemGroupBuilder
	.create(new Identifier("modid", "example")) // the identifier of the tab 
	.icon(() -> new ItemStack(Items.DIRT)) // the item used as an icon
	.build();
```

#### Adding Items
If you are creating a new [Item](item.md) use the [Item Settings](settings.md) `.group()` to add it to the group. To add already existing items to a tab use `.appendItems(provider)` while creating the group.

Example:
```java
public static final ItemGroup EXAMPLE_GROUP = FabricItemGroupBuilder
	.create(new Identifier("modid", "example"))
	.icon(() -> new ItemStack(Items.DIRT))
	.appendItems(stacks -> {
		stacks.add(new ItemStack(Items.DIRT));
		stacks.add(new ItemStack(Items.STONE));
		stacks.add(new ItemStack(Items.GRAVEL));
	})
	.build();
```


