## Mixin Plugins
[Back](mixins.md) [Javadoc](https://jenkins.liteloader.com/view/Other/job/Mixin/javadoc/org/spongepowered/asm/mixin/extensibility/IMixinConfigPlugin.html)

This feature of Mixin Library is not officially supported by Fabric Loader (but will work anyway). It can be used to disable or enable mixins at runtime.

**Warning:** Never access any game classes from within the Mixin Plugin, as it will make all mixins targeting them fail!

The Mixin Plugin class must be defined in the mixin config with the `plugin` key:
```patch
{
+	"plugin": "path.to.ExampleMixinPlugin"
}
```

Example:
```java 
public class ExampleMixinPlugin implements IMixinConfigPlugin {
	
	// initialize your plugin here
	// mixinPackage is the value read from "package" field in mixin.json file
	public void onLoad(String mixinPackage) {
	 
	}
	
	// get the path to the refmap file
	// return null to use the default file
	public String getRefMapperConfig() {
		
	}
	
	// decide if mixin 'mixinClassName' targeting 'targetClassName' should be applied
	// return true to apply @Override
	public boolean shouldApplyMixin(String targetClassName, String mixinClassName) {
	
	}
	
	// allows for removing mixins based on their target by removing that target from 'myTargets'
	// 'otherTargets' contains the list of all other targets of all other mixins
	public void acceptTargets(Set<String> myTargets, Set<String> otherTargets) {

	}

	// return a list of additional mixin classes to apply
	// or return null to only use the ones listed in mixin.json
	public List<String> getMixins() {
		return null;
	}
	
	// called before the class is mixed
	// can be used for some ASM fuckery
	public void preApply(String targetClassName, ClassNode targetClass, String mixinClassName, IMixinInfo mixinInfo) {

	}

	// called after the class is mixed
	// can be used for some ASM fuckery
	public void postApply(String targetClassName, ClassNode targetClass, String mixinClassName, IMixinInfo mixinInfo) {

	}
	
}
```

