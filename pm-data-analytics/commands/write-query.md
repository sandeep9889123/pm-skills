---
description: Generate defensible SQL from natural language with verified schema mapping, metric definitions, join/cardinality checks, and validation queries
argument-hint: "<what you want to know, in plain English>"
---

# /write-query -- Defensible SQL Query Generator

Translate a business question into SQL without inventing schema or hiding business-logic assumptions.

## Step 1: Define the Decision and Metric

Resolve:

- what decision/question the result supports
- output grain
- metric definition(s)
- time range / timezone
- filters / segments
- SQL dialect

Ambiguous terms such as `active`, `conversion`, `churn`, `revenue`, `customer`, or `session` must be defined before decision-critical SQL is treated as final.

## Step 2: Verify Schema

If schema/DDL/docs are available:

- map concepts to verified tables/columns
- identify keys/relationships
- note data types where relevant

If schema is missing:

- **do not infer plausible SaaS tables and present them as real**
- return `STATUS: TEMPLATE - SCHEMA NOT VERIFIED`
- use explicit placeholders such as `<users_table>`
- list the schema mappings required before execution

## Step 3: Generate SQL

Apply **sql-queries**.

Required safeguards:

- correct dialect or portable syntax if dialect unknown
- readable CTEs
- NULL/timezone handling
- duplicate/deduplication logic where needed
- join cardinality check
- explicit business assumptions
- read-only `SELECT` by default

Do not call the query production-ready unless schema and metric definitions were verified.

## Step 4: Validation

Provide one or more checks appropriate to the risk:

- row counts before/after joins
- duplicate-key check
- distinct entity count
- denominator reconciliation
- known-record spot check
- boundary-date/timezone check
- comparison against a trusted source
- dry-run / query plan where supported

Never fabricate execution results.

## Output

### Status
`VERIFIED SCHEMA | PARTIALLY VERIFIED | TEMPLATE - SCHEMA NOT VERIFIED | BLOCKED`

### Business / Metric Contract
[what the query actually means]

### Schema Mapping
| Concept | Table.Column | Status |
|---|---|---|

### SQL
[verified query or clearly labeled template]

### Validation Checks
[queries/checks]

### Assumptions / Unknowns
[what could make result wrong]

### Safety / Performance Notes
[only verified or explicitly proposed]

If a schema assumption remains material, do not hide it in a comment and present the query as final.
