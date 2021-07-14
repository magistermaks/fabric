## Vertex Consumers
[Back](rendering.md)

They allow for rendering geometry into a selected [Render Layer](../layer.md), `VertexConsumerProvider` is an object provided by the game, to then get `VertexConsumer` use the `VertexConsumerProvider.getBuffer(LAYER)`:

Example:
```java
VertexConsumerProvider consumers = /* ... */;

// solid layer
VertexConsumer consumer = consumers.getBuffer(RenderLayer.getSolid()); 
```

#### Rendering

**FIXME:** This section is a stub.

| Method | Description |
| ------ | ----------- |
| `.vertex(float x, float y, float z)` | vertex coordinates |
| `.color(int r, int g, int b, int a)` | vertex texture tint |
| `.texture(float u, float v)` | vertex texture coordinates |
| `.overlay(int overlay)` | overlay texture (block breaking animation) |
| `.light(int light)` | vertex light data |
| `.normal(Matrix3f normal, float x, float y, float z)` | normal vector |
| `.next()` | emit vertex and reset consumer state |

**Note:** Order of calls to these methods must correspond to the internal format of the vertex buffer being used.

Full example: (assumes being executed in [Block Entity Renderer](../dynamic/block.md))
```java
Identifier texture = new Identifier("textures/block/dirt.png");

// set texture and enable transparency 
VertexConsumer consumer = consumers.getBuffer(RenderLayer.getEntityTranslucentCull(texture));
MatrixStack.Entry matrix = matrices.peek();

// translate to the middle of the block
matrices.push();
matrices.translate(0.5, 0.5, 0.5);

Matrix4f model = matrix.getModel();
Matrix3f normal = matrix.getNormal();

int r = 255;
int g = 255;
int b = 255;
int a = 200;

// use the value provided (in block entity renderer) for breaking animation, or
// use 'OverlayTexture.DEFAULT_UV' to disable breaking animation
int overlay = OverlayTexture.DEFAULT_UV;

// provided by block entity renderer, or queried from WorldRenderer:
// (use only to query light at positions different than provided)
int light = WorldRenderer.getLightmapCoordinates(world, pos); 

// emit 4 vertices - one quad
consumer.vertex(model, -0.5f, -0.5f, -0.5f).color(r, g, b, a).texture(0, 0).overlay(overlay).light(light).normal(normal, 0.0F, 1.0F, 0.0F).next();

consumer.vertex(model, 0.5f, -0.5f, -0.5f).color(r, g, b, a).texture(1, 0).overlay(overlay).light(light).normal(normal, 0.0F, 1.0F, 0.0F).next();

consumer.vertex(model, 0.5f, -0.5f, 0.5f).color(r, g, b, a).texture(1, 1).overlay(overlay).light(light).normal(normal, 0.0F, 1.0F, 0.0F).next();

consumer.vertex(model, -0.5f, -0.5f, 0.5f).color(r, g, b, a).texture(0, 1).overlay(overlay).light(light).normal(normal, 0.0F, 1.0F, 0.0F).next();

matrices.pop();
```
