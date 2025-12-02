# Changelog

## 2.6.0 (2025-12-02)

Full Changelog: [v2.5.1...v2.6.0](https://github.com/channel3-ai/sdk-python/compare/v2.5.1...v2.6.0)

### Features

* **api:** manual updates ([9519dd8](https://github.com/channel3-ai/sdk-python/commit/9519dd8921ac035568f8655432d1525d8281e2c5))
* Use Product-Output schema in Stainless config ([b267853](https://github.com/channel3-ai/sdk-python/commit/b2678538464c4a68a8eee2502d961d5e0d9a929c))

## 2.5.1 (2025-11-28)

Full Changelog: [v2.5.0...v2.5.1](https://github.com/channel3-ai/sdk-python/compare/v2.5.0...v2.5.1)

### Bug Fixes

* ensure streams are always closed ([bb50c14](https://github.com/channel3-ai/sdk-python/commit/bb50c1480f16250cb9fe58a91cf4032a0091b354))


### Chores

* add Python 3.14 classifier and testing ([9af2199](https://github.com/channel3-ai/sdk-python/commit/9af2199a3c6b2f8d08ad4ce19fd2db7c1ec5b794))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([2f3e065](https://github.com/channel3-ai/sdk-python/commit/2f3e065bafeebac2f1c78cb8d4956b014264c63c))

## 2.5.0 (2025-11-12)

Full Changelog: [v2.4.0...v2.5.0](https://github.com/channel3-ai/sdk-python/compare/v2.4.0...v2.5.0)

### Features

* Test: Stainless permissions and docs update ([b210191](https://github.com/channel3-ai/sdk-python/commit/b2101914592aeff02fa684dd6223b9035c574647))
* Updating config ([67c3535](https://github.com/channel3-ai/sdk-python/commit/67c35353f5fa5958daef94694ddddb4ce091920e))


### Bug Fixes

* compat with Python 3.14 ([03cfdff](https://github.com/channel3-ai/sdk-python/commit/03cfdffbd9d1393ffa6119b20808821c7f90d8d8))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([e866804](https://github.com/channel3-ai/sdk-python/commit/e8668049c83afac33b78f0c6454da37be195491a))


### Chores

* **package:** drop Python 3.8 support ([677cd39](https://github.com/channel3-ai/sdk-python/commit/677cd392a32a1037f2445189a15a5500bf0790af))

## 2.4.0 (2025-11-10)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/channel3-ai/sdk-python/compare/v2.3.0...v2.4.0)

### Features

* **api:** api update ([f50613e](https://github.com/channel3-ai/sdk-python/commit/f50613e9cf5d2067b282896dfafcb73ef99ee0ae))


### Bug Fixes

* **client:** close streams without requiring full consumption ([4d44bb1](https://github.com/channel3-ai/sdk-python/commit/4d44bb1d045d7d2447bc305dd8463e27dd170175))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([ef7fe91](https://github.com/channel3-ai/sdk-python/commit/ef7fe91e5e5c14e15172642362aee07b96f19b3d))
* **internal:** grammar fix (it's -&gt; its) ([ae7ab14](https://github.com/channel3-ai/sdk-python/commit/ae7ab1494bc21b8b5aeefb91af3353b696949bcb))

## 2.3.0 (2025-10-28)

Full Changelog: [v2.2.1...v2.3.0](https://github.com/channel3-ai/sdk-python/compare/v2.2.1...v2.3.0)

### Features

* **api:** api update ([0f0cc28](https://github.com/channel3-ai/sdk-python/commit/0f0cc28d457562ccf192e206b7ca77a06ac32759))
* **api:** api update ([ddc05e6](https://github.com/channel3-ai/sdk-python/commit/ddc05e676b4faf282733af7ed40eb25a9fba1118))
* **api:** api update ([e2d274a](https://github.com/channel3-ai/sdk-python/commit/e2d274aabd3eaa4942a93cb1c212cad69f634f42))

## 2.2.1 (2025-10-21)

Full Changelog: [v2.2.0...v2.2.1](https://github.com/channel3-ai/sdk-python/compare/v2.2.0...v2.2.1)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([9fce17d](https://github.com/channel3-ai/sdk-python/commit/9fce17d430d871ec313c00be59baa4cc674405a6))
* do not install brew dependencies in ./scripts/bootstrap by default ([4195b56](https://github.com/channel3-ai/sdk-python/commit/4195b56c72109be10c6444cc66b262e405562f02))
* **internal:** detect missing future annotations with ruff ([ee0fee8](https://github.com/channel3-ai/sdk-python/commit/ee0fee8c45a79bbc7436bbdc9216fed4c4f8549f))
* **internal:** update pydantic dependency ([748c67f](https://github.com/channel3-ai/sdk-python/commit/748c67f3e609d241af1ee9342ef3755589d3534c))
* **types:** change optional parameter type from NotGiven to Omit ([61aab9b](https://github.com/channel3-ai/sdk-python/commit/61aab9bec310efab0ce7a4b13440f1207bcbef8a))

## 2.2.0 (2025-09-16)

Full Changelog: [v2.1.0...v2.2.0](https://github.com/channel3-ai/sdk-python/compare/v2.1.0...v2.2.0)

### Features

* **api:** manual updates ([79f6922](https://github.com/channel3-ai/sdk-python/commit/79f69227ff70ac778731b6dac5f1297a66800893))

## 2.1.0 (2025-09-16)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/channel3-ai/sdk-python/compare/v2.0.0...v2.1.0)

### Features

* **api:** api update ([b6dac15](https://github.com/channel3-ai/sdk-python/commit/b6dac1516907c474ecfd919c5fad34943b59b101))

## 2.0.0 (2025-09-16)

Full Changelog: [v0.0.2...v2.0.0](https://github.com/channel3-ai/sdk-python/compare/v0.0.2...v2.0.0)

### Features

* **api:** manual updates ([f91f4f1](https://github.com/channel3-ai/sdk-python/commit/f91f4f163ea386464efa5b307ec11b689922493e))


### Chores

* update SDK settings ([35e85c7](https://github.com/channel3-ai/sdk-python/commit/35e85c70a123d6dd8b745999388082499562347e))

## 0.0.2 (2025-09-16)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/channel3-ai/sdk-python/compare/v0.0.1...v0.0.2)

### Chores

* sync repo ([ab5e4db](https://github.com/channel3-ai/sdk-python/commit/ab5e4db3bb8b00b432e09fd05079277cad518277))
* update SDK settings ([1bdef96](https://github.com/channel3-ai/sdk-python/commit/1bdef969e22a85f658edc0f31eef8657df2b2090))
