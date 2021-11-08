############################################################################
# defaults
############################################################################
openapi-python-client=`which openapi-python-client`


############################################################################
# client generation
############################################################################
update:
	$(openapi-python-client) update --path openapi_schema.yml --config $(shell pwd)/bindings_config.yml

create:
	$(openapi-python-client) generate --path openapi_schema.yml --config $(shell pwd)/bindings_config.yml

