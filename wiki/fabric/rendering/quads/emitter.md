## Quad Emitter
[Back](quads.md)

**FIXME:** This article is a stub.

Quad emitters are used to either write to a mesh, or to directly output quads to be rendered.

To emit a square aligned with the axis:
```java
Sprite sprite = /* ... */

// add square from direction, left, bottom, right, top and distance from the block face
emitter.square(Direction.UP, 0.1F, 0.1F, 0.9F, 0.9F, 0.1F)
	
	// add sprite to the quad
	.spriteBake(0, sprite, MutableQuadView.BAKE_LOCK_UV)
	
	// magic values, TODO
	.spriteColor(0, -1, -1, -1, -1)
	
	// optionly make the quad lit
	// .lightmap(255, 255, 255, 255)
	
	// emit the quad, and reset the emitter
	.emit();

```
