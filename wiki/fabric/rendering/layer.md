## Render Layers
[Back](../fabric.md)

Render Layers allow specifying how textures of a model should be rendered.

```java
// change rander layer of one block/item
BlockRenderLayerMap.INSTANCE.putBlock(block, renderLayer)
BlockRenderLayerMap.INSTANCE.putItem(item, renderLayer)

// change rander layer of multiple blocks/items
BlockRenderLayerMap.INSTANCE.putBlocks(renderLayer, blocks)
BlockRenderLayerMap.INSTANCE.putItems(renderLayer, items)
```

| `RenderLayer` | Description | Example |
| ----------- | ----------- | ------- |
| `getSolid()` | Default value, non-255 alpha values are replaced with black color | Stone |
| `getCutout()` | Allows 0 or 255 alpha values for no or full transparency | Glass |
| `getTransparent()` | Enables full color blending | Stained Glass |

#### Vertex Consumers
Render Layers are used to get Vertex Consumers from Vertex Consumer Providers, learn more here: [Vertex Consumers](rendering/consumers.md).

#### Transparent Blocks
In glass-like blocks setting block's opacity (**TODO** link) and using cutout/translucent render layer is not enough, because the faces of other glass blocks will be visible behind it (see _Fig. 1_). To disable that behavior (make faces between two transparent glass blocks invisible, see _Fig. 2_) override `isSideInvisible(BlockState, BlockState, Direction)` method from block class to return `true` for blocks of the same type:

```java
public boolean isSideInvisible(BlockState state, BlockState stateFrom, Direction direction) {
	return stateFrom.isOf(this) ? true : super.isSideInvisible(state, stateFrom, direction);
}
```

... or make your block extend the `TransparentBlock` class which already does that.

![](/assets/fabric_rendering_layer.png)

