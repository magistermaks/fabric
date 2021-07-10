## Model Providers
[Back](models.md)

Model providers are used to supply the models requested by the game (block, item models) and addition models requested by other mods. This can, for example, be used to add support for loading of models of other formats, like `.obj` files, and to generate some specific models in code for greater flexibility.

There are two types of model providers: 
* Variant Providers - for loading of models from block state identifiers
* Resource Providers - for loading of models from direct paths

Example: Resource Provider
```java
ModelLoadingRegistry.INSTANCE.registerResourceProvider( manager -> (identifier, context) -> {
	// return the unbaked model for the given identifier
} );
```

To register a Variant Provider simply use `registerVariantProvider` the `identifier` will then be an instance of `ModelIdentifier` class. The `context` argument can be used to request the game to load other (sub-)unbaked models, with either `Identifier` or `ModelIdentifier`:

```java
UnbakedModel part = context.loadModel( someIdentifier );
```

The implementation can throw `ModelProviderException` if there was an error while loading the model.

This system can be used to "register" custom [Unbaked Models](unbaked.md):
```java
final EXMAPLE_ITEM = new Identifier("modid", "item/example");
final EXMAPLE_BLOCK = new Identifier("modid", "block/example");

ModelLoadingRegistry.INSTANCE.registerResourceProvider( manager -> (identifier, context) -> {
	if( identifier.equals(EXMAPLE_ITEM) || identifier.equals(EXMAPLE_BLOCK) ) {
		return new UnbakedModelExample();
	}
	
	return null;
} );
```
