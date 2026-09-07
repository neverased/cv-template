# Dependency and upstream review — 2026-09-07

## Dependency inventory

This is a LaTeX project, with a Python standard-library-only cover letter generator. There are no npm, pip or other application dependency manifests or lockfiles. TeX packages are supplied by TeX Live; CI actions use maintained major-version tags.

| Dependency | Previous reference | Current reference | Latest release verified |
| --- | --- | --- | --- |
| Font Awesome | `fontawesome6` | `fontawesome7`, minimum date `2026/08/09` | `7.3.1-1` |
| `actions/checkout` | `v6` | `v7` | `v7.0.1` |
| `actions/labeler` | `v6` | `v7` | `v7.0.0` |
| `actions/upload-artifact` | `v7` | unchanged | `v7.0.1` |
| `dorny/paths-filter` | `v4` | unchanged | `v4.0.3` |
| `codelytv/pr-size-labeler` | `v1` | unchanged | `v1.10.4` |
| `crazy-max/ghaction-github-labeler` | `v6` | unchanged | `v6.0.0` |
| `actions/first-interaction` | `v3` | unchanged | `v3.1.0` |

GitHub's compare API confirmed that every current major-version action tag points to the same commit as the latest release above. The official [checkout v7 documentation](https://github.com/actions/checkout/tree/v7) and [labeler v7 documentation](https://github.com/actions/labeler/tree/v7) were checked for compatibility. The workflows do not use checkout on `pull_request_target`, so checkout v7's restriction on checking out fork code under privileged triggers does not require an override.

[CTAN](https://ctan.org/pkg/fontawesome7) and the [package release](https://github.com/braniii/fontawesome/releases/tag/v7.3.1-1) confirm Font Awesome `7.3.1-1` as the current release. All other TeX packages remain distribution-managed. The build now runs `tlmgr update --self --all` before compilation. The tested `texlive/texlive:latest` image reported no available TeX updates, both before and after the build.

Tested image digest: `sha256:66446fb092ef02d6dc31bba079d9bdc83e8a6af00562c6062bb97ae8e91814ea`. Local container verification used Docker Desktop on ARM64; hosted CI uses an Ubuntu runner and was not dispatched.

## Upstream

Fetched `origin` and `upstream` and confirmed that the GitHub fork parent is `posquit0/Awesome-CV`. The common ancestor is `36075ed034f7dbb8d3d35ec0cfac725f743fc3e8`. Only two upstream commits were absent from this fork's history:

- [`8b850b4`](https://github.com/posquit0/Awesome-CV/commit/8b850b477803a929a6dd74a74e3d5ab6b735d869): checkout v6 → v7. Applied the equivalent workflow changes locally.
- [`35f27d6`](https://github.com/posquit0/Awesome-CV/commit/35f27d64863793feb324df0be31e4aaecd64884f): first-interaction v1 → v3. The fork already uses v3, so no equivalent change was needed.

There are no new upstream template changes to import. Existing fork font fallbacks and personalized CV contents were preserved. No upstream merge or cherry-pick was needed. Updates are recorded as local commits; nothing has been pushed.

## CI compatibility fixes

- Updated integration and label synchronization push triggers from `master` to the fork's actual default branch, `main`.
- Replaced deprecated `set-output` plumbing with the outputs provided directly by `dorny/paths-filter`.
- Enabled noninteractive LaTeX compilation with `-halt-on-error`, so a compile failure stops CI.
- Corrected existing YAML indentation errors in `welcome.yaml` and `.yamllint.yaml`, found by the full YAML lint check.

## Verification

- Existing Python unit tests: **2 passed**, locally and in the current TeX Live container.
- `actionlint` **passed**; `yamllint .github .yamllint.yaml` **passed**.
- All **8 PDF variants compiled** with LuaLaTeX, locally and in the current container.
- Rebuilt the old class with Font Awesome 6 in the same current container and font configuration: all **8 PDFs retain identical extracted text and page counts** after migration to Font Awesome 7. The four cover letters have 1 page each, both ATS variants have 2, the CV has 3, and the resume has 2.
- A smoke document containing all **23 icon commands** referenced by the class compiled successfully with Font Awesome 7.
- The cover letter generator produced TeX, JSON and a **1-page PDF** from a synthetic job description in the container.
- The container's installed Font Awesome package was verified as **7.3.1-1**, TeX Live revision **79928**.
- The first pages of the container-built CV and cover letter were visually inspected.

Validation files and logs are in the ignored `output/dependency-update/` directory. Tracked example PDFs were preserved; newly built PDFs are in `output/dependency-update/container-project/examples/`.

The local Homebrew TeX installation was not upgraded globally. Its March 2026 packages and installed font variants differ from the current container, so cross-environment PDF typography and extracted table reading order differ. Local compatibility checks used an isolated TeX package tree. The current package set was fully verified in the container.

The existing small overfull-box warnings (approximately 1.46 pt in headers and 2.67 pt in one cover letter paragraph) also occur with the old class in the same container. They are baseline layout issues and were not changed by this dependency update.
