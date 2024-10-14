#!/usr/bin/env python3
import argparse, urllib.request, json, subprocess

notification_icon='update-notifier'

parser = argparse.ArgumentParser(description='A script to check for the pacstall update. Flags, except "-h", set actions to do if there\'s an update available:', epilog='https://github.com/bibelin/pacstall-check-update')
parser.add_argument('-u', '--update', help='run "pacstall -U"', action='store_true')
parser.add_argument('-1', '--non-zero', help='return non-zero exit status', action='store_true')
parser.add_argument('-n', '--notify', help='send desktop notification', action='store_true')
args = parser.parse_args()

new_version = ""
with urllib.request.urlopen('https://api.github.com/repos/pacstall/pacstall/releases?page=1&per_page=1') as url:
    data = json.load(url)
    new_version = data[0]['tag_name']

pacstall_v = subprocess.check_output(['pacstall', '-V'])
current_version = pacstall_v.decode('utf-8').split()[0]

if current_version != new_version:
    print(f'\033[93mPacstall\033[0m can be updated to version \033[1m{new_version}\033[0m')
    if args.notify:
        subprocess.run(['notify-send', '-i', notification_icon, 'Pacstall update available', f'New version: {new_version}'])
    if args.update:
        print('Executing "pacstall -U"...')
        subprocess.run(['pacstall', '-U', 'pacstall', 'master'])
    if args.non_zero:
        exit(1)
exit(0)
