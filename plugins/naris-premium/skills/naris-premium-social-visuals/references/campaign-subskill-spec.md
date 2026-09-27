# Campaign sub-skill specification

Create one standalone, discoverable sibling skill for each Naris Premium campaign. Name it `naris-premium-campaign-<campaign-slug>` and register it in `campaign-registry.md`.

## Required campaign package

The campaign sub-skill must contain:

- `SKILL.md` with the campaign name, purpose, activation boundary, workflow, required inputs, and completion gate;
- a campaign visual-system reference that documents the key visual and all approved overrides;
- approved campaign assets such as logos, lockups, frames, textures, backgrounds, type references, or master key visuals;
- source guideline or campaign deck when supplied by the user;
- explicit rules for fixed elements, variable elements, and prohibited combinations.

## Required visual-system fields

Document these items when they exist:

- campaign objective and audience;
- master key visual and recognizable visual codes;
- primary and secondary palette;
- typography and copy hierarchy;
- layout grid, product scale, safe zones, and logo placement;
- lighting, materials, textures, props, people, and environments;
- campaign lockup, CTA, badges, disclaimers, and mandatory copy;
- supported ratios and adaptation rules;
- reference examples and anti-examples;
- which core Daily rules are retained, overridden, or not applicable.

Do not describe an override by implication. State it explicitly, including its scope. If the campaign package is incomplete on a point that materially affects output, the campaign skill must ask the user before generating.

## Precedence

Apply rules in this order:

1. The user's current explicit brief.
2. The selected campaign sub-skill and its approved assets.
3. Shared Naris requirements for product fidelity, exact copy, claims, authorized people, and approved brand assets.
4. Core Daily visual rules only when the campaign skill explicitly retains them or is silent on a non-conflicting foundational point.

Never combine two campaign sub-skills in one post unless the user supplies an approved co-campaign guideline.

## Registration and lifecycle

After validating a new campaign skill, add it to `campaign-registry.md`. Mark ended campaigns `archived` instead of deleting them so old work can still be reproduced when explicitly requested.
