## 1.3.0 (2023-12-11)

### Feat

- use sepal_ui==2.17 to avoid conflicts with ipyleaflet
- add license dialog
- separate reclassify tile

### Refactor

- **decorator**: remove debug arg

## 1.2.0 (2023-10-05)

### Feat

- add GWB system version on the appbar

### Refactor

- use warning color on deprecated tools
- separate reclassify process as different tile
- **ReclassifyUI**: fix order of loading_button params

## 1.1.0 (2023-10-05)

### Feat

- fix#72. Add stats param to fragmentation module
- deprecate modules. check https://ies-ows.jrc.ec.europa.eu/gtb/GWB/GWB_changelog.txt
- use landing page as ui default card
- define a landing page to load tiles
- change waiting message

### Fix

- fix image links https://github.com/sepal-contrib/gwb/pull/64#issue-1684805820
- fix legacy links. closes #68
- typo in false_value

### Refactor

- ignore vscode files
- do all imports on ui directly instead of calling notebooks and show a loading message
