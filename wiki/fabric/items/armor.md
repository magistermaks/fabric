## Armor Items
[Back](../fabric.md)

All armor items (helmet, chestplate, leggings, and boots) are created with the same Class - `ArmorItem`. Similarly to [Tool Items](tool.md) a special `ArmorMaterial` must be defined to construct armor items.

Example:
```java
public class ExampleArmorMaterial implements ArmorMaterial {

	// the 'DURABILITY' values are constant for all minecraft armors
    private static final int[] DURABILITY = new int[] {13, 15, 16, 11};
    private static final int[] PROTECTION = new int[] {2, 5, 6, 2};

	// the base number of uses an armor piece has
    public int getDurability(EquipmentSlot slot) {
        return DURABILITY[slot.getEntitySlotId()] * durabilityMultiplier;
    }

	// the base protection an armor piece has
    public int getProtectionAmount(EquipmentSlot slot) {
        return PROTECTION[slot.getEntitySlotId()];
    }
	
	// the enchantability of the material, see table below for reference
    public int getEnchantability() {
        return 12;
    }

	// the sound played when the armor is equipped
    public SoundEvent getEquipSound() {
        return SoundEvents.ITEM_ARMOR_EQUIP_CHAIN;
    }

	// the item used to repair this armor
    public Ingredient getRepairIngredient() {
        return Ingredient.ofItems(Items.DIRT, Items.STONE);
    }

    public String getName() {
        return "my_armor_name";
    }

	// the base toughness an armor piece has
    public float getToughness() {
        return 0;
    }

	// using this property requires mixins, leave at 0 to disable
    public float getKnockbackResistance() {
        return 0;
    }

}
```

Vanilla Armor Materials are stored in the `ArmorMaterials` enum.
Material reference table:
| Material | Durability | Protection | Enchantability | Toughness | Knockback Resistance |
| -------- | ---------- | ---------- | -------------- | --------- | -------------------- |
| **Leather** | 5       | 1, 2, 3, 1 | 15             | 0         | 0                    |
| **Chainmail** | 15    | 1, 4, 5, 2 | 12             | 0         | 0                    |
| **Iron** | 15         | 2, 5, 6, 2 | 9              | 0         | 0                    |
| **Gold** | 7          | 1, 3, 5, 2 | 25             | 0         | 0                    |
| **Diamond** | 33      | 3, 6, 8, 3 | 10             | 2         | 0                    |
| **Turtle** | 25       | 2, 5, 6, 2 | 9              | 0         | 0                    |
| **Netherrite** | 37   | 3, 6, 8, 3 | 15             | 3         | 0.1                  |
> 'Durability' is the `durabilityMultiplier` from `getDurability()`, and `Protection` are the values used in the `PROTECTION` final field.

Then the armor pieces can be created with `ArmorItem` class:
```java
ExampleArmorMaterial MATERIAL = new ExampleArmorMaterial();

Item HELMET = new ArmorItem(MATERIAL, EquipmentSlot.HEAD, new FabricItemSettings().group(ItemGroup.COMBAT));
Item CHESTPLATE = new ArmorItem(MATERIAL, EquipmentSlot.CHEST, new FabricItemSettings().group(ItemGroup.COMBAT));
Item LEGGINGS = new ArmorItem(MATERIAL, EquipmentSlot.LEGS, new FabricItemSettings().group(ItemGroup.COMBAT));
Item BOOTS = new ArmorItem(MATERIAL, EquipmentSlot.FEET, new FabricItemSettings().group(ItemGroup.COMBAT));
```

On how to register those items see: [Items](item.md).

#### Textures
To add a texture to the armor create `<name>_layer_1.png` and `<name>_layer_2.png`, where `<name>` is the string returned by armor material's `getName()`. Those files must then be placed in `resources/assets/minecraft/textures/models/armor/`. as to the contents of those files - you will need to experiment, For reference look at the textures of other armors (the vanilla ones).

#### Knockback Resistance
Knockback resistance is hardcoded into the `ArmorItem` so to enable it for you material a small mixin (Learn more about Mixins here: [Mixins](/wiki/mixins/mixins.md)) will be needed:

```java
@Mixin(ArmorItem.class)
public class ArmorItemMixin {

	// access to the knockbackResistance field
	@Shadow
	@Final
	protected float knockbackResistance;

	// access to the UUIDs of the armor pieces
	@Shadow
	@Final
	private static UUID[] MODIFIERS;

	@Inject(
		// inject into constructor
		method = "<init>(Lnet/minecraft/item/ArmorMaterial;Lnet/minecraft/entity/EquipmentSlot;Lnet/minecraft/item/Item$Settings;)V",
		
		// right before the 'attributeModifiers' is written to
		at = @At(
			value = "FIELD",
			opcode = Opcodes.PUTFIELD,
			target = "Lnet/minecraft/item/ArmorItem;attributeModifiers:Lcom/google/common/collect/Multimap;"
		),
		
		// capture local variable 'builder'
		locals = LocalCapture.CAPTURE_FAILHARD
	)
	private void init(ArmorMaterial material, EquipmentSlot slot, Item.Settings settings, CallbackInfo ci, ImmutableMultimap.Builder<EntityAttribute, EntityAttributeModifier> builder) {
		// perform the modification only for custom material
		if( material instanceof ExampleArmorMaterial ) {
		
			// add Knockback Resistance modifier
			builder.put(
				EntityAttributes.GENERIC_KNOCKBACK_RESISTANCE,
				new EntityAttributeModifier(
					MODIFIERS[slot.getEntitySlotId()],
					"Armor knockback resistance",
					this.knockbackResistance,
					EntityAttributeModifier.Operation.ADDITION
				)
			);
		}
	}

}
```
