---
name: sql-queries
description: "Generate SQL from natural-language questions with schema verification, metric-definition checks, join/cardinality safeguards, dialect awareness, and validation queries. Never invents tables/columns as if they exist. Use for product analytics, reports, database exploration, or translating business questions into SQL."
---

# SQL Query Generator

## Purpose

Translate a business/data question into SQL for `$ARGUMENTS` while keeping **schema facts, business-logic assumptions, and executable certainty separate**.

A syntactically valid query can still answer the wrong business question. Correctness therefore requires both SQL logic and metric/data-contract validation.

## P0 Reliability Contract

### Hard rules

1. **Never invent a table, column, relationship, enum value, event name, or data type and present it as verified schema.**
2. If schema is missing, either request it when required or provide a clearly labeled **TEMPLATE / PSEUDOSCHEMA QUERY** with placeholders to replace.
3. **Do not call a query production-ready unless the relevant schema and business definitions were verified.**
4. Ambiguous metrics such as `active user`, `conversion`, `churn`, `revenue`, `customer`, or `session` require an explicit definition before a decision-critical query.
5. **Join cardinality must be considered.** Many-to-many or one-to-many joins can silently multiply rows and corrupt counts/sums.
6. Default to read-only `SELECT` analysis. Do not generate destructive or mutating SQL (`DELETE`, `UPDATE`, `DROP`, broad `INSERT`, permission changes) unless the user explicitly requests it and the impact/scope is clear.
7. Tool/database execution failure means `NOT VALIDATED`, not success.
8. Never fabricate query results.

## Step 1: Resolve Decision and SQL Dialect

Capture:

- business question / decision
- SQL dialect/version if material
- desired output grain
- time range / timezone
- filters / segment definitions
- metric definitions
- expected result shape

If dialect is unknown, avoid dialect-specific syntax or label alternatives.

## Step 2: Schema Evidence Gate

Use only verified schema from:

- DDL / schema docs
- database metadata
- user-provided table/column descriptions
- connected data catalog

Create a mapping:

| Business concept | Verified table.column | Evidence | Unknown / assumption |
|---|---|---|---|

If a required mapping is unknown, do **not** hallucinate it.

### No-schema mode

Return:

`STATUS: TEMPLATE - SCHEMA NOT VERIFIED`

Use obvious placeholders such as:

- `<users_table>`
- `<user_id_column>`
- `<signup_timestamp>`

and list exactly what must be mapped before execution.

## Step 3: Define Metric Logic Before SQL

For every decision-critical metric specify:

- entity / grain
- numerator
- denominator
- inclusion/exclusion
- time window
- timezone
- deduplication rule
- status/refund/cancellation handling if relevant

Examples:

`DAU = distinct eligible user_id with qualifying core event during local calendar day`

not merely:

`COUNT(DISTINCT user_id)`

when “qualifying event” is undefined.

## Step 4: Join and Grain Check

Before writing the final aggregation, identify:

- base grain of each table
- join key(s)
- expected relationship: 1:1, 1:N, N:1, N:N
- duplicate risk
- whether aggregation must occur before joining

For high-risk sums/counts, include a validation query or sanity check for row multiplication.

## Step 5: Generate SQL

Prefer:

- readable CTEs
- explicit columns over `SELECT *` for stable analytical outputs
- safe date/time handling
- explicit NULL semantics
- explicit deduplication when required
- parameterization/placeholders for reusable filters
- comments for business logic, not obvious syntax

Do not suggest indexes/partition strategies as verified facts without schema/engine evidence. Label optimization ideas as proposals.

## Step 6: Validation Plan

Provide checks appropriate to the query:

- row count before/after joins
- distinct entity count
- duplicate-key check
- null-rate check
- denominator reconciliation
- known-account/user spot check
- boundary-date/timezone check
- comparison with trusted dashboard/source if available
- dry run / explain plan where supported

For financial or externally reported metrics, require stronger reconciliation before trusting output.

## Step 7: Data Safety and Privacy

When the query handles sensitive fields:

- return only columns needed for the decision
- avoid exposing raw PII when aggregation/anonymization suffices
- preserve access-control constraints
- do not infer permission to query restricted datasets

## Output

### Status
`VERIFIED SCHEMA | PARTIALLY VERIFIED | TEMPLATE - SCHEMA NOT VERIFIED | BLOCKED`

### Business / metric contract
[definitions and assumptions]

### Schema mapping
[verified vs unknown]

### SQL
[query or clearly labeled template]

### Validation queries / checks
[how to prove the output is plausible]

### Assumptions and unknowns
[what could change the answer]

### Performance / safety notes
[only evidence-supported or explicitly proposed]

Never imply successful execution unless the query was actually executed and results were observed.

---

### Further Reading

- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [How to Become a Technology-Literate PM](https://www.productcompass.pm/p/how-to-become-a-technology-literate)
