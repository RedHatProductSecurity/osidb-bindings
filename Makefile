############################################################################
# defaults
############################################################################
openapi-python-client=`which openapi-python-client`
pc=`which pip-compile`
ps=`which pip-sync`
package_dir=osidb_bindings/
bindings_dir=$(package_dir)bindings/


############################################################################
# client generation
############################################################################
update:
	cd $(package_dir) \
	&& $(openapi-python-client) update --path openapi_schema.yml \
	--config $(shell pwd)/$(package_dir)bindings_config.yml \
	--custom-template-path templates
	touch $(bindings_dir)__init__.py

create:
	cd $(package_dir) \
	&& $(openapi-python-client) generate --path openapi_schema.yml \
	--config $(shell pwd)/$(package_dir)bindings_config.yml \
	--custom-template-path templates
	touch $(bindings_dir)__init__.py


############################################################################
# dev entrypoints
############################################################################
compile-deps:
	@echo ">compiling python dependencies"
	$(pc) --generate-hashes --allow-unsafe requirements/base.in
	$(pc) --generate-hashes --allow-unsafe requirements/dev.in
	[ -f requirements/local.in ] && $(pc) --generate-hashes --allow-unsafe requirements/local.in || true

sync-deps:
	@echo ">synchronizing python dependencies"
	$(ps) requirements/base.txt requirements/dev.txt $$([ -f requirements/local.txt ] && echo 'requirements/local.txt')

patch-release:
	@echo ">preparing patch release"
	scripts/patch_release.sh

release:
	@echo ">preparing release"
	scripts/update_release.sh $$(cat $(package_dir)openapi_schema.yml | grep -Po '(?<=version: )\d+\.\d+\.\d+')
	$(MAKE) update
