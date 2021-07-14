## Rendering Blocks
[Back](rendering.md)

Minecraft provides a way to render blocks with `renderBlockAsEntity` method from `BlockRenderManager` class. Instance of this class can be obtained by calling `MinecraftClient.getInstance().getBlockRenderManager()`. See how to render items here: [Rendering Items](item.md).

Example:
```java
BlockState state = Blocks.STONE.getDefaultState();

MinecraftClient.getInstance().getBlockRenderManager().renderBlockAsEntity(
	state, // the block state to render
	matrices, // matrix stack
	consumers, // vertex consumers
	light, // light value, provided by block entity renderer
	OverlayTexture.DEFAULT_UV // the overlay texture, or DEFAULT_UV for no overlay
);
```

