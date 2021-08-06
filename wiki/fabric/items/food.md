## Food Items
[Back](../fabric.md)

To make an item edible add a food component to it with the [Item Settings](settings.md) `.food(food)` method.

To create a food component use `FoodComponent.Builder` class:
```java
FoodComponent food = new FoodComponent.Builder()
```

| Method | Description |
| ------ | ----------- |
| `.hunger(int)` | one 'hunger' restores half of a hunger bar icon |
| `.saturationModifier(float)` | the [Saturation](https://minecraft.fandom.com/wiki/Hunger#Mechanics) of a food item |
| `.meat()` | marks meat-like foods, only meat foods can be feed to a dog |
| `.alwaysEdible()` | allows the food to be eaten even if the player isn't hungry |
| `.snack()` | shortens eating time |
| `.statusEffect(effect, chance)` | apply status effect when eaten, `chance` is a value between `0` and `1` |

Example:
```java
FoodComponent FOOD_COMPONENT = new FoodComponent.Builder()
	.hunger(1).
	.saturationModifier(0.6F)
	.statusEffect(new StatusEffectInstance(StatusEffects.HUNGER, 600, 0), 0.8F)
	.meat()
	.build();
	
// create the food item
Item FOOD_ITEM = new Item( new FabricItemSettings().food(FOOD_COMPONENT) );
```
