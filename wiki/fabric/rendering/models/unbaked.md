## Unbaked Models
[Back](models.md)

Unbaked models store raw model data, they are used as factories of [Baked Models](baked.md), and are created by [Model Providers](provider.md).

To create the mesh of the model use a `QuadEmitter`, learn more here: [Rendering](rendering.md), and to register this Unbaked Model use a [Model Provider](provider.md).

```java
class UnbakedModelExample implements UnbakedModel {

	private final static SPRITE_ID = new SpriteIdentifier(
		SpriteAtlasTexture.BLOCK_ATLAS_TEXTURE, // load sprite from block texture atlas
		new Identifier("modid", "block/example") // sprite identifier
	);

	public UnbakedModelExample() {
		// init model, called from Model Provider
	}

	@Override
	public Collection<Identifier> getModelDependencies() {
		// return a collection of all models this model depends on
		return Collections.emptySet();
	}

	@Override
	public Collection<SpriteIdentifier> getTextureDependencies(Function<Identifier, UnbakedModel> unbakedModelGetter, Set<Pair<String, String>> unresolvedTextureReferences) {
		// return sprite identifiers used by the model and all it's dependencies
		// so that the game can load them before the 'bake()' method is called
		return Collections.singletonList(SPRITE_ID);
	}
	
	@Override
	public BakedModel bake(ModelLoader loader, Function<SpriteIdentifier, Sprite> textureGetter, ModelBakeSettings rotationContainer, Identifier modelId) {
		// return new Baked Model, preferably create model mesh here using 
		// Fabric Rendering API, but dynamic models can create their meshes 
		// in Baked Models
		
		// Example:
		Sprite sprite = textureGetter.apply(SPRITE_ID);
		
		// get the renderer and a new mesh builder, see 'Renderer'
		Renderer renderer = RendererAccess.INSTANCE.getRenderer();
		MeshBuilder builder = renderer.meshBuilder();
		
		// this emitter will emit quads to the mesh
		QuadEmitter emitter = builder.getEmitter();
		
		// emit model quads with emitter
		// ...
		
		return new BakedModelExample( sprite, builder.get() );
	}

}
```

Continue reading in: [Baked Models](baked.md).
