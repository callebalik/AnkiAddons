# Changelog

All notable changes to [BetterTags](https://www.patreon.com/glutanimate/posts?tag=BetterTags) will be documented here.

BetterTags is currently exclusively available through Patreon early access:

<p align="center">
<a href="https://www.patreon.com/glutanimate" rel="nofollow" title="Support me on Patreon 😄"><img src="https://glutanimate.com/logos/patreon_button.svg"></a>
</p>

:heart: My heartfelt thanks goes out to everyone who has supported this add-on through their tips, contributions, or any other means (you know who you are!). All of this would not have been possible without you. Thank you for being awesome!

## [Unreleased]

## [1.0.4] - 2020-04-28

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.4)

### Added

- Added compatibility for Anki 2.1.24 and up

### Fixed

- Fixed a rare RuntimeError that would occur when performing modificaitons right before closing the browser (thanks to @aleksejrs for the report!)
- Fixed an incompatibility with "Customize Sidebar" that would cause an AttributeError when deleting tags in some scenarios (thanks to @DoctorToBein23 for the report!)


## [1.0.4-beta.1] - 2020-04-28

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.4-beta.1)

## [1.0.3] - 2020-01-28

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.3)

### Fixed

- Fixed incompatibility with other add-ons using libaddon (typing-related vendoring troubles on Anki <2.1.16)

## [1.0.2] - 2020-01-26

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.2)

### Fixed

- Actually fix incompatibility introduced by the latest Night Mode update. Starting with Anki 2.1.20, please use Anki's native Night Mode implementation.

## [1.0.1] - 2020-01-26

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.1)

### Fixed

- Fix incompatibility introduced by the latest Night Mode update. Starting with Anki 2.1.20, please use Anki's native Night Mode implementation.

## [1.0.0] - 2020-01-21

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.0)

### Added

- Support for the super-fast sidebar introduced in Anki versions 2.1.17 and up
- Support for multi-selections for almost all context menu actions
- In-place editing of tags by double-clicking on them or using the F2 hot-key
- Right-click action to pin tags to the top/bottom of the hierarchy
- Right-click action to add custom colors to tags
- Persistent storage of tag expansion state across restarting Anki, alongside storing pins and colors (thanks to qubrganor for the suggestion)
- Right-click action to expand all/collapse all sidebar items
- Option to expand/collapse all tags by default on opening the browser (thanks to qubrganor for the suggestion)
- Option to disable tag deletion confirmation pop-up (thanks to AnKing for the suggestion)
- A fully-featured options menu to configure all of these settings

### Changed

- Fully rewrote the add-on with a focus on speed, stability, and usability.
- Optimizations across the board solidify best-in-class performance for all tag modifications (e.g. updating 15K notes in 1s)
- Dropped support for Anki 2.0. You can continue using earlier versions of BetterTags with Anki 2.0 of course
- Almost all actions performed by the add-on now properly preserve item selection and keyboard focus, greatly improving telegraphing of performed actions and keyboard usage
- Tweak scrolling behavior to keep modified items in focus, but at the same time only move the view around if necessary
- Added GUI-accessible logging and debugging capabilities for easier bug reporting
- In the rare case that operations take long, the add-on now shows an interactive progress bar
- Dropped `enableHierarchicalTags` option. To disable hierarchical tree rendering you can still set a different tag separator.
- Always display Find and Replace Tags window at the center of the browser
- Prevent accidental tag deletion on empty tag entries
- Better cross-addon- and Anki-compatibility by reducing the potential interaction surface for collisions
- Allow changing most settings without Anki needing to be restarted

### Fixed

- Fix drag and drop of multiple tags causing Anki to freeze in some scenarios (thanks to galantra for the report)
- Fix tags list in sidebar closing when deleting tag (thanks to AnKing for the report)
- Fix item expansion state sometimes changing when performing drag-and-drop operations
- Fix drag-and-drop indicator jumping around on macOS (requires Anki 2.1.17+)
- Fix loss of focus when undoing actions

### Known Issues

- Anki 2.1.17+ on Windows: Tags in the tag entry drop-down box are slightly hard to read due to the background color
- All operating systems, with Night Mode installed: Tag entry drop-down box is rendered completely black or white. As a workaround you can disable "editor styling" in Night Mode's options for now. I will be working with Night Mode's dev to fix this.
- Anki 2.1.17+, all operating systems, with Night Mode installed: This is not specific to BetterTags, as vanilla Anki is also affected by this, but Night Mode currently does not color the sidebar properly. This should be fixed with Night Mode's upcoming release

### Other Notes

- For the best possible experience, please update to the [latest Anki release](https://apps.ankiweb.net/#download).https://www.patreon.com/glutanimate/posts?tag=BetterTags)on Anki versions 2.1.17 and up. Future versions of BetterTags will drop support for Anki releases prior to 2.1.17.
- Similarly, please make sure to update all add-ons that modify Anki's card browser both before updating Anki and installing BetterTags. Among the add-ons you will have to update are: [Night Mode](https://ankiweb.net/shared/info/1496166067), [Customize Sidebar](https://ankiweb.net/shared/info/1988760596). You can use Anki's add-on manager to update them via Tools → Add-ons → Check for updates.

## [1.0.0-beta.2] - 2020-01-20

### [Download](https://github.com/glutanimate/bettertags/releases/tag/v1.0.0-beta.2)

### Fixed

- Fix ConfigNotLoadedError on profile switch (thanks to @AnKingMed for the report!)

## [v1.0.0-beta.1] - 2020-01-17

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)
### Added

- Support for the super-fast sidebar introduced in Anki versions 2.1.17 and up
- Support for multi-selections for almost all context menu actions
- In-place editing of tags by double-clicking on them or using the F2 hot-key
- Right-click action to pin tags to the top/bottom of the hierarchy
- Right-click action to add custom colors to tags
- Persistent storage of tag expansion state across restarting Anki, alongside storing pins and colors (thanks to qubrganor for the suggestion)
- Right-click action to expand all/collapse all sidebar items
- Option to expand/collapse all tags by default on opening the browser (thanks to qubrganor for the suggestion)
- Option to disable tag deletion confirmation pop-up (thanks to AnKing for the suggestion)
- A fully-featured options menu to configure all of these settings

### Changed

- Fully rewrote the add-on with a focus on speed, stability, and usability.
- Optimizations across the board solidify best-in-class performance for all tag modifications (e.g. updating 15K notes in 1s)
- Dropped support for Anki 2.0. You can continue using earlier versions of BetterTags with Anki 2.0 of course
- Almost all actions performed by the add-on now properly preserve item selection and keyboard focus, greatly improving telegraphing of performed actions and keyboard usage
- Tweak scrolling behavior to keep modified items in focus, but at the same time only move the view around if necessary
- Added GUI-accessible logging and debugging capabilities for easier bug reporting
- In the rare case that operations take long, the add-on now shows an interactive progress bar
- Dropped `enableHierarchicalTags` option. To disable hierarchical tree rendering you can still set a different tag separator.
- Always display Find and Replace Tags window at the center of the browser
- Prevent accidental tag deletion on empty tag entries
- Better cross-addon- and Anki-compatibility by reducing the potential interaction surface for collisions
- Allow changing most settings without Anki needing to be restarted

### Fixed

- Fix drag and drop of multiple tags causing Anki to freeze in some scenarios (thanks to galantra for the report)
- Fix tags list in sidebar closing when deleting tag (thanks to AnKing for the report)
- Fix item expansion state sometimes changing when performing drag-and-drop operations
- Fix drag-and-drop indicator jumping around on macOS (requires Anki 2.1.17+)
- Fix loss of focus when undoing actions

### Known Issues

- Anki 2.1.17+ on Windows: Tags in the tag entry drop-down box are slightly hard to read due to the background color
- All operating systems, with Night Mode installed: Tag entry drop-down box is rendered completely black or white. As a workaround you can disable "editor styling" in Night Mode's options for now. I will be working with Night Mode's dev to fix this.
- Anki 2.1.17+, all operating systems, with Night Mode installed: This is not specific to BetterTags, as vanilla Anki is also affected by this, but Night Mode currently does not color the sidebar properly. This should be fixed with Night Mode's upcoming release

### Other Notes

- For the best possible experience, please update to the [latest Anki release](https://apps.ankiweb.net/#download).https://www.patreon.com/glutanimate/posts?tag=BetterTags)on Anki versions 2.1.17 and up. Future versions of BetterTags will drop support for Anki releases prior to 2.1.17.
- Similarly, please make sure to update all add-ons that modify Anki's card browser both before updating Anki and installing BetterTags. Among the add-ons you will have to update are: [Night Mode](https://ankiweb.net/shared/info/1496166067), [Customize Sidebar](https://ankiweb.net/shared/info/1988760596). You can use Anki's add-on manager to update them via Tools → Add-ons → Check for updates.

## [v0.1.4] - 2019-02-28

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Changed

- Make sure to also quote single tags

## [v0.1.3] - 2019-01-29

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Changed

- Refactored GUI components

### Fixed

- UnicodeEncodeError when editing certain non-latin tags on Anki 2.0

## [v0.1.2] - 2018-08-21

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Fixed

- Drag and drop actions on Anki 2.0 not working as expected on Windows & macOS

### Changed

- Sidebar is now reset after undoing add-on actions

## [v0.1.1] - 2018-08-21

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Changed

- Rename add-on to BetterTags

## [0.1.1-beta] - 2018-06-23

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Added

- Drag and drop support, including multiple items
- Tag repositioning
- Filtered deck action
- Sidebar hotkeys
- Hierarchical tags settings
- All other basic features

### Changed

- Various bug fixes and performance improvements

## [0.1.0-beta] - 2018-06-17

### [Download](https://www.patreon.com/glutanimate/posts?tag=BetterTags)

### Added

- Initial release of BetterTags

[Unreleased]: https://github.com/glutanimate/bettertags/compare/v0.1.4...HEAD
[v0.1.4]: https://github.com/glutanimate/bettertags/compare/v0.1.3...v0.1.4
[v0.1.3]: https://github.com/glutanimate/bettertags/compare/v0.1.2...v0.1.3
[v0.1.2]: https://github.com/glutanimate/bettertags/compare/v0.1.1...v0.1.2
[v0.1.1]: https://github.com/glutanimate/bettertags/compare/0.1.1-beta...v0.1.1
[0.1.1-beta]: https://github.com/glutanimate/bettertags/compare/0.1.0-beta...0.1.1-beta
[0.1.0-beta]: https://github.com/glutanimate/bettertags/tree/0.1.0-beta

-----

The format of this file is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).