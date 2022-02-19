{ pkgs ? import <nixpkgs> {} }:

pkgs.python38Packages.buildPythonApplication {
  pname = "nixmyshell";
  src = ./.;
  version = "0.0.1";
}
