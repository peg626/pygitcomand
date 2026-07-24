import argparse
import os
import subprocess
parser = argparse.ArgumentParser(prog="pygit")
sub = parser.add_subparsers(dest='command')
def grun(*args):
    
    subprocess.run(["git", *args])
def cmd_init(args):
    grun("init")
def cmd_remote_set(args):
    grun("remote","add",args.name,args.remote)
def cmd_add(args):
    grun("add", args.path)
    if args.commit:
        grun("commit", "-m", args.commit)
def cmd_publish(args):
    if args.push:
        grun("pull", args.repo)
    grun("push", args.repo)
def main():
    p_init = sub.add_parser('register', help='Initialize a new repo')
    p_init.set_defaults(func=cmd_init)
    p_remote = sub.add_parser('remote', help="Remote")
    p_r_cmd = p_remote.add_subparsers(dest='rc')
    p_r_add = p_r_cmd.add_parser('add', help='add a new remote')
    p_r_add.set_defaults(func=cmd_remote_set)
    p_r_add.add_argument('name', help="Remote name")
    p_r_add.add_argument('remote', help="Remote url")
    p_add = sub.add_parser('add', help="add a path to the repo. use '.' to here")
    p_add.set_defaults(func=cmd_add)
    p_add.add_argument('path', help='path. use "." to here')
    p_add.add_argument('-c',"--commit",help="commit message")
    p_p = sub.add_parser('publish', help='Publish the repo. use -p or --pull to use pull')
    p_p.set_defaults(func=cmd_publish)
    p_p.add_argument('repo', help='Remote name')
    p_p.add_argument('-p', "--pull", help="Pull before")
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()