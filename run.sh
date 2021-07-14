#!/bin/bash
export FLASK_APP=ner.app
export FLASK_ENV=development
export CUDA_VISIBLE_DEVICES="" # Uncomment this if you want to use CUDA

flask run
