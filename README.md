# expense_notify

Extracts expense data stored in notion, interprets it using LLM Agent and triggers a periodic notification

## Workflow

```mermaid
graph LR
    A[Start] -->|Establish Connection| B{Connect to NotionDB}
    B -->|Load Metadata| C[NotionDataLoader: Load and Process Metadata]
    C -->|Analyze Data| D[DataFrameAnalyzer: Analyze Data]
    D -->|Prepare Message| E[Send Telegram Message]
    E -->|Complete Process| F[End]
    
    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#bbf,stroke:#333,stroke-width:4px
    style C fill:#bbf,stroke:#333,stroke-width:4px
    style D fill:#bbf,stroke:#333,stroke-width:4px
    style E fill:#bbf,stroke:#333,stroke-width:4px
    style F fill:#f9f,stroke:#333,stroke-width:4px

```

## Installation

<!-- ```bash
$ pip install expense_notify
``` -->

## Usage

placebolder


## TODO
- [ ] Work on tests and refactoring
- [ ] Set up CICD
- [ ] Documentation

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`expense_notify` was created by hy. It is licensed under the terms of the MIT license.

## Credits

`expense_notify` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
