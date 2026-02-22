# Data Model Decisions

## Core Philosophy: The Popolo Standard
We are adopting the [Popolo Data Standard](https://www.popoloproject.com/) for this registry to ensure international interoperability and completeness. Popolo is specifically designed for the "messy" reality of political data, allowing us to track complex relationships across 54+ African nations.

## Primary Entities

### 1. Person
* **Decision:** Names are stored as a single string to accommodate diverse cultural naming conventions.
* **Logic:** We do not enforce "First Name / Last Name" splits, as this does not reflect the naming realities in many African regions.

### 2. Organization & Chambers
* **Concept:** Hierarchical groups with common purposes (e.g., "National Assembly", "Political Party").
* **Refinement (Phase 1.3):** Organizations now support **Bicameral** systems. A "Parliament" (Parent) can contain a "Senate" (Upper Chamber) and a "National Assembly" (Lower Chamber).
* **Enforcement:** The `chamber_type` field prevents ambiguity between different legislative houses within a single country.



### 3. GeographicArea (Phase 1.2)
* **Decision:** Administrative regions are **normalized**, not free-text.
* **Hierarchy:** Supports recursive parenting, allowing the system to traverse from a `Constituency` up to a `State/Province` and finally to a `Country`.
* **Spatial Support:** Includes a PostGIS `GeometryField` for storing constituency boundaries (Polygons) or office locations (Points) to enable future map visualizations.

### 4. Post
* **Concept:** A position existing independently of the person holding it (e.g., "The Speaker").
* **Geographic Link:** Every `Post` is linked to a specific `GeographicArea`, ensuring we can track exactly which region an official represents.

## Technical Implementation Details

### UUIDs vs Integers
* **Decision:** Use **UUIDs** (Universally Unique Identifiers) for all Primary Keys.
* **Reasoning:** This prevents enumeration attacks and allows for seamless data merging from distributed sources without ID collisions.

### Soft Deletion
* **Implementation:** Models inherit from `SoftDeleteModel` with an `is_active` boolean.
* **Reasoning:** Maintaining a historical audit trail is critical; we must preserve records of former officials for accountability.

### Multi-Country Support (ISO-3166)
* **Decision:** Use ISO-3166-1 alpha-3 (3-letter codes) for all country identifiers (e.g., `NGA`, `ZAF`, `KEN`).
* **Reasoning:** These are more readable and the standard for international data exchange.

## Naming & Titles (Design Decisions)

### 1. Handling Honorifics and Titles
* **Decision:** Honorifics (e.g., Chief, Emir, Oba, Alhaji, Dr.) are included directly in the `name` field.
* **Reasoning:** African titles are highly varied; restrictive Enums would fail to capture local specificities.

### 2. Geographic Normalization (Phase 1.2)
* **Decision:** Mandatory mapping to a `GeographicArea` instance instead of free-text strings.
* **Reasoning:** This prevents data fragmentation (e.g., "Lagos" vs "Lagos State") and enables accurate regional filtering and comparison.

### 3. Selection Methods (Enums)
* **Decision:** Use a strictly controlled vocabulary for how an official enters a role.
* **Categories:** `elected`, `appointed`, `hereditary`, and `ex_officio`.