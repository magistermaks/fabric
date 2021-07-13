## @At
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/At.html)

Selects an injection point, for usage see: [@Inject](inject.md).

#### Value Property
| Name | Description | Offset | Args |
| ---- | ----------- | ------ | ---- |
| HEAD | Selects first instruction in a method | Before | N/A |
| RETURN | Selects **all** return points | Before | N/A |
| TAIL | Selects the last return point | Before | N/A |
| INVOKE | Selects method calls | Before | `target` full method signature |
| INVOKE_ASSIGN | Selects method calls that get assigned to a variable | **After** | `target` full method signature |
| FIELD | Selects reading and writing to fields | Before | `target` full field signature |
| NEW | Selects constructor calls | Before | `target` class or constructor signature |
| INVOKE_STRING | Selects method calls which takes a single string and returns void | Before | TODO |
| JUMP | Selects jump calls: if, try/catch, break, etc | Before | takes an optional arg `opcode` |
| CONSTANT | selects a constant, similar to [@Constant](constant.md) | Before | takes named args from `args` |

Where `Offset` indicates if the injection point is before or after the section point.
If the selection results in a multiple injection point, `ordinal` property can be used to specify the index of the desired injection point. default value is -1, allowing multiple injection points.

Example:
```java
// Selectes second return instruction
@At(value="RETURN", ordinal=1)
```

Example:
```java
// Selects all calls to `int method(int, int)` from class `Example`
@At(value="INVOKE", target="Lnet/example/Example;method(II)I")
```

#### Shifting
the `shift` property can be set to:
| Name | Description |
| ---- | ----------- |
| NONE | Don't shift, the default value |
| BEFORE | Shift by one instruction back |
| AFTER | Shift by one instruction forward |
| BY | Shift by N instructions, specified with `by` property |

Example:
```java
// Selects one instruction after a method call to 'func()'
@At(value="INVOKE", target="func()V" shift=Shift.BY, by=2)
```
