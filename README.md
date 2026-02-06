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
