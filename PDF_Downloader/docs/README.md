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