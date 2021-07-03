## Mixins
[Back](/README.md)

This article describes how to use Mixins to effectively modify existing classes. Note: The method modifications listed in these articles are more of a reference of what the code effectively does, and not exactly how it does it.

#### Table of Contents
* Basics
	* [@Mixin](mixin.md)
	* [Signatures](signatures.md)
* Injectors
	* [@Overwrite](overwrite.md)
	* [@Inject](inject.md)
	* [@ModifyConstant](modify_constant.md)
	* [@ModifyVariable](modify_variable.md)
	* [@ModifyArgs](modify_args.md)
	* [@ModifyArg](modify_arg.md)
	* [@Redirect](redirect.md)
* Other Annotations
	* [@Constant](constant.md)
	* [@At](at.md)
	* ~~[@Slice](slice.md)~~
	* [@Pseudo](pseudo.md)

Mixin are a powerful tool but sometimes something more is needed. [Access Wideners](access_wideners.md) are not a part of the mixin library, but a tool added in Fabric Loaded 0.8,
they allow to change the access and finality of classes, methods, and fields.
