# Branches
This repository has 2 protected branches:
1. `staging`
1. `master`

Releases will be deployed from master while staging collects all features for next release. For saving ci-cycles, tests will only run on feature branches and staging, while deploy jobs only run on master.
