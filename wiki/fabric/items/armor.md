## Armor Items
[Back](../fabric.md)

All armor items (helmet, chestplate, leggings, and boots) are created with the same Class - `ArmorItem`. Similarly to [Tool Items](tool.md) a special `ArmorMaterial` must be defined to construct armor items.

Example:
```java
public class ExampleArmorMaterial implements ArmorMaterial {

    private static final int[] DURABILITY = new int[] {169, 195, 208, 143};
    private static final int[] PROTECTION = new int[] {2, 5, 6, 2};

	// the base number of uses an armor piece has
    public int getDurability(EquipmentSlot slot) {
        return DURABILITY[slot.getEntitySlotId()];
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

Then the armor pieces can be created with `ArmorItem` class:
```java
ExampleArmorMaterial MATERIAL = new ExampleArmorMaterial();

Item HELMET = new ArmorItem(MATERIAL, EquipmentSlot.HEAD, new FabricItemSettings());
Item CHESTPLATE = new ArmorItem(MATERIAL, EquipmentSlot.CHEST, new FabricItemSettings());
Item LEGGINGS = new ArmorItem(MATERIAL, EquipmentSlot.LEGS, new FabricItemSettings());
Item BOOTS = new ArmorItem(MATERIAL, EquipmentSlot.FEET, new FabricItemSettings());
```

On how to register those items see: [Items](item.md).

#### Textures
To add a texture to the armor create `<name>_layer_1.png` and `<name>_layer_2.png`, where `<name>` is the string returned by armor material's `getName()`. Those files must then be placed in `resources/assets/minecraft/textures/models/armor/`. as to the contents of those files - you will need to experiment, For reference look at the textures of other armors (the vanilla ones).

**TODO** knock back stuff
