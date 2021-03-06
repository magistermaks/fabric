## Baked Models
[Back](models.md)

This article shows how to use Baked Models in combination with Fabric Rendering API, note that using models in this way will require a [Renderer](../renderer.md) to be available. To learn about how Baked Models are created see: [Unbaked Models](unbaked.md).

To create the dynamic mesh inside of Baked Model use a `QuadEmitter`, learn more here: [Rendering](rendering.md).

Baked models must extend the vanilla class `BakedModel`, and `FabricBakedModel` if you want to use the Fabric Rendering API, as using it is both easier and more powerful that's what this example will use: (Note that this code is the continuation of the example from article [Unbaked Models](unbaked.md))

```java
class BakedModelExample implements BakedModel, FabricBakedModel {

	// this sprite and mesh are created in Unbaked Model
	final private Sprite sprite;
	final private Mesh mesh;
	
	public BakedModelExample( Sprite sprite, Mesh mesh ) {
		// called from Unbaked Model
		this.sprite = sprite;
		this.mesh = mesh;
	}

	/*
	 * methods inherited from FabricBakedModel
	 */
	public boolean isVanillaAdapter() {
		// return false, we are going to use Fabric Rendering API
		return false;
	}
 
	public void emitBlockQuads(BlockRenderView blockRenderView, BlockState blockState, BlockPos blockPos, Supplier<Random> supplier, RenderContext renderContext) {
		// emit block quads
		
		// warning: the 'pos' may not be the actual pos if the model is 
		// rendered as an entity.
		
		// append static mesh to chunk mesh
		renderContext.meshConsumer().accept(this.mesh);
		
		// to dynamically generate the model here every time the chunk is rebuild use
		// QuadEmitter emitter = renderContext.getEmitter();
		
		// you can also access Block Entity Data Attachment here from 'blockRenderView'
		// see: 'Data Attachments'
	}
 
	public void emitItemQuads(ItemStack itemStack, Supplier<Random> supplier, RenderContext renderContext) {
		// emit item quads
		
		// render the same mesh used for blocks
		renderContext.meshConsumer().accept(this.mesh);
	}
	
	/*
	 * methods inherited from BakedModel
	 */
	public List<BakedQuad> getQuads(BlockState state, Direction face, Random random) {
		// leave empty, we are using FabricBakedModel
		return null;
	}
 
	public boolean useAmbientOcclusion() {
		// enable/disable ambient occlusion
		return true;
	}
 
	public boolean isBuiltin() {
		// todo: document
		return false;
	}
 
	public boolean hasDepth() {
		// todo: document
		return false;
	}
 
	public boolean isSideLit() {
		// used to specify how the item should be lighted in the GUI
		// use true to light the model from the side, like a block
		// use false to light it from the front, like an item
		return false;
	}
 
	public Sprite getSprite() {
		// block breaking particle sprite, this can be generated 
		// in Unbaked Model and passed here by the constructor
		return sprite;
	}
 
	public ModelTransformation getTransformation() {
		// this method returns the GUI model transformations used on items
		// JSON models usualy use the standard transformations defined in 'block/block'
		// we will use the same transformations as them
		return ModelHelper.MODEL_TRANSFORM_BLOCK;
	}
 
	public ModelOverrideList getOverrides() {
		// part of item JSON model (https://minecraft.fandom.com/wiki/Model)
		// works like blockstates for items.
		// don't use them in models generated in the code
		return ModelOverrideList.EMPTY;
	}

}
```

An instance of this class must be returned by the `bake()` method of [Unbaked Model](unbaked.md). To register this model use a [Model Provider](provider.md).
