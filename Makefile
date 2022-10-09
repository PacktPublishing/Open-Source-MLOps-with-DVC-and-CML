#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_VERSION = python3.8
VIRTUALENV := venv

#################################################################################
# COMMANDS                                                                      #
#################################################################################

# Set the default location for the virtualenv to be stored
# Create the virtualenv by installing the requirements and test requirements

.PHONY: virtualenv
$(VIRTUALENV)/.installed: requirements.txt
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python $(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -r requirements.txt
	touch $@

# Update the requirements to latest. This is required because typically we won't
# want to incldue test requirements in the requirements of the application, and
# because it makes life much easier when we want to keep our dependencies up to
# date.

.PHONY: update-requirements-txt
update-requirements-txt: unpinned_requirements.txt
update-requirements-txt: VIRTUALENV := /tmp/update-requirements-virtualenv
update-requirements-txt:
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python $(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install --upgrade -r unpinned_requirements.txt
	$(VIRTUALENV)/bin/pip freeze | grep -v pkg_resources==0.0.0 > requirements.txt

.PHONY: virtualenv
virtualenv: $(VIRTUALENV)/.installed

.PHONY: show
show:
	dvc exp show --drop "." --md --keep "(Experiment|.*weight.*f1.*|.*learning*|.*max_df*)" \
		--no-pager --num 2 --sort-by "results/test_metrics.json:weighted avg.f1-score"
	@ #cat exps.md
	@ #dvc exp show --drop "." --keep ".*(Experiment|weighted avg.f1*|train*)" 
	@ #dvc exp show --drop "." --keep "(Experiment|.*weighted avg.f1*|train\.*)" \

.PHONY: clear-queue
clear-queue:
	dvc queue remove --all

.PHONY: clear-exps
clear-exps:
	dvc exp remove --rev HEAD --num 1

.PHONY: clear
clear: clear-queue clear-exps

.PHONY: queue
queue:
	dvc exp run --queue \
		--set-param train.learning_rate=0.0001,0.001 \
		--set-param train.min_df=5,50,100 \
		--set-param train.max_ngrams=2,3,4 

.PHONY: run
run:
	dvc queue start --jobs 10

.PHONY: stop
stop:
	dvc queue stop