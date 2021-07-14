export CUDA_VISIBLE_DEVICES="" # Uncomment this if you want to use CUDA

pytest -v -s --cov-report html --cov=ner tests
