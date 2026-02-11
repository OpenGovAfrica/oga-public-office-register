# Data Model Decisions

## Core Philosophy: The Popolo Standard
We are adopting the [Popolo Data Standard](https://www.popoloproject.com/) for this registry. Popolo is an international open data specification for monitoring legislatures and governments.

**Why Popolo?**
1.  **Interoperability:** Allows data to be easily shared with other civic tech tools.
2.  **Completeness:** Covers complex edge cases (e.g., generic posts, changing district boundaries) that custom models often miss.
3.  **Flexibility:** Designed specifically for the messy reality of political data.

## Primary Entities (Phase 1)

The database schema revolves around four core models.

### 1. Person
* **Concept:** A real human being.
* **Key Fields:** Name, Biography, Birth Date, Gender, Image URL.
* **Design Decision:** Names are stored as a single string (Popolo standard) rather than split into First/Last to accommodate diverse cultural naming conventions.

### 2. Organization
* **Concept:** A group with a common purpose (e.g., "Ministry of Finance", "Parliament", "Liberal Party").
* **Key Fields:** Name, Classification (Ministry, Committee, Party), Parent Organization.
* **Logic:** Organizations are hierarchical. A "Committee" can belong to the "Parliament".

### 3. Post
* **Concept:** A position that exists independently of the person holding it.
* **Example:** "The Minister of Finance" is the **Post**. "Ngozi Okonjo-Iweala" is the **Person**.
* **Why separate from Membership?** This allows us to track **vacancies**. If a Minister resigns, the *Post* remains in the database, but the current *Membership* ends.

### 4. Membership
* **Concept:** The connecting link between a **Person**, an **Organization**, and optionally a **Post**.
* **Key Fields:** Start Date, End Date, Role.
* **Logic:** `Person A` has a `Membership` in `Organization B` holding `Post C` from `Date X` to `Date Y`.

## Technical Implementation Details

### UUIDs vs Integers
* **Decision:** Use **UUIDs** (Universally Unique Identifiers) for all Primary Keys.
* **Reasoning:**
    * Prevents enumeration attacks (users guessing IDs like `/person/1`, `/person/2`).
    * Allows for easier data merging from distributed sources later without ID collisions.

### Soft Deletion
* **Decision:** No record is ever truly deleted from the database via the API.
* **Implementation:** All models inherit from a `SoftDeleteModel` abstract class containing an `is_active` boolean.
* **Reasoning:** Maintaining a historical audit trail is critical for government accountability data. We need to know who *was* in office, even if they aren't anymore.

### Geospatial Data
* **Tool:** PostGIS
* **Usage:** Storing constituency boundaries (Polygons) and office locations (Points).
* **Standard:** SRID 4326 (WGS 84) is used for storage to ensure compatibility with standard GPS and mapping tools (Leaflet/Mapbox).

## Naming & Titles (Design Decisions)

### 1. Handling Honorifics and Titles
* **Decision:** We do not provide a separate field for "Prefix" or "Suffix." 
* **Implementation:** Honorifics (e.g., Chief, Emir, Oba, Alhaji, Rev, Dr.) should be included in the `name` field if they are part of the public's primary recognition of the official.
* **Reasoning:** Titles in African governance are highly varied and culturally specific. Attempting to create an Enum for titles would be restrictive. If a specific title is required for a project (like "Chief" for traditional roles), it should be handled via the `Post` label (e.g., "Post Label: Paramount Chief").

### 2. Multi-Country Support (ISO-3166)
* **Decision:** Use ISO-3166-1 alpha-3 (3-letter codes) for all country identifiers.
* **Reasoning:** 3-letter codes (e.g., `ZAF`, `KEN`, `NGA`) are more readable than 2-letter codes and are the standard for international data exchange. This ensures the registry can scale to all 54+ African nations without ambiguity.

### 3. Language and Historical Variants
* **Decision:** Store the primary name in English (or the country's official administrative language) but allow for "alternative names" in Phase 1.2.
* **Reasoning:** To support searchability across colonial vs. post-colonial spellings and local-language variants, the data model must eventually support an `OtherNames` table (Popolo standard) linked to the `Person`.

### 4. Selection Methods (Enums)
* **Decision:** Use a strictly controlled vocabulary for how an official enters a role.
* **Implementation:** * `elected`: For parliamentary or executive roles chosen by vote.
    * `appointed`: For ministerial or judicial roles.
    * `hereditary`: Specifically for traditional authorities (Emirs, Kings, etc.).
    * `ex_officio`: For roles held automatically by virtue of holding another office.

---    