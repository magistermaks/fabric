## Block States
[Back](../fabric.md)

As all the blocks of one type are represented by the same object instance, to add a state to a block `BlockStates` must be used.

First create new property object that extends the `Property` class or use a predefined one:

| Property | Description | Example |
| -------- | ----------- | ------- |
| `BooleanProperty` | Stores a `boolean` value | `BooleanProperty.of(name)` |
| `IntProperty` | Stores an integer value in range | `IntProperty.of(name, min, max)` |
| `EnumProperty` | Stores an enum value | `EnumProperty.of(name, clazz)` |
| `DirectionProperty` | Stores a direction enum value | `DirectionProperty.of(name)` |

**Note:** Property object don't need to be unique and can be reused for many blocks to save memory, all properties used by vanilla game are stored in the `Properties` class.

Then add that property to a block in the `appendProperties` method.

Example:
```java
class ExampleBlock extends Block {

	// the block state
	private static final BooleanProperty POWERED = BooleanProperty.of("powered");
	
	// add the property to a block
    protected void appendProperties(StateManager.Builder<Block, BlockState> builder) {
        builder.add(POWERED);
    }
	
	public ExampleBlock(Settings settings) {
        super(settings);
		
		// set the default (initial) state of the block
        setDefaultState( getStateManager().getDefaultState().with(POWERED, false) );
    }

}
```

To set and get the state of a block use `setBlockState` and `getBlockState`. Value of a particular property can be queried with `state.get(property)` and set with `state.with(property, value)`.

**Note:** `with` **doesn't** modify the state of the block in the world, nor of the object on with it is called, it returns a new state object with the requested changes.

Example:
```java
public ActionResult onUse(BlockState state, World world, BlockPos pos, PlayerEntity player, Hand hand, BlockHitResult hit) {
	// set POWERED state to true at pos
	world.setBlockState(pos, state.with(POWERED, true)); 
		
	// cycle all possible states of a property (one at a time)
	world.setBlockState(pos, state.cycle(POWERED));
		
	// if state is not available it can be queried from the world using:
	BlocState foo = world.getBlockState(pos);
}
```

**Note:** As every combination of all the states in a block is defined as a unique block be careful with adding too many properties. For example a block with 6 `boolean` properties and a one int property in range 0 to 15 would have `2 * 2 * 2 * 2 * 2 * 2 * 16 = ` 1024 total states. Try to keep the states count below that value. For more complex data use [Block Entities](entities.md).

