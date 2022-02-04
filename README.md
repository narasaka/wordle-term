# wordle-term
displays the word of the day for the [viral wordle game](https://powerlanguage.co.uk/wordle) in your terminal when it starts.
<br>
i made this purely out of boredom.
<br>
don't flame me.

## install
source wordle.sh at the end of your rc files (zshrc, bashrc, etc.)
<br>
generally it goes like: open your rc file -> "reference" the wordle.sh file.
<br>
for example, you can do this:
```
cd $HOME
git clone git@github.com:narasaka/wordle-term.git
chmod +x wordle/wordle.sh
echo "\n. $HOME/wordle/wordle.sh\n" >> .zshrc
```
or if you prefer to do it manually:
```
git clone git@github.com:narasaka/wordle-term.git
cd wordle
chmod +x wordle.sh
```
and then assuming that you cloned in your home directory, add this to your rc file:
```
. $HOME/wordle/wordle.sh
```

## other things to note
- i made the script to run only ONCE per day so it will not show up if you create other terminal sessions
- the wordle.sh assumes that your starting directory is $HOME, change it if that's not your preference
- i don't know what to do with windows systems as i don't use them, so please fork if you want this on powershell or something :)
- if you can make the installing tutorial above better or more complete, i would highly appreciate if you contribute!
- yeah
