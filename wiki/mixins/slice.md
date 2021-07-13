## @Slice
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/injection/Slice.html)

Allows for a more specific injection, it specifies a range in with the selection can be made. `from` marks the starting position, and `to` marks the ending position. Read more about [@Inject](inject.md).

Example:
```java
@Inject(slice=@Slice(from=@At(...), to=@At(...)), at = @At(...))
```
