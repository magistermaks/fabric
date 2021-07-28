## Blocks
[Back](../fabric.md)

To create a block new instance of `Block` class will is needed for registration in the block registry.

```java
// new block object
Block EXAMPLE = new Block(FabricBlockSettings.of(Material.STONE));

// register block (call in mod initializer)
Registry.register(Registry.BLOCK, new Identifier("modid", "example"), EXAMPLE);
```

`FabricBlockSettings` class is used to add (some) properties to blocks, learn more here: [Block Settings](settings.md).

The `EXAMPLE` block will now be available in game with the `\setblock ~ ~ ~ modid:example` command to learn how to add an item to this block see: [Block Items](item.md).

To give the block some visuals use [JSON Block Models](/wiki/json/block.md) for simple models like fences, redstone, full blocks etc. Or [Block Entity Renderers](../rendering/dynamic/block.md) for blocks with dynamic or animated elements. [Baked Models](../rendering/models/models.md) can also be used for a performant compromise between Block Entity Renderers and static JSON Models.

#### Custom Block Classes
To add more advanced properties to a block a custom class must be created, and extend the `Block` class.

Example:
```java
class ExampleBlock extends Block {
     
	public ExampleBlock(Settings settings) {
		// block settings, those are the 'FabricBlockSettings' passed in the first example
		super(settings);
	}
	
	// used to add block states to a block
	// learn more in blockstates article
	protected void appendProperties(StateManager.Builder<Block, BlockState> builder) {
	}
	
	// called when the block is broken
	public void onBroken(WorldAccess world, BlockPos pos, BlockState state) {
	}
	
	// called on scheduled block ticks, and, if randomTick is not overridden, 
	// on random ticks
	public void scheduledTick(BlockState state, ServerWorld world, BlockPos pos, Random random) {
	}

	// called randomly in a 'Random Tick', to enable random ticks for this block
	// use 'ticksRandomly()' on block settings.
	public void randomTick(BlockState state, ServerWorld world, BlockPos pos, Random random) {
	}
	
	// called randomly on the client side, used mostly for emitting particles,
	// the frequency of this method being called depend on the distance from the player 
	public void randomDisplayTick(BlockState state, World world, BlockPos pos, Random random) {
	}
	
	// used to tell the game if the side of the block should not be rendered (independet
	// of culling, used by glass and other transparent blocks)
	public boolean isSideInvisible(BlockState state, BlockState stateFrom, Direction direction ) {
	}
	
	// called when the state of one of the neighbors of this block is changed
	// can be used for checking if the position of the block is still valid
	public void neighborUpdate(BlockState state, World world, BlockPos pos, Block block, BlockPos fromPos, boolean notify) {
		// Note: call super!
	}
	
	// called when the state of one of the neighbors of this block is changed
	// replaces block's state with the one returned from this method
	public BlockState getStateForNeighborUpdate(Direction direction, BlockState neighborState, WorldAccess world, BlockPos pos, BlockPos neighborPos) {
	}
	
	// called when the block is placed (by hand or command)
	// can be used for scheduling an initial block tick
	public void onBlockAdded(BlockState state, World world, BlockPos pos, BlockState oldState, boolean notify) {
	}

	// called when this block is being removed
	// used for cleanup
	public void onStateReplaced(BlockState state, World world, BlockPos pos, BlockState newState, boolean moved) {
		// Note: call super!
	}
	
	// called when a player right clicks on this block, called on both server & client
	// if the actions is 'Successfull' on the client the action would also be performed on the server
	public ActionResult onUse(BlockState state, World world, BlockPos pos, PlayerEntity player, Hand hand, BlockHitResult hit) {
		// ActionResult.SUCCESS - successfull   - swing hand       - break
		// ActionResult.CONSUME - successfull   - don't swing hand - break
		// ActionResult.PASS    - unsuccessfull - don't swing hand - continue
		// ActionResult.FAIL    - unsuccessfull - don't swing hand - break
		
		// continue - the game will try seraching for a diffrent action to perform
		// break - the game won't try seraching for a diffrent action
		
		// default return value: ActionResult.PASS
	}
	
	// indicates how to render this block
	// by default (BlockRenderType.MODEL) block uses models
	public BlockRenderType getRenderType(BlockState state) {
	}
	
	// indicates if the block CAN emit signal for the given blockstate
	// block's redstone getters are only called if this returns true, default: false
	public boolean emitsRedstonePower(BlockState state) {
	}
	
	// returns the weak redstone signal of this block
	// this method won't be called if emitsRedstonePower returnes false
	public int getWeakRedstonePower(BlockState state, BlockView world, BlockPos pos, Direction direction) {
	}

	// returns the strong redstone signal of this block
	// this method won't be called if emitsRedstonePower returnes false
	public int getStrongRedstonePower(BlockState state, BlockView world, BlockPos pos, Direction direction) {
	}

	// indicates if the block CAN emit comparator signal for the given blockstate
	// block's comparator getter is only called if this returns true, default: false
	public boolean hasComparatorOutput(BlockState state) {
	}
	
	// returns the strength of comparator output
	// this method won't be called if hasComparatorOutput returnes false
	public int getComparatorOutput(BlockState state, World world, BlockPos pos) {
	}
	
	// get model offset type, used to sligly offset the model while rendering 
	// use: .NONE, .XZ, .XYZ, default: AbstractBlock.OffsetType.NONE
	public AbstractBlock.OffsetType getOffsetType() {
	}

	// get maximum offset in one direction
	// 1.0f - one block, default: 0.25f
	public float getMaxModelOffset() {
	}
	
	// random number used for rendering
	// by default it's a hash code of block's pos
	public long getRenderingSeed(BlockState state, BlockPos pos) {
	}
	
	// returns whatever this block can be placed 
	// at this position
	public boolean canPlaceAt(BlockState state, WorldView world, BlockPos pos) {
	}
	
	// called when a projetile such as arrow or snowball hits
	// block's hitbox
	public void onProjectileHit(World world, BlockState state, BlockHitResult hit, ProjectileEntity projectile) {
	}
	
	// voxel shape used for rendering block outlines
	// by default, a full cube
	public VoxelShape getOutlineShape(BlockState state, BlockView world, BlockPos pos, 	ShapeContext context) {
	}

	// voxel shape used for block collisions
	// by default calls to getOutlineShape
	public VoxelShape getCollisionShape(BlockState state, BlockView world, BlockPos pos, ShapeContext context) {
	}
	
	// voxel shape used for camera collision (in 3th person view)
	// by default calls to getCollisionShape
	public VoxelShape getCameraCollisionShape(BlockState state, BlockView world, BlockPos pos, ShapeContext context) {
      return this.getCollisionShape(state, world, pos, context);
	}
	
	// caled when a block breaking starts
	// (when a block is hit by a player)
	public void onBlockBreakStart(BlockState state, World world, BlockPos pos, PlayerEntity player) {
	}
	
	// called after all drop stacks are spowned in the world
	// used by minecraft to spawn experience, with the helper method 'dropExperience'
	public void onStacksDropped(BlockState state, ServerWorld world, BlockPos pos, ItemStack stack) {
	}

}
```
