### Contributing to OGA Public Office Register

Thank you for your interest in contributing to the OGA Public Office Register.  
This project is a **long-term civic data infrastructure initiative**, and contributions are expected to prioritize accuracy, maintainability, and transparency.

This document explains how to contribute code, data models, documentation, and research responsibly.

---

### Who This Project Is For

This repository welcomes contributors who are interested in:

- Civic technology and open governance
- Public data modeling and standards
- Long-term, maintainable systems
- Careful, source-driven data work

You do **not** need prior experience with African governance systems, but you must be willing to:
- rely on verifiable sources,
- document assumptions,
- and follow established standards.

### Project Status and Expectations

This is a **greenfield repository**.  
There is no pre-existing production environment or dataset.

Early contributors are expected to:
- help establish architecture and conventions,
- document decisions clearly,
- and avoid shortcuts that would hinder future contributors.

All work should assume that others will build on it.

### Contribution Types

You may contribute in several ways:

- Data modeling and schema design
- Backend API development
- Frontend UI components
- Documentation and technical writing
- Research and sourcing improvements
- Testing and validation logic

Each Pull Request should focus on **one coherent change**.

### Contribution Workflow

1. **Find or open an issue**
   - Start with existing issues on this repo or find the [roadmap doc here:]([https://github.com/OpenGovAfrica/gsoc/issues/19](https://github.com/OpenGovAfrica/oga-public-office-register/blob/main/ROADMAP.md)). All work must be done in this repository. 
   - If proposing a new change, open an issue describing:
     - the problem being solved
     - the proposed approach
     - any trade-offs

2. **Fork the repository**
   - Create a personal fork under your GitHub account

3. **Create a feature branch**
   - Use descriptive branch names  
     Examples:
     - `feat/geographic-area-model`
     - `docs/architecture-enums`
     - `fix/membership-date-validation`

4. **Implement your changes**
   - Follow existing patterns
   - Add tests where applicable
   - Update documentation when behavior or structure changes

5. **Open a Pull Request**
   - Link the related issue (e.g., `Closes #12`)
   - Clearly describe:
     - what changed
     - why it was necessary
     - any limitations or open questions

---

### Contributors & Roles

This project follows an individual-ownership, collaborative-development model across all phases of work and maintains explicit attribution for all contributors. Contributors are encouraged to collaborate through discussion, reviews, and coordination at every stage of the project. However, all implemented work must have clearly attributable ownership.

Each contributor is credited with the specific components, tasks, or deliverables they owned or led. Participation, discussion, or review alone does not imply ownership.

| Contributor | Role / Focus Area | Owned Deliverables |
|:-----------|:------------------|:-------------------|
| **@Raziel206** | Infrastructure, Backend & DevOps | **Phase 0 Scaffold:** Docker/PostGIS environment setup, CI/CD Pipeline configuration (Linting/Tests), Core Architecture & Data Model documentation, Django Project initialization. |

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

### Coding Standards

All code contributions must adhere to project-wide standards.

#### Version Control
- Use Conventional Commits:
  - `feat:` new functionality
  - `fix:` bug fixes
  - `docs:` documentation changes
  - `refactor:` non-functional code changes
  - `test:` adding or updating tests

#### Code Quality
- Linting must pass with zero errors
- Formatting must follow enforced project tools
- Business logic must include test coverage

CI checks must pass before a PR can be merged.

### Data Modeling and Schema Rules

Because this project models public offices and careers:

- Do not add free-text fields where structured fields exist
- Use enums and controlled vocabularies consistently
- Avoid country-specific shortcuts unless justified and documented
- All schema changes must include:
  - migration files
  - updated documentation
  - validation tests

If a design decision is debatable, document it in `DATA_MODEL_DECISIONS.md`.

### Provenance and Sourcing Requirements

Every record that represents a public role, tenure, or affiliation **must have at least one verifiable source**.

Acceptable sources include:
- Official gazettes
- Parliamentary or government websites
- Electoral commission publications
- Reputable media outlets

Each source must include:
- a URL or reference identifier
- publisher name
- publication date where available

Pull Requests that introduce unsourced data will not be merged.

### Geographic and Jurisdiction Data

- Geographic areas must use normalized structures
- No free-text regions or administrative names
- Country codes must follow ISO-3166
- Geometry fields must be PostGIS-compatible

Future support for external identifiers (e.g., GADM, OpenStreetMap) should be documented but not hard-required unless approved.

### Documentation Responsibilities

If your contribution affects:
- architecture
- data models
- enums or constraints
- API behavior

You must update at least one of:
- `ARCHITECTURE.md`
- `DATA_MODEL_DECISIONS.md`
- API documentation

Documentation is not optional.

### Review and Merge Criteria

A Pull Request is considered ready to merge when it includes:

- Clear, focused changes
- Passing CI checks
- Relevant tests
- Updated documentation
- At least one approved review

Maintainers may request revisions to improve clarity or long-term maintainability.

### Community Conduct

Contributors are expected to:
- communicate respectfully
- keep discussions technical and evidence-based
- be open to feedback and iteration

This project values thoughtful disagreement and documented reasoning.

### Getting Help

If you are unsure about:
- data modeling decisions
- governance structures
- sourcing reliability

Open an issue and ask.  
Early discussion is preferred over rework.

### Final Note

This project prioritizes **accuracy, provenance, and sustainability** over speed.

Well-documented, carefully reasoned contributions are valued more than volume.

Thank you for helping build durable public data infrastructure.