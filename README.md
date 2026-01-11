
# subj-reader

Small CLI utility that subscribes to one or more **Almanach** topics and logs every received message.

It is a thin wrapper around [`almanach.AlmanachSubscriber`](https://github.com/bateau-ais/almanach) and is useful for quickly “tailing” messages from a broker during development.

## Requirements

- Python $>= 3.14$ (required by `almanach`)
- Network access / broker configuration as required by `almanach`

## Install

This repo is set up to be used with `uv`.

```zsh
cd /home/safenein/Repos/nova-tools/subj-reader
uv sync
```

If you prefer pip (not the recommended path for this repo’s current setup), install in a virtualenv and ensure `almanach` is available.

## Usage

The CLI takes one or more topic names and prints/logs each received message.

```zsh
uv run python main.py some.topic another.topic
```

### Wildcards (NATS)

Topics support native NATS wildcards (e.g. `*` and `>`). Example:

```zsh
uv run python main.py 'nats://127.0.0.1/raw_ais.*' --key=msg-uuid
```

### Options

- `--key`: currently parsed but not used by the program (default: `msg_uuid`). It is reserved for future filtering/formatting.

Example:

```zsh
uv run python main.py some.topic --key msg_uuid
```

## What it does

- Creates an `AlmanachSubscriber`
- Subscribes a handler to the given topics
- Logs each message at INFO level
- Runs the subscriber loop until interrupted

## Development

Run locally:

```zsh
uv run python main.py some.topic
```

Notes:

- Logging is configured to INFO when executed as a script.
- If you need structured output or filtering, the handler in `main.py` is the place to adapt.

