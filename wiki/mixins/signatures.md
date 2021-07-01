## Signatures

Method signature takes the following form: `<qualifier><name>(<args>)<return>`
* **qualifier** Optional in most circumstances, the type of the class in which the method is located. For example: `Ljava/lang/String;` to specify the String class.
* **name** The name the method, `<init>` for constructors, `<clinit>` for static constructors.
* **arg** Method argumets, for example: `IIILjava/lang/String;` for `int, int, int, String`.
* **return** Method's return type, for example: `V` for `void`.

| Symbol | Type | Description |
| --- | --- | --- |
| B | byte | signed byte |
| C | char | Unicode character code point in the Basic Multilingual Plane, encoded with UTF-16 |
| D | double | double-precision floating-point value |
| F | float | single-precision floating-point value |
| I | int | integer |
| J | long | long integer |
| Lpath/to/ClassName; | reference | an instance of ClassName |
| S | short | signed short |
| Z | boolean | true or false |
| \[ | reference | one array dimension |

Examples:
* `method()V` for: `method()`
* `method(III)Ljava/lang/String;` for: `String method(int, int, int)`
* `method([I)Ljava/lang/Object;` for `Object method( int[] )`
* `method(J[B)V` for: `void method(long, byte...)`


