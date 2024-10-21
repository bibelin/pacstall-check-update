# Check updates for Pacstall :llama:

This script allows you to check for a pacstall update (currently the script only checks for official releases) and run additional actions.

Download `pacstall-check-update.py`, place it wherever you want and make it executable.

If you simply run the script, it will show a text message if there's an update available. Some options set actions that will happen after that:

* `-1`/`--non-zero` will make the script exit with non-zero exit status if there's an update available. This can be useful for aliases (see below).
* `-u`/`--update` will run `pacstall -U pacstall master` immediately if there's an update available.
* `-n`/`--notify` will show desktop notification if there's an update available. Requires `libnotify-bin` package to be installed.

There are a few more options:

* `--systemd-service {enable,disable}` — enables/disables a systemd user service that will run `pacstall-check-update.py -n` on start (= after login and network connection) and then every 12 hours.
* `--notify-icon ICON_NAME` — changes the icon for notification, works for both `-n` and `--systemd-service enable`.

Examples:

```
alias pacstall='pacstall-check-update.py -1 && pacstall'
```

^ Set this for your shell (in `~/.bashrc` for bash) to prevent running any pacstall command until it will be updated to the latest version (use `pacstall-check-update.py -u` for it).

```
pacstall-check-update.py -n
```

^ If you don't want to use systemd service, add this command to autostart and you will see a notification about an available update on log in.

```
pacstall-check-update.py --systemd-service enable --notify-icon utilities-x-terminal
```

^ Enables systemd service, and notifications sent by it will use `utilities-x-terminal` icon.

![Notification screenshot](notification.png)
