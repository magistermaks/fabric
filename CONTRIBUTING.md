## The Contributing Guide

Do you have some knowledge you would like to share? Fix some errors or typos? Or maybe you have a spare star to give? Don't hesitate to write issues and open pull requests! Here are some guidelines on how to contribute to the project:

#### Style
The style of the wiki should be kept consistent on all articles.
* Avoid using ordered lists, if the order of the points is not important. This can minimize the amount of Merge Conflicts.
* The first line must be a title of the article, the second, a link to go back to the parent article, and third must be empty.
* Keep all the resources (pictures, etc) in the `/assets` directory.
* Make sure all articles are approachable even for people with very limited knowledge, provide links to articles about all mentioned concepts.
* Provide full examples, examples are usually the best way to describe something.
* Stay on topic, full examples are good but make sure that they don't spiral into explaining other unrelated things
* Use links, every time you reference something provide a relevant link
* Don't copy-paste, write your own explanations, don't copy javadocs or other wikis, _especially from the Official Fabric Wiki whose license is incompatible!_
* Avoid using _we_, _our_.
* Don't use the \` char (backtick) inside of multiline block comments
* Use proper Github markdown - see [here](https://guides.github.com/features/mastering-markdown/).
* Check your grammar, you can use the `utils/check.sh` script to scan the repo for possible errors, add false-positives to `utils/exceptions.dict`.
* Use `TODO` and `FIXME` to mark unfinished/invalid sections.

#### What can i do?
We accept any help, but if you don't have an idea what to do, you can run the spell checking script `utils/check.sh`, it will list all usages of words `TODO` and `FIXME`
 as warnings. 
 
_This article, and the wiki as a whole is still very WIP, expect unannounced changes._
