#!/usr/bin/env bash
# perform a major or minor release

source scripts/helpers.sh

# Check for python dependencies needed for release
check_python_deps() {
    if [ -z $(command -v openapi-python-client) ]; then
        echo "openapi-python-client python dependency not found"
        exit 1
    fi
}

# Commit changed files
# $1: version
commit_version_changes() {
    local version=${1}

    echo "Committing version changes"

    git add setup.py osidb_bindings
    git commit -m "Preparation of ${version} release"
    echo
}

# Commit changed files
# $1: version
commit_bindings_changes() {
    local version=${1}

    echo "Committing bindings changes"

    git add setup.py osidb_bindings
    git commit -m "Regenerate bindings for ${version} release"
    echo
}

# Get number of the latest OSIDB version
get_new_version() {
    osidb_github_base_link="https://api.github.com/repos/RedHatProductSecurity/osidb"

    # Get latest tagged OSIDB version
    local response=$(curl -s -f "${osidb_github_base_link}/tags" \
    -f -w 'HTTPSTATUS:%{http_code}\n')

    local body=$(echo ${response} | sed -E 's/HTTPSTATUS\:[0-9]{3}$//')
    local status=$(echo ${response} | tr -d '\n' | sed -E 's/.*HTTPSTATUS:([0-9]{3})$/\1/')

    if [ ! ${status} -eq 200 ]; then
        echo "Error accessing \"${osidb_github_base_link}/tags\" [HTTP status: ${status}]"
        exit 1
    fi

    latest_osidb_version=$(echo ${body} | jq -r ".[0] | .name")
    local split_osidb_version=($(echo "${latest_osidb_version}" | tr "." '\n'))

    # PATCH version is not synced between OSIDB and bindings, set it to zero
    split_osidb_version[2]="0"

    # Get latest tagged bindings version
    latest_bindings_version=$(git tag --sort '-authordate' | head -n 1)
    local split_bindings_version=($(echo "${latest_bindings_version}" | tr "." '\n'))

    # Based on the versions check whether the major/minor release is needed
    if [ ${split_osidb_version[0]} -gt ${split_bindings_version[0]} ]; then
        echo "New major version of OSIDB found [${latest_osidb_version}]"
        new_version=$(echo $(local IFS="." ; echo "${split_osidb_version[*]}"))
    elif [ ${split_osidb_version[1]} -gt ${split_bindings_version[1]} ];then
        echo "New minor version of OSIDB found [${latest_osidb_version}]"
        new_version=$(echo $(local IFS="." ; echo "${split_osidb_version[*]}"))
    else
        echo "No new major or minor version of OSIDB. Release is not needed."
        echo "OSIDB latest version: ${latest_osidb_version}"
        echo "bindings latest version: ${latest_bindings_version}"

        exit 1
    fi

    echo "Preparing ${new_version} bindings release"
    echo
}

# Get OpenAPI schema from gitlab API
# $1: version
get_schema() {
    local version=$1

    echo "Downloading OSIDB schema version "
    local response=$(curl -s "https://raw.githubusercontent.com/RedHatProductSecurity/osidb/${version}/openapi.yml" \
    -o osidb_bindings/openapi_schema.yml -f -w 'HTTPSTATUS:%{http_code}\n')

    local status=$(echo ${response} | tr -d '\n' | sed -E 's/.*HTTPSTATUS:([0-9]{3})$/\1/')

    if [ ! ${status} -eq 200 ]; then
        echo "Error accessing \"https://raw.githubusercontent.com/RedHatProductSecurity/osidb/${version}/openapi.yml\" [HTTP status: ${status}]"
        exit 1
    fi
}

# Main section
check_are_you_serious
check_python_deps
check_master_branch
get_new_version

create_new_branch "v${new_version}"
get_schema ${latest_osidb_version}
make update
review
commit_bindings_changes ${new_version}

update_version ${new_version}
review
commit_version_changes ${new_version}

push_branch "v${new_version}"
merge_request ${new_version}

exit 0
