#!/usr/bin/env bash
# helpers used across BASH scripts

# Check before starting the release process
# $1: release type
check_are_you_serious() {
    echo "Starting the OSIDB bindings release process."
    read -erp "Do you want to continue? [y/N]: " answer
    echo
    if [[ "${answer}" != "y" ]]; then
        exit 1
    fi
}

# Check if current branch is master.
check_master_branch() {
    current_branch=$( git branch | awk '/^* / {FS = " "; print $2}' )
    # TODO: fix this branch name back to master
    if [[ "${current_branch}" != "master" ]]; then
        echo "ERROR: Your branch is not 'master'. A new release has to be done from master."
        echo
        echo "Please switch the branch to master and start this script again."
        echo
        exit 1
    fi
}

# Increments the part of the string
# $1: current version
# $2: version part: 0 – major, 1 – minor, 2 – patch
increment_version() {
    local current_version=$1
    local version_part=$2

    local version=($(echo "${current_version}" | tr "." '\n'))
    version[${version_part}]=$((version[${version_part}]+1))
    echo $(local IFS="." ; echo "${version[*]}")
}

# Update the version in files
# $1: new version
update_version() {
    local version=$1

    echo

    echo "Replacing version in setup.py to ${version}"
    sed -i 's/version="[0-9]*\.[0-9]*\.[0-9]*"/version="'${version}'"/g' setup.py

    echo "Replacing version in pyproject.toml of low level bindings to ${version}"
    sed -i 's/version = "[0-9]*\.[0-9]*\.[0-9]*"/version = "'${version}'"/g' osidb_bindings/bindings/pyproject.toml

    echo
}

# Create new git branch
# $1: branch name
create_new_branch() {
    local branch_name=$1

    echo "New branch name is ${branch_name}"


    echo "Creating new branch ${branch_name}"
    echo

    git checkout -b ${branch_name}
}

# Push branch
# $1: branch name
push_branch() {
    local branch_name=$1

    echo "Pushing release branch"
    read -erp "Push branch ${branch_name} to Git server? [y/N]: " answer
    if [[ "$answer" != "y" ]]; then
        exit 1
    fi

    git push --set-upstream origin ${branch_name}
    echo
}

# Commit changed files
# $1: version
merge_request() {
    local version="${1}"

    base_link="https://git.prodsec.redhat.com/devops/osidb-bindings/merge_requests/new"
    url_with_args="${base_link}?merge_request%5Bsource_branch%5D=v${version}&merge_request%5Btitle%5D=preparation%20of%20${version}%20release"
    echo "Trying to open the following link in browser to create a merge request into the master branch:"
    echo
    echo "    ${url_with_args}"
    echo
    xdg-open "${url_with_args}" || (
        echo "Failed to open URL to create merge request automatically."
        echo "Please open URL manually in your browser"
        echo
    )
}

# Review changes
review() {
    echo "Review of changes"
    echo
    echo "Please run command \"git diff\" in another terminal"
    echo "to check if versions were updated properly."
    read -erp "Are changes OK? [y/N]: " answer

    if [[ "${answer}" != "y" ]]; then
        exit 1
    fi
    echo
}
