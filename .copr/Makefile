srpm:
	@echo ">Installing SRPM dependencies"
	dnf install -y python3-setuptools rpmdevtools

	@echo ">Setting up rpm build environment"
	rpmdev-setuptree -d

	@echo ">Building SRPM"
	scripts/build_srpm.sh $(outdir)
