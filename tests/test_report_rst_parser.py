from flowdump.nipype_report_parser import read_report_rst_str, ReportSection

EXAMPLE_REPORT_RST = """Node: desc-sm_falff_zstd_290 (z_score_std (z_score (fsl)
========================================================


 Hierarchy : cpac_sub-123_ses-1.desc-sm_falff_zstd_290.z_score_std.z_score
 Exec ID : z_score.a0.a0.a0.a0


Original Inputs
---------------


* args : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* in_file : /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/falff_smooth_FSL_290/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/smooth/falff_maths.nii.gz
* internal_datatype : <undefined>
* nan2zeros : <undefined>
* op_string : -sub 0.673051 -div 0.058259 -mas %s
* operand_files : ['/default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/_scan_rest_run-1_acq-1/func_get_brain_mask_AFNI_129/sub-123_ses-1_task-rest_acq-1_run-1_bold_resample_calc_tshift_volreg_mask.nii.gz']
* out_file : <undefined>
* output_datatype : <undefined>
* output_type : NIFTI_GZ


Execution Inputs
----------------


* args : <undefined>
* environ : {'FSLOUTPUTTYPE': 'NIFTI_GZ'}
* in_file : /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/falff_smooth_FSL_290/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/smooth/falff_maths.nii.gz
* internal_datatype : <undefined>
* nan2zeros : <undefined>
* op_string : -sub 0.673051 -div 0.058259 -mas %s
* operand_files : ['/default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/_scan_rest_run-1_acq-1/func_get_brain_mask_AFNI_129/sub-123_ses-1_task-rest_acq-1_run-1_bold_resample_calc_tshift_volreg_mask.nii.gz']
* out_file : <undefined>
* output_datatype : <undefined>
* output_type : NIFTI_GZ


Execution Outputs
-----------------


* out_file : /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/desc-sm_falff_zstd_290/z_score_std/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/z_score/falff_maths_maths.nii.gz


Runtime info
------------


* cmdline : fslmaths /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/falff_smooth_FSL_290/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/smooth/falff_maths.nii.gz -sub 0.673051 -div 0.058259 -mas /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/_scan_rest_run-1_acq-1/func_get_brain_mask_AFNI_129/sub-123_ses-1_task-rest_acq-1_run-1_bold_resample_calc_tshift_volreg_mask.nii.gz /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/desc-sm_falff_zstd_290/z_score_std/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/z_score/falff_maths_maths.nii.gz
* cpu_percent : 105.3
* duration : 0.988226
* hostname : r036.ib.bridges2.psc.edu
* mem_peak_gb : 0.5959930419921875
* prev_wd : /default/sub-123
* working_dir : /default/sub-123/output/working/pipeline_cpac-default-pipeline/cpac_sub-123_ses-1/desc-sm_falff_zstd_290/z_score_std/_scan_rest_run-1_acq-1/_hp_0.01/_lp_0.1/_fwhm_4/z_score


Terminal output
~~~~~~~~~~~~~~~


 


Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~


 


Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~


 


Environment
~~~~~~~~~~~


* ANTSPATH : /usr/lib/ants
* C3DPATH : /opt/c3d
* FIX_VERTEX_AREA : 
* FREESURFER_HOME : /usr/lib/freesurfer
* FSFAST_HOME : /usr/lib/freesurfer/fsfast
* FSF_OUTPUT_FORMAT : nii.gz
* FSLBROWSER : /etc/alternatives/x-www-browser
* FSLDIR : /usr/share/fsl/5.0
* FSLLOCKDIR : 
* FSLMACHINELIST : 
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLREMOTECALL : 
* FSLTCLSH : /usr/bin/tclsh
* FSLWISH : /usr/bin/wish
* FSL_BIN : /usr/share/fsl/5.0/bin
* FSL_DIR : /usr/share/fsl/5.0
* FS_OVERRIDE : 0
* FUNCTIONALS_DIR : /usr/lib/freesurfer/sessions
* HOME : /jet/home/rupprech
* ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS : 1
* KMP_DUPLICATE_LIB_OK : True
* KMP_INIT_AT_FORK : FALSE
* LANG : en_US.UTF-8
* LC_ALL : en_US.UTF-8
* LD_LIBRARY_PATH : /usr/lib/fsl/5.0::/.singularity.d/libs
* LOCAL_DIR : /usr/lib/freesurfer/local
* MINC_BIN_DIR : /usr/lib/freesurfer/mni/bin
* MINC_LIB_DIR : /usr/lib/freesurfer/mni/lib
* MKL_NUM_THREADS : 1
* MNI_DATAPATH : /usr/lib/freesurfer/mni/data
* MNI_DIR : /usr/lib/freesurfer/mni
* MNI_PERL5LIB : /usr/lib/freesurfer/mni/share/perl5
* MSMBINDIR : /opt/msm/Ubuntu
* NO_FSFAST : 1
* OMP_NUM_THREADS : 1
* OS : Linux
* PATH : /usr/lib/freesurfer/bin:/usr/lib/freesurfer/fsfast/bin:/usr/lib/freesurfer/tktools:/usr/share/fsl/5.0/bin:/usr/lib/fsl/5.0:/usr/lib/freesurfer/mni/bin:/usr/lib/freesurfer/bin:/opt/ICA-AROMA:/usr/lib/ants:/opt/afni:/opt/afni:/opt/c3d/bin:/usr/bin/nvm/versions/node/v12.12.0/bin:/usr/local/miniconda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/msm/Ubuntu
* PERL5LIB : /usr/lib/freesurfer/mni/share/perl5
* POSSUMDIR : /usr/share/fsl/5.0
* PROMPT_COMMAND : PS1="Singularity> "; unset PROMPT_COMMAND
* PWD : /default/sub-123
* SHLVL : 1
* SINGULARITY_BIND : /cpac_patched/CPAC:/code/CPAC,/cpac_patched/dev/docker_data/run.py:/code/run.py,/cpac_patched/dev/docker_data:/cpac_resources,/ocean/projects/med220004p/shared/data_raw/CPAC-Regression/ADHD200/RawDataBIDS/KKI:/ocean/projects/med220004p/shared/data_raw/CPAC-Regression/ADHD200/RawDataBIDS/KKI:ro,/default/sub-123/output:/default/sub-123/output
* SINGULARITY_COMMAND : run
* SINGULARITY_CONTAINER : /images/nightly.sif
* SINGULARITY_ENVIRONMENT : /.singularity.d/env/91-environment.sh
* SINGULARITY_NAME : nightly.sif
* SUBJECTS_DIR : /usr/lib/freesurfer/subjects
* TZ : America/New_York
* _ : /code/run.py

"""


def test_workflow_from_scratch():
    document = read_report_rst_str(EXAMPLE_REPORT_RST)

    assert ReportSection.ENVIRONMENT in document
    assert ReportSection.EXECUTION_INFO in document
    assert ReportSection.ORIGINAL_INPUTS in document
    assert ReportSection.EXECUTION_INPUTS in document
    assert ReportSection.EXECUTION_OUTPUTS in document

    assert document[ReportSection.ENVIRONMENT]['OS'] == 'Linux'
