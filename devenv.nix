{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    package = pkgs.python314;
    uv = {
      enable = true;
      sync.enable = true;
    };
  };

  # https://devenv.sh/services/
  services.nats.enable = true;

  # https://devenv.sh/tasks/
  tasks = {
    "parser:setup".exec = "uv sync";
    "parser:run".exec = "uv run parser";
  };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    uv run pytest
  '';
}
