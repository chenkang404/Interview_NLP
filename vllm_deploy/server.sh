# ps -ef |grep /root/miniconda3/envs/MiniCPMV2/bin/vllm |grep -v grep |awk -F" "  {'print $2'}|xargs -i kill -9 {}

export CUDA_VISIBLE_DEVICES=2

nohup python -m vllm.entrypoints.openai.api_server \
    --model /workspace/HOSTDIR/model_path/Qwen/Qwen2.5-32B-Instruct \
    --served-model-name Qwen2-5-32B \
    --dtype float16 \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90 \
    --max-num-seqs 8 \
    --trust-remote-code \
    --tensor-parallel-size 1 \
    --port 5115 \
    --host 0.0.0.0 \
    > ./vllm_qwen2-5-32B.log 2>&1 &
