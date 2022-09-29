# dead_function_finder

Utility to find dead functions within a codebase.

## Languages supported

 - Python
 - PHP

## Usage

```bash
pip3 install .
dead_function_finder --path "~/my/codebase" --language python
```

## Limitations

 - The program searches for unique function names; it is not currently aware of class context.
 - Functions called with magic methods or whose names are dynamically resolved might result in false positives.
