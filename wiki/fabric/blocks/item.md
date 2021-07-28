## Adding a Block Item
[Back](../fabric.md)

Creating an item that places a block when used can get quite complicated when we take into account all the possible edge cases (nbt tags, statistics, permissions), So it's best to use a predefined class created by Mojang for all other block items in the game - `BlockItem`. Learn more about items here: [Items](../items/item.md), and about blocks here: [Blocks](block.md).

Example:
```java
Item EXAMPLE_BLOCK_ITEM = new BlockItem(EXAMPLE_BLOCK, ITEM_SETTINGS);
```

Item create like that will be place the specified block (`EXAMPLE_BLOCK`) when right-clicked in game, to register this item see: [Items](../items/item.md).
