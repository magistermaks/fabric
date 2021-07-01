## @At
[Back](mixins.md)

Selects an injection point, for usage see: [@Inject](inject.md).

#### Value Property
| Name | Description | Offset |
| --- | --- | --- |
| HEAD | Selects first instruction in a method | N/A |
| RETURN | Selects **all** return points | Before |
| TAIL | Selects the last return point | Before |
| INVOKE | Selects method calls | Before |
| INVOKE_ASSIGN | Selects method calls that get assigned to a variable | **After** |
| FIELD | Selects reading and writing to fields | Before |
| NEW | Selects constructor calls | Before |
| INVOKE_STRING | Selects method calls which takes a single string and returns void | Before |
| JUMP | Selects jump calls: if, try/catch, break, etc | Before |
| CONSTANT | selects a constant, simillar to [@Constant](constant.md) | Before |

Where `Offset` indicates if the injection point is before or after the section point.
If the selection results in a multiple injection point, `ordinal` property can be used to specify the index of the desired injection point. default value is -1, allowing multiple injection points.

Example:
```java
@Inject(method="target(II)V", at=@At("RETURN"), ordinal=1)
public void injection(int a, int b, CallbackInfo info) {
	// code to be injected before the second return
}
```

#### Shifting
the `shift` property can be set to:
| Name | Description |
| --- | --- |
| NONE | Don't shift, the default value |
| BEFORE | Shift by one instruction back |
| AFTER | Shift by one instruction forward |
| BY | Shift by N instructions, specified with `by` property |

Example:
```java
// Selects one instruction after a method call to `func()`
@At(value="INVOKE", target="func()V" shift=Shift.BY, by=2)
```
