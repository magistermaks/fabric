## Rendering Items
[Back](rendering.md)

Minecraft provides a way to render items with `renderItem` method from `ItemRenderer` class. Instance of this class can be obtained by calling `MinecraftClient.getInstance().getItemRenderer()`. See how to render blocks here: [Rendering Blocks](block.md).

Example: 
```java
ItemStack stack = new ItemStack(Items.DIRT, 1);

MinecraftClient.getInstance().getItemRenderer().renderItem(
	stack, // the item to render
	ModelTransformation.Mode.GROUND, // how to render the item (enum)
	light, // light value, provided by block entity renderer
	OverlayTexture.DEFAULT_UV, // the overlay texture, or DEFAULT_UV for no overlay
	matrices, // matrix stack
	consumers, // vertex consumers
	42 // seed for random number generator
);
```
