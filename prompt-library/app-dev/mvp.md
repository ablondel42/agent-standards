You are a senior product engineer and technical project planner.

Using the PRD provided previously, turn it into a concrete MVP task breakdown optimized for a solo developer or very small team.

Goal:
Produce a realistic, implementation-ready execution plan that turns the PRD into a buildable MVP with the smallest viable scope, the lowest reasonable complexity, and the fastest path to launch.

Instructions:
- Use the PRD as the source of truth.
- Optimize for a product that can be built in 2 to 6 weeks.
- Favor the narrowest MVP that still delivers real value.
- Prefer standard web app patterns, managed services, and API-based integrations over custom infrastructure.
- Keep the plan realistic for one person building and shipping the product.
- Reduce technical risk, operational burden, and maintenance complexity wherever possible.
- If the PRD includes optional AI features, separate required AI work from optional AI enhancements.
- If some PRD details are ambiguous, make reasonable assumptions and label them clearly.

Planning constraints:
- Low hosting and infrastructure cost
- Low maintenance burden
- Minimal manual operations
- Minimal compliance and moderation complexity
- Smallest reasonable feature set
- Fast feedback from real users
- Clear separation between must-have, should-have, and later work

Output format:

# MVP Task Breakdown

## 1. MVP scope summary
- One-sentence description of the MVP
- Core user outcome
- What the MVP must do
- What is explicitly out of scope for v1

## 2. Build strategy
- Recommended implementation approach
- Simplifications that reduce time and cost
- Features or technical choices that should be deferred
- What to fake, do manually, or avoid automating in v1

## 3. Workstreams
Break the MVP into workstreams such as:
- Product setup
- Frontend
- Backend
- Data model
- Authentication
- Payments, if needed
- AI integration, if needed
- Notifications, if needed
- Observability
- Security and privacy
- Deployment and release

For each workstream include:
- Objective
- Main tasks
- Dependencies
- Notes on simplification

## 4. Task list
Create a detailed task breakdown grouped by workstream.

For each task include:
- Task name
- Why it matters
- Priority: must-have / should-have / later
- Estimated difficulty: low / medium / high
- Dependencies
- Clear completion criteria

## 5. Recommended build order
List the order in which the tasks should be implemented.
Explain the reasoning briefly.
Prioritize tasks that unlock validation, reduce risk, or enable vertical slices.

## 6. Vertical slices
Define the smallest end-to-end slices that can be built and tested early.
For each slice include:
- What user value it proves
- What components it touches
- Why it should be built early or late

## 7. AI task breakdown, if applicable
If AI is part of the MVP, separate:
- Required AI features for launch
- Optional AI improvements after launch
- Fallback behavior when AI fails
- Cost-control measures
- Testing and evaluation needs

If AI is not necessary, explicitly say so and remove it from the critical path.

## 8. Technical foundation tasks
List the minimum technical setup required, such as:
- Project scaffolding
- Routing and layout
- Database setup
- Auth setup
- Environment variables
- Error handling
- Logging
- Analytics
- Basic security protections
- Deployment pipeline

Keep this section lean and avoid gold-plating.

## 9. Launch-critical checklist
Identify the minimum set of tasks required before first release.
Separate:
- Must ship before launch
- Can wait until after first users
- Nice-to-have but unnecessary for MVP

## 10. Time-boxed execution plan
Provide either a 2-week or 4-week solo-builder plan, depending on the complexity of the PRD.

Break it down by week with:
- Main goals
- Tasks to complete
- Deliverable by end of week
- Risks to watch

## 11. Risk reduction plan
Highlight:
- The biggest technical risks
- The biggest scope risks
- The biggest cost risks
- The fastest way to validate assumptions before overbuilding

## 12. Final advice
End with:
- The sharpest possible MVP cut
- The first thing to build
- The first thing to defer
- The most likely way this project could become too big

Writing rules:
- Be concrete and implementation-oriented.
- Avoid generic agile/process fluff.
- Do not turn this into a large-team project plan.
- Optimize for speed, simplicity, maintainability, and launchability.
- Prefer shipping a narrow working product over planning an impressive but oversized roadmap.

Where possible, organize the task list so each major feature can be built and tested as an end-to-end vertical slice rather than as isolated frontend and backend chunks.
For each must-have task, include the likely files/modules/components involved and the key implementation decisions.
