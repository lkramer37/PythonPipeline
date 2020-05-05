# Tic Tac Toe Pipeline

The 
[Build a Python app with PyInstaller](https://jenkins.io/doc/tutorials/build-a-python-app-with-pyinstaller/)
tutorial was used as a template for this pipeline repository.

The repository contains a simple Python application for playing Tic Tac Toe on the command line. It also contains unit tests with 80% coverage. These are tested with pytest to check that this function works as expected and the results are saved to a JUnit XML report.

The delivery of the Tic Tac Toe game through PyInstaller converts this tool into a standalone executable file for Linux, which you can download through Jenkins and execute at the command line on Linux machines without Python.

The `Jenkinsfile` implements the pipeline through Jenkins
Webhook for automated build


