## Dynamic Block Renderers
[Back](dynamic.md)

They allow for dynamic rendering of blocks, and are commonly called `BER`s (Block Entity Renderers). 
To do this with items see: [Dynamic Item Renderers](item.md)

We first must create a new block renderer class:
```java
public class SomeBlockEntityRenderer extends BlockEntityRenderer<SomeBlockEntity> {
	
	public ChestBlockEntityRenderer(BlockEntityRendererFactory.Context context) {
		// init here
	}
		
	@Override
	public void render(SomeBlockEntity blockEntity, float tickDelta, MatrixStack matrices, VertexConsumerProvider vertexConsumers, int light, int overlay) {
		// render here
	}

}
```

and attach it to the block entity type of our block entity:

```java
BlockEntityRendererRegistry.INSTANCE.register(blockEntityType, context -> {
	return new SomeBlockEntityRenderer<SomeBlockEntity>(context);
} );

// or simply:
BlockEntityRendererRegistry.INSTANCE.register(blockEntityType, SomeBlockEntityRenderer::new);
```
