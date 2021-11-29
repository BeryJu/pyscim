.SHELLFLAGS += -x -e
PWD = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)

gen-web:
	docker run \
		--rm -v ${PWD}:/local \
		--user ${UID}:${GID} \
		openapitools/openapi-generator-cli generate \
		-i https://raw.githubusercontent.com/JanssenProject/jans-scim/master/server/src/main/resources/jans-scim-openapi.yaml \
		-g python \
		-o /local/ \
		--additional-properties=packageName=pyscim
