## Model Loading
[Back](models.md)

To load JSON model for later use (e.g. rendering them dynamically) a model provider must first me registered, it can then request multiple models for the game to load:

```java

// will load: /assets/modid/models/path/to/example.json
final Identifier MODEL = new Identifier("modid", "path/to/example");

// to load a model through the blockstate system use 'ModelIdentifier'
final ModelIdentifier BLOCKSTATE = new ModelIdentifier("modid", "example#state");

ModelLoadingRegistry.INSTANCE.registerModelProvider( (manager, out) -> {
	out.accept( MODEL ); 
	out.accept( BLOCKSTATE ); 
} );
```

To then retrieve the baked model object for rendering use `BakedModelManager`:

```java
BakedModelManager manager = MinecraftClient.getInstance().getBakedModelManager();

// get a model loaded through the blockstate system
BakedModel foo = manager.getModel( BLOCKSTATE );

// get a model loaded directly
BakedModel bar = BakedModelManagerHelper.getModel( manager, MODEL );
```


