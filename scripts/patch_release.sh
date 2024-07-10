#!/usr/bin/env bash
# perform a patch release

source scripts/helpers.sh

# Parse current version from setup.py file and increment the PATCH digit
get_new_version() {
    local current_version=$(cat setup.py | grep -Po '(?<=version=\")\d+\.\d+\.\d+')
    new_version=$(increment_version ${current_version} 2)
}

# Commit changed files
# $1: version
commit() {
    local version=${1}

    echo "Committing changes"

    git add setup.py CHANGELOG.md osidb_bindings/bindings/pyproject.toml osidb_bindings/constants.py osidb_bindings.spec
    git commit -m "Preparation of ${version} release"
    echo
}

# Main section
check_are_you_serious
check_master_branch
get_new_version

create_new_branch "v${new_version}"
update_version ${new_version}
review

commit ${new_version}
push_branch "v${new_version}"
pull_request ${new_version}

exit 0
