class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/cx/cx1/github-repo/SUTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/cx/cx1/github-repo/SUTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/cx/cx1/github-repo/SUTrack/pretrained_networks'
        self.lasot_dir = '/home/cx/cx1/github-repo/SUTrack/data/lasot'
        self.vasttrack_dir = '/home/cx/cx1/github-repo/SUTrack/data/vasttrack'
        self.got10k_dir = '/home/cx/cx1/github-repo/SUTrack/data/got10k/train'
        self.lasot_lmdb_dir = '/home/cx/cx1/github-repo/SUTrack/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/cx/cx1/github-repo/SUTrack/data/got10k_lmdb'
        self.trackingnet_dir = '/home/cx/cx1/github-repo/SUTrack/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/cx/cx1/github-repo/SUTrack/data/trackingnet_lmdb'
        self.coco_dir = '/home/cx/cx1/github-repo/SUTrack/data/coco'
        self.coco_lmdb_dir = '/home/cx/cx1/github-repo/SUTrack/data/coco_lmdb'
        self.imagenet1k_dir = '/home/cx/cx1/github-repo/SUTrack/data/imagenet1k'
        self.imagenet22k_dir = '/home/cx/cx1/github-repo/SUTrack/data/imagenet22k'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/cx/cx1/github-repo/SUTrack/data/vid'
        self.imagenet_lmdb_dir = '/home/cx/cx1/github-repo/SUTrack/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
        self.depthtrack_dir = '/home/cx/cx1/github-repo/SUTrack/data/depthtrack/train'
        self.lasher_dir = '/home/cx/cx1/github-repo/SUTrack/data/lasher/trainingset'
        self.visevent_dir = '/home/cx/cx1/github-repo/SUTrack/data/visevent/train'
        self.refcoco_dir = '/home/cx/cx1/github-repo/SUTrack/data/refcoco'
        self.tnl2k_dir = '/home/cx/cx1/github-repo/SUTrack/data/tnl2k/train'
        self.otb99_dir = '/home/cx/cx1/github-repo/SUTrack/data/otb_lang'
