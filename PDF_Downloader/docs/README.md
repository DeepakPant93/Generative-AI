# Sample Readme

- ![Sequence Diagram](images/sequence-diagram.mermaid)
- [Flow Diagram](images/flow-chart.mermaid)

```mermaid
sequenceDiagram
    participant User
    participant App
    User->>App: Provide URL
    activate App
    App->>requests: Fetch data from URL
    activate requests
    requests-->>App: Return data
    deactivate requests
    App->>pdf_converter: Convert data to PDF
    activate pdf_converter
    pdf_converter-->>App: Return PDF
    deactivate pdf_converter
    App->>filesystem: Save PDF to 'pdf_downloads'
    activate filesystem
    filesystem-->>App: Confirmation
    deactivate filesystem
    App-->>User: PDF Downloaded
    deactivate App
```

Here is the markdown code to match the styling and content you provided:


# MLflow Models Lifecycle

[![Docs](https://img.shields.io/badge/DOCS-LATEST-brightgreen)](https://mlflow.org/docs/latest/index.html)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Downloads](https://img.shields.io/badge/Downloads-3.9M/week-brightgreen)](https://mlflow.org)
[![Slack](https://img.shields.io/badge/Slack-%40mlflow--users-purple)](https://mlflow.org)
[![Follow @mlflow](https://img.shields.io/twitter/follow/mlflow?style=social)](https://twitter.com/mlflow)

## Packages

| Repository      | Version |  Package |
| --------------- |:-------:|:--------:|
| **PyPI**        | [v2.17.0](https://pypi.org/project/mlflow/) | [MLflow-skinny v2.17.0](https://pypi.org/project/mlflow-skinny/) |
| **conda-forge** | [v2.17.0](https://anaconda.org/conda-forge/mlflow) | [MLflow-skinny v2.17.0](https://anaconda.org/conda-forge/mlflow-skinny) |
| **CRAN**        | [v2.16.2](https://cran.r-project.org/package=mlflow) | |
| **Maven Central**| [MLflow-client v2.17.0](https://mvnrepository.com/artifact/org.mlflow/mlflow-client) | [MLflow-parent v2.17.0](https://mvnrepository.com/artifact/org.mlflow/mlflow-parent) <br/> [MLflow-scoring v2.17.0](https://mvnrepository.com/artifact/org.mlflow/mlflow-scoring) <br/> [MLflow-spark v2.17.0](https://mvnrepository.com/artifact/org.mlflow/mlflow-spark) |

## Job Statuses

| Task               | Status |
| ------------------ |:------:|
| **Examples**       | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Cross Version Tests** | ![failing](https://img.shields.io/badge/failing-red) |
| **R-devel**        | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Test Requirements** | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Stale**          | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Push-Images**    | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Slow-tests**     | ![passing](https://img.shields.io/badge/passing-brightgreen) |
| **Website-E2E**    | ![passing](https://img.shields.io/badge/passing-brightgreen) |

You can replace the URLs in the brackets with actual links from your project if necessary. The shields are generated using standard badge creation from shields.io.