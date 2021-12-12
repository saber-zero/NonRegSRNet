python train.py --name=chikusei_5 --model_name=deformated_fusion --gpu_ids=0 --num_rho=100 --niter=2000 --niter_decay=8000 --lr=3e-4 --lr_policy=lambda --lr_decay_gamma=0.8 --lr_decay_iters=1000 --display_port=8097 --alpha=1 --beta=0.01 --gamma=0.01 --delta=1 --theta=0.01 --mu=1 --isCalSP=True --data_dir=chikusei_normal_nonrigid_5_center --print_freq=10 --batchsize=1 --which_epoch=9000 --useClamp=True

python train.py --name=wadc_5 --model_name=deformated_fusion --gpu_ids=0 --num_rho=100 --niter=2000 --niter_decay=8000 --lr=3e-4 --lr_policy=lambda --lr_decay_gamma=0.8 --lr_decay_iters=1000 --display_port=8097 --alpha=1 --beta=0.01 --gamma=0.01 --delta=1 --theta=0.01 --mu=1 --isCalSP=True --data_dir=wadc_normal_nonrigid_5_center --print_freq=10 --batchsize=1 --which_epoch=9000 --useClamp=True
