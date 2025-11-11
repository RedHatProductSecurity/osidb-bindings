#!/usr/bin/env bash
# perform a major or minor release

source scripts/helpers.sh

# Get number of the latest OSIDB version
get_new_version() {
    osidb_repo_url="https://github.com/RedHatProductSecurity/osidb.git"

    # Get latest OSIDB release branch name using git ls-remote
    latest_osidb_release_branch=$(git ls-remote --heads "${osidb_repo_url}" 'release-*' | \
        sed 's|.*/||' | \
        grep -E '^release-[0-9]+\.[0-9]+\.[0-9]+$' | \
        sort -r -V | head -n 1)

    if [ -z "${latest_osidb_release_branch}" ]; then
        echo "Error: Could not fetch release branches from ${osidb_repo_url}"
        exit 1
    fi

    latest_osidb_version=${latest_osidb_release_branch#"release-"}
    IFS='.' read -ra split_osidb_version <<< "${latest_osidb_version}"

    # PATCH version is not synced between OSIDB and bindings, set it to zero
    split_osidb_version[2]="0"

    # Get latest tagged bindings version
    latest_bindings_version=$(git tag --sort=-v:refname | head -n 1)
    IFS='.' read -ra split_bindings_version <<< "${latest_bindings_version}"

    # Based on the versions check whether the major/minor release is needed
    if [ ${split_osidb_version[0]} -gt ${split_bindings_version[0]} ]; then
        echo "New major version of OSIDB found [${latest_osidb_version}]"
        new_version=$(IFS='.'; echo "${split_osidb_version[*]}")
    elif [ ${split_osidb_version[1]} -gt ${split_bindings_version[1]} ];then
        echo "New minor version of OSIDB found [${latest_osidb_version}]"
        new_version=$(IFS='.'; echo "${split_osidb_version[*]}")
    else
        echo "No new major or minor version of OSIDB. Release is not needed."
        echo "OSIDB latest version: ${latest_osidb_version}"
        echo "bindings latest version: ${latest_bindings_version}"

        exit 1
    fi

    echo "Preparing ${new_version} bindings release"
    echo
}

# Main section
check_are_you_serious
check_python_deps
check_master_branch
get_new_version

create_new_branch "v${new_version}"
get_schema ${latest_osidb_release_branch}
make update
review
commit_bindings_changes ${new_version}

update_version ${new_version}
update_schema_version ${new_version}
review
commit_version_changes ${new_version}

push_branch "v${new_version}"
pull_request ${new_version}

exit 0
