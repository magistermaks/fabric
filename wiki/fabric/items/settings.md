## Item Settings
[Back](../fabric.md)

Item settings are passed to the `Item` constructor, they add (some) properties to the item, learn more about item registration here: [Items](item.md).

Once we create the `FabricItemSettings` object we can use it to build the item settings with the provided methods:

| Name | Description |
| ---- | ----------- |
| `.maxCount(count)` | maximal stack size, must be <= 64 |
| `.recipeRemainder(item)` | crafting reminder, used by milk, water and lava buckets |
| `.fireproof()` | marks the item as fireproof, used by netherrite items |
| `.food(food)` | adds a [Food Component](food.md) to the item |
| `.group(group)` | adds the item to a [Item Group](group.md) (creative tab) |
| `.rarity(rarity)` | see the section 'Rarity' below |

Example:
```java
Item EXAMPLE = new Item( new FabricItemSettings()
	.group(ItemGroup.MISC)
	.rarity(Rarity.RARE)
	.fireproof()
);
```

#### Rarity
Affects the color of the item's name, it be set to one of 4 values:

| Rarity | Color |
| ------ | ----- |
| `Rarity.COMMON` | White |
| `Rarity.UNCOMMON` | Yellow |
| `Rarity.RARE` | Aqua |
| `Rarity.EPIC` | Light Purple |
