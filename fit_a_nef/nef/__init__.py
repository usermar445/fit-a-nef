from ..nef.mfn import FourierNet, FourierNet_key, GaborNet, GaborNet_key
from ..nef.mlp import MLP, MLP_key
from ..nef.rffnet import RFFNet, RFFNet_key
from ..nef.siren import SIREN, SIREN_key
from ..nef.hsiren import HSIREN, HSIREN_key
from ..nef.hypllmlp import HYPLLMLP, HYPLLMLP_key

param_key_dict = {
    "FourierNet": FourierNet_key,
    "GaborNet": GaborNet_key,
    "MLP": MLP_key,
    "RFFNet": RFFNet_key,
    "SIREN": SIREN_key,
    "HSIREN": HSIREN_key,
    "HYPLLMLP": HYPLLMLP_key
}
