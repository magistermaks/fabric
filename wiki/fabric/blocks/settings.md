## Block Settings
[Back](../fabric.md)

Block settings are passed to the `Block` constructor, they add (some) properties to a block, learn more about block registration here: [Blocks](block.md).

Block settings are always derived from a [Material](../materials/Material.md) or other block settings with the `of()` or `copyOf()` methods. The settings object can be reused.

Example:
```java
// create settings from a material
FabricBlockSettings.of(material);

// create settings from a material, but override the material color
FabricBlockSettings.of(material, color);

// copy settings of another block
FabricBlockSettings.copyOf(block);

// copy settings of another settings object
FabricBlockSettings.copyOf(settings);
```

Once we have the `FabricBlockSettings` object we can use it to build the block settings with the provided methods:

| Name | Description |
| ---- | ----------- |
| `.noCollision()` | disable collisions with the block |
| `.nonOpaque()` | mark the block as non-full-cube or/and transparent |
| `.slipperiness(value)` | sets the slipperiness, default `0.6f`, blue ice uses `0.989f` |
| `.sounds(soundGroup)` | sets the sound group to use **TODO**: link |
| `.luminance(lightLevel)` | set the light level emitted from a block |
| `.luminance(provider)` | provide a function used to map a block state to a light level |
| `.hardness(hardness)` | sets the breaking time, stone uses `2.0f` |
| `.resistance(resistance)` | sets the explosion resistance, stone uses `6.0f` |
| `.strength(hardness, resistance)` | a short hand for calling `.hardness().resistance()` | 
| `.requiresTool()` | require the right tool to be used or item won't drop |
| `.breakByHand(flag)` | mark player hand as the right tool for this block |
| `.breakByTool(tool, level)` | marks a tool, of given level, as the right one to use |
| `.breakByTool(tool)` | marks a tool, of any level, as the right one to use |
| `.breakInstantly()` | makes the block break instantly when mined |
| `.ticksRandomly()` | enables random ticks for a block, **TODO**: link |
| `.dropsNothing()` | disable loot table for a block | 
| `.dropsLike(block)` | copy the loot table of another block |
| `.drops(identifier)` | specify a custom loot table to use |
| `.air()` | mark air blocks |
**TODO**: some predicates are missing from this list

Example:
```java
Block EXAMPLE_BLOCK = new Block(

	// settings; derived from material METAL, mark non-opaque, and that
	// the effective tool for this block is the player hand
	FabricBlockSettings.of(Material.METAL)
	.nonOpaque()
	.breakByHand(true)
	
);
```
