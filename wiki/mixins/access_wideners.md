## Access Wideners
[Back](mixins.md)

Access Wideners can be used to:
* Make a private class, method, or fields public
* Make a final class, method, or fields non-final

Access Widener is a file that should be placed in the `resources` directory, and have `.accesswidener` extension. 

The first line in this file should be: `accessWidener   v1   <namespace>` where `<namespace>` is the name of the mapping used, for the default yarn mapping use: `named`. The file can contain empty lines and comments starting with the `#` symbol.

Each modification must be placed in a separate line:
Class: `<access>   class   <class>`,
Method: `<access>   method   <class>   <name>   <descriptor>`,
Field: `<access>   field   <class>   <name>   <descriptor>`

`<access>` value:
* `extendable` removes the `final` keyword from class or method
* `accessible` removes the `private` keyword from the target
* `mutable` removes the `final` keyword from field

`<class>` is the class in with target is located
`<name>` is the name of the filed or method
`<descriptor>` is the field or method descriptor (the entire part after the method name in its [Signature](signatures.md))

The location of Access Widener must be specified in `build.gradle` in `minecraft` task:
```gradle
minecraft {
    accessWidener = file("src/main/resources/modid.accesswidener")
}
```

... and in `modid.mod.json` in the root object:
```json
{
	"accessWidener": "modid.accesswidener",
	...
}
```

**Note:** For Access Widener changes to be visible in the decompiled source, re-run the `genSources` gradle task. 

Example:
```
accessWidener   v1   named

# Remove private keyword from subclass net.example.Example.SubClass
accessible   class   net/example/Example$SubClass

# Remove private keyword from method `void net.example.Example.target( int, int, int )`
accessible   method   net/example/Example   target   (III)V
```


