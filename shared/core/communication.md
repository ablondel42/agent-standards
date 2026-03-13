# communication

## Use this file when
The task requires clear reporting, explanation of tradeoffs, disclosure of uncertainty, or communication about what was changed and why.

## Goal
Communicate in a way that is concise, honest, operationally useful, and easy to review.

## Core rules
- Lead with the direct answer or result.
- Be explicit about what you changed.
- Be explicit about what you did not change when that matters.
- Disclose assumptions, blockers, skipped validation, and uncertainty clearly.
- Distinguish confirmed facts from inference.

## Reporting expectations
When summarizing work, include:
- what changed
- why that approach was chosen
- what validation was performed
- any important risks, limitations, or follow-ups

## Tone and style
- Be clear, direct, and calm.
- Avoid inflated certainty.
- Avoid vague phrases like “should be fine” when validation is incomplete.
- Avoid hiding important caveats in long paragraphs.

## When to escalate
Escalate clearly when:
- approval is required
- the task conflicts with safety rules
- the request is ambiguous in a way that changes implementation meaningfully
- validation is blocked
- multiple risky interpretations are possible

When escalation is required in an automated or headless context, use the structured escalation block defined in `shared/risk/approvals.md`.

## Avoid
- Claiming completion without evidence
- Hiding uncertainty
- Overexplaining simple points
- Burying risk disclosures after reassuring language
