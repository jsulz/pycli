This is a repository designed primarily to help me learn a variety of things (math, Unix commands, classic algorithms, etc) through code. Inside the `pycli` directory are all of the available commands.

To download this and run it locally, you can either:

- Clone the repository
- Install it as a package using Pipx

If you clone the repository, you must `cd` into the directory where it was downloaded and run `poetry install` (follow these steps to download Poetry on your machine if you do not already have it installed). The commands are then available by using `poetry run pycli <command>`.

If you choose to install this as a package using Pipx, first make sure you have Pipx installed (follow [these steps](https://github.com/pypa/pipx#readme) if not) and then install this repository using the following command:

```shell
$ pipx install git+https://github.com/jsulz/pycli.git
```

Then, you can run each of the supported commands using `pycli <command>`

Initially, this began as an exercise in learning Unix commands. As a result, there are a set of commands inside the `pycli` namespace that mirror the Unix functionality provided by that same command.

The current supported Unix commands are:

- `head`
- `cat`
- `wc`
- `cut`
- `uniq`

Not all flags are supported, but each command does support the `-h` flag, e.g., `pycli head -h` which will show what options are available.

Additionally, this is a space where I've spent time learning about Natural Language Processing algorithms. In that vein, following commands are supported:

- `bpe`
- `wordpiece`
