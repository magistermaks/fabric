## Renderer 
[Back](../fabric.md)

Renderer Plugin is the (active) implementation of the Fabric Rendering API. There can only be one Renderer Plugin active at a time, the `RendererAccess` interface can be used to retrieve the active plugin. By default Fabric API ships with the "Indigo" Renderer.

#### Accessing the Renderer

```java
// get current renderer instance
// by default this returns the "Indigo" renderer
RendererAccess.INSTANCE.getRenderer();

// check if a renderer is avaible
// some mods can conflict with FRAPI unregister the renderer
RendererAccess.INSTANCE.hasRenderer();

// register your own renderer
// if you are smart enough to do this you don't need this wiki :P
RendererAccess.INSTANCE.registerRenderer(Renderer plugin);
```

#### Renderer Interface

**FIXME:** This article is a stub, add links and better explanations  

* `meshBuilder()` returns new Mesh builder, used to create meshes and [Baked Models](models/baked.md) with enhanced features.
* `materialFinder()` used to get new Material Finders.
* `registerMaterial(id, material)` used to register a `RenderMaterial`.
* `materialById(id)` used to get registered material by id.

