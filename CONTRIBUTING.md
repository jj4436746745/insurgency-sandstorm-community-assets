# Contributing

## Pull requests

Branch from `main` for one change, such as `little-bird/seat-fix`. Open a pull request against `main`, review and test the change, then merge and delete the branch.

Use the Sandstorm Mod Editor (UE 4.27.2). Coordinate edits to the same Unreal package since Git cannot merge those files. Preserve paths relative to `Content/` and give new packs a dedicated folder under `/Game/Assets/`.

In the pull request, list changed packages, the SDK version, and checks performed. Document any required SDK assets and credit third-party assets with their sources and reuse terms.

## Build a pack ZIP

```sh
python3 scripts/build_pack.py little-bird
```

This writes `dist/little-bird.zip` with the pack README and installable files at their `Content/` paths.

## Publish a Little Bird preview

Update [VERSION](packs/little-bird/VERSION) and [release notes](packs/little-bird/RELEASE_NOTES.md) in a pull request. Use a new preview version such as `0.1.0-preview.2`. Include the SDK version and validation status in the notes.

When the version change merges to `main`, the workflow builds the ZIP and attaches it with its SHA-256 checksum to a prerelease tagged from that commit. The original ZIP link in `previews/` stays available.

Install Git LFS before cloning editable assets. In an existing clone, run `git lfs install` and `git lfs pull` after updating.
