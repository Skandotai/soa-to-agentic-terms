# Context: why this mapping exists

The short version of the argument. For the full paper — including what SOA got *wrong* and why those failures matter here — see the [whitepaper](whitepaper.md), also available as a [PDF](docs/downloads/skan-agentic-ai-terminology-whitepaper.pdf).

## The parallel with SOA

The current agentic AI landscape resembles enterprise computing before SOA: fragmented, proprietary, and lacking cohesive architectural principles. Individual vendors have built impressive capabilities, but the absence of standardized frameworks limits broader adoption and integration.

Service-Oriented Architecture faced the same fragmentation in the early 2000s. Before it, organizations struggled with monolithic applications that were difficult to maintain, scale, and integrate. Standardized concepts — services, contracts, registries, orchestration — changed how enterprises approached system architecture, and did so as much through shared vocabulary as through technical merit.

## What's the same, and what isn't

Both domains involve autonomous entities (services, agents) that must collaborate to achieve business objectives. Both need orchestration to coordinate complex workflows. Both require governance to ensure reliability, security, and compliance. Standardized approaches reduce implementation risk and speed adoption in both.

Where they diverge: services execute predefined operations. Agents adapt, learn, and make autonomous decisions. That doesn't invalidate SOA's architectural thinking — it means SOA's patterns are a foundation to build on, not a finished answer.

## How the problem shows up

Absent a shared vocabulary, the same failure shows up in a few recognizable shapes:

- **Procurement confusion.** Two vendors both claim to sell "agentic orchestration," describing meaningfully different architectures — one a central task router, the other a peer-to-peer negotiation layer — and the buyer has no term-level way to tell which is which until deep into a pilot.
- **Integration friction.** A team building multi-agent workflows across two platforms discovers each uses "agent" to mean something different in scope and autonomy, so contracts, permissions, and failure-handling assumptions don't line up at the seam.
- **Governance blind spots.** Risk and compliance teams inherit a vocabulary built by engineering, one platform at a time, with no consistent definition of what "autonomy," "oversight," or "audit trail" mean across systems — which makes enterprise-wide policy nearly impossible to write, let alone enforce.

These aren't hypothetical categories. They're the same three failure modes SOA's common vocabulary was built to close, in the same order SOA closed them: name the entities first, then standardize how they interact, then govern the whole system with confidence that everyone means the same thing by the same word.

## What's still unsolved

The mapping in this repository is the first, smallest piece of a much larger standardization agenda. The parts still open:

- **Agent definition and classification** — taxonomies distinguishing agent types by autonomy level, decision-making capability, and interaction pattern, so organizations can select the right agent type for a given use case
- **Interaction protocols** — standardized methods for agents to communicate, negotiate, and collaborate, which is a harder problem than service-to-service messaging because it can involve negotiation, shared learning, and dynamic role allocation
- **Orchestration patterns** — frameworks for coordinating multi-agent workflows that adapt to changing conditions and handle exceptions, while preserving agent autonomy and overall system coherence
- **Governance frameworks** — managing agent lifecycle, ensuring ethical behavior, maintaining audit trails, and enabling human oversight, including explainability, bias detection, and accountability for autonomous decisions
- **Quality and performance standards** — metrics and methodologies for evaluating agent performance, reliability, and business value contribution

## How the vocabulary grows

Version 2 of this mapping (`mapping-table.json`) covers twenty-eight SOA concepts and their agentic equivalents — an approved, canonical set. It started as eighteen pairs with the most direct analogues, the ones practitioners hit first when describing a multi-agent system to someone who came up on service architecture, and grew to include secondary concepts: choreography alongside orchestration, runtime discovery, gateways, fallback behavior, idempotency, versioning, canonical context models, performance objectives, state boundaries, and the requester/fulfiller relationship.

Related concepts are ordered next to each other rather than by when they were added, so the list reads as one vocabulary. Not every pairing translates with equal precision — a circuit breaker and an agent fallback protocol fail in meaningfully different ways, and SOA's preference for statelessness inverts for agents that need deliberate memory. Those seams are where the vocabulary will keep moving, and where feedback is most useful.

## Where this goes next

Skan is not claiming ownership of SOA, and isn't proposing to solve the full standardization agenda alone. This repository is an opening move: a shared vocabulary offered to the field, with the expectation that the harder architectural questions — protocols, orchestration patterns, governance frameworks, performance standards — get worked out in the open, with input from the broader community, the same way SOAP, WSDL, and BPEL emerged after SOA's vocabulary had already taken hold.
