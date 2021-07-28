## Materials
[Back](../fabric.md)

Material are used to store common properties of blocks such as color on a map, piston  behavior etc.Materials used by Vanilla game are defined and stored in the `Material` class, they should be reused when possible for maximum mod compatibility. But if that is not possible a new material can be defined `FabricMaterialBuilder`: 

| Method | Description |
| ------ | ----------- |
| `.burnable()` | makes the block burnable by fire |
| `.lightPassesThrough()` | makes the light pass through the block |
| `.blocksPistons()` | makes the block block the piston when pushed |
| `.destroyedByPiston()` | makes the block break when pushed by pistons |
| `.pistonBehavior(behavior)` | set other `PistonBehavior` |
| `.replaceable()` | makes the block replaceable, like Tall Grass or Vines |
| `.allowsMovement()` | disable collisions for the block |

```java
Material EXAMPLE = new FabricMaterialBuilder(MapColor.BLACK)
	.blocksPistons()
	.burnable()
	.buid();
```

The material can then be used to create [Block Settings](settings.md).
