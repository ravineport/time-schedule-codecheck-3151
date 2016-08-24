# CLI Applications with Python3

Here's how to build your codecheck challenge solution as a CLI application.  

## Requirements

- Python3 (For the version see our [docs](https://code-check.github.io/docs/en/reference_users/#serverside-language-and-tool-versions) .)
- The standard library's [`argparse`](https://docs.python.org/3.5/library/argparse.html) module

## Recieve Inputs

In [app/app.py](app/app.py) is a function called `main`.
Build your console application there.  

``` python
def main(args, options):
  for arg in args:
    # Replace below line with your code.
    result = arg
```

All `stdin` input arguments are passed into `args` as an array.  

If you want to use optional arguments, add them using `argparse`'s `parser.add_argument` in [cli.py](cli.py)

## Output Results
Use the standard `print()` method to output results to `stdout`.

``` python
  print(result)
```

## Install External Libraries
If you want to use external libraries, do the following:

- Write the library name and version in [requirements.txt](requirements.txt)
- Add the following to [codecheck.yml](codecheck.yml):

``` yaml
build:
  - pip3 install -r requirements.txt
```
