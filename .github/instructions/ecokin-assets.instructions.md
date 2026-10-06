---
applyTo: "**/*.md,**/*.html,**/*.json,**/*.csv"
---

# Eco-Kin asset/catalog instructions

This repository is a supporting Eco-Kin asset/catalog source. The 125-ID Permanent Dex in `Dlomotion/Echohearts-Rebearth` remains authoritative.

Do not auto-promote historical names, prototypes, forms, mutations, image filenames, or intake IDs into new Permanent Dex identities. Preserve approved visual identity and provenance. Use Vibrance, Density, Harmony, and Purity for production attribute references. Keep Nature classified as a Legendary Humanoid-Kin with conditional Mutations.

Executable UE5.8 implementation belongs in `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-`.

## Toolchain-resolution routing (2026-10-06 intake)

This repository is support/archive only. Do not copy a compiler driver or add executable build/runtime code here.

- Executable compiler resolution lives in `Dlomotion/ECHOHEARTS-REBEARTH-BUILD-/BuildScripts/EchoheartsCompiler.py`; route repairs there. Canonical documentation goes to `Dlomotion/Echohearts-Rebearth`.
- Explicit compiler targets must resolve via PATH or be regular executable files; reject blank, missing, directory, and unsupported targets. Never treat `shutil.which(x) or x` as proof a tool exists, and never silently classify unknown tools as GNU.
- Use argv-based subprocess calls; filename blacklists (e.g. 'hack'/'override') are not security controls.
- Do not add the proposed Unreal Blueprint string library, the broken std::string-to-char-array example, or magic tracking IDs 0x2C/0x2D here.
- Do not turn this technical intake into Eco-Kin canon; the 125-ID Permanent Dex is unchanged.
- STATIC CHECK PASSED requires retained evidence; UE5.8 runtime is NOT YET VERIFIED without BUILD evidence.
