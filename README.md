# plot-bot
Create random scripts from a template

## Install
1. `git clone git@github.com:pard68/plot-bot`
2. Profit

## How To
Create a script template and then `python plot-bot.py my/awesome/template`

Templates can consist of three things:
1. Random parts of speech. Any part of speech (noun, verb, adverb, adjective) prefixed with a `$`.
This will result in a random word being selected from the appropriate POS list.
2. Random word from predefined list. Any words in `[brackets]` `seperated|by|pipes` will be parsed as a list
and one word from that list will be randomly selected.
3. Predetermined words. Anything in the template file that isn't prefixed with a `$` or in brackets
will be put directly into the script as a word.

## To Do
- [ ] Punctuation
- [ ] Capitalization

## Credits
The word list was shameless plundered from [Mangle Bot][0]

[0]: https://github.com/RocketBit/mangler-bot
