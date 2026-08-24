# PM AI Shipping

AI product shipping workflows for intended-vs-implemented review, launch readiness, documentation, test derivation, security checks, and performance checks.

This plugin is part of Sandeep Kumar M's enhanced `pm-skills` fork. It is designed for PMs shipping AI-enabled products who need practical readiness checks, not vague AI strategy language.

## When to use

Use this plugin when you need to:

- review whether the implemented app matches the intended product behavior
- prepare shipping artifacts
- derive tests from product requirements
- document an app
- run static security and performance checks
- identify AI-specific launch risks
- convert prototype output into PM-ready evidence

## Skills included

- `intended-vs-implemented`
- `shipping-artifacts`

## Commands included

- `/derive-tests`
- `/document-app`
- `/performance-audit-static`
- `/security-audit-static`
- `/ship-check`

## Operating rules

1. Distinguish demo quality from production readiness.
2. Test intended behavior, failure behavior, and edge cases.
3. Do not declare security or performance safety from superficial inspection.
4. Flag assumptions and unverified implementation details.
5. Connect findings to launch risk and user impact.
6. Produce concrete fixes, not generic warnings.

## Example use

```text
Use pm-ai-shipping to review this AI prototype before launch. Compare intended behavior with implemented behavior, derive test scenarios, flag security/performance risks, and produce a launch readiness checklist.
```

## Output standard

A strong output from this plugin should include:

- intended behavior
- implemented behavior
- gap analysis
- test scenarios
- launch blockers
- security and performance caveats
- analytics and monitoring recommendations
- final ship/no-ship view

## Attribution

Based on the original `phuryn/pm-skills` AI shipping workflows. Enhanced in this fork with stronger AI PM launch-readiness and evidence discipline.
