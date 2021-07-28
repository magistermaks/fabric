## JSON Block Models
[Back](json.md)

This article shows how to create JSON models for [Blocks](../fabric/blocks/block.md).

#### Block States
Each block must have a block state file, it tells the game how to map a combination of `blockstates` into a model. It can also be used to combine multiple models, rotate them or to add variants to the block (choosing the model and/or rotations randomly).

File location: `/assets/<modid>/blockstates/<blockid>.json`  
Minecraft Wiki page: https://minecraft.fandom.com/wiki/Model#Block_states

#### Block Models
The actual model of the block that the Block State points to, it consists of textured boxes that can be rotated, moved and tinted. Model can also contain GUI transformations. They can also inherit properties from other models; it's recommended to always extend the `minecraft:block/block`, as it contains the item GUI transformations used by all other blocks in game. Learn about item models here: [Items](item.md).

File location: `/assets/<modid>/models/block/<path>.json`  
Minecraft Wiki page: https://minecraft.fandom.com/wiki/Model#Block_models

For editing and creating models check out [Blockbench](https://www.blockbench.net/), simple, free and popular cuboid model editor.
