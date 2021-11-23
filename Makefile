############################################################################
# defaults
############################################################################
openapi-python-client=`which openapi-python-client`
pc=`which pip-compile`
ps=`which pip-sync`


############################################################################
# client generation
############################################################################
update:
	$(openapi-python-client) update --path openapi_schema.yml --config $(shell pwd)/bindings_config.yml --custom-template-path templates

create:
	$(openapi-python-client) generate --path openapi_schema.yml --config $(shell pwd)/bindings_config.yml --custom-template-path templates


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
