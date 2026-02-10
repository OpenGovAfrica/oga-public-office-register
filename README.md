### OGA Public Office Register

A verifiable, Africa-wide public record of individuals who hold or have held public office, their roles, tenures, and affiliations — built for long-term civic use, auditability, and cross-country comparison.

### Project Status

This repository represents the **foundational stage** of the OGA Public Office Register.  
Core architecture, data models, and contribution standards are being established. There is **no pre-existing environment or legacy system**; early contributors are expected to help design and implement the initial scaffolding that future contributors will build upon.

The project is intended to outlive any single program or contributor and is maintained as long-term civic infrastructure.

### Project Goals

The OGA Public Office Register aims to:

- Maintain a permanent, verifiable record of public officials across African countries
- Support diverse governance systems:
  - Unicameral and bicameral legislatures
  - Elected, appointed, and traditional authority roles
- Enable cross-country and historical comparison
- Enforce strong provenance and auditability for every record
- Provide structured, reusable data for journalists, researchers, and civic technologists

This project is designed to scale across:
- 54+ countries
- Multiple languages and naming conventions
- National, regional, and local levels of government

### What This Project Is (and Is Not)

**This project is:**
- A long-term civic data infrastructure project
- A source-driven, verifiable registry of public officeholders
- Designed for gradual expansion and community stewardship

**This project is not:**
- A scraped or crowd-sourced dataset without verification
- A country-specific tracker
- A closed or proprietary data platform

All published records must be attributable to reliable sources.

### Core Design Principles

- **Individual-first data modeling**: People, roles, organizations, and tenures are modeled separately to preserve accuracy over time.
- **Strong provenance**: Every tenure, role, or affiliation must reference at least one verifiable source.
- **Geographic normalization**: Administrative regions are structured, not free-text.
- **Future-proofing**: The data model favors extensibility over short-term convenience.
- **Transparency**: Architectural decisions are documented and open to review.

### Repository Structure

Each repository under OpenGovAfrica is self-contained. This repository includes:

- `README.md`  
  Project overview, scope, and roadmap (this file)

- `ARCHITECTURE.md`  
  Technical decisions, data models, enums, and system design rationale

- `DATA_MODEL_DECISIONS.md`  
  Design trade-offs, future considerations, and non-mandatory extensions

- `CONTRIBUTING.md`  
  Contribution workflow, environment setup (as it evolves), and data entry rules.

---

### Contributors & Roles

This project follows an individual-ownership, collaborative-development model across all phases of work and maintains explicit attribution for all contributors. Contributors are encouraged to collaborate through discussion, reviews, and coordination at every stage of the project. However, all implemented work must have clearly attributable ownership.

Each contributor is credited with the specific components, tasks, or deliverables they owned or led. Participation, discussion, or review alone does not imply ownership.

| Contributor | Role / Focus Area | Owned Deliverables |
|------------|------------------|--------------------|
| Name / GitHub | Backend, Frontend, Data, Infra, Research | Clearly scoped features, services, or setup tasks |

This table must be kept up to date as the project evolves, from Phase 0 through final delivery. Phase-level credit is insufficient on its own; ownership must always be traceable to concrete deliverables, from initial scaffolding (Phase 0) through final handover.

**Clarification on Collaboration and Ownership (All Phases)**

From Phase 0 through the final phase, contributors may not jointly claim the same implementation output unless responsibilities are explicitly separated and documented. Collaboration should strengthen implementation quality, not dilute accountability.

---

### Definition of Done

A task or feature is considered complete only when all of the following are satisfied:

1. Code is clean, readable, and compliant with project linting and formatting rules.
2. Appropriate unit and/or integration tests are included and CI passes.
3. Relevant documentation is updated (README, ARCHITECTURE, API docs where applicable).
4. Database migrations are provided and reviewed if schema changes are involved.
5. The Pull Request has received at least one peer review and maintainer approval.

---

### Relationship to Tech Programs, Hackathons & Internships

This project may be developed in part through tech programs. If you are contributing through GSoC, MLH, Outreachy etc, please find your [project standard here](https://github.com/OpenGovAfrica/gsoc/blob/main/docs/project-standard.md) & roadmap [here](https://github.com/OpenGovAfrica/gsoc/issues/20). 
_If this becomes obselete please raise an issue for_

Contributors are expected to:
- Build reusable, well-documented components
- Respect long-term maintenance needs
- Treat programs as an entry point, not a finish line

The roadmap and contribution guidelines are designed for continuity beyond any single program.

### GSoC Compatibility Note

GSoC compatibility: Contributors may collaborate through discussion and peer review, but all submitted work must have clear individual ownership and be attributable to a single contributor for evaluation.

---

### Maintainer Enforcement Guidelines

These guidelines apply from Phase 0 through final project delivery.

Maintainers are responsible for ensuring clear ownership and accountability throughout the project lifecycle. When reviewing work, maintainers should verify that:

1. Every pull request has a clearly identifiable primary owner.
2. Each deliverable, regardless of phase, is attributable to a specific contributor.
3. The README “Contributors & Roles” section reflects actual implementation ownership, not participation alone.
4. Multiple contributors are not credited for the same deliverable unless roles and responsibilities are explicitly differentiated.
5. Collaboration is demonstrated through reviews, discussions, and coordination — not shared ownership of identical outputs.

If ownership is unclear at any stage, maintainers should request clarification or restructuring before merging.
Clear ownership is required for all phases to ensure sustainability, accountability, and long-term project health.

---

### Roadmap (Sustainability-Focused)

This roadmap reflects **project maturity stages**, not program-specific timelines.

#### Phase 1: Core Architecture and Data Modeling
- Popolo-aligned models for Persons, Organizations, Posts, Memberships
- Geography and jurisdiction modeling suitable for African administrative diversity
- Controlled vocabularies and enforced enums
- Documentation of all schema decisions

#### Phase 2: Provenance and Data Integrity
- Source and evidence system
- Mandatory sourcing for all tenures
- Verification metadata and audit fields
- Constraints preventing unsourced publication

#### Phase 3: Public and Analytical APIs
- Read-only public query endpoints
- Career timeline and tenure history queries
- Filters for country, chamber, party, and time period
- Fully documented OpenAPI specification

#### Phase 4: Admin and Research Tooling
- Authentication and role-based access
- Admin interface for structured data entry
- Inline provenance enforcement
- Change history and audit logs

#### Phase 5: Public User Experience
- Official profile pages
- Career timeline visualizations
- Party and affiliation history
- Clear source citation at every level

#### Phase 6: Search and Discovery
- Full-text search
- Country and legislature landing pages
- SEO and structured metadata

#### Phase 7: Data Quality and Validation
- Date and tenure consistency checks
- Prevention of invalid overlaps
- Country and geography validation
- Automated tests for schema rules

#### Phase 8: Expansion and Stewardship
- Adding new countries and legislatures
- Improving sourcing depth
- Community-driven validation
- Ongoing schema evolution

### Sustainability Beyond Programs

While this repository may be used by contributors participating in programs such as Google Summer of Code, Hacktoberfest, & other Tech prgrams it is **not scoped or designed exclusively for that**.

All contributions are expected to:
- Be maintainable beyond a single development cycle
- Include documentation and rationale
- Follow project-wide architectural patterns

Any program participation is treated as one of many contribution pathways.

### Contribution Pathways

This repository welcomes contributors with different experience levels.

Issues are labeled to indicate suitability:
- `good first issue` – onboarding-friendly tasks
- `data-modeling` – schema and architecture work
- `backend` – API and database logic
- `frontend` – public UI components
- `documentation` – technical writing and standards
- `research` – sourcing and validation improvements

See `CONTRIBUTING.md` for workflow and expectations.

### Data Ethics and Responsibility

This project handles politically and socially sensitive information. Contributors are expected to:

- Rely on reputable, verifiable sources
- Avoid speculative or unsourced claims
- Document uncertainty clearly
- Respect regional and cultural naming differences

Accuracy and transparency take precedence over completeness.

### License and Governance

This project is maintained under the OpenGovAfrica organization.  
Licensing, governance, and contribution rules are documented in the repository.

### Getting Involved

If you are interested in contributing:
- Read `ARCHITECTURE.md` to understand design decisions
- Review open issues to find a suitable starting point
- Ask clarifying questions in public discussion channels

Early contributors are helping define the foundation — thoughtful design and documentation are as valuable as code.
