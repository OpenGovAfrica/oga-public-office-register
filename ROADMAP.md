### Project 1: Citizens-in-Office Tracker

**Goal:** Establish a permanent, verifiable, and Africa-wide record of public officials and their career trajectories.

**Before you start, please ensure you have checked the project standard for all OGA projects [here](https://github.com/OpenGovAfrica/oga-public-office-register/blob/main/PROJECT-STANDARD.md)**

This project must support:
- 54+ countries
- Unicameral and bicameral legislatures
- Elected, appointed, and traditional roles
- Strong provenance and auditability
- Cross-country comparison and long-term maintainability

### Phase 1: Architecture & Data Modeling

#### 1.1 Core Data Model (Popolo-Based)

- [ ] Define `Person` model
  - Full name, alternative names
  - Gender (optional / nullable)
  - Date of birth / death (nullable)
  - Unique internal identifier

- [ ] Define `Organization` model
  - Types:
    - legislature
    - executive_body
    - judiciary
    - political_party
    - ministry
    - committee
  - Attributes:
    - name
    - organization_type
    - country_code (ISO-3166)
    - parent_organization_id (for hierarchies)

- [ ] Define `Post` model
  - Role title (MP, Senator, Minister, Governor, etc.)
  - Post type:
    - legislative
    - executive
    - judicial
    - local_government
    - traditional_authority/ruler
  - Linked organization
  - Linked geographic area

- [ ] Define `Membership` model
  - Person ↔ Post relationship
  - Start date / end date
  - Selection method:
    - elected
    - appointed
    - ex_official
    - hereditary
  - Electoral system (where applicable)
  - Party affiliation (Organization reference)

**Design Note (Non-Blocking):**
Implementations should be flexible enough to support:
- Alternative and local-language name variants
- Colonial vs post-colonial spellings
- Honorifics and traditional titles (e.g. Chief, Emir, Oba, Alhaji)

This is not a strict schema requirement, but design decisions and trade-offs must be documented in `DATA_MODEL_DECISIONS.md`.

#### 1.2 Geography & Jurisdiction Modeling

- [ ] Define `GeographicArea` model
  - name
  - country_code (ISO-3166)
  - continent_region (North, West, East, Central, Southern Africa)
  - admin_level:
    - country
    - state / province
    - district
    - constituency
  - Optional geometry (PostGIS-ready)

- [ ] Link `Post` to `GeographicArea`
  - Constituency-based offices
  - National-level offices
  - Regional / local offices

- [ ] Enforce geographic normalization (no free-text regions)

**Future-Proofing Note (Optional):**
Implementations are encouraged to consider how external geographic references
(e.g. GADM IDs, OpenStreetMap IDs) could be supported in the future.

This is not required for initial implementation, but any assumptions or decisions
should be documented in `DATA_MODEL_DECISIONS.md`.

#### 1.3 Legislature & Chamber Modeling

- [ ] Model legislatures as Organizations
  - Classification:
    - unicameral
    - lower_chamber
    - upper_chamber

- [ ] Encode chamber relationships
  - Parliament → Senate
  - Parliament → National Assembly

- [ ] Ensure queries can distinguish:
  - MPs vs Senators
  - Upper vs Lower chamber officials
  - Unicameral parliaments

#### 1.4 Controlled Vocabularies & Enums

- [ ] Define enums for:
  - post_type
  - organization_type
  - selection_method
  - chamber_type
  - source_type

- [ ] Add database constraints to enforce enum usage

- [ ] Document all enums in `ARCHITECTURE.md`

### Phase 2: Provenance & Data Integrity

#### 2.1 Source & Evidence System

- [ ] Implement `Source` model
  - source_url
  - source_type:
    - official_gazette
    - parliamentary_website
    - electoral_commission
    - reputable_media
  - publisher
  - publication_date

- [ ] Link Sources to:
  - Memberships
  - Posts
  - Party affiliations

- [ ] Enforce at least one source per Membership record

#### 2.2 Audit & Verification Metadata

- [ ] Add verification fields
  - last_verified_at
  - verified_by (user reference)
  - confidence_level (optional)

- [ ] Prevent publishing records without provenance

### Phase 3: Backend API Development

#### 3.1 Core REST API

- [ ] Implement CRUD endpoints for:
  - Persons
  - Organizations
  - Posts
  - Memberships
  - Geographic Areas
  - Sources

- [ ] Implement read-only public endpoints for:
  - Officials by name
  - Officials by country
  - Officials by chamber
  - Officials by party
  - Officials by time period

- [ ] Implement filtering and pagination
  - country_code
  - role
  - chamber_type
  - active_at_date

### 3.2 Query & Analysis Endpoints

- [ ] Career history endpoint (Person timeline)
- [ ] Cross-role movement detection (MP → Minister → Governor)
- [ ] Party-switch detection over time
- [ ] Currently-serving officials endpoint

#### 3.3 API Documentation

- [ ] OpenAPI / Swagger integration
- [ ] Document all enums and filters
- [ ] Provide example queries per endpoint

### Phase 4: Authentication & Admin Tooling

#### 4.1 Authentication & Authorization

- [ ] Implement JWT or session-based auth
- [ ] Define roles:
  - Admin
  - Researcher
  - Read-only reviewer

- [ ] Restrict write access to authorized users only

#### 4.2 Admin Dashboard

- [ ] Admin UI for:
  - Creating/editing Persons
  - Managing Organizations and Posts
  - Assigning Memberships
  - Attaching Sources

- [ ] Inline provenance enforcement
  - Block save without source

- [ ] Change history / audit log view


### Phase 5: Frontend Public Experience

#### 5.1 Official Profile Pages

- [ ] Public profile page per Person
  - Biography summary
  - Current position
  - Career timeline
  - Party affiliations over time

- [ ] Display provenance per role

#### 5.2 Career Timeline Visualization

- [ ] Timeline component
  - Time-based role changes
  - Color-coded by role type
  - Hover/click for source citation

- [ ] Support overlapping roles

#### 5.3 Affiliation & Conflict Mapping

- [ ] Display political party history
- [ ] Display corporate or board affiliations (where available)
- [ ] Flag overlapping political + corporate roles

### Phase 6: Search, SEO & Discovery

- [ ] Implement full-text search
  - Names
  - Offices
  - Organizations

- [ ] Country and chamber landing pages
- [ ] SEO metadata for official profiles
- [ ] Structured data (Schema.org where applicable)

### Phase 7: Data Quality & Validation

- [ ] Prevent overlapping memberships for the same post
- [ ] Validate date ranges
- [ ] Enforce country + area consistency
- [ ] Unit tests for schema constraints

### Phase 8: Finalization & Handover

- [ ] Populate example countries (minimum 3)
  - One unicameral
  - One bicameral
  - One mixed governance system

- [ ] Produce demo dataset with full provenance

- [ ] Write:
  - `ARCHITECTURE.md`
  - `DATA_MODEL_DECISIONS.md`
  - `CONTRIBUTING.md` (data entry rules)

- [ ] Identify at least 5 “Good First Issues”
  - Add a country
  - Add a legislature
  - Improve sourcing
  - UI polish
  - Data validation rules

---

### Definition of Done (Project 1)

- [ ] Supports multi-country African data
- [ ] Distinguishes chambers and selection methods
- [ ] Every tenure has a source
- [ ] Career timelines are accurate and queryable
- [ ] API is documented and test-covered
