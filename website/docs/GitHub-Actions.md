on:
  push:
    branches:
      - main
```

This configuration triggers the workflow to run whenever there is a push to the "main" branch.

### Jobs

Jobs define the tasks that need to be executed as part of the workflow. Each job runs in a separate environment. For example:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

This configuration defines a job named "build" that runs on the latest version of Ubuntu.

### Steps

Steps are the individual tasks that need to be performed within a job. Each step can run a command or execute an action. For example:

```yaml
steps:
  - name: Checkout repository
    uses: actions/checkout@v2
