# Check updates for Pacstall :llama:

This script allows you to check for a pacstall update (currently the script only checks for official releases) and run additional actions.

Download `pacstall-check-update.py`, place it wherever you want and make it executable.

If you simply run the script, it will show a text message if there's an update available. Options set actions after it:

* `-1`/`--non-zero` will make the script exit with non-zero exit status if there's an update available. This can be useful for aliases (see below).
* `-u`/`--update` will run `pacstall -U pacstall master` immediately if there's an update available.
* `-n`/`--notify` will show desktop notification if there's an update available. Requires `libnotify-bin` package to be installed.

Examples:

```
alias pacstall='pacstall-check-update.py -1 && pacstall'
```

^ Set this for your shell (in `~/.bashrc` for bash) to prevent running any pacstall command until it will be updated to the latest version (use `pacstall-check-update.py -u` for it).

```
pacstall-check-update.py -n
```

^ Add this command to autostart and you will see a notification about an available update on log in.
