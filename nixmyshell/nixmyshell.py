import argparse
import os
import sys

HEADER = ("{ pkgs ? import <nixpkgs> {} }:\n"
          "pkgs.mkShell {\n"
          "  nativeBuildInputs = with pkgs; [ \n")
FOOTER = "  ];\n}\n"
FILE_NAME = "shell.nix"


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("packages", nargs="*", metavar=("packages"),
                        help="Packages you want to add to nix-shell")
    parser.add_argument("-p", "--path", nargs="?",
                        metavar="path", default=None,
                        help="Path of the directory to create shell.nix for")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force creation of a new shell.nix")

    args = parser.parse_args()
    try:
        file_path = check_path(args.path, args.force)
    except OSError as e:
        print(e)
        sys.exit(1)
    write_file(file_path, args.packages)


def check_path(in_path, force):
    if in_path is not None:
        dest = in_path
        if os.path.exists(dest) and os.path.isdir(dest):
            file_path = os.path.join(dest, FILE_NAME)
            if os.path.exists(file_path) or force:
                raise OSError("Existing shell.nix file in " + dest)
        else:
            raise OSError("There is no such directory: " + dest)
    elif not os.path.exists(FILE_NAME) or force:
        file_path = FILE_NAME
    else:
        raise OSError("Existing shell.nix file in current directory")
    return file_path


def write_file(file_path, packages):
    with open(file_path, "w") as nix_file:
        nix_file.write(HEADER)
        for p in packages:
            nix_file.write(" " * 4 + p + "\n")
        nix_file.write(FOOTER)
