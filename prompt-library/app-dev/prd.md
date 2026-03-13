You are a product strategist and technical product manager.

Using the app ideas and insights generated previously, create a practical PRD for the most promising idea, optimized for a solo developer or very small team.

Prefer products that can be launched with standard web infrastructure, off-the-shelf auth, managed database hosting, and API-based AI features.
Reject any idea that likely requires more than one full-time developer, complex DevOps, ongoing manual operations, heavy moderation, or custom ML infrastructure for the MVP.

Before writing the PRD, compare the top 3 shortlisted ideas and select the one with the best balance of:
- User value
- Ease of development
- Low operating cost
- Low maintenance burden
- Monetization potential
- Competitive differentiation

Goal:
Produce a lean, implementation-oriented PRD for an app that is useful, commercially viable, fast to build, cheap to operate, and low-maintenance after launch.

Instructions:
- Use the previous analysis as the main input.
- Select the single best idea from the prior shortlist unless multiple options are explicitly requested.
- If the previous output contains uncertainty, make the most reasonable assumptions and label them clearly.
- Optimize for a product that can be built in 2 to 6 weeks as an MVP.
- Favor a narrow MVP over an ambitious roadmap.
- Prefer standard web app patterns and API-based AI features over complex infrastructure.
- Keep the product realistic for a solo builder.
- Avoid unnecessary enterprise complexity, large-team process, or speculative features.

Product constraints:
- Low hosting and infrastructure cost
- Low maintenance burden
- Minimal manual operations
- Minimal compliance and moderation complexity
- Simple onboarding
- Clear monetization path
- Strong differentiation through niche usefulness, not feature bloat

Output format:

# Product Requirements Document

## 0. Idea selection
- Compare the top 3 candidate ideas from the previous output
- Explain why one idea is the best choice
- Briefly explain why the other 2 were not selected

## 1. Product summary
- Product name
- One-sentence positioning
- Target user
- Core problem solved
- Why now

## 2. Opportunity
- What trend or market shift makes this timely
- Why this problem is worth solving now
- Why this product is a good fit for a solo builder

## 3. Target users
- Primary user persona
- Secondary user persona, if relevant
- Jobs to be done
- Current alternatives and frustrations

## 4. MVP definition
- Smallest viable product scope
- Core features
- Explicit non-goals
- What is intentionally deferred

## 5. User flows
Describe the main end-to-end flows for:
- First-time onboarding
- Main recurring use case
- Upgrade or monetization moment
- Retention loop

## 6. Feature requirements
For each core feature include:
- Purpose
- User value
- Functional requirements
- Edge cases
- Simplicity notes

## 7. AI usage, if applicable
- Whether AI is required, optional, or not needed
- Exact AI-powered features
- Why AI helps here
- Fallback behavior when AI is unavailable
- Cost-control strategy for AI usage

## 8. PWA or platform strategy
- Why this should be a PWA, web app, or hybrid
- Installability and offline behavior, if relevant
- Notifications, background sync, file handling, camera, or device features only if truly justified

## 9. Technical approach
- Lean recommended stack
- Backend approach
- Data model overview
- Third-party services
- Auth approach
- Hosting/deployment approach
- Observability basics
- Security/privacy basics

Include a minimal schema outline, API surface, and deployment architecture only for the MVP-critical parts.

## 10. Monetization
- Pricing model
- Free vs paid boundaries
- Cheapest viable launch strategy
- Upgrade path

## 11. Success metrics
- Activation metric
- Retention metric
- Revenue metric
- Product quality metric
- Leading indicators for early traction

## 12. Risks
- Product risks
- Technical risks
- Market risks
- Cost risks
- What could make this a bad idea

## 13. MVP build plan
Break the MVP into phases:
- Phase 1: foundation
- Phase 2: core value
- Phase 3: polish and launch
For each phase, list the minimum work required.

## 14. Launch checklist
- Must-have before launch
- Nice-to-have after launch
- What to postpone

## 15. Final recommendation
End with:
- A one-paragraph verdict on whether this idea is worth building
- The sharpest possible MVP version
- The biggest mistake to avoid

## 16. Solo-builder implementation plan
After the PRD, provide a 2-week or 4-week solo-builder implementation plan with:
- Features in recommended build order
- What to build first
- What to fake/manual-handle early
- What to defer until after first users
- The minimum launchable version

Writing rules:
- Be specific and practical.
- Keep the PRD lean and realistic.
- Avoid generic product-speak.
- Do not invent enterprise requirements unless clearly justified.
- Optimize for speed, simplicity, cost control, and maintainability.
