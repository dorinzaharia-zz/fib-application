#!/bin/bash
pylint3 fibonacci --rcfile pylintrc.rc

pytest tests/
