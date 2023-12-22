#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=${1} python3 trainer.py \
    --train_file ../processed_data/FCGEC_train.json \
    --max_source_length 512 \
    --model_name_or_path fnlp/bart-base-chinese \
    --tokenizer_name voidful/bart-base-chinese \
    --use_slow_tokenizer \
    --text_column instruction \
    --summary_column output \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 1 \
    --learning_rate 1e-5 \
    --num_train_epochs 16 \
    --checkpointing_steps epoch \
    --output_dir models/model_FCGEC01