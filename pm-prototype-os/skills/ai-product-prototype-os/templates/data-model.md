# Logical data model
Why required / why omitted:
Entities, IDs, ownership, tenancy and relationships:
Lifecycle, constraints, retention, security and mock/live indicators:
ERD (when persistent or relational data):
```mermaid
erDiagram
 ORGANIZATION ||--o{ MEMBER : has
 MEMBER ||--o{ DOCUMENT : owns
```
API/data contract references:
