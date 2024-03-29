# Changelog

All notable changes to Hint Hotkeys will be documented here. You can click on each release number to be directed to a detailed log of all code commits for that particular release. The download links will direct you to the GitHub release page, allowing you to manually install a release if you want.

If you enjoy Hint Hotkeys, please consider supporting my work on Patreon:

<p align="center">
<a href="https://www.patreon.com/glutanimate" rel="nofollow" title="Support me on Patreon 😄"><img src="https://glutanimate.com/logos/patreon_button.svg"></a>
</p>

:heart: My heartfelt thanks goes out to everyone who has supported this add-on through their tips, contributions, or any other means (you know who you are!). All of this would not have been possible without you. Thank you for being awesome!

## [Unreleased]

## [1.0.0] - 2023-04-14

### [Download](https://github.com/glutanimate/hint-hotkeys/releases/tag/v1.0.0)

### Changed

- Completely rewrote the add-on with 2.1.5x+ compatibility in mind (tested on 2.1.49 - 2.1.62)
- Changed default hotkey for revealing all hints to "Shift+H" in order to avoid key conflict with Image Occlusion Enhanced

### Added

- Hotkeys can now be configured via Anki's built-in add-on config editor

### Fixed

- Fixed an issue that was causing the add-on not to work properly when audio or TTS was present on the card (thanks to DoctorToBeIn23 for the report and ijgnd for the fix!)
- Fixed an issue that was preventing the reveal all hotkey from actually revealing all hints


## 0.1.0 - 2017-08-23

### Added

- Initial release of Hint Hotkeys, based on [Hint-peeking Keyboard Bindings](https://ankiweb.net/shared/info/2616209911) for Anki 2.0 by Ben Lickly

[Unreleased]: https://github.com/glutanimate/hint-hotkeys/compare/v0.0.0...HEAD

-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).