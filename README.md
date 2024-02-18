# muppy

Muppy demonstrates a Python implementation of the map/reduce pattern using the `concurrent.futures` library.

### Prerequisites

- install recommend extension from ./vscode/extensions.json
- install [pipenv](https://pipenv.pypa.io/en/latest/installation.html) and run command:

```sh
pipenv install
```

- start debugging

### Problem 

Optimize task execution for maximum CPU utilization. Here's how:

Glossary:

- `micro-task`: basic calculation unit producing a computed result.
- `task`: contains one or more micro-tasks, each task has its own processing method for micro-task results.

Solution:

Implement the map/reduce pattern.

- Fetch all micro-tasks and execute them using concurrent.futures.
- Ensure each micro-task returns both the calculation result and its corresponding `task ID`.
- Upon completion of micro-tasks, construct the final reduced result based on task IDs.