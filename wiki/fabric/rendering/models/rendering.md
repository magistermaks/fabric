## Rendering
[Back](models.md)

This method of rendering can only be used in [Baked](baked.md) and [Unbaked](unbaked.md) models. 

#### Getting a `QuadEmitter`
There are two ways to use a quad emitter - either to directly output geometry to a `RenderContext` instance or to create a static mesh. The first can be used in Baked Models for dynamic creation of models that depend on some external state (Block entity data, etc). While the second can be used to create high performance static models in Unbaked Models.

Emit into `RenderContext`:
```java
QuadEmitter emitter = renderContext.getEmitter();
```

Emit into a `Mesh`:
```java
Renderer renderer = RendererAccess.INSTANCE.getRenderer();
MeshBuilder builder = renderer.meshBuilder();
		
// this emitter will emit quads to the mesh
QuadEmitter emitter = builder.getEmitter();

// get the static mesh
Mesh mesh = buider.get();
```

#### Using a `QuadEmitter`
**FIXME:** This section is a stub.

Example:
```java
Sprite sprite = /* ... */

// add square from direction, left, bottom, right, top and distance from the block face
emitter.square(Direction.UP, 0.1F, 0.1F, 0.9F, 0.9F, 0.1F);
	
// add sprite to the quad, 3th argument specifies how the texture
// should be rotated
emitter.spriteBake(0, sprite, MutableQuadView.BAKE_LOCK_UV);
	
// require after adding a sprite, can be used for adding a tint. 
// -1 disables any tinting, otherwise pass RGBA data formated as
// an int where the 4 bytes representing it are: B, G, R, A values
emitter.spriteColor(0, -1, -1, -1, -1);
	
// optionally add light data, if not used the light value will 
// be calculated automatically
// emitter.lightmap(255, 255, 255, 255)
	
// emit the quad, this also resets the internal state of the emitter
emitter.emit();
```

| `MutableQuadView` |
| --------------- |
| `BAKE_ROTATE_NONE` |
| `BAKE_ROTATE_90` |
| `BAKE_ROTATE_180` |
| `BAKE_ROTATE_270` |
| `BAKE_LOCK_UV` |
| `BAKE_FLIP_U` |
| `BAKE_FLIP_V` |
| `BAKE_NORMALIZED` |
