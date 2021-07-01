## Signatures

Method signature takes the following form: `<qualifier><name>(<args>)<return>`
* **qualifier** Optional in most circumstances, the type of the class in which the method is located. For example: `Ljava/lang/String;` to specify the String class.
* **name** The name the method, `<init>` for constructors, `<clinit>` for static constructors.
* **arg** Method argumets, for example: `IIILjava/lang/String;` for `int, int, int, String`.
* **return** Method's return type, for example: `V` for `void`.

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
| **\[** | an array dimension |

Class paths special cases:
* Sub-classes are separated with `$`, `Lnet/minecraft/block/AbstractBlock$Settings;`
* All generics (`Class<T>`) are ignored in signatures, `LClass;`

Examples:
* `method()V` for: `method()`
* `method(III)Ljava/lang/String;` for: `String method(int, int, int)`
* `method([I)Ljava/lang/Object;` for `Object method( int[] )`
* `method(J[B)V` for: `void method(long, byte...)`


