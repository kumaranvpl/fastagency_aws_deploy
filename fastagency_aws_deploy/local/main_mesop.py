from fastagency import FastAgency
from fastagency.ui.mesop import MesopUI

from ..workflow import wf

app = FastAgency(
    provider=wf,
    ui=MesopUI(),
    title="FastAgency AWS Deploy",
)

# start the fastagency app with the following command
# gunicorn fastagency_aws_deploy.local.main_mesop:app
