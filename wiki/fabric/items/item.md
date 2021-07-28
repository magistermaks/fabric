## Items
[Back](../fabric.md)

To create an item new instance of `Item` class will is needed for registration in the item registry.

Example:
```java
// new item object
Item EXAMPLE = new Item(new FabricItemSettings().group(ItemGroup.MISC));

// register item (call in mod initializer)
Registry.register(Registry.ITEM, new Identifier("modid:example"), EXAMPLE);
```

`FabricItemSettings` class is used to add (some) properties to items, learn more here: [Item Settings](settings.md).

The `EXAMPLE` item will now be available in game with the `\give @a modid:example` command.

To give the item some visuals use [JSON Item Models](../../json/item.md) for simple models. Or [Item Renderers](../dynamic/item.md) for items with dynamic or animated elements. [Baked Models](../rendering/models/models.md) can also be used for a performant compromise between Item Renderers and static JSON Models.

#### Recipes
To add a crafting recipe for your item use [JSON Recipes](../../json/recipe.md).
**TODO**: link dynamic recipes
