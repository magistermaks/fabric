## Render Data Attachments
[Back](../fabric.md)

Data attachments are a simple way to safely transfer data between a `BlockEntity` and [Baked Model](./models/baked.md). The block entity must implement the `RenderAttachmentBlockEntity` interface. The `getRenderAttachmentData()` must then return the data intended for the model, can be `null`.

On the model's side this object can be retrieved by casting `BlockRenderView` to `RenderAttachmentBlockEntity` and calling `getRenderAttachmentData(blockPos)`.

```java
// block entity:
class MyBlockEntity implements RenderAttachmentBlockEntity {

	// ...
	
	@Override
	public Block getRenderAttachmentData() {
		return new Integer(123);
	}

}

// baked block model:
class MyBlockModel /*...*/ {

	// ...
	
	@Override
	public void emitBlockQuads(BlockRenderView blockView, BlockState state, BlockPos pos, Supplier<Random> randomSupplier, RenderContext context) {
	
		RenderAttachedBlockView renderAttachedBlockView = (RenderAttachedBlockView) blockView;
		Integer value = (Integer) renderAttachedBlockView.getRenderAttachmentData(pos);
		
		// value == 123
		// ...
	}

}
```
