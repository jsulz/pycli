This is small collection of Python classes that mimic the functionality of core Unix commands.

The primary goal of this repository is to build up the knowledge of these Unix commands while also practicing my Python programming and preparing me to do these same exercises in future languages that I want to learn.

All of these (as well as the idea of practicing on these commands) are inspired by [John Crickett's Coding Challenges](https://codingchallenges.fyi/).

To download this and run it locally, you can either:

- Clone the repository
- Install it as a package using Pipx

If you clone the repository, you must `cd` into the directory where it was downloaded and run `poetry install` (follow these steps to download Poetry on your machine if you do not already have it installed). The commands are then available by using `poetry run pycli <command>`.

If you choose to install this as a package using Pipx, first make sure you have Pipx installed (follow [these steps](https://github.com/pypa/pipx#readme) if not) and then install this repository using the following command:

```shell
$ pipx install git+https://github.com/jsulz/pycli.git
```

Then, you can run each of the supported commands using `pycli <command>`

The current supported Unix commands are:

- `head`
- `cat`
- `wc`
- `cut`

Not all flags are supported, but each command does support the `-h` flag, e.g., `pycli head -h` which will show what options are available.
