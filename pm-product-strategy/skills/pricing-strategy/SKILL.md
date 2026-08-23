---
name: pricing-strategy
description: "Analyze and design pricing strategies including pricing models, competitive pricing analysis, willingness-to-pay estimation, and price elasticity. Use when setting prices, evaluating pricing models, preparing for a pricing change, or comparing freemium vs paid approaches."
---

## Pricing Strategy

Design a pricing strategy grounded in value delivery, competitive positioning, and willingness to pay.

### Context

You are developing a pricing strategy for **$ARGUMENTS**.

If the user provides files (competitor pricing, survey data, financial models, or usage data), read them first. Use web search to research competitor pricing if needed.

### Instructions

1. **Understand the value delivered**:
   - What is the core value proposition?
   - What is the customer's alternative (and its cost)?
   - What quantifiable outcomes does the product deliver? (time saved, revenue gained, cost reduced)
   - What is the customer's willingness to pay based on that value?

2. **Evaluate pricing models** — recommend the best fit:

   | Model | Best For | Example |
   |---|---|---|
   | **Flat-rate** | Simple products, predictable costs | Basecamp |
   | **Per-seat** | Collaboration tools, team products | Slack, Figma |
   | **Usage-based** | Infrastructure, API products | AWS, Twilio |
   | **Tiered** | Products with distinct user segments | Most SaaS |
   | **Freemium** | Products with viral/network effects | Spotify, Notion |
   | **Freemium + usage** | Platform products | Vercel, OpenAI API |
   | **Value-based** | High-impact enterprise tools | Enterprise software/services |

3. **Analyze competitive pricing**:
   - Map competitor pricing tiers and what's included
   - Identify where your product sits (premium, mid-market, budget)
   - Find pricing gaps or opportunities
   - Note any industry pricing conventions

4. **Design the pricing structure**:
   - **Tiers**: Define 2-4 tiers with clear differentiation
   - **Feature gating**: Which features go in which tier? Use value metrics, not arbitrary limits
   - **Value metric**: What unit do you charge on? users, events, storage, API calls, outcomes, etc.
   - **Anchor pricing**: Make comparisons intentional, not manipulative
   - **Contract cadence**: Monthly/annual/multi-year only where justified by buying behavior and cost structure

5. **Estimate price sensitivity**:
   - Use Van Westendorp only when real survey data exists and the sample/context are credible
   - Use conjoint/Gabor-Granger, sales evidence, historical deal data, or controlled tests when appropriate
   - Competitor pricing is context, not willingness-to-pay evidence

6. **Plan pricing experiments**:
   - sales conversations with structured questions
   - proposal or packaging tests across comparable cohorts
   - landing/pricing page tests when buying motion supports them
   - controlled changes with margin/conversion/retention guardrails

7. **Output a pricing recommendation**:
   ```
   Recommended Model: [Model type]
   Value Metric: [What you charge on]

   | Tier | Price/Range | Target Segment | Value Boundary | Evidence |
   |---|---|---|---|---|

   Key Assumptions:
   - [Assumption] → [How to test]

   Risks:
   - [Risk] → [Mitigation]
   ```

## Reliability and Economics Gate

Before recommending a price:

- classify key inputs as `MEASURED`, `SOURCE-BACKED`, `ESTIMATE`, `ASSUMPTION`, or `UNKNOWN`;
- do not infer willingness to pay from competitor list price;
- distinguish list price, realized price, discounting, services/implementation, minimum commitments, and usage overages;
- verify whether public competitor prices are current and comparable;
- model gross margin and cost-to-serve, especially for AI/usage-heavy products;
- test whether the proposed value metric scales with customer value rather than merely vendor cost;
- check price cliffs, bill shock, procurement friction, predictability, and gaming incentives;
- model at least conservative/base/upside economics when volume or usage is uncertain;
- identify the break-even condition if WTP or volume is unknown;
- include enterprise implementation/support burden in TCO where relevant;
- state where price discrimination/packaging may create fairness, trust, or channel conflict;
- recommend `TEST` rather than a precise price when evidence is weak.

### Contradiction pass

Ask:
- Could higher conversion at a lower price destroy margin or support capacity?
- Could a usage metric discourage the behavior customers need to succeed?
- Is the proposed premium supported by differentiated value or only positioning language?
- Are high-WTP interview respondents different from actual buyers?
- Would procurement prefer predictability even when usage-based pricing is theoretically efficient?

### Decision

End with `LAUNCH | PILOT | TEST WTP | REPACKAGE | HOLD`, confidence, load-bearing assumptions, and what evidence would change the recommendation.

Think step by step. Save as markdown. Flag any assumptions that need validation before launch.

---

### Further Reading

- [Product Pricing Strategies 101](https://www.productcompass.pm/p/product-pricing-strategies-101)
- [The AI Product Pricing Masterclass: OpenAI Product Lead on Why SaaS Pricing Fails in AI (and How to Fix It)](https://www.productcompass.pm/p/ai-product-pricing) (video course)
