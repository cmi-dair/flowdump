# `flowdump`

NiPype workflow serializer for use with [`flowview`](https://cmi-dair.github.io/flowview/).

## Usage

### Simple:

```Python
import nipype.pipeline.engine as pe  # pypeline engine
from flowdump import run_and_save_workflow

# Typical NiPype workflow creation
amazing_workflow = pe.Workflow(name="main_workflow")
# amazing_workflow.connect(...)
# amazing_workflow.connect(...)
# amazing_workflow.connect(...)

# Let `flowdump` execute and save pre- and post-execution data.
run_and_save_workflow(
    amazing_workflow,
    out_dir='my/target/dir'
)
```

### Advanced:

If more control over the workflow execution is needed

```Python
import nipype.pipeline.engine as pe  # pypeline engine
import os.path
from flowdump import WorkflowJSONMeta, save_workflow_json

# Typical NiPype workflow creation
amazing_workflow = pe.Workflow(name="main_workflow")
# amazing_workflow.connect(...)
# amazing_workflow.connect(...)
# amazing_workflow.connect(...)

# Create workflow metadata object (traces execution time and stage)
workflow_meta = WorkflowJSONMeta(
    pipeline_name='My amazing pipeline',
    stage='pre'
)
# Dump pre-execution workflow
save_workflow_json(
    filename=os.path.join('my/target/dir', workflow_meta.filename()),
    workflow=amazing_workflow,
    meta=workflow_meta
)

# Execute NiPype workflow
amazing_workflow_result = amazing_workflow.run()

# Update metadata
workflow_meta.stage = 'post'
# Dump post-execution workflow
save_workflow_json(
    filename=os.path.join('my/target/dir', workflow_meta.filename()),
    workflow=amazing_workflow_result,
    meta=workflow_meta
)
```

### Custom field serialization

Custom serializers can be implemented for projects with custom NiPype Node types

```Python
def my_custom_serializer(
        flowdump_serializer: Callable[[object], object],
        obj: object
):
    if isinstance(obj, MyType):
        return my_make_string(obj)
    return flowdump_serializer(obj)

save_workflow_json(
    filename=os.path.join('my/target/dir', workflow_meta.filename()),
    workflow=amazing_workflow_result,
    meta=workflow_meta
)
```

## Todo

This is a template repository. Below is a checklist of things you should do to use it:

1. Rewrite this `README` file.
2. Update the pre-commit versions in `.pre-commit-config.yaml`.
3. Install the `pre-commit` hooks.
4. Update the `LICENSE` file to your desired license and set the year.
5. Replace "ENTER_YOUR_EMAIL_ADDRESS" in `CODE_OF_CONDUCT.md`
6. Remove the placeholder src and test files, these are there merely to show how the CI works.
7. Update `pyproject.toml`
8. Update the name of `src/APP_NAME`
