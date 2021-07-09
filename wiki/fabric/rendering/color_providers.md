## Color Providers
[Back](../fabric.md)

Those are lambdas used to add tint to textures of blocks or items, this is the mechanism used by grass blocks to change color depending on the biome. This system is client-side only.

```java
// BlockColorProvider
ColorProviderRegistry.BLOCK.register( (blockState, blockRenderView, blockPos, tintIndex) -> 0xFF0000, blocks... );

// ItemColorProvider
ColorProviderRegistry.ITEM.register( (itemStack, tintIndex) -> 0xFF0000, items... );
```

**Note:** It's also required to add a tint index to every face in the mode file using the `tintindex` property.

Example:
```json
{
	"parent": "block/block",
	"textures": {
		"all": "block/white_wool",
		"particle": "#all"
	},
	"elements": [
		{
			"from": [ 0, 0, 0 ],
			"to": [ 16, 16, 16 ],
			"faces": {
				"down": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 },
				"up": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 },
				"north": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 },
				"south": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 },
				"west": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 },
				"east": { "uv": [ 0, 0, 16, 16 ], "texture": "#all", "tintindex": 0 }
			}
		}
	]
}
```
