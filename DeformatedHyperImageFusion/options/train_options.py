"""
@Author: zhengke
@Date: 2020-07-19 21:16:57
@LastEditors: zhengke
@LastEditTime: 2020-07-20 06:47:16
@Description: Do not edit
@FilePath: \DeformatedHyperImageFusion\options\train_options.py
"""
"""
@Author: zhengke
@Date: 2020-07-19 21:16:57
@LastEditors: zhengke
@LastEditTime: 2020-07-20 06:19:17
@Description: training parser options including learning rate, lr decay policy, total training epoch, 

@FilePath: \DeformatedHyperImageFusion\options\train_options.py
"""
from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)

        parser.add_argument("--batchsize", type=int, default=1)
        parser.add_argument("--nThreads", type=int, default=0)

        parser.add_argument("--lr", type=float, default=8e-3)
        parser.add_argument(
            "--epoch_count",
            type=int,
            default=1,
            help="the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...",
        )
        parser.add_argument(
            "--which_epoch",
            type=str,
            default="latest",
            help="which epoch to load? set to latest to use latest cached model",
        )
        parser.add_argument(
            "--niter",
            type=int,
            default=1000,
            help="# of iter at starting learning rate",
        )
        parser.add_argument(
            "--niter_decay",
            type=int,
            default=3000,
            help="# of iter to linearly decay learning rate to zero",
        )
        parser.add_argument(
            "--lr_policy",
            type=str,
            default="lambda",
            help="learning rate policy: lambda|step|plateau",
        )
        parser.add_argument(
            "--lr_decay_iters",
            type=int,
            default=100,
            help="multiply by a gamma every lr_decay_iters iterations",
        )
        parser.add_argument("--lr_decay_gamma", type=float, default=0.8)
        parser.add_argument("--lr_decay_patience", type=int, default=50)
        parser.add_argument(
            "--save_epoch_freq",
            type=int,
            default=20,
            help="frequency of saving checkpoints at the end of epochs",
        )

        # new parameters
        # parser.add_argument("--deform_type", type=int, default=1, help="deformation type")

        self.isTrain = True
        return parser
