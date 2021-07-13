## Vertex Consumers
[Back](rendering.md)

**FIXME:** This article is a stub. Missing info on actual rendering.

They allow for rendering geometry into a selected [Render Layer](../layer.md), `VertexConsumerProvider` is an object provided by the game, to then get `VertexConsumer` use the `VertexConsumerProvider.getBuffer(LAYER)`:

Example:
```java
VertexConsumerProvider consumers = /* ... */;

// solid layer
VertexConsumer consumer = consumers.getBuffer(RenderLayer.getSolid()); 
```
