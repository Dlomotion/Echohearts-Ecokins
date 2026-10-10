# Eco-Kin Art Catalog and Visual Master Catalog — Reconciliation Intake (2026-10-10)

**Status:** SOURCE METADATA / PROPOSED RECONCILIATION. **No art files, model assets, permanent IDs, or runtime implementation are approved or verified by this record.**

**Authority:** the main Dlomotion/Echohearts-Rebearth repository retains canon, the 125-ID Permanent Dex and protected identity approvals; this repository is a visual/provenance companion; the BUILD repo owns executable UE5.8 integration.

## Two user-supplied sources in this intake

1. A large pasted art/audio table with fields `source_filename`, `catalog_filename`, `depicted_names`, `category`, `md5`, `catalog_relative_path`, `status`, `visual_lock`, `notes` (original export not attached as a parseable CSV in this pass).
2. **Visual Master Catalog**, dated 2026-10-05, supplied as a working reference: 36 fully-rowed records, approximately 158 historical name mentions (with overlap), zero assigned permanent IDs **within its surveyed source files**, two `Approved Canon Art` labels in the 36-row section (Piplin and Unbound), and explicit blocked collision groups.

The full pasted asset inventory is **not** reconstituted here. The accompanying `ECOKIN_PRIORITY_ASSET_HASH_REVIEW_2026-10-10.csv` contains 30 specifically transcribed *priority* filename/hash records; it is NOT a complete asset inventory or verified checksum report. Original rows, source filenames, MD5s, and provenance must be retained during a future complete manifest import.

## Precise interpretation / integrity

- `filed` records the *user's catalog claim*; not evidence a binary is tracked in Git. `duplicate-member` denotes a supplied hash match, not a recomputed checksum. `superseded` means preserve old image bytes/lineage for provenance, not delete. `visual-lock` protects approved visual identity and source asset from silent redesign; it **does not itself approve species, form, Essences, naming, game-ready quality or permanent IDs**.
- Exact GitHub path checks returned NOT_FOUND in this repository for `user_uploads/ecokin_art/EK_ART_Justica_USER_v1.jpg`, `user_uploads/ecokin_art/EK_ART_FoxFur_Tideform_v1.jpg`, `user_uploads/ecokin_art/EK_ART_ZuriStripe_USER_v1.png` and `user_uploads/audio/SFX_Animal_Sound_Effects_Compilation.mp3`. Other paths or branches may differ. Do not claim actual byte import, MD5 verification or LFS roundtrip.
- Normalize mojibake (`â`, `Â·`, `â`) only in human-readable *display notes*. Preserve original names, raw hashes, and aliases in lossless source fields. Never auto-normalize `Pharoah / Pharaoh`, `Skryaxis`, `Chrisma Moth / ChrisMoth`, or `Thunderhoof / Thundhoof` into canon without approval.
- Catalog item count and namespace are not the canonical roster. The separate 554-record corrected registry is staged on [primary draft PR #58](https://github.com/Dlomotion/Echohearts-Rebearth/pull/58): 125 protected numbered slots plus 429 unnumbered intake records. A 2026-10-05 search limited to historic files finding zero EcoKinIDs does not negate the protected 125-ID Dex nor confirm those protected slots' identity status.
- `ECO_KIN_ASSET_INDEX.md` currently contains visual **example** `EKIN-####` labels. These cannot automatically become the primary `EcoKinID`/Echoprint IDs; confirm registry mappings and avoid second Dex. Its historical `Nature → Floauwer → Dandelion` sequence must not override Nature's identity as Guardian of Life with **conditional Mutations**, rather than ordinary forced evolution.

## Preservation and form lineage decisions to audit

| Group | Supplied visual continuity | Blocker / test |
|---|---|---|
| **Fox Fur** | Pyreform and Tideform are two presentations of **one** Eco-Kin; older orange version superseded but retained | Confirm same fox anatomy, color and regalia; no second species ID |
| **Veridran** | Verdant Rainforest and Arid Form intended as one species; old Oasis deer image superseded | New tortoise Arid Form versus original deer morphology requires biological/body-plan continuity sign-off |
| **ZuriStripe** | Base tiger-girl + corrected Sunclaw Matriarch/Prowlguard/Glitch-Tigris | Keep originals as superseded evidence. Blight/glitch manifestation is not automatic species |
| **Boney Bone** | Base showman + corrected Midnight Encore; retain raw DarkShowman separately | Same skull/hat identity and motion language, originality |
| **Jordane** | Sky-Ace eagle reference and corrected Divine Ascendant version; retain conflicting raw angel | Review morphology and Growth Rite; avoid outdated 'Divine Evolution' labeling |
| **Zangoro, Fanatic, Flames, Totemflare, Psylopath, Sandveil, Marmara** | Multi-card named Ecoforms of one respective identity | Do not allocate separate species IDs for each stage; stage names are not independently approved growth logic |
| **Moth/butterfly cluster** | Emberatlas, Chrismoth, Emperor Moth, Moth, Emperyx, Prismavex, Plainsman + historical Luna Moth/Chrisma Moth aliases | Collision, lineage and Plainsman-white-moth appearance vs existing protected representation |
| **Thunderhoof / Thundhoof** | Two distinct supplied card hashes, similar bison premise | Treat as collision review, not presumed rename or separate confirmed species |
| **Dandelion / Floauwer / Nature** | Multiple historical references and lineage descriptions | Nature conditional Mutation rule takes precedence over ordinary evolution/parentage inference |

## Visual Master Catalog snapshot and acceptance gates

- Scope of its 36 fully-rowed items: 3 proposed bee-line roles, 5 Ancient Vanguard candidates, 10 ecology-restoration candidates, 2 working Gnarled-Wood/Pebble-Kin labels, 7 named Eco-Kin intake records (Dryad, Ember, Glow Worm, Piplin, Sherlock Hound, Skyraxis, Unbound), 3 form-family entries (Frostclaw, Radiant Typhoon, Psylopath), and **6 real-animal references that are NOT Eco-Kin**. Hence 36 catalog rows are not 36 new species.
- The 2026-10-05 document's two approved-art statuses count **Piplin** and **Unbound in its §2 scope only**; Nature is separately asserted as an existing protected visual anchor in §5. Neither status proves the files' bytes were imported or that UE runtime assets exist.
- **Skyraxis** (historical spelling `Skryaxis`) retains its exactly-two-leg anatomy lock; three-legged rendering is rejected source evidence, never a production rig/model input.
- **Frostclaw** Glacierkin quadruped vs upright Icesentinel/Auroraguard requires a single coherent body-plan rule before form art can be production-approved.
- **Paw/Pupular/Chaos Woof**, **Solarion/Lunaris vs Sol-Spectra/Luna-Spectra**, **Mime/Misery Mime**, **Azurbuzz/Florafinity**, **Tidrush comparator group**, **Spectra card names**, **Moth variants**, **Aegis-Core versus A.E.G.I.S.**, and **Pharoah/Pharaoh** remain unresolved collision/relationship reviews.
- **Poison Ivy** in historical collages is an external-IP naming collision; current existing art index proposes **Poyzin Ivvee** as a different display name. Preserve alias/provenance; do not republish third-party named likeness. **King Luther / King Luthar** and **Minnie Ripton** are similarly flagged for alias/originality review.
- **Braziliana**, **Prismana/Prusmana**, superseded artwork, and malformed depictions are historical/retired-only. **Zora** and **Aurivelle Form** are reconciliation anchors, not automatic new Dex approvals.
- Real wildlife photos, reference advertisements, map boards and external art-book images must stay in **reference-only** folders, not Eco-Kin creature-art imports. Human/character portraits, Genie, and the Shattered Frontier cast belong in character/NPC provenance records, not the creature roster. Unnamed images (pink poodle butterfly, starfish boxer, blue jester, lioness warrior, elephant shrew, glider, feline, etc.) remain unnamed intake until identities are explicitly chosen.
- Card text containing generic `HP/DEF/EVOLUTION`, '18 ELEMENTS', '12-element chart', 'capture/catching', unsanctioned `Divine Evolution`, or other old labels is **presentation-only, historical**, not runtime. Current front-facing Essences: **Flora, Torrent, Pyre, Terra, Aero, Glaze, Voltic, Aura, Shade**. Core stats: **Vibrance, Density, Harmony, Purity**. Growth and bonding require agency, Kindling and appropriate forms/mutation governance.
- Nine provided MP3 names were cataloged as prospective sound effects / ambience sources; no licensing, bytes, audio QC, loop points, volume normalization, spectral suitability, or import verification was established. Any samples not original/licensed for commercial use must be blocked from shipping.

## Suggested reconciliation order / completion criteria

1. Obtain the **original export as a file** plus original image/audio binaries or accessible Git LFS pointers. Hash actual bytes (MD5 for historical comparison; SHA-256 for stronger integrity); never derive an expected checksum from a thumbnail or conversational record.
2. Validate normalized paths, exact dedupe groups by computed digest, declared supersession edges, multi-form common identity, known animal-photo / game-ad reference exclusions, and no orphan asset links.
3. Reconcile names with primary Permanent Dex, historical 1,120-name archive and 554-row proposed registry PR #58. Mark aliases, legacy/retired states and pending status; avoid invented IDs and unapproved species promotion.
4. Enforce a clear approval state: `ACTIVE_CANON_ART`, `PENDING_CANON_REVIEW`, `REFERENCE_RETIRED_NEEDS_REDESIGN`. Map `filed`, `visual-lock`, and `duplicate-member` to separate *source-catalog* metadata fields instead of pretending they are canonical art states.
5. Review species DNA, anatomy, real ecology, silhouette, colour, camera, materials and form continuity; map approved art sources to `07_Art` manifest, primary Dex intake, UE5.8 BUILD asset pipeline and audio imports only after evidence.

**Do not merge or publish asset catalog entries solely from this prose; no repository binaries or runtime tests were executed.**
