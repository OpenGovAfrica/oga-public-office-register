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