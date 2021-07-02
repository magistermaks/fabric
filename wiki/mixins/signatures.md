## Signatures
[Back](mixins.md)

Signatures in java are strings identifing methods, classes, and fields, those strings are commony used when working with mixins, this article describes how those strings are formmated and how to write thaem based on a method/field definition. 

**Note:** If you are using IDEA with the [Minecraft Development](https://github.com/minecraft-dev/MinecraftDev) as recomended by our [Setup Guide](/basics/setup/ide.md) you can right click on a method or field usage/definition and select `Copy Mixin Targe Reference` to get the correct signature.

* Method signature: `<qualifier><name>(<args>)<return>`
* Field signature: `<qualifier><name>:<return>`
* Class signature: `<qualifier>` *(in this signature the `L` and `;` are omitted)*

`<qualifier>` - Optional in most circumstances, used only for full signatures. The type of the class in which the method is located. For example: `Ljava/lang/String;` to specify the String class.  
`<name>` - The name the method, `<init>` for constructors, `<clinit>` for static constructors.  
`<args>` - Method argumets, for example: `IIILjava/lang/String;` for `int, int, int, String`.  
`<return>` - Method's return type, for example: `V` for `void`.  

| Symbol | Type |
| --- | --- | 
| **B** | `byte` | 
| **C** | `char` | 
| **D** | `double` |
| **F** | `float` |
| **I** | `int` |
| **J** | `long` |
| **Lpath/to/ClassName;** | `ClassName` |
| **S** | `short` |
| **Z** | `boolean` |
| **\[** | array dimension |

Special cases:
* Sub-classes are separated with `$`, `Lnet/minecraft/block/AbstractBlock$Settings;`
* All generics (`Example<T>`) are ignored in signatures, `Lnet/example/Example;`
* VarArgs (`int...`) are represented by arrays, `[I`

Examples:
* `method()V` for: `method()`
* `method(III)Ljava/lang/String;` for: `String method(int, int, int)`
* `method([I)Ljava/lang/Object;` for: `Object method( int[] )`
* `method(J[B)V` for: `void method(long, byte...)`
* `method(I[DLjava/lang/Thread;)Ljava/lang/Object;` for: `Object method(int i, double[] d, Thread<T> t)`
* `Lnet/example/Example;field:I` for: `int field` in class `Example`
* `net/example/Example` for: `class Example`


