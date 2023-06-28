# From: https://nipype.readthedocs.io/en/1.8.6/users/examples/workflow_from_scratch.html
import json

from flowdump.workflow_json import save_workflow_json_string, WorkflowJSONMeta

def test_workflow_from_scratch():
    from builtins import range

    import nipype.interfaces.io as nio  # Data i/o
    import nipype.interfaces.spm as spm  # spm
    import nipype.pipeline.engine as pe  # pypeline engine
    import nipype.algorithms.modelgen as model  # model specification
    from nipype.interfaces.base import Bunch
    import os  # system functions

    realign = pe.Node(interface=spm.Realign(), name="realign")
    realign.inputs.register_to_mean = True

    smooth = pe.Node(interface=spm.Smooth(), name="smooth")
    smooth.inputs.fwhm = 4

    preprocessing = pe.Workflow(name="preprocessing")
    preprocessing.connect(realign, "realigned_files", smooth, "in_files")

    specify_model = pe.Node(interface=model.SpecifyModel(), name="specify_model")
    specify_model.inputs.input_units = 'secs'
    specify_model.inputs.time_repetition = 3.
    specify_model.inputs.high_pass_filter_cutoff = 120
    specify_model.inputs.subject_info = [
        Bunch(
            conditions=['Task-Odd', 'Task-Even'],
            onsets=[list(range(15, 240, 60)),
                    list(range(45, 240, 60))],
            durations=[[15], [15]])
    ] * 4

    level1design = pe.Node(interface=spm.Level1Design(), name="level1design")
    level1design.inputs.bases = {'hrf': {'derivs': [0, 0]}}
    level1design.inputs.timing_units = 'secs'
    level1design.inputs.interscan_interval = specify_model.inputs.time_repetition

    level1estimate = pe.Node(interface=spm.EstimateModel(), name="level1estimate")
    level1estimate.inputs.estimation_method = {'Classical': 1}

    contrastestimate = pe.Node(
        interface=spm.EstimateContrast(), name="contrastestimate")
    cont1 = ('Task>Baseline', 'T', ['Task-Odd', 'Task-Even'], [0.5, 0.5])
    cont2 = ('Task-Odd>Task-Even', 'T', ['Task-Odd', 'Task-Even'], [1, -1])
    contrastestimate.inputs.contrasts = [cont1, cont2]

    modelling = pe.Workflow(name="modelling")
    modelling.connect(specify_model, 'session_info', level1design, 'session_info')
    modelling.connect(level1design, 'spm_mat_file', level1estimate, 'spm_mat_file')
    modelling.connect(level1estimate, 'spm_mat_file', contrastestimate,
                      'spm_mat_file')
    modelling.connect(level1estimate, 'beta_images', contrastestimate,
                      'beta_images')
    modelling.connect(level1estimate, 'residual_image', contrastestimate,
                      'residual_image')

    main_workflow = pe.Workflow(name="main_workflow")
    main_workflow.base_dir = "workflow_from_scratch"
    main_workflow.connect(preprocessing, "realign.realignment_parameters",
                          modelling, "specify_model.realignment_parameters")
    main_workflow.connect(preprocessing, "smooth.smoothed_files", modelling,
                          "specify_model.functional_runs")

    datasource = pe.Node(
        interface=nio.DataGrabber(infields=['subject_id'], outfields=['func']),
        name='datasource')
    datasource.inputs.base_directory = os.path.abspath('.')  # Changed from 'data' (has to exist)
    datasource.inputs.template = '%s/%s.nii'
    datasource.inputs.template_args = dict(
        func=[['subject_id', ['f3', 'f5', 'f7', 'f10']]])
    datasource.inputs.subject_id = 's1'
    datasource.inputs.sort_filelist = True

    main_workflow.connect(datasource, 'func', preprocessing, 'realign.in_files')

    datasink = pe.Node(interface=nio.DataSink(), name="datasink")
    datasink.inputs.base_directory = os.path.abspath(
        'workflow_from_scratch/output')

    main_workflow.connect(modelling, 'contrastestimate.spmT_images', datasink,
                          'contrasts.@T')

    assert json.loads(save_workflow_json_string(main_workflow, meta=WorkflowJSONMeta('Main', 'pre'))) is not None

