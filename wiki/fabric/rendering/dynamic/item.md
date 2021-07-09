## Dynamic Item Renderers
[Back](dynamic.md)

They allow for dynamic rendering of items. To do this with blocks see: [Dynamic Block Renderers](block.md) To register a custom renderer for a block `BuiltinItemRendererRegistry` can be used: 

```java
BuiltinItemRendererRegistry.INSTANCE.register(item, new MyDynamicItemRenderer()); 
// where DynamicItemRenderer implements BuiltinItemRendererRegistry.DynamicItemRenderer

// or by using an lambda:
BuiltinItemRendererRegistry.INSTANCE.register(item, (stack, modelTransformationMode, matrixStack, vertexConsumerProvider, light, overlay) -> {
	// render here
} );
```
