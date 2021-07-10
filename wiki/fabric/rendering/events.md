## Render Events
[Back](../fabric.md)

This article list render events (that is events called when the game is being rendered) and how to use them. `WorldRenderEvents` are executed in the same order that they were listed.

#### `HudRenderCallback`
Called after the HUD is rendered in the world

Usage:
```java
HudRenderCallback.EVENT.register( (matrixStack, tickDelta) -> {
	// callback
} );
```

#### `InvalidateRenderStateCallback`
Called after the world renderer reloads, this can be caused by changing video settings, using `F3+A`, or changing the selected resource packs.

```java
InvalidateRenderStateCallback.EVENT.register( () -> {
	// callback
} );
```

#### `WorldRenderEvents.START`
Called before world rendering starts, view frustum is not yet available. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.START.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.AFTER_SETUP`
Called after all modified chunks are rebuilt but before they are uploaded for rendering. View frustum is available. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.AFTER_SETUP.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.BEFORE_ENTITIES`
Called after all the `Solid`, `Cutout`, and `CutoutMipped` terrain render layers are rendered. Use to render non-translucent geometry. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.BEFORE_ENTITIES.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.AFTER_ENTITIES`
Called after solid terrain and entities have been rendered, but before block entity renderers are called. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.AFTER_ENTITIES.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.BEFORE_BLOCK_OUTLINE`
Called before the block outline is drawn, callback can return `false` to cancel the rendering of the default vanilla outline (this won't cancel executing other listeners attached to this event). `context` is an instance of `WorldRenderContext`, and `hit` is an instance of `HitResult`.

```java
WorldRenderEvents.BEFORE_BLOCK_OUTLINE.register( (context, hit) -> {
	// callback
} );
```

#### `WorldRenderEvents.BLOCK_OUTLINE`
Called before the block outline is drawn, **this event will not be called if it was canceled from the `BEFORE_BLOCK_OUTLINE` event**, callback can return `false` to cancel the rendering of the default vanilla outline, `context` is an instance of `WorldRenderContext`, and `outline` is an instance of `BlockOutlineContext`.

```java
WorldRenderEvents.BLOCK_OUTLINE.register( (context, outline) -> {
	// callback
} );
```

#### `WorldRenderEvents.BEFORE_DEBUG_RENDER`
Called after all non-translucent elements are rendered but before the debug renderers are called and before the translucency. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.BEFORE_DEBUG_RENDER.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.AFTER_TRANSLUCENT`
Called after entity, terrain, and particle translucency has be drawn to the frame buffer. but before translucency combine has happened in fabulous mode. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.AFTER_TRANSLUCENT.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.LAST`
Called after all world rendering is complete, but before the `GL` state is reset. Precedes rendering of `GUI`s and other overlay elements. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.LAST.register( context -> {
	// callback
} );
```

#### `WorldRenderEvents.END`
Called after all world rendering is complete and the changes to `GL` states are reverted. Precedes rendering of `GUI`s and other overlay elements. `context` is an instance of `WorldRenderContext`.

```java
WorldRenderEvents.END.register( context -> {
	// callback
} );
```
