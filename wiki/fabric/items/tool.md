## Tool Items
[Back](../fabric.md)

Tools include items like pickaxes, swords, hoes, etc. They all share one `ToolMaterial` (diamond, iron, gold, etc) but also have certain modifiers unique to each tool (speed, damage).

To create a new tool a `ToolMaterial` will be needed first, this can be one of the materials already defined by the game (those are located in the `ToolMaterials` enum) or a new material:

Example:
```java
public class ExampleToolMaterial implements ToolMaterial {

	// the base number of uses a tool has
	public int getDurability() {
		return 1000;
	}

	// the mining speed, see table below for reference
	public float getMiningSpeedMultiplier() {
		return 6.0f;
	}

	// the base attack damage, every tool has an additional, independent, damage value added
	public float getAttackDamage() {
		return 0;
	}

	// the 'tier' of the tool, where 0 is wood, and 4 is netherite, see MiningLevels enum
	public int getMiningLevel() {
		return MiningLevels.DIAMOND;
	}

	// the enchantability of the material, see table below for reference
	public int getEnchantability() {
		return 12;
	}

	// the item used to repair this material
	public Ingredient getRepairIngredient() {
		return Ingredient.ofItems(Items.DIRT, Items.STONE);
	}

}
```

Material reference table:
| Material | Durability | Mining Speed | Damage | Mining Level | Enchantability |
| -------- | ---------- | ------------ | ------ | ------------ | -------------- |
| **Wood** | 59         | 2.0f         | 0.0f   | 0            | 15             |
| **Stone** | 131       | 4.0f         | 1.0f   | 1            | 5              |
| **Iron** | 250        | 6.0f         | 2.0f   | 2            | 14             |
| **Diamond** | 1561    | 8.0f         | 3.0f   | 3            | 10             |
| **Gold** | 32         | 12.0f        | 0.0f   | 0            | 22             |
| **Netherrite** | 2031 | 9.0f         | 4.0f   | 4            | 15             |


The final attack damage of a tool is calculate by adding material's attack damage and the value passed to the tool constructor:

Example:
```java
ToolItem tool = new ShovelItem( MATERIAL, toolAttackDamage, toolAttackSpeed, settings );
```

The `toolAttackSpeed` is an negative number, for reference Diamond Axe has an attack speed of `-3.0f` (slower) and Diamond Sword of `-2.4f` (faster). Learn about Item Settings here: [Item Settings](settings.md).

Minecraft provides specialized [Item](item.md) classes for creation of tools: `ShovelItem`, `SwordItem`, `PickaxeItem`, `AxeItem`, and `HoeItem`. But three of those have protected constructors (`PickaxeItem`, `AxeItem`, and `HoeItem`) to use them first define those 3 classes:

```java
static final class PublicPickaxeItem extends PickaxeItem {
	public PublicPickaxeItem(ToolMaterial material, int attackDamage, float attackSpeed, Settings settings) {
		super(material, attackDamage, attackSpeed, settings);
	}
}

static final class PublicAxeItem extends AxeItem {
	public PublicAxeItem(ToolMaterial material, float attackDamage, float attackSpeed, Settings settings) {
		super(material, attackDamage, attackSpeed, settings);
	}
}

static final class PublicHoeItem extends HoeItem {
	public PublicHoeItem(ToolMaterial material, int attackDamage, float attackSpeed, Settings settings) {
		super(material, attackDamage, attackSpeed, settings);
	}
}
```

Then, new tool items can be easy created:

```java
ToolMaterial MATERIAL = new ExampleToolMaterial();

public static ToolItem SHOVEL = new ShovelItem(MATERIAL, 1.0f, -3.0F, new FabricItemSettings().group(ItemGroup.TOOLS));
public static ToolItem SWORD = new SwordItem(MATERIAL, 3, -2.4F, new FabricItemSettings().group(ItemGroup.COMBAT));
public static ToolItem PICKAXE = new PublicPickaxeItem(MATERIAL, 2, -2.8F, new FabricItemSettings().group(ItemGroup.TOOLS));
public static ToolItem AXE = new PublicAxeItem(MATERIAL, 4.0F, -3.2F, new FabricItemSettings().group(ItemGroup.TOOLS));
public static ToolItem HOE = new PublicHoeItem(MATERIAL, -3, 0.0f, new FabricItemSettings().group(ItemGroup.TOOLS));
```

On how to register those items see: [Items](item.md).

The last step is to add the tools into the correct Item ~~[Tag](/wiki/json/tags.md)~~ in `/resources/data/fabric/tags/items/`, use `axes.json` for axes, `pickaxes.json` for pickaxes etc. 

Example:
```json
{
	"replace": false,
	"values": [
		"modid:example_pickaxe"
	]
}
```
