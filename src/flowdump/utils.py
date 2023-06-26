from os import PathLike
from typing import Union, Optional, Callable

from .core import WorkflowRaw
from .workflow_json import WorkflowJSONMeta, save_workflow_json
import pathlib as pl


def run_and_save_workflow(
        workflow: WorkflowRaw,
        out_dir: Union[PathLike, str],
        workflow_name: Optional[str] = None,
        custom_serializer: Optional[Callable[[Callable[[object], object], object], object]] = None
):
    out_dir = pl.Path(out_dir)
    workflow_name = 'Workflow' if workflow_name is None else workflow_name

    workflow_meta = WorkflowJSONMeta(
        pipeline_name=workflow_name,
        stage='pre'
    )
    save_workflow_json(
        filename=out_dir / workflow_meta.filename(),
        workflow=workflow,
        meta=workflow_meta,
        custom_serializer=custom_serializer
    )

    amazing_workflow_result = workflow.run()

    workflow_meta.stage = 'post'
    save_workflow_json(
        filename=out_dir / workflow_meta.filename(),
        workflow=amazing_workflow_result,
        meta=workflow_meta,
        custom_serializer=custom_serializer
    )
