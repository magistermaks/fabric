## Block Entities
[Back](../fabric.md)

Block entities are object attached to blocks. They are unique to every block in the world similarly to [Block States](states.md), but use more memory so should only e used if block states are not enough.

To create a block entity 3 thing will be needed:
* `BlockEntity` class
* `BlockEntityType` object
* Target `Block`, the block to which the entity will be attached

Example:
```java
// The Block to with the entity is to be attached:
public static Block EXAMPLE_BLOCK = /* ... */;

// Block Entity Type:
public static BlockEntityType<BlockEntityExample> EXAMPLE_BLOCK_ENTITY_TYPE;

// Block Entity Class:
public class ExampleBlockEntity extends BlockEntity {

	public ExampleBlockEntity(BlockPos pos, BlockState state) {
		super(BLOCK_ENTITY_TYPE, pos, state);
	}

}
```

Also the target block must implement `BlockEntityProvider` and define the `createBlockEntity` method:
```java
public BlockEntity createBlockEntity(BlockPos pos, BlockState state) {
	return new ExampleBlockEntity(pos, state);
}
```

To stitch it all together call this from the common mod initializer:
```java
EXAMPLE_BLOCK_ENTITY_TYPE = Registry.register(
	Registry.BLOCK_ENTITY_TYPE,
	"modid:example_block_entity", // id of the block entity
	FabricBlockEntityTypeBuilder.create( 
		ExampleBlockEntity::new, // block entity constructor
		EXAMPLE_BLOCK // target block
	).build()
);
```

The `FabricBlockEntityTypeBuilder#create` can take multiple target blocks to add the same block entity to them:
```java
FabricBlockEntityTypeBuilder.create( 
	ExampleBlockEntity::new,
	EXAMPLE_BLOCK_1,
	EXAMPLE_BLOCK_2,
	// ...
).build()
```
