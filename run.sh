#!/bin/bash
# Uncomment this if you want to use CUDA. You will need enough memory in your card
export CUDA_VISIBLE_DEVICES=""

uvicorn ner:app --reload
