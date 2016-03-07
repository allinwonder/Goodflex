LIBS_PATH = $(PWD)/libs
TEST_FILES  ?= $(shell find ./tests -iname test_*.py)
CONFIG_FILE ?= $(PWD)/private/test.yml

.PHONY: test


test: 
	@CONFIG_FILE=$(CONFIG_FILE) $(PWD)/scripts/ci/run-test


