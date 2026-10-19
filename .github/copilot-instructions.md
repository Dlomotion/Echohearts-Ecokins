# Echohearts: Rebearth — GitHub Copilot Master Instructions




Last updated: 2026-10-09
Repository: `Dlomotion/Echohearts-Ecokins`
Role: `ECOKIN_SUPPORT`




## 2026-10-09 secure Unreal/LFS/CI dependency gate




This section governs GitHub Copilot work related to public PR #14, public Issues #12–13, and their successor BUILD-repository work. Status is evidence-based; never infer verification from an issue or pull request being closed or merged.




### Live tracking state




- `Dlomotion/Echohearts-Rebearth#14` is still open and is a candidate source-control, Git LFS, recovery, and CI baseline. Re-read its current head and compare it with current `main` before reusing or merging anything; do not rely on an older mergeability or commit-count snapshot.
- Public Issue #12 was closed through merged `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-#2`. Public Issue #13 was transferred to `Dlomotion/Echohearts#3` and closed. These closures record contract/planning work; they are not UE5.8 build or runtime proof.

## 2026-10-09 Eco-Kin intake and Fab-import governance

- Public issues `Dlomotion/Echohearts-Rebearth#48` and `#49` are proposal/reconciliation work only. They do not promote candidates, generated EK labels, source images, stats, forms, or IDs into the 125-ID Permanent Eco-Kin Dex.
- For #48, keep Terakla, Nyashaq, Trembala, Lithassa, Dunelurk, Kapsa, Tidarak, Mycotrak, Azeni, and Vumbaki in `03_EcoKin_Dex/Intake` until exact/fuzzy name, species-role, anatomy, ecology, originality, source-image, ownership/provenance, and roster-capacity review passes. The issue contains no image binaries; do not claim asset integration until approved original files and provenance records exist.
- For #49, EK-065 through EK-097 are visual-wave labels, never permanent IDs. The current corrected registry finds Hammerwake at protected `DEX-099` with `PENDING REVIEW`; preserve that slot and do not infer identity approval. Every other candidate remains `PROPOSAL` even when no exact-name match is found. EK-041 through EK-064 remain `REFERENCE / REDESIGN REQUIRED` unless a separate originality pass approves a rebuilt Echohearts-native identity.
- Route canon/Dex decisions to `Dlomotion/Echohearts-Rebearth`; web presentation to `echohearts-web`; visual source/provenance work to `Echohearts-Ecokins`; executable UE5.8 code, imported packages, tests, and runtime evidence to `ECHOHEARTS-REBEARTH-BUILD-`; treat the remaining repositories as legacy/support surfaces according to their declared role. Never duplicate authoritative media or runtime code across all repositories.
- `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-#39` is a **draft pull request**, not an issue. Repository-checkable scope is limited to its scripts, schemas, workflow, empty staging roots, path/provenance safeguards, and offline tests. Fab acquisition, entitlement/license review, first pack import, MetaHuman creation/import, redirector/dependency repair, Editor load, PIE, cook, package, server/client, performance, and platform validation require the actual Windows UE5.8 workstation and matching checkout.
- Record for every third-party asset: listing URL and immutable product identifier where available, publisher/creator, acquisition date/account context without secrets, license/entitlement evidence location, engine/platform compatibility claim, intended role, imported package roots, dependency/plugin requirements, modification restrictions, redistribution limits, source revision, reviewer, and evidence status. Asset-file presence is never runtime proof.
- The proposed 62 lineage, 45 dynamic-swap, and 12 frequency-band counts and the Prime/Vector/Apex, Prismatic, Obsidian, DNA Fusion, and Colossal/Anomalous terminology are **CONCEPT / NOT CANON-LOCKED** until reconciled with the current Dex, Essence framework, Growth Rite/Mutation/Shimmer rules, Purity/Corruption model, and approved design vocabulary. Do not generate schemas or runtime enums that make these proposals authoritative.
- If retained after review, habitat morphology must use stable base identity plus an explicit mutually-exclusive morphology state, typed Essence/interaction references, Vibrance/Density/Harmony/Purity only, deterministic validation, versioned save migration, server authority, Anima-Link consequences, and reversible failure handling. Surface overlays must remain cosmetic unless an approved gameplay contract says otherwise.
- Implementation order: approve the data contract/schema first; then validators and fixtures; then C++/DataAsset or DataTable integration; then versioned serialization; finally UE5.8 compile, Editor, PIE, networking, save/load/rollback, cook/package, and performance evidence.
- COBOL and BASIC remain optional isolated legacy utilities for deterministic conversion, validation, or reporting with pinned compilers and tests. They must not own UE gameplay/runtime, Fab import, MetaHuman, rendering, replication, save, packaging, or web production responsibilities.


## Production synchronization, Git/LFS, debugging, and CI protocol

Use this section when the user asks Copilot to create, repair, reconcile, build, test, or synchronize Echohearts work across repositories.

### Knowledge consolidation
- Treat chat exports, AI-generated notes, architecture documents, combat math, art notes, and design assets as intake material until reconciled against the canonical repository structure.
- Do not create a competing canon root. Route reconciled material into the established folders and registries owned by the primary production repository.
- Preserve provenance and historical context. Do not silently discard older designs; classify them as canonical, historical, retired, reference-only, or unresolved.
- Before a large change, inspect the repository tree, relevant source files, tests, workflows, and source-of-truth documents. Do not infer architecture from filenames alone.

### Git branch discipline
- Do not develop directly on `main` unless the user explicitly orders an emergency direct commit.
- Use short-lived task branches such as `feature/*`, `fix/*`, `docs/*`, or `ci/*`.
- Preferred flow: `main → task branch → implementation → checks → pull request → review/evidence → merge`.
- Keep commits coherent and narrowly scoped. Do not combine unrelated canon, gameplay, web, build, and publishing changes in one patch.
- Never rewrite shared history or force-push unless the user explicitly requests it and the consequences are understood.

### Unreal repository hygiene and Git LFS
For Unreal repositories, inspect existing `.gitignore` and `.gitattributes` before changing them.
- Unreal generated/local directories normally excluded from source control include `Binaries/`, `DerivedDataCache/`, `Intermediate/`, `Saved/`, IDE-local state such as `.vs/`, and generated solution/user files.
- Do not blindly ignore the entire `Build/` directory; inspect whether it contains required packaged metadata, platform resources, or project configuration.
- Use Git LFS for Unreal binary assets that require it. `*.uasset` and `*.umap` are mandatory candidates for review; large source assets such as `*.fbx` may also belong in LFS.
- Do not automatically place every `*.png` in LFS. Decide by file size, churn, repository role, and existing asset policy.
- After LFS policy changes, verify `.gitattributes`, pointer behavior, and a clean-clone + `git lfs pull` path before claiming success.

### C++ and Unreal debugging loop
When repairing Unreal C++:
1. inspect the actual compiler/UHT/UBT/UAT error and the touched call graph;
2. identify the root cause instead of applying speculative syntax edits;
3. close the editor for module/build-system changes or when Live Coding is unsafe;
4. make the smallest coherent fix;
5. run available static checks and, when an actual UE5.8 environment exists, UHT/UBT/UAT as applicable;
6. relaunch through the canonical `.uproject`;
7. validate the affected map/system and record evidence.

Do not claim a Live Coding iteration proves a clean full build. Do not download arbitrary GitHub fixes and paste them into the project. External fixes require license/provenance review, API/version compatibility review, and adaptation to Echohearts architecture.

### Shader/material and pooling work
- Material/shader work must preserve frame-time stability and platform scalability. Avoid expensive per-pixel effects or uncontrolled dynamic parameter churn when a cheaper material-function, Niagara, instance, or precomputed approach works.
- Audio/FX/component pooling must use repository-established ownership/lifetime patterns. Do not invent `UGlobalAudioPoolManager` or any manager class unless it actually exists or the task explicitly calls for designing it.
- Any new pool must define acquisition, reset, release, exhaustion behavior, ownership, thread/game-thread assumptions, and teardown.

### GitHub research
When searching public GitHub or external sources for an engine error:
- prefer current official Epic/Unreal documentation first;
- search by exact error text, engine subsystem, API symbol, and version;
- inspect license and provenance before incorporating code;
- treat search results as research, not authoritative patches;
- never import proprietary or incompatible code merely because it compiles elsewhere.

### GitHub Actions and Unreal CI
Do not create a workflow that merely looks correct. Reconcile it with existing workflows, project names, runner capabilities, and the actual engine installation.
- Target **Unreal Engine 5.8** for the active production architecture unless a repository-specific file proves otherwise.
- Do not hardcode stale engine paths such as `UE_5.7`.
- Validate YAML syntax. Keep `name:` and `on:` as separate keys.
- For self-hosted runners, verify labels, engine path, toolchain, Git LFS, disk capacity, and permissions.
- Prefer staged gates: checkout/LFS → required-file preflight → static repository checks → UHT/Development Editor compile → tests/PIE where automatable → cook/package → artifact/report.
- A passing metadata/static workflow is not UE runtime verification.
- Never suppress a failing required check solely to make CI green.
- Never fabricate workflow results, build logs, or packaged artifacts.

### Cross-repository responsibility
- `Dlomotion/Echohearts-Rebearth` is the primary production authority.
- `Dlomotion/echohearts-web` owns web/presentation experiences and must not become a second Unreal runtime.
- `Dlomotion/Echohearts-Ecokins` is Eco-Kin support/reference and must defer roster authority to the canonical 125-ID Permanent Dex.
- `Dlomotion/ECO-KIN-Game`, `Dlomotion/ECHOHEARTS-REBEARTH-`, and `Dlomotion/Echohearts` are supporting/legacy sources unless a task explicitly targets them.
- `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-` owns executable UE5.8 runtime/build/evidence. Canon and production contracts remain in `Dlomotion/Echohearts-Rebearth`.
- When repositories disagree, report the conflict and reconcile toward the primary production authority; do not silently fork canon or runtime architecture.

### Required Copilot behavior for fixes
When the user asks to “fix the code,” Copilot must:
- inspect before editing;
- state the root cause when evidence supports one;
- repair related compile/runtime hazards encountered in the touched path;
- preserve existing public contracts unless the fix requires a documented migration;
- add or update tests/checks where practical;
- avoid fake placeholders presented as finished gameplay;
- distinguish repository/static success from UE5.8 runtime verification;
- finish with files changed, tests run, results, unresolved risks, and the smallest next step.

### Verification language
Use only evidence-supported statuses such as:
- `STATIC CHECK PASSED`
- `REPOSITORY CONTRACT PASSED`
- `CI PREFLIGHT PASSED`
- `NOT VERIFIED — UE5.8 BUILD/RUNTIME EVIDENCE REQUIRED`

A feature becomes runtime-verified only after applicable real-engine evidence exists, such as clean clone/LFS retrieval, UHT, Development Editor build, editor launch, map load, PIE/runtime execution, packaged Development build, server/client testing, save recovery, target-hardware execution, or other task-specific proof.

