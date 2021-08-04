## The Contributing Guide

Do you have some knowledge you would like to share? Fix some errors or typos? Or maybe you have a spare star to give? Don't hesitate to write issues and open pull requests! Here are some guidelines on how to contribute to the project:

#### Style
The style of the wiki should be kept consistent on all articles.
* Avoid using ordered lists, if the order of the points is not important. This can minimize the amount of Merge Conflicts.
* The first line must be a title of the article. The second, a link to go back to the parent article, it can also contain related links - like a link to java doc or source material. Leave the third line empty.
* Keep all the resources (pictures, etc) in the `/assets` directory.
* Make sure all articles are approachable even for people with very limited knowledge, provide links to articles about all mentioned concepts.
* Provide full examples, examples are usually the best way to describe something.
* Stay on topic, full examples are good but make sure that they don't spiral into explaining other unrelated things
* Use links, every time you reference something provide a relevant link
* Don't copy-paste, write your own explanations, don't copy javadocs or other wikis, _especially from the Official Fabric Wiki whose license is incompatible!_
* Try to avoid using _we_ and _our_.
* Don't use the \` char (backtick) inside of multiline code blocks
* Use proper Github markdown - see [here](https://guides.github.com/features/mastering-markdown/).
* Check your grammar, you can use the `utils/check.sh spell` command to scan the repo for possible errors, add false-positives to `utils/exceptions.dict`.
* Use `TODO` and `FIXME` to mark unfinished/invalid sections.

#### What can I do?
We accept any help, but if you don't have an idea what to do, you can run the spell checking script `utils/check.sh spell`, it will list all usages of words `TODO` and `FIXME` as warnings.

#### Why?
"*Isn't there an XYZ Wiki? Why don't you contribute to that?*" I hear you ask, actually there are reasons why I started this project:
* Regarding *Fabric Wiki*:
	* The wiki system used by Fabric Wiki is terrible in my opinion
	* Markdown/Github combo is easier to maintain and contribute to (for example: branches can be used to create separate wikis for separate versions)
	* Fabric Wiki uses a restrictive non-foss license CC BY-NC-SA 4.0 (no commercial use), mine is free, some peoples (including me) value that
* Regarding *Mixin Cheatsheet*
	* It's a cheat sheet, while I prefer more in-depth explanations
 
> This article, and the wiki as a whole is still very WIP, expect unannounced changes.
