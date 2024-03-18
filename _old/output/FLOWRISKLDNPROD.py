
#System Imports
from datetime import datetime

# Base Airflow Imports
import airflow
from airflow import DAG

# Imports for Handling SSHOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.providers.google.cloud.hooks.compute_ssh import ComputeEngineSSHHook

# Imports for DummyOperator
from airflow.operators.dummy import DummyOperator


# Global Variabls
UNKNOWN = None

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="JOB_FLOWRISKLDNPROD",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
) as dag:

# DAG Tasks


    # ---- Task Metadata ---- JOB_LDN_CORP_RS_INTRADAY_PNL_1 ------
	#
	# Control-M Job Name: LDN-CORP-RS-Intraday-PnL-1 	-->	 Airflow Job Name: JOB_LDN_CORP_RS_INTRADAY_PNL_1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_RS_INTRADAY_PNL_1 = SSHOperator(
        task_id='JOB_LDN_CORP_RS_INTRADAY_PNL_1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -Dhost=rs-ldn-prod-corp-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/corp/intraday-pnl-dated date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_RS_INTRADAY_PNL_CPY_1 ------
	#
	# Control-M Job Name: LDN-CORP-RS-Intraday-PnL-Cpy-1 	-->	 Airflow Job Name: JOB_LDN_CORP_RS_INTRADAY_PNL_CPY_1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_RS_INTRADAY_PNL_CPY_1 = SSHOperator(
        task_id='JOB_LDN_CORP_RS_INTRADAY_PNL_CPY_1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 intraday_pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL ------
	#
	# Control-M Job Name: LDN-CORP-RS-DB_LUX-Intraday-PnL 	-->	 Airflow Job Name: JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL = SSHOperator(
        task_id='JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -Dhost=rs-ldn-prod-corp-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/corp/intraday-pnl.DB_LUX",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL_COPY ------
	#
	# Control-M Job Name: LDN-CORP-RS-DB_LUX-Intraday-PnL-Copy 	-->	 Airflow Job Name: JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL_COPY = SSHOperator(
        task_id='JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 intraday_pnl_dblux",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_RS_INTRADAY_PNL_1 ------
	#
	# Control-M Job Name: LDN-IDX-RS-Intraday-PnL-1 	-->	 Airflow Job Name: JOB_LDN_IDX_RS_INTRADAY_PNL_1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_RS_INTRADAY_PNL_1 = SSHOperator(
        task_id='JOB_LDN_IDX_RS_INTRADAY_PNL_1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/intraday-pnl-dated date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_RS_INTRADAY_PNL_CPY_1 ------
	#
	# Control-M Job Name: LDN-IDX-RS-Intraday-PnL-Cpy-1 	-->	 Airflow Job Name: JOB_LDN_IDX_RS_INTRADAY_PNL_CPY_1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_RS_INTRADAY_PNL_CPY_1 = SSHOperator(
        task_id='JOB_LDN_IDX_RS_INTRADAY_PNL_CPY_1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 intraday_pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_GET_FUTURE_PRICE ------
	#
	# Control-M Job Name: LDN-IDX-Get-Future-Price 	-->	 Airflow Job Name: JOB_LDN_IDX_GET_FUTURE_PRICE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_GET_FUTURE_PRICE = SSHOperator(
        task_id='JOB_LDN_IDX_GET_FUTURE_PRICE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/intraday-get-futures",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNODVSStartPROD1 	-->	 Airflow Job Name: JOB_LDNODVSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNODVSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRTCORPVSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTOPPROD1SUN ------
	#
	# Control-M Job Name: LDNRTCORPVSStopPROD1Sun 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTOPPROD1SUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTOPPROD1SUN = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTOPPROD1SUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNODVSStopPROD1 	-->	 Airflow Job Name: JOB_LDNODVSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNODVSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRTCORPVSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNODVSStartPROD1 	-->	 Airflow Job Name: JOB_LDNODVSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNODVSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNODVSStopPROD1 	-->	 Airflow Job Name: JOB_LDNODVSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNODVSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRTCORPVSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRTCORPVSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTTOTALRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRTTOTALRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRTTOTALRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTTOTALRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRTTOTALRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_TOTAL.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNOD3RSStartPROD1 	-->	 Airflow Job Name: JOB_LDNOD3RSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNOD3RSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNOD3RSStopPROD1 	-->	 Airflow Job Name: JOB_LDNOD3RSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNOD3RSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTTOTALRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRTTOTALRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRTTOTALRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTTOTALRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRTTOTALRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_TOTAL.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNOD1RSStopPROD1 	-->	 Airflow Job Name: JOB_LDNOD1RSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNOD1RSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD2RSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNOD2RSStopPROD1 	-->	 Airflow Job Name: JOB_LDNOD2RSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD2RSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNOD2RSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD2.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNOD1RSStartPROD1 	-->	 Airflow Job Name: JOB_LDNOD1RSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNOD1RSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNODVSStartPROD2 	-->	 Airflow Job Name: JOB_LDNODVSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNODVSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNODVSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNODVSStopPROD2 	-->	 Airflow Job Name: JOB_LDNODVSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNODVSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNODVSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNRTCORPVSStartPROD2 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTCORPVSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNRTCORPVSStopPROD2 	-->	 Airflow Job Name: JOB_LDNRTCORPVSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTCORPVSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNRTCORPVSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStopPROD2 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStartPROD2 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNOD3RSStartPROD2 	-->	 Airflow Job Name: JOB_LDNOD3RSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNOD3RSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStopPROD2 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNOD3RSStopPROD2 	-->	 Airflow Job Name: JOB_LDNOD3RSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNOD3RSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNOD1RSStopPROD2 	-->	 Airflow Job Name: JOB_LDNOD1RSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNOD1RSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD2RSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNOD2RSStopPROD2 	-->	 Airflow Job Name: JOB_LDNOD2RSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD2RSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNOD2RSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD2.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStartPROD2 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNOD1RSStartPROD2 	-->	 Airflow Job Name: JOB_LDNOD1RSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNOD1RSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD2RSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNOD2RSStartPROD2 	-->	 Airflow Job Name: JOB_LDNOD2RSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD2RSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNOD2RSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD2.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSPOTVOLPROD2 ------
	#
	# Control-M Job Name: LDNSPOTVOLPROD2 	-->	 Airflow Job Name: JOB_LDNSPOTVOLPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSPOTVOLPROD2 = SSHOperator(
        task_id='JOB_LDNSPOTVOLPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runAllReports.MRM.EOD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOSSRSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNEXOSSRSStopPROD2 	-->	 Airflow Job Name: JOB_LDNEXOSSRSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOSSRSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNEXOSSRSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_EXOTICS_SS.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOSSRSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNEXOSSRSStartPROD2 	-->	 Airflow Job Name: JOB_LDNEXOSSRSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOSSRSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNEXOSSRSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_EXOTICS_SS.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPSPOTSODPROD2 ------
	#
	# Control-M Job Name: LDNCORPSPOTSODPROD2 	-->	 Airflow Job Name: JOB_LDNCORPSPOTSODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPSPOTSODPROD2 = SSHOperator(
        task_id='JOB_LDNCORPSPOTSODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.spot.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPDBRSSPOTEODPROD2 ------
	#
	# Control-M Job Name: LDNCORPDBRSSPOTEODPROD2 	-->	 Airflow Job Name: JOB_LDNCORPDBRSSPOTEODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPDBRSSPOTEODPROD2 = SSHOperator(
        task_id='JOB_LDNCORPDBRSSPOTEODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/dbriskstore.scenarios.report.spot.corp",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPSPOTPIVTWSODDAILYPROD2 ------
	#
	# Control-M Job Name: LDNCORPSPOTPIVTWSODDAILYPROD2 	-->	 Airflow Job Name: JOB_LDNCORPSPOTPIVTWSODDAILYPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPSPOTPIVTWSODDAILYPROD2 = SSHOperator(
        task_id='JOB_LDNCORPSPOTPIVTWSODDAILYPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD2 ------
	#
	# Control-M Job Name: LDNCORPDBRSSPOTPIVTWEODDAILYPROD2 	-->	 Airflow Job Name: JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD2 = SSHOperator(
        task_id='JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.corp",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPSPOTPIVTWSODPROD2 ------
	#
	# Control-M Job Name: LDNCORPSPOTPIVTWSODPROD2 	-->	 Airflow Job Name: JOB_LDNCORPSPOTPIVTWSODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPSPOTPIVTWSODPROD2 = SSHOperator(
        task_id='JOB_LDNCORPSPOTPIVTWSODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.MRM.spot-piv-tw.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPDBRSSPOTPIVTWEODPROD2 ------
	#
	# Control-M Job Name: LDNCORPDBRSSPOTPIVTWEODPROD2 	-->	 Airflow Job Name: JOB_LDNCORPDBRSSPOTPIVTWEODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPDBRSSPOTPIVTWEODPROD2 = SSHOperator(
        task_id='JOB_LDNCORPDBRSSPOTPIVTWEODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/dbriskstore.scenarios.report.spot-pivtw.corp",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTSODPROD2 ------
	#
	# Control-M Job Name: LDNIDXSPOTSODPROD2 	-->	 Airflow Job Name: JOB_LDNIDXSPOTSODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTSODPROD2 = SSHOperator(
        task_id='JOB_LDNIDXSPOTSODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.spot.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXDBRSSPOTEODPROD2 ------
	#
	# Control-M Job Name: LDNIDXDBRSSPOTEODPROD2 	-->	 Airflow Job Name: JOB_LDNIDXDBRSSPOTEODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXDBRSSPOTEODPROD2 = SSHOperator(
        task_id='JOB_LDNIDXDBRSSPOTEODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/dbriskstore.scenarios.report.spot.idx",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTPIVTWSODDAILYPROD2 ------
	#
	# Control-M Job Name: LDNIDXSPOTPIVTWSODDAILYPROD2 	-->	 Airflow Job Name: JOB_LDNIDXSPOTPIVTWSODDAILYPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTPIVTWSODDAILYPROD2 = SSHOperator(
        task_id='JOB_LDNIDXSPOTPIVTWSODDAILYPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD2 ------
	#
	# Control-M Job Name: LDNIDXDBRSSPOTPIVTWEODDAILYPROD2 	-->	 Airflow Job Name: JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD2 = SSHOperator(
        task_id='JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.idx",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTPIVTWSODPROD2 ------
	#
	# Control-M Job Name: LDNIDXSPOTPIVTWSODPROD2 	-->	 Airflow Job Name: JOB_LDNIDXSPOTPIVTWSODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTPIVTWSODPROD2 = SSHOperator(
        task_id='JOB_LDNIDXSPOTPIVTWSODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.MRM.spot-piv-tw.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXDBRSSPOTPIVTWEODPROD2 ------
	#
	# Control-M Job Name: LDNIDXDBRSSPOTPIVTWEODPROD2 	-->	 Airflow Job Name: JOB_LDNIDXDBRSSPOTPIVTWEODPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXDBRSSPOTPIVTWEODPROD2 = SSHOperator(
        task_id='JOB_LDNIDXDBRSSPOTPIVTWEODPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/dbriskstore.scenarios.report.spot-pivtw.idx",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_STOP_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-VS-stop-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_STOP_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_STOP_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_STOP_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_EOD.sh ldn.eod.od.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_START_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-VS-Start-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_START_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_START_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_START_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_EOD.sh ldn.eod.od.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_STOP_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-VS-stop-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_STOP_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_STOP_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_STOP_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_EOD.sh ldn.eod.od.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_START_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-VS-Start-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_START_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_START_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_START_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_EOD.sh ldn.eod.od.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNINTRAPKSRECON ------
	#
	# Control-M Job Name: LDNIntraPKSRecon 	-->	 Airflow Job Name: JOB_LDNINTRAPKSRECON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNINTRAPKSRECON = SSHOperator(
        task_id='JOB_LDNINTRAPKSRECON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/intrapks-recon_wrapper.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_DBPFILES_CHECK ------
	#
	# Control-M Job Name: LDN-EOD-DBPFiles-Check 	-->	 Airflow Job Name: JOB_LDN_EOD_DBPFILES_CHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_DBPFILES_CHECK = SSHOperator(
        task_id='JOB_LDN_EOD_DBPFILES_CHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/check_dbPalace_files.sh ldn.eod.idx.prod1 `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_SA_EOD_DBPFILES_CHECK ------
	#
	# Control-M Job Name: SA-EOD-DBPFiles-Check 	-->	 Airflow Job Name: JOB_SA_EOD_DBPFILES_CHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_SA_EOD_DBPFILES_CHECK = SSHOperator(
        task_id='JOB_SA_EOD_DBPFILES_CHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/check_dbPalace_files.sh sa.cars1 `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_NEXUS_JMS ------
	#
	# Control-M Job Name: LDN-EOD-Nexus-JMS 	-->	 Airflow Job Name: JOB_LDN_EOD_NEXUS_JMS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_NEXUS_JMS = SSHOperator(
        task_id='JOB_LDN_EOD_NEXUS_JMS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/dbnexus/get-migrated-books_to-file_PROD.sh LONDON",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_NEXUS_MQ_DE ------
	#
	# Control-M Job Name: LDN-EOD-Nexus-MQ-DE 	-->	 Airflow Job Name: JOB_LDN_EOD_NEXUS_MQ_DE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_NEXUS_MQ_DE = SSHOperator(
        task_id='JOB_LDN_EOD_NEXUS_MQ_DE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.corp.prod com.db.ged.report.service.dbnexus.DbNexusPull -Dlog4j.logFileName=dbNexus",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_NEXUS_MQ_UK ------
	#
	# Control-M Job Name: LDN-EOD-Nexus-MQ-UK 	-->	 Airflow Job Name: JOB_LDN_EOD_NEXUS_MQ_UK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_NEXUS_MQ_UK = SSHOperator(
        task_id='JOB_LDN_EOD_NEXUS_MQ_UK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.service.dbnexus.DbNexusPull -Dlog4j.logFileName=dbNexus",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PERSIST_DBAX ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Persist-Dbax 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PERSIST_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PERSIST_DBAX = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PERSIST_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-position-and-dbax-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-CORP-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_CORP_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_COPY_DBAX = SSHOperator(
        task_id='JOB_LDN_CORP_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-latest-position-and-dbax-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNT0POSSIGNOFF ------
	#
	# Control-M Job Name: LDNt0possignoff 	-->	 Airflow Job Name: JOB_LDNT0POSSIGNOFF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNT0POSSIGNOFF = SSHOperator(
        task_id='JOB_LDNT0POSSIGNOFF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/pks-aso-wrapper.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LNIDXRISKPNLPILOT ------
	#
	# Control-M Job Name: LNIDXriskpnlPilot 	-->	 Airflow Job Name: JOB_LNIDXRISKPNLPILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LNIDXRISKPNLPILOT = SSHOperator(
        task_id='JOB_LNIDXRISKPNLPILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-risk-pnl-pilot-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXPOPULATEGRIMISEODCACHE ------
	#
	# Control-M Job Name: ldnIDXpopulategrimiseodcache 	-->	 Airflow Job Name: JOB_LDNIDXPOPULATEGRIMISEODCACHE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXPOPULATEGRIMISEODCACHE = SSHOperator(
        task_id='JOB_LDNIDXPOPULATEGRIMISEODCACHE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/populate-grimis-eod-cache date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PNL_LATEST ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Pnl-Latest 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PNL_LATEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PNL_LATEST = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PNL_LATEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-pnl-dated date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FR_EOD_T0_POS_SIGNOFF_CHECK ------
	#
	# Control-M Job Name: FR-EOD-T0-Pos-Signoff-Check 	-->	 Airflow Job Name: JOB_FR_EOD_T0_POS_SIGNOFF_CHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FR_EOD_T0_POS_SIGNOFF_CHECK = SSHOperator(
        task_id='JOB_FR_EOD_T0_POS_SIGNOFF_CHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/check-tso-labels.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_RAG_STATUS_REPORT ------
	#
	# Control-M Job Name: LDN-EOD-RAG-Status-Report 	-->	 Airflow Job Name: JOB_LDN_EOD_RAG_STATUS_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_RAG_STATUS_REPORT = SSHOperator(
        task_id='JOB_LDN_EOD_RAG_STATUS_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_RAG_DIR/status_eod_report.pl %%FR_RAG_DIR/EMEA %%FRDATE 15:00 'EMEA' | mutt -e 'set content_type=text/html' -s 'EMEA FlowRisk EOD Batch Status %%FRDATE' %%EMAIL_LIST",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_COPY_FRPYPLFEB ------
	#
	# Control-M Job Name: LDN-EOD-YE-Copy-FRPYPLFeb 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_COPY_FRPYPLFEB
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_COPY_FRPYPLFEB = SSHOperator(
        task_id='JOB_LDN_EOD_YE_COPY_FRPYPLFEB',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.ss.prod1 fr-pypl-adj",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_BS_DUMMY ------
	#
	# Control-M Job Name: LDN-EOD-YE-BS-DUMMY 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_BS_DUMMY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_BS_DUMMY = DummyOperator(
        task_id='JOB_LDN_EOD_YE_BS_DUMMY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPPOPULATEGRIMISEODCACHE ------
	#
	# Control-M Job Name: LDNCORPpopulategrimiseodcache 	-->	 Airflow Job Name: JOB_LDNCORPPOPULATEGRIMISEODCACHE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPPOPULATEGRIMISEODCACHE = SSHOperator(
        task_id='JOB_LDNCORPPOPULATEGRIMISEODCACHE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/populate-grimis-eod-cache date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PNL_LATEST ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Pnl-Latest 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PNL_LATEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PNL_LATEST = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PNL_LATEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-pnl-dated date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPCOPYRPICOMREPORT ------
	#
	# Control-M Job Name: LDNCORPCopyRPIComReport 	-->	 Airflow Job Name: JOB_LDNCORPCOPYRPICOMREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPCOPYRPICOMREPORT = SSHOperator(
        task_id='JOB_LDNCORPCOPYRPICOMREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 t0_latest_risk_pnl_ipv_combined_dated",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPRPICOMREPORT ------
	#
	# Control-M Job Name: LDNCORPRPIComReport 	-->	 Airflow Job Name: JOB_LDNCORPRPICOMREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPRPICOMREPORT = SSHOperator(
        task_id='JOB_LDNCORPRPICOMREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-risk-pnl-ipv-combined-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-CORP-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-rate-fixing-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPGRIMISATT ------
	#
	# Control-M Job Name: LDNCORPGrimisAtt 	-->	 Airflow Job Name: JOB_LDNCORPGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPGRIMISATT = SSHOperator(
        task_id='JOB_LDNCORPGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-grimis-persist-att-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_COPY_TOD_OLD ------
	#
	# Control-M Job Name: LDN-CORP-Copy-ToD-Old 	-->	 Airflow Job Name: JOB_LDN_CORP_COPY_TOD_OLD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_COPY_TOD_OLD = SSHOperator(
        task_id='JOB_LDN_CORP_COPY_TOD_OLD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 t0_latest_tradesOnDay_multiday",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_TOD ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Tod 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_TOD = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-tradesOnDay-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_COPY_TOD ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Copy-TOD 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_COPY_TOD = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-latest-tradesOnDay-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_STATICDATA ------
	#
	# Control-M Job Name: LDN-EOD-StaticData 	-->	 Airflow Job Name: JOB_LDN_EOD_STATICDATA
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_STATICDATA = SSHOperator(
        task_id='JOB_LDN_EOD_STATICDATA',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/t0-static-data date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_KANNON_STATIC ------
	#
	# Control-M Job Name: LDN-EOD-Kannon-Static 	-->	 Airflow Job Name: JOB_LDN_EOD_KANNON_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_KANNON_STATIC = SSHOperator(
        task_id='JOB_LDN_EOD_KANNON_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/t0-static-data-kannon 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_COPY_ALL_REPORTS ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Copy-All-reports 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_COPY_ALL_REPORTS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_COPY_ALL_REPORTS = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_COPY_ALL_REPORTS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_all_LDN_report.sh IDX `%%FR_SCRIPT_DIR/Tzero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXMIS3NOTIFICATIONRISK ------
	#
	# Control-M Job Name: LDNIDXMis3NotificationRisk 	-->	 Airflow Job Name: JOB_LDNIDXMIS3NOTIFICATIONRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXMIS3NOTIFICATIONRISK = SSHOperator(
        task_id='JOB_LDNIDXMIS3NOTIFICATIONRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod mis3-notification portfolio=LD.IDX_MGMT date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPMIS3NOTIFICATIONATT ------
	#
	# Control-M Job Name: LDNCORPMis3NotificationAtt 	-->	 Airflow Job Name: JOB_LDNCORPMIS3NOTIFICATIONATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPMIS3NOTIFICATIONATT = SSHOperator(
        task_id='JOB_LDNCORPMIS3NOTIFICATIONATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod mis3-notification portfolio=LD.CORP date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_MODELNFO_DQEMAIL ------
	#
	# Control-M Job Name: LDN-EOD-Modelnfo-DQEmail 	-->	 Airflow Job Name: JOB_LDN_EOD_MODELNFO_DQEMAIL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_MODELNFO_DQEMAIL = SSHOperator(
        task_id='JOB_LDN_EOD_MODELNFO_DQEMAIL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/sendModelInfoLDN.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXEODMODELINFO ------
	#
	# Control-M Job Name: LDNIDXEODModelInfo 	-->	 Airflow Job Name: JOB_LDNIDXEODMODELINFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXEODMODELINFO = SSHOperator(
        task_id='JOB_LDNIDXEODMODELINFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/modelinfo-combined mode=anyrule date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPEODMODELINFO ------
	#
	# Control-M Job Name: LDNCORPEODModelInfo 	-->	 Airflow Job Name: JOB_LDNCORPEODMODELINFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPEODMODELINFO = SSHOperator(
        task_id='JOB_LDNCORPEODMODELINFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/modelinfo-combined mode=anyrule date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_BOOK_TABLE_UPDATE ------
	#
	# Control-M Job Name: LDN-EOD-Book-Table-Update 	-->	 Airflow Job Name: JOB_LDN_EOD_BOOK_TABLE_UPDATE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_BOOK_TABLE_UPDATE = SSHOperator(
        task_id='JOB_LDN_EOD_BOOK_TABLE_UPDATE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/grimis-book-update",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_GPF_BOOK_TABLE_UPDATE ------
	#
	# Control-M Job Name: LDN-GPF-Book-Table-Update 	-->	 Airflow Job Name: JOB_LDN_GPF_BOOK_TABLE_UPDATE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_GPF_BOOK_TABLE_UPDATE = SSHOperator(
        task_id='JOB_LDN_GPF_BOOK_TABLE_UPDATE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.gpf.eod.ait.prod ldn/gpf/grimis-book-update",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXMIS3NOTIFICATIONATT ------
	#
	# Control-M Job Name: LDNIDXMis3NotificationAtt 	-->	 Airflow Job Name: JOB_LDNIDXMIS3NOTIFICATIONATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXMIS3NOTIFICATIONATT = SSHOperator(
        task_id='JOB_LDNIDXMIS3NOTIFICATIONATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod mis3-notification portfolio=LD.IDX_MGMT date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXCOPYRPICOMREPORT ------
	#
	# Control-M Job Name: LDNIDXCopyRPIComReport 	-->	 Airflow Job Name: JOB_LDNIDXCOPYRPICOMREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXCOPYRPICOMREPORT = SSHOperator(
        task_id='JOB_LDNIDXCOPYRPICOMREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 t0_latest_risk_pnl_ipv_combined_dated",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXGRIMISATT ------
	#
	# Control-M Job Name: LDNIDXGrimisAtt 	-->	 Airflow Job Name: JOB_LDNIDXGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXGRIMISATT = SSHOperator(
        task_id='JOB_LDNIDXGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-grimis-persist-att-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXEODTRADESONDAYREPORT ------
	#
	# Control-M Job Name: LDNIDXEODtradesOnDayReport 	-->	 Airflow Job Name: JOB_LDNIDXEODTRADESONDAYREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXEODTRADESONDAYREPORT = SSHOperator(
        task_id='JOB_LDNIDXEODTRADESONDAYREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-tradesOnDay-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXEODCOPYTRADESONDAYREPORT ------
	#
	# Control-M Job Name: LDNIDXEODCopytradesOnDayReport 	-->	 Airflow Job Name: JOB_LDNIDXEODCOPYTRADESONDAYREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXEODCOPYTRADESONDAYREPORT = SSHOperator(
        task_id='JOB_LDNIDXEODCOPYTRADESONDAYREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 t0_latest_tradesOnDay_multiday",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_COPY_ALL_REPORTS ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Copy-All-reports 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_COPY_ALL_REPORTS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_COPY_ALL_REPORTS = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_COPY_ALL_REPORTS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_all_LDN_report.sh CORP `%%FR_SCRIPT_DIR/Tzero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PERSIST_DBAX ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Persist-Dbax 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PERSIST_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PERSIST_DBAX = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PERSIST_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-position-and-dbax-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXMIS3NOTIFICATIONPNL ------
	#
	# Control-M Job Name: LDNIDXMis3NotificationPnl 	-->	 Airflow Job Name: JOB_LDNIDXMIS3NOTIFICATIONPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXMIS3NOTIFICATIONPNL = SSHOperator(
        task_id='JOB_LDNIDXMIS3NOTIFICATIONPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod mis3-notification portfolio=LD.IDX_MGMT date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_DBP_REPORT ------
	#
	# Control-M Job Name: LDN-EOD-DBP-Report 	-->	 Airflow Job Name: JOB_LDN_EOD_DBP_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_DBP_REPORT = SSHOperator(
        task_id='JOB_LDN_EOD_DBP_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report_dbPalace.sh ldn.eod.idx.prod `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_SA_EOD_DBP_REPORT ------
	#
	# Control-M Job Name: SA-EOD-DBP-Report 	-->	 Airflow Job Name: JOB_SA_EOD_DBP_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_SA_EOD_DBP_REPORT = SSHOperator(
        task_id='JOB_SA_EOD_DBP_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report_dbPalace.sh sa.cars `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_BS ------
	#
	# Control-M Job Name: LDN-EOD-YE-BS 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_BS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_BS = SSHOperator(
        task_id='JOB_LDN_EOD_YE_BS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/t0-latest-ye-balancesheet date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_BS2 ------
	#
	# Control-M Job Name: LDN-EOD-YE-BS.2 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_BS2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_BS2 = SSHOperator(
        task_id='JOB_LDN_EOD_YE_BS2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/t0-latest-ye-balancesheet.2 date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_BS_GPF ------
	#
	# Control-M Job Name: LDN-EOD-YE-BS-GPF 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_BS_GPF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_BS_GPF = SSHOperator(
        task_id='JOB_LDN_EOD_YE_BS_GPF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.gpf.eod.other.prod ldn/gpf/ye-balancesheet date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_COPY_FRPYPLJAN ------
	#
	# Control-M Job Name: LDN-EOD-YE-Copy-FRPYPLJan 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_COPY_FRPYPLJAN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_COPY_FRPYPLJAN = SSHOperator(
        task_id='JOB_LDN_EOD_YE_COPY_FRPYPLJAN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.ss.prod1 fr-pypl-adj",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_LDN_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 persist-dbax-dictionaries `%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEODT0TMXSIGNOFF ------
	#
	# Control-M Job Name: LdnEodT0TmxSignoff 	-->	 Airflow Job Name: JOB_LDNEODT0TMXSIGNOFF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEODT0TMXSIGNOFF = SSHOperator(
        task_id='JOB_LDNEODT0TMXSIGNOFF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/t0-position-sign-off-dated date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXRPICOMREPORT ------
	#
	# Control-M Job Name: LDNIDXRPIComReport 	-->	 Airflow Job Name: JOB_LDNIDXRPICOMREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXRPICOMREPORT = SSHOperator(
        task_id='JOB_LDNIDXRPICOMREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-latest-risk-pnl-ipv-combined-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-IDX-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="sleep 180;%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-rate-fixing-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LNCORPRISKPNLPILOT ------
	#
	# Control-M Job Name: LNCORPRiskpnlPilot 	-->	 Airflow Job Name: JOB_LNCORPRISKPNLPILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LNCORPRISKPNLPILOT = SSHOperator(
        task_id='JOB_LNCORPRISKPNLPILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-latest-risk-pnl-pilot-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LNCORPRISKPNLPILOTRECON ------
	#
	# Control-M Job Name: LNCORPRiskpnlPilotRecon 	-->	 Airflow Job Name: JOB_LNCORPRISKPNLPILOTRECON
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LNCORPRISKPNLPILOTRECON = DummyOperator(
        task_id='JOB_LNCORPRISKPNLPILOTRECON',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LNIDXRISKPNLPILOTRECON ------
	#
	# Control-M Job Name: LNIDXriskpnlPilotRecon 	-->	 Airflow Job Name: JOB_LNIDXRISKPNLPILOTRECON
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LNIDXRISKPNLPILOTRECON = DummyOperator(
        task_id='JOB_LNIDXRISKPNLPILOTRECON',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LNIDXRISKPNLPILOTCOPY ------
	#
	# Control-M Job Name: LNIDXriskpnlPilotCopy 	-->	 Airflow Job Name: JOB_LNIDXRISKPNLPILOTCOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LNIDXRISKPNLPILOTCOPY = SSHOperator(
        task_id='JOB_LNIDXRISKPNLPILOTCOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 t0-latest-risk-pnl-pilot-dated",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPRISKPNLPILOTCOPY ------
	#
	# Control-M Job Name: LDNCORPriskpnlPilotCopy 	-->	 Airflow Job Name: JOB_LDNCORPRISKPNLPILOTCOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPRISKPNLPILOTCOPY = SSHOperator(
        task_id='JOB_LDNCORPRISKPNLPILOTCOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 t0-latest-risk-pnl-pilot-dated",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_PRICE_CAPTURE_CHECK_EMEA ------
	#
	# Control-M Job Name: Price_Capture_Check_EMEA 	-->	 Airflow Job Name: JOB_PRICE_CAPTURE_CHECK_EMEA
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_PRICE_CAPTURE_CHECK_EMEA = SSHOperator(
        task_id='JOB_PRICE_CAPTURE_CHECK_EMEA',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/geneos/toolkits/capacity/run-flowrisk-ticker-report.sh -d %%$ODATE -r EMEA",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_RISK_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Risk-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_RISK_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_RISK_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_RISK_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 ipv_modelswitch",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_RISK_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Risk-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_RISK_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_RISK_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_RISK_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 ipv_modelswitch",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPMIS3NOTIFICATIONRISK ------
	#
	# Control-M Job Name: LDNCORPMis3NotificationRisk 	-->	 Airflow Job Name: JOB_LDNCORPMIS3NOTIFICATIONRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPMIS3NOTIFICATIONRISK = SSHOperator(
        task_id='JOB_LDNCORPMIS3NOTIFICATIONRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod mis3-notification portfolio=LD.CORP date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPMIS3NOTIFICATIONPNL ------
	#
	# Control-M Job Name: LDNCORPMis3NotificationPnl 	-->	 Airflow Job Name: JOB_LDNCORPMIS3NOTIFICATIONPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPMIS3NOTIFICATIONPNL = SSHOperator(
        task_id='JOB_LDNCORPMIS3NOTIFICATIONPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod mis3-notification portfolio=LD.CORP date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE` jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PERSIST_RISK ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Persist-Risk 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PERSIST_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PERSIST_RISK = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PERSIST_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/jar-to-grimis-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PERSIST_ATT ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Persist-Att 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PERSIST_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PERSIST_ATT = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PERSIST_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/jar-to-grimis-att date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PERSIST_SOD ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Persist-Sod 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PERSIST_SOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PERSIST_SOD = DummyOperator(
        task_id='JOB_LDN_CORP_EOD_PERSIST_SOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PERSIST_RISK ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Persist-Risk 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PERSIST_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PERSIST_RISK = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PERSIST_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/jar-to-grimis-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PERSIST_ATT ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Persist-Att 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PERSIST_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PERSIST_ATT = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PERSIST_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/jar-to-grimis-att date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PERSIST_SOD ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Persist-Sod 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PERSIST_SOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PERSIST_SOD = DummyOperator(
        task_id='JOB_LDN_IDX_EOD_PERSIST_SOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPCOPYSOD ------
	#
	# Control-M Job Name: LDNCORPCopySod 	-->	 Airflow Job Name: JOB_LDNCORPCOPYSOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPCOPYSOD = SSHOperator(
        task_id='JOB_LDNCORPCOPYSOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.corp.prod1 t0_sod",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXCOPYSOD ------
	#
	# Control-M Job Name: LDNIDXCopySod 	-->	 Airflow Job Name: JOB_LDNIDXCOPYSOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXCOPYSOD = SSHOperator(
        task_id='JOB_LDNIDXCOPYSOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.idx.prod1 t0_sod",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_EUSFILES_CHECK ------
	#
	# Control-M Job Name: LDN-EOD-EUSFiles-Check 	-->	 Airflow Job Name: JOB_LDN_EOD_EUSFILES_CHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_EUSFILES_CHECK = SSHOperator(
        task_id='JOB_LDN_EOD_EUSFILES_CHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/check_EUS_files.sh ldn.eod.ss.prod1 `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_EUS_REPORT ------
	#
	# Control-M Job Name: LDN-EOD-EUS-Report 	-->	 Airflow Job Name: JOB_LDN_EOD_EUS_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_EUS_REPORT = SSHOperator(
        task_id='JOB_LDN_EOD_EUS_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report_EUS.sh ldn.eod.ss.prod1 `%%FR_SCRIPT_DIR/Tminus1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_GRIMIS_ADDUP ------
	#
	# Control-M Job Name: LDN-EOD-Grimis-Addup 	-->	 Airflow Job Name: JOB_LDN_EOD_GRIMIS_ADDUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_GRIMIS_ADDUP = SSHOperator(
        task_id='JOB_LDN_EOD_GRIMIS_ADDUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/grimis-persist-ldn-daily-add-up date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_EUS_YEBS_DUMMY ------
	#
	# Control-M Job Name: LDN-EOD-EUS-YEBS-DUMMY 	-->	 Airflow Job Name: JOB_LDN_EOD_EUS_YEBS_DUMMY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_EUS_YEBS_DUMMY = DummyOperator(
        task_id='JOB_LDN_EOD_EUS_YEBS_DUMMY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_ADDUP ------
	#
	# Control-M Job Name: LDN-EOD-YE-Addup 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_ADDUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_ADDUP = SSHOperator(
        task_id='JOB_LDN_EOD_YE_ADDUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/ye-add-up date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_EUS_YE_BS ------
	#
	# Control-M Job Name: LDN-EOD-EUS-YE-BS 	-->	 Airflow Job Name: JOB_LDN_EOD_EUS_YE_BS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_EUS_YE_BS = SSHOperator(
        task_id='JOB_LDN_EOD_EUS_YE_BS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/ye-eus-balancesheet date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_EUS_YE_BS2 ------
	#
	# Control-M Job Name: LDN-EOD-EUS-YE-BS.2 	-->	 Airflow Job Name: JOB_LDN_EOD_EUS_YE_BS2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_EUS_YE_BS2 = SSHOperator(
        task_id='JOB_LDN_EOD_EUS_YE_BS2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/ye-eus-balancesheet.2 date=%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_BSMERGE ------
	#
	# Control-M Job Name: LDN-EOD-YE-BS.MERGE 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_BSMERGE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_BSMERGE = SSHOperator(
        task_id='JOB_LDN_EOD_YE_BSMERGE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/merge_csv.sh ldn.eod.idx.prod1 %%$ODATE/fr_pypl_adj_LDN_%%FRDATE fr_pypl_adj_LDN1_%%FRDATE fr_pypl_adj_LDN2_%%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_KICKOFF ------
	#
	# Control-M Job Name: LDN-EOD-KICKOFF 	-->	 Airflow Job Name: JOB_LDN_EOD_KICKOFF
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_KICKOFF = DummyOperator(
        task_id='JOB_LDN_EOD_KICKOFF',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_YE_COPY_FRPYPL ------
	#
	# Control-M Job Name: LDN-EOD-YE-Copy-FRPYPL 	-->	 Airflow Job Name: JOB_LDN_EOD_YE_COPY_FRPYPL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_YE_COPY_FRPYPL = SSHOperator(
        task_id='JOB_LDN_EOD_YE_COPY_FRPYPL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.ss.prod1 fr-pypl-adj",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PERSIST_YE ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Persist-YE 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PERSIST_YE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PERSIST_YE = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PERSIST_YE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/jar-to-grimis-ye date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PERSIST_YE ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Persist-YE 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PERSIST_YE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PERSIST_YE = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PERSIST_YE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/jar-to-grimis-ye date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXMCCREPORT ------
	#
	# Control-M Job Name: LDNIDXMccReport 	-->	 Airflow Job Name: JOB_LDNIDXMCCREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXMCCREPORT = SSHOperator(
        task_id='JOB_LDNIDXMCCREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-mcc date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXCOPYMCCREPORT ------
	#
	# Control-M Job Name: LDNIDXCopyMccReport 	-->	 Airflow Job Name: JOB_LDNIDXCOPYMCCREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXCOPYMCCREPORT = SSHOperator(
        task_id='JOB_LDNIDXCOPYMCCREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod -copy ldn/idx/t0-mcc date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPMCCREPORT ------
	#
	# Control-M Job Name: LDNCORPMccReport 	-->	 Airflow Job Name: JOB_LDNCORPMCCREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPMCCREPORT = SSHOperator(
        task_id='JOB_LDNCORPMCCREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-mcc date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPCOPYMCCREPORT ------
	#
	# Control-M Job Name: LDNCORPCopyMccReport 	-->	 Airflow Job Name: JOB_LDNCORPCOPYMCCREPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPCOPYMCCREPORT = SSHOperator(
        task_id='JOB_LDNCORPCOPYMCCREPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-mcc date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_ECM_MCC ------
	#
	# Control-M Job Name: LDN-ECM-MCC 	-->	 Airflow Job Name: JOB_LDN_ECM_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_ECM_MCC = SSHOperator(
        task_id='JOB_LDN_ECM_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-mcc-ecm date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_ECM_COPY_MCC ------
	#
	# Control-M Job Name: LDN-ECM-Copy-MCC 	-->	 Airflow Job Name: JOB_LDN_ECM_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_ECM_COPY_MCC = SSHOperator(
        task_id='JOB_LDN_ECM_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-mcc-ecm date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_FLOW_EOD_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-IDX-FLOW-EOD-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_IDX_FLOW_EOD_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_FLOW_EOD_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_IDX_FLOW_EOD_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'index' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_FLOW_EOD_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-CORP-FLOW-EOD-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_CORP_FLOW_EOD_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_FLOW_EOD_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_CORP_FLOW_EOD_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'corporates' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_COPY_XCCY_ADJ_REPORT ------
	#
	# Control-M Job Name: LDN-CORP-EOD-Copy-Xccy-Adj-Report 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_COPY_XCCY_ADJ_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_COPY_XCCY_ADJ_REPORT = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_COPY_XCCY_ADJ_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-latest-risk-pnl-ipv-combined-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_COPY_XCCY_ADJ_REPORT ------
	#
	# Control-M Job Name: LDN-IDX-EOD-Copy-Xccy-Adj-Report 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_COPY_XCCY_ADJ_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_COPY_XCCY_ADJ_REPORT = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_COPY_XCCY_ADJ_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod -copy ldn/idx/t0-latest-risk-pnl-ipv-combined-dated date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE` date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-CORP-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/pvmanifest date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-IDX-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/pvmanifest date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_STOP_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Stop-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_STOP_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_STOP_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_STOP_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_START_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Start-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_START_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_START_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_START_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_OD_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-OD-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_OD_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_OD_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_OD_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.od.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.od.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_STOP_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Stop-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_STOP_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_STOP_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_STOP_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_START_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Start-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_START_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_START_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_START_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_START_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Start-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_START_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_START_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_START_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_STOP_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Stop-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_STOP_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_STOP_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_STOP_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_RESTART_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-ReStart-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_RESTART_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_RESTART_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_RESTART_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod1;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_STOP_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Stop-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_STOP_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_STOP_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_STOP_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_RESTART_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-ReStart-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_RESTART_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_RESTART_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_RESTART_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod1;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_RESTART_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-ReStart-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_RESTART_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_RESTART_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_RESTART_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod1;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_OD_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-OD-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_OD_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_OD_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_OD_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.od.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.od.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_SS_RS_RESTART_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-SS-RS-ReStart-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_SS_RS_RESTART_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_SS_RS_RESTART_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_SS_RS_RESTART_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.ss.prod2;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.ss.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_RESTART_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-ReStart-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_RESTART_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_RESTART_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_RESTART_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod1;sleep 120;%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_START_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Start-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_START_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_START_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_START_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_PILOT_VC_SYNC ------
	#
	# Control-M Job Name: LDN-PILOT-VC-SYNC 	-->	 Airflow Job Name: JOB_LDN_PILOT_VC_SYNC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_PILOT_VC_SYNC = SSHOperator(
        task_id='JOB_LDN_PILOT_VC_SYNC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SSH_LDN_PROD1 %%FR_SCRIPT_DIR/synchPilot.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_START_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Start-PROD1-Pilot 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_START_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_START_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_START_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_PILOT_CONFIRM ------
	#
	# Control-M Job Name: LDN-PILOT-Confirm 	-->	 Airflow Job Name: JOB_LDN_PILOT_CONFIRM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_PILOT_CONFIRM = SSHOperator(
        task_id='JOB_LDN_PILOT_CONFIRM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="sleep 5;",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_STOP_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-VS-stop-PROD1-PILOT 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_STOP_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_STOP_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_VS_STOP_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_EOD.sh ldn.eod.od.prod1;sleep 30",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-DBA-Upgrade-PROD1-PILOT 	-->	 Airflow Job Name: JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%LNFLOWVS 'source ~/.bashrc && ./install.sh -v  $(readlink $VSDIR/current | cut -d- -f 3) -s $(readlink $VSDIR/current | cut -d- -f 6) -e $(readlink $VSDIR/current | cut -d- -f 7) -r $(readlink $VSDIR/current | cut -d- -f 8) -f updatePilotDba'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_START_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-VS-Start-PROD1-PILOT 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_START_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_START_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_VS_START_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="sleep 120;%%FR_SCRIPT_DIR/start_VS_EOD.sh ldn.eod.od.prod1;sleep 60",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_VS_STOP_PROD_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-VS-Stop-PROD-PILOT 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_VS_STOP_PROD_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_VS_STOP_PROD_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_VS_STOP_PROD_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_LDN_EXO_EOD_PROD.sh;sleep 30",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-DBA-Upgrade-PROD1-PILOT 	-->	 Airflow Job Name: JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%LNEXOVS 'source ~/.bashrc && ./install.sh -v  $(readlink $VSDIR/current | cut -d- -f 3) -s $(readlink $VSDIR/current | cut -d- -f 6) -e $(readlink $VSDIR/current | cut -d- -f 7) -r $(readlink $VSDIR/current | cut -d- -f 8) -f updatePilotDba'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_VS_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-VS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_VS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_VS_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_VS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="sleep 120;%%FR_SCRIPT_DIR/start_VS_LDN_EXO_EOD_PROD.sh;sleep 60",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_STOP_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Stop-PROD1-Pilot 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_STOP_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_STOP_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_STOP_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IDX_RS_STOP_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-IDX-RS-Stop-PROD1-Pilot 	-->	 Airflow Job Name: JOB_LDN_EOD_IDX_RS_STOP_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IDX_RS_STOP_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_IDX_RS_STOP_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.idx.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_CORP_RS_START_PROD1_PILOT ------
	#
	# Control-M Job Name: LDN-EOD-CORP-RS-Start-PROD1-Pilot 	-->	 Airflow Job Name: JOB_LDN_EOD_CORP_RS_START_PROD1_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_CORP_RS_START_PROD1_PILOT = SSHOperator(
        task_id='JOB_LDN_EOD_CORP_RS_START_PROD1_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_EOD.sh ldn.eod.corp.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_STOP_PROD_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Stop-PROD-Pilot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_STOP_PROD_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_STOP_PROD_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_STOP_PROD_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_IDX_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_START_PROD_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Start-PROD-Pilot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_START_PROD_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_START_PROD_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_START_PROD_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_PILOT_DBA_UPGRADE_ALL ------
	#
	# Control-M Job Name: LDN-Pilot-DBA-Upgrade-All 	-->	 Airflow Job Name: JOB_LDN_PILOT_DBA_UPGRADE_ALL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_PILOT_DBA_UPGRADE_ALL = SSHOperator(
        task_id='JOB_LDN_PILOT_DBA_UPGRADE_ALL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%LNEXOVS /apps/flowrisk/prodldn/valservice/pilotDBA/upgrade_london_pilot_dba.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NFSSERVERSCLEANUP ------
	#
	# Control-M Job Name: NFSServersCleanUP 	-->	 Airflow Job Name: JOB_NFSSERVERSCLEANUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NFSSERVERSCLEANUP = SSHOperator(
        task_id='JOB_NFSSERVERSCLEANUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/NFSandServersCleanUp.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_ESVSLOGSCOPY ------
	#
	# Control-M Job Name: ESVSLogsCopy 	-->	 Airflow Job Name: JOB_ESVSLOGSCOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_ESVSLOGSCOPY = SSHOperator(
        task_id='JOB_ESVSLOGSCOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_elstSrch_logs.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNOD1RSStartPROD1 	-->	 Airflow Job Name: JOB_LDNOD1RSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNOD1RSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD2RSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNOD2RSStartPROD1 	-->	 Airflow Job Name: JOB_LDNOD2RSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD2RSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNOD2RSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD2.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNOD3RSStartPROD1 	-->	 Airflow Job Name: JOB_LDNOD3RSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNOD3RSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTOPPROD1SUN ------
	#
	# Control-M Job Name: LDNRT1CORPRSStopPROD1Sun 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTOPPROD1SUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTOPPROD1SUN = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTOPPROD1SUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTOPPROD1SUN ------
	#
	# Control-M Job Name: LDNRT2CORPRSStopPROD1Sun 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTOPPROD1SUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTOPPROD1SUN = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTOPPROD1SUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD1RSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNOD1RSStopPROD1 	-->	 Airflow Job Name: JOB_LDNOD1RSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD1RSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNOD1RSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNOD3RSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNOD3RSStopPROD1 	-->	 Airflow Job Name: JOB_LDNOD3RSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNOD3RSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNOD3RSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_OD3.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1CORPRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRT1CORPRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRT1CORPRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1CORPRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRT1CORPRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT1IDXRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRT1IDXRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRT1IDXRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT1IDXRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRT1IDXRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_IDX.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRT2CORPRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRT2CORPRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRT2CORPRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRT2CORPRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRT2CORPRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT2_CORP.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNRTTOTALRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNRTTOTALRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNRTTOTALRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNRTTOTALRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNRTTOTALRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_TOTAL.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_WEEKENDCLEANUP ------
	#
	# Control-M Job Name: WeekendCleanUp 	-->	 Airflow Job Name: JOB_WEEKENDCLEANUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_WEEKENDCLEANUP = SSHOperator(
        task_id='JOB_WEEKENDCLEANUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/weekendCleanUp.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOSSRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNEXOSSRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNEXOSSRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOSSRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNEXOSSRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_EXOTICS_SS.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOSSRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNEXOSSRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNEXOSSRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOSSRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNEXOSSRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_EXOTICS_SS.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOIDXRSSTOPPROD1 ------
	#
	# Control-M Job Name: LDNEXOIDXRSStopPROD1 	-->	 Airflow Job Name: JOB_LDNEXOIDXRSSTOPPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOIDXRSSTOPPROD1 = SSHOperator(
        task_id='JOB_LDNEXOIDXRSSTOPPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_EXOTICS_IDX.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOIDXRSSTARTPROD1 ------
	#
	# Control-M Job Name: LDNEXOIDXRSStartPROD1 	-->	 Airflow Job Name: JOB_LDNEXOIDXRSSTARTPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOIDXRSSTARTPROD1 = SSHOperator(
        task_id='JOB_LDNEXOIDXRSSTARTPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_EXOTICS_IDX.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOIDXRSSTOPPROD2 ------
	#
	# Control-M Job Name: LDNEXOIDXRSStopPROD2 	-->	 Airflow Job Name: JOB_LDNEXOIDXRSSTOPPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOIDXRSSTOPPROD2 = SSHOperator(
        task_id='JOB_LDNEXOIDXRSSTOPPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_RT_EXOTICS_IDX.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXOIDXRSSTARTPROD2 ------
	#
	# Control-M Job Name: LDNEXOIDXRSStartPROD2 	-->	 Airflow Job Name: JOB_LDNEXOIDXRSSTARTPROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXOIDXRSSTARTPROD2 = SSHOperator(
        task_id='JOB_LDNEXOIDXRSSTARTPROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_RT_EXOTICS_IDX.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT_RS_ORCH_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT-RS-ORCH-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT_RS_ORCH_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT_RS_ORCH_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT_RS_ORCH_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_ORCH_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT1_RS_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT1-RS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT1_RS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT1_RS_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT1_RS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_VIEWER1_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT1_RS_START_PROD_SUNDAY ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT1-RS-Start-PROD-Sunday 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT1_RS_START_PROD_SUNDAY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT1_RS_START_PROD_SUNDAY = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT1_RS_START_PROD_SUNDAY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_VIEWER1_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT2_RS_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT2-RS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT2_RS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT2_RS_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT2_RS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_VIEWER2_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT2_RS_START_PROD_SUNDAY ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT2-RS-Start-PROD-Sunday 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT2_RS_START_PROD_SUNDAY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT2_RS_START_PROD_SUNDAY = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT2_RS_START_PROD_SUNDAY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_VIEWER2_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT1_RS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT1-RS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT1_RS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT1_RS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT1_RS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_IDX_VIEWER1_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT2_RS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT2-RS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT2_RS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT2_RS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT2_RS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_IDX_VIEWER2_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_IDX_RT_RS_ORCH_STOP_PROD ------
	#
	# Control-M Job Name: LDN-EXO-IDX-RT-RS-ORCH-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_IDX_RT_RS_ORCH_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_IDX_RT_RS_ORCH_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_IDX_RT_RS_ORCH_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_ORCH_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_CORP ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-CORP 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_CORP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_CORP = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_CORP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%CORP %%RUN_REP -Dhost=rs-ldn-prod-corp-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/corp/intraday-risk-snap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_GPFAIT ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-GPFAIT 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_GPFAIT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_GPFAIT = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_GPFAIT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%GPF_AIT %%RUN_REP -Dhost=rs-ldn-prod-gpf-ait-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/gpfait/intraday-risk-snap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_GPFDEVEUR ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-GPFDEVEUR 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_GPFDEVEUR
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_GPFDEVEUR = DummyOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_GPFDEVEUR',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_IDX ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-IDX 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_IDX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_IDX = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_IDX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%CORP %%RUN_REP -Dhost=rs-ldn-prod-idx-flx-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idx/intraday-risk-snap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_QIS ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-QIS 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_QIS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_QIS = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_QIS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%IDX_EXO %%RUN_REP -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/qis/intraday-risk-snap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_SSEXOTICS ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-SSEXOTICS 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_SSEXOTICS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_SSEXOTICS = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_SSEXOTICS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%SS_EXO %%RUN_REP -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-risk-snap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKPROFILE_LDN_DATED ------
	#
	# Control-M Job Name: IntradayRiskProfile-LDN-dated 	-->	 Airflow Job Name: JOB_INTRADAYRISKPROFILE_LDN_DATED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKPROFILE_LDN_DATED = SSHOperator(
        task_id='JOB_INTRADAYRISKPROFILE_LDN_DATED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP -Dhost=rs-ldn-prod-od.dk0149-l.ukp2f.paas.intranet.db.com -Dport=18080 ldn/intraday-riskProfile-dated  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKPROFILE_LDN_MONTHLY ------
	#
	# Control-M Job Name: IntradayRiskProfile-LDN-Monthly 	-->	 Airflow Job Name: JOB_INTRADAYRISKPROFILE_LDN_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKPROFILE_LDN_MONTHLY = SSHOperator(
        task_id='JOB_INTRADAYRISKPROFILE_LDN_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP -Dhost=rs-ldn-prod-od.dk0149-l.ukp2f.paas.intranet.db.com -Dport=18080 ldn/intraday-riskProfile-monthly   month=%%YEARMONTH ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKPROFILE_LDN_GPF_DATED ------
	#
	# Control-M Job Name: IntradayRiskProfile-LDN-GPF-dated 	-->	 Airflow Job Name: JOB_INTRADAYRISKPROFILE_LDN_GPF_DATED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKPROFILE_LDN_GPF_DATED = SSHOperator(
        task_id='JOB_INTRADAYRISKPROFILE_LDN_GPF_DATED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP ldn/intraday-riskProfile-dated.GPF  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKPROFILE_LDN_GPF_MONTHLY ------
	#
	# Control-M Job Name: IntradayRiskProfile-LDN-GPF-monthly 	-->	 Airflow Job Name: JOB_INTRADAYRISKPROFILE_LDN_GPF_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKPROFILE_LDN_GPF_MONTHLY = SSHOperator(
        task_id='JOB_INTRADAYRISKPROFILE_LDN_GPF_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP ldn/intraday-riskProfile-monthly.GPF   month=%%YEARMONTH ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_COPY_GPFAIT ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-Copy-GPFAIT 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_COPY_GPFAIT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_COPY_GPFAIT = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_COPY_GPFAIT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%GPF_AIT %%RUN_REP -copy -Dhost=rs-ldn-prod-gpf-ait-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/gpfait/intraday-risk-snap  date=`date  +%Y-%m-%d`; datetime=`date +%Y-%m-%d.%Y%m%d.%H` && date=`date +%Y%m%d` &&  scp -o StrictHostKeyChecking=no frrun@lonplflowrcfp3.uk.db.com:/data/flowrisk/prodldn/reportserver/reports/$date/intraday-RiskLimitCheck-LDN-GPF-AIT-$datetime* frrun@fraplflowrcfp12.de.db.com:/data/flowrisk/prodldn/reports/$date ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_COPY_GPFDEVEUR ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-Copy-GPFDEVEUR 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_COPY_GPFDEVEUR
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_COPY_GPFDEVEUR = DummyOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_COPY_GPFDEVEUR',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_CORP_LEGACY ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-CORP-Legacy 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_CORP_LEGACY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_CORP_LEGACY = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_CORP_LEGACY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%ANYRS %%RUN_REP -Dhost=rs-ldn-prod-corp-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/corp/intraday-risk-snap-legacy  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_IDX_LEGACY ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-IDX-Legacy 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_IDX_LEGACY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_IDX_LEGACY = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_IDX_LEGACY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%ANYRS %%RUN_REP -Dhost=rs-ldn-prod-idx-flx-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idx/intraday-risk-snap-legacy-idx  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKMERGELDNGEDLEGACY ------
	#
	# Control-M Job Name: IntradayRiskMergeLDNGedLegacy 	-->	 Airflow Job Name: JOB_INTRADAYRISKMERGELDNGEDLEGACY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKMERGELDNGEDLEGACY = SSHOperator(
        task_id='JOB_INTRADAYRISKMERGELDNGEDLEGACY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP -Dhost=rs-ldn-prod-od.dk0149-l.ukp2f.paas.intranet.db.com -Dport=18080 ldn/intradayMergeGEDLegacyRiskSnap  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISK_LDNGEDLEGACY_BREACHCHECK ------
	#
	# Control-M Job Name: IntradayRisk-LDNGEDLegacy-BreachCheck 	-->	 Airflow Job Name: JOB_INTRADAYRISK_LDNGEDLEGACY_BREACHCHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISK_LDNGEDLEGACY_BREACHCHECK = SSHOperator(
        task_id='JOB_INTRADAYRISK_LDNGEDLEGACY_BREACHCHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP -Dhost=rs-ldn-prod-od.dk0149-l.ukp2f.paas.intranet.db.com -Dport=18080 ldn/intraday-breachCheck-merged-dated-Legacy  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNLEGACYEODCOPYXCCYADJREPORTNARROW ------
	#
	# Control-M Job Name: LDNLegacyEODCopyXccyAdjReportNarrow 	-->	 Airflow Job Name: JOB_LDNLEGACYEODCOPYXCCYADJREPORTNARROW
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNLEGACYEODCOPYXCCYADJREPORTNARROW = SSHOperator(
        task_id='JOB_LDNLEGACYEODCOPYXCCYADJREPORTNARROW',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/copy_report.sh ldn.eod.ss.prod1 t0_latest_eusReport_xccy_adj_dated",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISK_LDN_BREACHCHECK ------
	#
	# Control-M Job Name: IntradayRisk-LDN-BreachCheck 	-->	 Airflow Job Name: JOB_INTRADAYRISK_LDN_BREACHCHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISK_LDN_BREACHCHECK = SSHOperator(
        task_id='JOB_INTRADAYRISK_LDN_BREACHCHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP -Dhost=rs-ldn-prod-od.dk0149-l.ukp2f.paas.intranet.db.com -Dport=18080 ldn/intraday-breachCheck-dated  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK ------
	#
	# Control-M Job Name: IntradayRisk-LDN-GPF-BreachCheck 	-->	 Airflow Job Name: JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK = SSHOperator(
        task_id='JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%OD %%RUN_REP ldn/intraday-breachCheck-dated.GPF  date=`date  +%Y-%m-%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYRISKSNAP_LDN_CLEANUP ------
	#
	# Control-M Job Name: IntradayRiskSnap-LDN-cleanup 	-->	 Airflow Job Name: JOB_INTRADAYRISKSNAP_LDN_CLEANUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYRISKSNAP_LDN_CLEANUP = SSHOperator(
        task_id='JOB_INTRADAYRISKSNAP_LDN_CLEANUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%DAYS_TO_RETAIN;%%CORP 'find  %%REPORTS \( -name 'intraday-breachCheckDetails-*' -o -name 'intraday-RiskLimitCheck*' \) -mtime +${daysToRetain} -print -delete';",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_IDXEXO ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-IDXEXO 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_IDXEXO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_IDXEXO = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_IDXEXO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%IDXEXO %%RUN_REP -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-flash-idxexo ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_IDXEXOQISSLOW ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-IDXEXOQISSLOW 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_IDXEXOQISSLOW
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_IDXEXOQISSLOW = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_IDXEXOQISSLOW',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%IDXEXOQISSLOW %%RUN_REP -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/qis/intraday-flash-qis ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_IDXEXOPBC ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-IDXEXOPBC 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_IDXEXOPBC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_IDXEXOPBC = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_IDXEXOPBC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%IDXEXOPBC %%RUN_REP -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-flash-pbc ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_SSEXO ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-SSEXO 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_SSEXO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_SSEXO = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_SSEXO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%SSEXO %%RUN_REP -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-flash-ssexo ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_SSEXO_WASH_B2B ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-SSEXO-WASH-B2B 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_SSEXO_WASH_B2B
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_SSEXO_WASH_B2B = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_SSEXO_WASH_B2B',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_CORP ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-CORP 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_CORP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_CORP = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_CORP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%CORP %%RUN_REP -Dhost=rs-ldn-prod-corp-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/corp/intraday-flash-corp ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_IDX ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-IDX 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_IDX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_IDX = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_IDX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%ANYRS %%RUN_REP -Dhost=rs-ldn-prod-idx-flx-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idx/intraday-flash-idx  ; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_DEVEUR ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-DEVEUR 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_DEVEUR
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_DEVEUR = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_DEVEUR',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_DEVEUR_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-DEVEUR-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_DEVEUR_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_DEVEUR_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_DEVEUR_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERETF ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERETF 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERETF
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERETF = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERETF',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERETF_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERETF-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERETF_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERETF_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERETF_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHEREMSS 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHEREMSS-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERWASH 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERWASH-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERB2BSYD 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERB2BSYD-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERINVTRADING 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERINVTRADING-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERSEF 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-OTHERSEF-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_AIT ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-AIT 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_AIT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_AIT = SSHOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_AIT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="if [ %%WEEKDAY -gt 0 ] && [ %%WEEKDAY -lt 6 ]; then %%AIT %%RUN_REP -Dhost=rs-ldn-prod-gpf-ait-rt1.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/gpfait/intraday-flash-ait  executionDateShort=`date  +%Y%m%d`; fi",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYFLASHSNAP_LDN_AIT_COPY ------
	#
	# Control-M Job Name: IntradayFlashSnap-LDN-AIT-Copy 	-->	 Airflow Job Name: JOB_INTRADAYFLASHSNAP_LDN_AIT_COPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYFLASHSNAP_LDN_AIT_COPY = DummyOperator(
        task_id='JOB_INTRADAYFLASHSNAP_LDN_AIT_COPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_INTRADAYLONDON_COPYALL ------
	#
	# Control-M Job Name: IntradayLondon-CopyAll 	-->	 Airflow Job Name: JOB_INTRADAYLONDON_COPYALL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_INTRADAYLONDON_COPYALL = SSHOperator(
        task_id='JOB_INTRADAYLONDON_COPYALL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="ssh lonplflowrcfp1.uk.db.com rsync -a --ignore-existing /data/flowrisk/prodldn/reportserver/reports/`date +%Y%m%d`/Intraday-*.jar fraeqflocfp35.de.db.com:/data/flowrisk/prodldn/reports/`date +%Y%m%d`/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GPF_RISKPNL_COPY_TO_LONDON ------
	#
	# Control-M Job Name: GPF-RiskPnl-Copy-To-London 	-->	 Airflow Job Name: JOB_GPF_RISKPNL_COPY_TO_LONDON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GPF_RISKPNL_COPY_TO_LONDON = SSHOperator(
        task_id='JOB_GPF_RISKPNL_COPY_TO_LONDON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="rsync -a --ignore-existing /data/flowrisk/prodldn/reports/`%%FR_SCRIPT_DIR/Tminus1`/RiskPnl-LDN-GPF-*.jar lonplflowrcfp1.uk.db.com:/data/flowrisk/prodldn/reportserver/reports/`%%FR_SCRIPT_DIR/Tminus1`/ ; date",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_START_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-VS-Start-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_START_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_START_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_START_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_EOD.sh ldn.eod.od.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_START_PROD2 ------
	#
	# Control-M Job Name: LDN-EOD-VS-Start-PROD2 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_START_PROD2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_START_PROD2 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_START_PROD2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_EOD.sh ldn.eod.od.prod2",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_VS_STOP_PROD1 ------
	#
	# Control-M Job Name: LDN-EOD-VS-stop-PROD1 	-->	 Airflow Job Name: JOB_LDN_EOD_VS_STOP_PROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_VS_STOP_PROD1 = SSHOperator(
        task_id='JOB_LDN_EOD_VS_STOP_PROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_EOD.sh ldn.eod.od.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_01 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-01 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_01
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_01 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_01',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP01 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_01 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-01 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_01
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_01 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_01',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP01 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP01 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_01 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-01 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_01
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_01 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_01',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP01 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_01 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-01 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_01
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_01 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_01',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP01 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP01' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_01 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-01 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_01
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_01 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_01',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP01 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_02 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-02 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_02
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_02 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_02',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP02 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_03 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-03 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_03
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_03 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_03',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP03 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_04 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-04 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_04
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_04 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_04',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP04 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_05 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-05 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_05
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_05 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_05',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP05 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_07 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-07 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_07
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_07 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_07',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP07 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_08 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-08 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_08
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_08 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_08',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP08 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_DAILY_RESTART_09 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Daily-Restart-09 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_DAILY_RESTART_09
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_DAILY_RESTART_09 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_DAILY_RESTART_09',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP09 -c '/home/frrun/tradeplant/geneos/NPCtrl -c restartAll' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_02 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-02 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_02
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_02 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_02',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP02 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_03 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-03 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_03
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_03 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_03',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP03 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_04 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-04 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_04
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_04 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_04',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP04 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_05 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-05 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_05
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_05 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_05',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP05 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_07 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-07 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_07
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_07 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_07',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP07 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_08 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-08 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_08
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_08 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_08',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP08 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_NETPROBE_WATCHDOG_09 ------
	#
	# Control-M Job Name: Geneos-Netprobe-Watchdog-09 	-->	 Airflow Job Name: JOB_GENEOS_NETPROBE_WATCHDOG_09
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_NETPROBE_WATCHDOG_09 = SSHOperator(
        task_id='JOB_GENEOS_NETPROBE_WATCHDOG_09',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP09 -c '/home/frrun/tradeplant/geneos/NPCtrl -c watchDog ALLPROBES' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_02 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-02 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_02
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_02 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_02',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP02 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP02 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_03 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-03 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_03
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_03 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_03',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP03 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP03 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_04 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-04 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_04
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_04 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_04',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP04 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP04 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_05 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-05 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_05
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_05 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_05',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP05 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP05 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_07 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-07 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_07
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_07 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_07',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP07 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP07 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_08 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-08 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_08
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_08 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_08',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP08 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP08 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GENEOS_REBOOT_MONITORING_09 ------
	#
	# Control-M Job Name: Geneos-Reboot-Monitoring-09 	-->	 Airflow Job Name: JOB_GENEOS_REBOOT_MONITORING_09
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GENEOS_REBOOT_MONITORING_09 = SSHOperator(
        task_id='JOB_GENEOS_REBOOT_MONITORING_09',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP09 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_predict_reboot.sh -b GED_GROUP09 -f 366 -c ged_reboot.cfg' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_02 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-02 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_02
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_02 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_02',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP02 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_03 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-03 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_03
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_03 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_03',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP03 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_04 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-04 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_04
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_04 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_04',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP04 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_05 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-05 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_05
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_05 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_05',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP05 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_07 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-07 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_07
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_07 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_07',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP07 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_08 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-08 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_08
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_08 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_08',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP08 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_CREATION_09 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Creation-09 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_CREATION_09
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_CREATION_09 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_CREATION_09',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP09 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_touch_dnr.sh' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_02 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-02 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_02
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_02 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_02',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP02 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP02' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_03 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-03 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_03
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_03 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_03',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP03 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP03' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_04 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-04 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_04
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_04 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_04',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP04 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP04' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_05 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-05 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_05
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_05 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_05',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP05 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP05' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_07 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-07 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_07
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_07 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_07',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP07 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP07' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_08 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-08 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_08
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_08 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_08',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP08 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP08' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_REBOOT_DNR_FILE_DELETION_09 ------
	#
	# Control-M Job Name: REBOOT-DNR-File_Deletion-09 	-->	 Airflow Job Name: JOB_REBOOT_DNR_FILE_DELETION_09
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_REBOOT_DNR_FILE_DELETION_09 = SSHOperator(
        task_id='JOB_REBOOT_DNR_FILE_DELETION_09',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/opt/misc/tp_byhost.sh -p -f /home/frrun/tradeplant/etc/misc/hosts.cfg -b FR_LDN_GROUP09 -c '/home/frrun/tradeplant/opt/calendar_schedular/tp_decide.sh -c ged_reboot.cfg -t n_occ_of_day_this_month_lbl -b GED_GROUP09' -g",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS ------
	#
	# Control-M Job Name: Daily_Housekeeping_London_Servers 	-->	 Airflow Job Name: JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS = SSHOperator(
        task_id='JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/bin/run-file-hkp-multi-host-PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS_NFS ------
	#
	# Control-M Job Name: Daily_Housekeeping_London_Servers_NFS 	-->	 Airflow Job Name: JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS_NFS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS_NFS = SSHOperator(
        task_id='JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS_NFS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="/home/frrun/tradeplant/bin/run-file-hkp-multi-host-PROD-nfs.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_KICK_OFF ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Kick-Off 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_KICK_OFF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_KICK_OFF = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_KICK_OFF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="echo 1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_PNL ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Pnl 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_PNL = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: LDN-QIS-EOD-FairValue 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_FAIRVALUE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_FAIRVALUE = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_FAIRVALUE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-fair-value-modelswitch 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: LDN-QIS-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_FAIRVALUECOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_FAIRVALUECOPY = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_FAIRVALUECOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-fair-value-modelswitch 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_PNL ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Pnl 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_PNL = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-FairValue 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_FAIRVALUE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_FAIRVALUE = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_FAIRVALUE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-fair-value-modelswitch 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_FAIRVALUECOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_FAIRVALUECOPY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_FAIRVALUECOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-fair-value-modelswitch 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_STATIC ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Static 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_STATIC = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-static-data 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_STATIC ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Static 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_STATIC = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-static-data 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COMBINE ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Combine 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COMBINE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COMBINE = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COMBINE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COMBINE ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Combine 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COMBINE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COMBINE = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COMBINE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-QIS-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_RATEFIXING ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-RateFixing 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_XCCY ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-Xccy 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_XCCY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_XCCY = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_XCCY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_XCCY ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-Xccy 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_XCCY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_XCCY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_XCCY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_ATT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Att 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_ATT = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_ATT ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Att 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_ATT = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod mis3-notification portfolio=LD.QIS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod mis3-notification portfolio=LD.IDXEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod mis3-notification portfolio=LD.QIS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod mis3-notification portfolio=LD.IDXEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod mis3-notification portfolio=LD.QIS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod mis3-notification portfolio=LD.IDXEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_TOD ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Tod 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_TOD = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_TOD ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_TOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_TOD = DummyOperator(
        task_id='JOB_NY_LDN_EXO_EOD_TOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_QIS_TOD ------
	#
	# Control-M Job Name: NY-LDN-QIS-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_QIS_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_QIS_TOD = SSHOperator(
        task_id='JOB_NY_LDN_QIS_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-tradesOnDay-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_QIS_COPY_TOD ------
	#
	# Control-M Job Name: NY-LDN-QIS-Copy-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_QIS_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_QIS_COPY_TOD = SSHOperator(
        task_id='JOB_NY_LDN_QIS_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-tradesOnDay-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Model-Info 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_MODEL_INFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_MODEL_INFO = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_MODEL_INFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/modelinfo-combined mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Model-Info 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_MODEL_INFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_MODEL_INFO = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_MODEL_INFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/modelinfo-combined mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_TOD ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_TOD = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_TOD ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_TOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_TOD = DummyOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_TOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_DBAX ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Dbax 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_DBAX = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="sleep 1800;%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_DBAX ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Dbax 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_DBAX = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-QIS-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_IPV_DAILY ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-IPV-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_IPV_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_IPV_SEED ------
	#
	# Control-M Job Name: LDN-EXO-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_IPV_SEED ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_COPY_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Copy-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_COPY_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_COPY_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_COPY_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_IPV_MONTHEND ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-IPV-Monthend 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_IPV_MONTHEND = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-EXO-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_IPV_MONTHEND = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_COPY_IPV_SEED ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Copy-IPV-Seed 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_COPY_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_COPY_IPV_SEED = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_COPY_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/idxexotics/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_IPV_SEED ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-IPV-Seed 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_IPV_SEED = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_KICK_OFF ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Kick-Off 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_KICK_OFF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_KICK_OFF = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_KICK_OFF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="echo 1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_PNL ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Pnl 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_PNL = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-FairValue 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_FAIRVALUE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_FAIRVALUE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_FAIRVALUE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-fair-value-modelswitch  'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_FAIRVALUECOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_FAIRVALUECOPY = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_FAIRVALUECOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-fair-value-modelswitch  'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_PNL ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Pnl 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_PNL = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-FairValue 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_FAIRVALUE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_FAIRVALUE = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_FAIRVALUE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-fair-value-modelswitch  'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_FAIRVALUECOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_FAIRVALUECOPY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_FAIRVALUECOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-fair-value-modelswitch  'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_STATIC ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Static 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_STATIC = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-static-data 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_STATIC ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Static 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_STATIC = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-static-data 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COMBINE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Combine 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COMBINE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COMBINE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COMBINE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COMBINE ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Combine 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COMBINE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COMBINE = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COMBINE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_RATEFIXING ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-RateFixing 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_ATT ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Att 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_ATT = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_ATT ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Att 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_ATT = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_IPV_DAILY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-IPV-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_IPV_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MONTHEND ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-IPV-Monthend 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MONTHEND = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_IPV_SEED ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-IPV-Seed 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_IPV_SEED = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_IPV_SEED ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-IPV-Seed 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_IPV_SEED = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_TOD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_TOD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_TOD ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_TOD = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_XCCY ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-Xccy 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_XCCY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_XCCY = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_XCCY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_XCCY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-Xccy 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_XCCY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_XCCY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_XCCY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-pnl-persist 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_DBAX ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Dbax 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_DBAX = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_DBAX ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Dbax 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_DBAX = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-position-and-dbax-dated-idxexo 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_COPY_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_COPY_DBAX = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_COPY_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-position-and-dbax-dated-idxexo 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_DBAX ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Dbax 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_DBAX = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-ipv-att-monthly-idxexo date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_COPY_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Copy-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_COPY_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_COPY_IPV_MONTHEND = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_COPY_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-ipv-att-monthly-idxexo date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_IPV_MONTHEND
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_IPV_MONTHEND = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_IPV_MONTHEND',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_IPV_SEED ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_IPV_SEED ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Model-Info 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_MODEL_INFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_MODEL_INFO = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_MODEL_INFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/modelinfo-combined mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Model-Info 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_MODEL_INFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_MODEL_INFO = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_MODEL_INFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/modelinfo-combined-idxexo mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Model-Info 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_MODEL_INFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_MODEL_INFO = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_MODEL_INFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/modelinfo-combined mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.SSEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.IDXEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod mis3-notification portfolio=LD.SSEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Att",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.SSEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.IDXEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod mis3-notification portfolio=LD.SSEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Pnl",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.SSEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod mis3-notification portfolio=LD.IDXEXOTICS  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod mis3-notification portfolio=LD.SSEXOTICS.NY  'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`' jobType=Risk",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_TOD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Tod 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_TOD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_TOD ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Tod 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_TOD = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-tradesOnDay-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_COPY_TOD ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_COPY_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_COPY_TOD = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_COPY_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-tradesOnDay-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_TOD ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Tod 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_TOD = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_RISKPNL_PILOT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-RiskPnL-PILOT 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_RISKPNL_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_RISKPNL_PILOT = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_RISKPNL_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-latest-risk-pnl-pilot-dated 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_RECON_PILOT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Recon-PILOT 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_RECON_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_RECON_PILOT = DummyOperator(
        task_id='JOB_LDN_QIS_EOD_RECON_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_PILOT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-PILOT 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_PILOT = DummyOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Email-Risk-PnL-Pilot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_PILOT = DummyOperator(
        task_id='JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_PILOT ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-PILOT 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_PILOT = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_PILOT_RECON ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-PILOT-RECON 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_PILOT_RECON
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_PILOT_RECON = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_PILOT_RECON',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_PILOT ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-PILOT 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_PILOT = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_EMAIL_RISK_PNL_PILOT ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Email-Risk-PnL-Pilot 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_EMAIL_RISK_PNL_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_EMAIL_RISK_PNL_PILOT = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_EMAIL_RISK_PNL_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_RISKPNL_MERGE ------
	#
	# Control-M Job Name: LDN-QIS-EOD-RiskPnl-Merge 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_RISKPNL_MERGE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_RISKPNL_MERGE = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_RISKPNL_MERGE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/histRiskPnlMerge 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RISKPNL_MERGE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RiskPnl-Merge 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RISKPNL_MERGE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RISKPNL_MERGE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_RISKPNL_MERGE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/histRiskPnlMerge 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_RISKPNL_MERGE ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-RiskPnl-Merge 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_RISKPNL_MERGE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_RISKPNL_MERGE = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_RISKPNL_MERGE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/histRiskPnlMerge-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_CORRRISK_WEEKLY ------
	#
	# Control-M Job Name: LDN-EXO-EOD-CorrRisk-Weekly 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_CORRRISK_WEEKLY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_CORRRISK_WEEKLY = DummyOperator(
        task_id='JOB_LDN_EXO_EOD_CORRRISK_WEEKLY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-EXO-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.exo.prod ldn/idxexotics/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.exo.prod -copy ldn/idxexotics/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-ipv-att-modelswitch date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_PERSISTRISK ------
	#
	# Control-M Job Name: LDN-QIS-PersistRisk 	-->	 Airflow Job Name: JOB_LDN_QIS_PERSISTRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_PERSISTRISK = SSHOperator(
        task_id='JOB_LDN_QIS_PERSISTRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod  ldn/qis/jar-to-grimis-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_PERSISTRISK ------
	#
	# Control-M Job Name: NY-LDN-EXO-PersistRisk 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_PERSISTRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_PERSISTRISK = SSHOperator(
        task_id='JOB_NY_LDN_EXO_PERSISTRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod  ldn/qisus/jar-to-grimis-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_PERSISTSOD ------
	#
	# Control-M Job Name: LDN-QIS-PersistSOD 	-->	 Airflow Job Name: JOB_LDN_QIS_PERSISTSOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_PERSISTSOD = DummyOperator(
        task_id='JOB_LDN_QIS_PERSISTSOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_PERSISTRISK ------
	#
	# Control-M Job Name: LDN-SSEXO-PersistRisk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_PERSISTRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_PERSISTRISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_PERSISTRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/jar-to-grimis-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_PERSISTRISK ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-PersistRisk 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_PERSISTRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_PERSISTRISK = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_PERSISTRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/jar-to-grimis-risk 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_PERSISTSOD ------
	#
	# Control-M Job Name: LDN-SSEXO-PersistSOD 	-->	 Airflow Job Name: JOB_LDN_SSEXO_PERSISTSOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_PERSISTSOD = DummyOperator(
        task_id='JOB_LDN_SSEXO_PERSISTSOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNQISJARTOGRIMISPNL ------
	#
	# Control-M Job Name: LdnQisJarToGrimisPnl 	-->	 Airflow Job Name: JOB_LDNQISJARTOGRIMISPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNQISJARTOGRIMISPNL = SSHOperator(
        task_id='JOB_LDNQISJARTOGRIMISPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/jar-to-grimis-pnl 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNEXOJARTOGRIMISPNL ------
	#
	# Control-M Job Name: NY-LdnExoJarToGrimisPnl 	-->	 Airflow Job Name: JOB_NY_LDNEXOJARTOGRIMISPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNEXOJARTOGRIMISPNL = SSHOperator(
        task_id='JOB_NY_LDNEXOJARTOGRIMISPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/jar-to-grimis-pnl 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNQISJARTOGRIMISATT ------
	#
	# Control-M Job Name: LdnQisJarToGrimisAtt 	-->	 Airflow Job Name: JOB_LDNQISJARTOGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNQISJARTOGRIMISATT = SSHOperator(
        task_id='JOB_LDNQISJARTOGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/jar-to-grimis-att 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNEXOJARTOGRIMISATT ------
	#
	# Control-M Job Name: NY-LdnExoJarToGrimisAtt 	-->	 Airflow Job Name: JOB_NY_LDNEXOJARTOGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNEXOJARTOGRIMISATT = SSHOperator(
        task_id='JOB_NY_LDNEXOJARTOGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/jar-to-grimis-att 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NYLDNIDXEXOJAR2GRIMISYE ------
	#
	# Control-M Job Name: NyLdnIdxExoJar2grimisYE 	-->	 Airflow Job Name: JOB_NYLDNIDXEXOJAR2GRIMISYE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NYLDNIDXEXOJAR2GRIMISYE = SSHOperator(
        task_id='JOB_NYLDNIDXEXOJAR2GRIMISYE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/jar-to-grimis-ye 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSSEXOJARTOGRIMISATT ------
	#
	# Control-M Job Name: LdnSSExoJarToGrimisAtt 	-->	 Airflow Job Name: JOB_LDNSSEXOJARTOGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSSEXOJARTOGRIMISATT = SSHOperator(
        task_id='JOB_LDNSSEXOJARTOGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/jar-to-grimis-att 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNSSEXOJARTOGRIMISATT ------
	#
	# Control-M Job Name: NY-LdnSSExoJarToGrimisAtt 	-->	 Airflow Job Name: JOB_NY_LDNSSEXOJARTOGRIMISATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNSSEXOJARTOGRIMISATT = SSHOperator(
        task_id='JOB_NY_LDNSSEXOJARTOGRIMISATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/jar-to-grimis-att 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NYLDNSSEXOJAR2GRIMISYE ------
	#
	# Control-M Job Name: NyLdnSsExoJar2grimisYE 	-->	 Airflow Job Name: JOB_NYLDNSSEXOJAR2GRIMISYE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NYLDNSSEXOJAR2GRIMISYE = SSHOperator(
        task_id='JOB_NYLDNSSEXOJAR2GRIMISYE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/jar-to-grimis-ye 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB__LDN_QIS_EOD_PNL2 ------
	#
	# Control-M Job Name: #LDN-QIS-EOD-Pnl2 	-->	 Airflow Job Name: JOB__LDN_QIS_EOD_PNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB__LDN_QIS_EOD_PNL2 = DummyOperator(
        task_id='JOB__LDN_QIS_EOD_PNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB__LDN_SSEXO_EOD_PNL2 ------
	#
	# Control-M Job Name: #LDN-SSEXO-EOD-Pnl2 	-->	 Airflow Job Name: JOB__LDN_SSEXO_EOD_PNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB__LDN_SSEXO_EOD_PNL2 = DummyOperator(
        task_id='JOB__LDN_SSEXO_EOD_PNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSSEXOJARTOGRIMISPNL ------
	#
	# Control-M Job Name: LdnSSExoJarToGrimisPnl 	-->	 Airflow Job Name: JOB_LDNSSEXOJARTOGRIMISPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSSEXOJARTOGRIMISPNL = SSHOperator(
        task_id='JOB_LDNSSEXOJARTOGRIMISPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/jar-to-grimis-pnl 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNSSEXOJARTOGRIMISPNL ------
	#
	# Control-M Job Name: NY-LdnSSExoJarToGrimisPnl 	-->	 Airflow Job Name: JOB_NY_LDNSSEXOJARTOGRIMISPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNSSEXOJARTOGRIMISPNL = SSHOperator(
        task_id='JOB_NY_LDNSSEXOJARTOGRIMISPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/jar-to-grimis-pnl 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB__LDNSSEXOJARTOGRIMISPNL2 ------
	#
	# Control-M Job Name: #LdnSSExoJarToGrimisPnl2 	-->	 Airflow Job Name: JOB__LDNSSEXOJARTOGRIMISPNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB__LDNSSEXOJARTOGRIMISPNL2 = DummyOperator(
        task_id='JOB__LDNSSEXOJARTOGRIMISPNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB__LDNQISJARTOGRIMISPNL2 ------
	#
	# Control-M Job Name: #LdnQisJarToGrimisPnl2 	-->	 Airflow Job Name: JOB__LDNQISJARTOGRIMISPNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB__LDNQISJARTOGRIMISPNL2 = DummyOperator(
        task_id='JOB__LDNQISJARTOGRIMISPNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNQISJARTOGRIMISYE ------
	#
	# Control-M Job Name: LdnQisJarToGrimisYE 	-->	 Airflow Job Name: JOB_LDNQISJARTOGRIMISYE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNQISJARTOGRIMISYE = SSHOperator(
        task_id='JOB_LDNQISJARTOGRIMISYE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/jar-to-grimis-ye 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSSEXOJARTOGRIMISYE ------
	#
	# Control-M Job Name: LdnSSExoJarToGrimisYE 	-->	 Airflow Job Name: JOB_LDNSSEXOJARTOGRIMISYE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSSEXOJARTOGRIMISYE = SSHOperator(
        task_id='JOB_LDNSSEXOJARTOGRIMISYE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/jar-to-grimis-ye 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_MCC ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Mcc 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_MCC = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_COPY_MCC ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_COPY_MCC = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_MCC ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Mcc 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_MCC
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_MCC = DummyOperator(
        task_id='JOB_NY_LDN_EXO_EOD_MCC',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_COPY_MCC ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_COPY_MCC
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_COPY_MCC = DummyOperator(
        task_id='JOB_NY_LDN_EXO_EOD_COPY_MCC',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_QIS_LDN_MCC ------
	#
	# Control-M Job Name: NY-QIS-LDN-Mcc 	-->	 Airflow Job Name: JOB_NY_QIS_LDN_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_QIS_LDN_MCC = SSHOperator(
        task_id='JOB_NY_QIS_LDN_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-mcc-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_QIS_LDN_COPY_MCC ------
	#
	# Control-M Job Name: NY-QIS-LDN-Copy-Mcc 	-->	 Airflow Job Name: JOB_NY_QIS_LDN_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_QIS_LDN_COPY_MCC = SSHOperator(
        task_id='JOB_NY_QIS_LDN_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-mcc-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_MCC ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Mcc 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_MCC = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_MCC ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Mcc 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_MCC = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-mcc-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_EOD_COPY_MCC ------
	#
	# Control-M Job Name: LDN-IDXEXO-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_EOD_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_EOD_COPY_MCC = SSHOperator(
        task_id='JOB_LDN_IDXEXO_EOD_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-mcc-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_COPY_MCC ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_COPY_MCC = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_MCC ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Mcc 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_MCC = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_COPY_MCC ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_COPY_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_COPY_MCC = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_COPY_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RISKPNL_WEEKLY_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RiskPnL-WEEKLY-PILOT 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RISKPNL_WEEKLY_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RISKPNL_WEEKLY_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RISKPNL_WEEKLY_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/t0-latest-risk-pnl-pilot-dated-WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RECON_WEEKLY_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Recon-WEEKLY-PILOT 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RECON_WEEKLY_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RECON_WEEKLY_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RECON_WEEKLY_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/recon-risk-pnl-weekly-pilot-dated 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_WEEKLY_PILOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Email-Risk-PnL-WEEKLY-Pilot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_WEEKLY_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_WEEKLY_PILOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_WEEKLY_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/pilotDiff/runDiffAnalyzerPilotExotics.sh ldnexo.pilot.diff ldn_exo_weekly %%FR_SCRIPT_DIR/T-zero",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_DBAX_PILOT ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Dbax-Pilot 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_DBAX_PILOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_DBAX_PILOT = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_DBAX_PILOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-position-and-dbax-pilot-dated 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-QIS-EOD-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'eqt_qis_ldn' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'PnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'ny_index_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'PnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Risk-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'eqt_qis_ldn' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Risk-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'ny_index_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'single_stock_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'PnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'ny_single_stock_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'PnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Risk-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'single_stock_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Risk-Pnl-Error-Checks 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/eod_checks.py '-region' 'uk' '-desk' 'ny_single_stock_exotics' '-business' 'Ged' '-reports' 'Tech' '-type' 'PnL' '-risktype' 'RiskPnL'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-QIS-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-EXO-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-PVManifest 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-PVManifest 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_SPOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Spot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_SPOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_SPOT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_SPOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.spot.LDN.INDEX-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Spot 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.spot.LDN.QIS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.INDEX-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.QIS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNEXODBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNEXODBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNEXODBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNEXODBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_LDNEXODBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport3.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.idx-exo",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNEXODBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: NY-LDNEXODBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_NY_LDNEXODBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNEXODBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_NY_LDNEXODBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport3.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.qis-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Weekly-Spot-Vol 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-piv-tw.LDN.INDEX-EXOTICS.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Weekly-Spot-Vol 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.MRM.spot-piv-tw.LDN.QIS-NY.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Spot-fast 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.spot.LDN.SS-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Spot-fast 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.spot.LDN.SS-EXOTICS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: LDN-SSEXO-SOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY = SSHOperator(
        task_id='JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.SS-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-SOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.SS-EXOTICS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: NY-LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_NY_LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_NY_LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport3.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.ss-exo-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO3707_SOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: LDN-SSEXO3707-SOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_LDN_SSEXO3707_SOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO3707_SOD_SCENARIO_SPOT_VOL_DAILY = SSHOperator(
        task_id='JOB_LDN_SSEXO3707_SOD_SCENARIO_SPOT_VOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.SS-EXOTICS.3707.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport3.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.ss-exo.3707",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASHEXO_SOD_SCENARIO_SPOT_VOL_DAILY ------
	#
	# Control-M Job Name: LDN-WASHEXO-SOD-Scenario-Spot-Vol-Daily 	-->	 Airflow Job Name: JOB_LDN_WASHEXO_SOD_SCENARIO_SPOT_VOL_DAILY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASHEXO_SOD_SCENARIO_SPOT_VOL_DAILY = DummyOperator(
        task_id='JOB_LDN_WASHEXO_SOD_SCENARIO_SPOT_VOL_DAILY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1 = DummyOperator(
        task_id='JOB_LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-DivSpotVol 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL = DummyOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_COMPLEXPVEGA ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Weekly-ComplexPVega 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_COMPLEXPVEGA
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_COMPLEXPVEGA = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_COMPLEXPVEGA',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.spot.LDN.SS-EXOTICS-NY.ComplexPVega.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Weekly-NU 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.spot.LDN.SS-EXOTICS.NU.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Weekly-NU 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.spot.LDN.SS-EXOTICS-NY.NU.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Fast 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.MRM.spot-piv-tw.LDN.SS-EXOTICS.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Fast 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.MRM.spot-piv-tw.LDN.SS-EXOTICS-NY.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Slow 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.MRM.spot-piv-tw.LDN.SS-EXOTICS.3707.SOD.WEEKLY 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_DIV_SPOT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Div-Spot 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_DIV_SPOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_DIV_SPOT = DummyOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_DIV_SPOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_DIV_SPOT ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Div-Spot 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_DIV_SPOT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_DIV_SPOT = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_DIV_SPOT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.div-spot.LDN.QIS-NY.NU.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Spot-fast-dbriskstore 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot.ss-exo",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Spot-fast-dbriskstore 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot.ss-exo-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Spot-dbriskstore 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot.idx-exo",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Spot-dbriskstore 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot.idx-exo-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Fast-dbriskstore 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot-pivtw.ss-exo",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Fast-dbriskstore 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot-pivtw.ss-exo-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW_DBRISKSTORE ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-Weekly-Spot-Vol-Slow-dbriskstore 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW_DBRISKSTORE = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot-pivtw.ss-exo.3707",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Weekly-Spot-Vol-dbriskstore 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot-pivtw.idx-exo",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-Weekly-Spot-Vol-dbriskstore 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%OD %%APP_SCRIPT_DIR/runReport.sh ldn/dbriskstore.scenarios.report.spot-pivtw.qis-ny",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_SCENARIO_HYBRID_SOD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Scenario-Hybrid-SOD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_SCENARIO_HYBRID_SOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_SCENARIO_HYBRID_SOD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_SCENARIO_HYBRID_SOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.spot.LDN.INDEX-EXOTICS.SOD-Hybrids 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_SPOTVOL_BASKETCONST ------
	#
	# Control-M Job Name: LDN-EXO-SpotVol-BasketConst 	-->	 Airflow Job Name: JOB_LDN_EXO_SPOTVOL_BASKETCONST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_SPOTVOL_BASKETCONST = SSHOperator(
        task_id='JOB_LDN_EXO_SPOTVOL_BASKETCONST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-div.LDN.INDEX-EXOTICS.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_SPOTVOL_BASKETCONST ------
	#
	# Control-M Job Name: LDN-QIS-SpotVol-BasketConst 	-->	 Airflow Job Name: JOB_LDN_QIS_SPOTVOL_BASKETCONST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_SPOTVOL_BASKETCONST = SSHOperator(
        task_id='JOB_LDN_QIS_SPOTVOL_BASKETCONST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-div.LDN.QIS.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_SCENARIO_GAP_RISK ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-Scenario-GAP-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_SCENARIO_GAP_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_SCENARIO_GAP_RISK = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_SCENARIO_GAP_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.MRM.spot-div.LDN.QIS-NY.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_TERM_STRUCTURE ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Term-Structure 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_TERM_STRUCTURE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_TERM_STRUCTURE = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_TERM_STRUCTURE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/idxexotics/t0-termstructure 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_SCENARIO_GAP_RISK ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-Scenario-GAP-Risk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_SCENARIO_GAP_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_SCENARIO_GAP_RISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_SCENARIO_GAP_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.MRM.spot-div.LDN.SS-EXOTICS.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_SCENARIO_GAP_RISK ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-Scenario-GAP-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_SCENARIO_GAP_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_SCENARIO_GAP_RISK = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_SCENARIO_GAP_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.MRM.spot-div.LDN.SS-EXOTICS-NY.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_DISCONTINUITY ------
	#
	# Control-M Job Name: LDN-EXO-Discontinuity 	-->	 Airflow Job Name: JOB_LDN_EXO_DISCONTINUITY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_DISCONTINUITY = SSHOperator(
        task_id='JOB_LDN_EXO_DISCONTINUITY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/ssexotics/t0-discontinuity-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_DISCONTINUITY ------
	#
	# Control-M Job Name: NY-LDN-EXO-Discontinuity 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_DISCONTINUITY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_DISCONTINUITY = SSHOperator(
        task_id='JOB_NY_LDN_EXO_DISCONTINUITY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/t0-discontinuity 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_DISCONTINUITY ------
	#
	# Control-M Job Name: LDN-SSEXO-Discontinuity 	-->	 Airflow Job Name: JOB_LDN_SSEXO_DISCONTINUITY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_DISCONTINUITY = SSHOperator(
        task_id='JOB_LDN_SSEXO_DISCONTINUITY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-discontinuity 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_DISCONTINUITY ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-Discontinuity 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_DISCONTINUITY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_DISCONTINUITY = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_DISCONTINUITY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/t0-discontinuity 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_SIZE_RISK ------
	#
	# Control-M Job Name: LDN-SSEXO-Size-Risk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_SIZE_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_SIZE_RISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_SIZE_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.size-risk-spot-time-decay.LDN.SS-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_SIZE_RISK ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-Size-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_SIZE_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_SIZE_RISK = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_SIZE_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/scenario.size-risk-spot-time-decay.LDN.SS-EXOTICS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_SIZE_RISK ------
	#
	# Control-M Job Name: LDN-EXO-Size-Risk 	-->	 Airflow Job Name: JOB_LDN_EXO_SIZE_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_SIZE_RISK = SSHOperator(
        task_id='JOB_LDN_EXO_SIZE_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.size-risk-spot-time-decay.LDN.INDEX-EXOTICS.SOD 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_SIZE_RISK ------
	#
	# Control-M Job Name: NY-LDN-EXO-Size-Risk 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_SIZE_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_SIZE_RISK = SSHOperator(
        task_id='JOB_NY_LDN_EXO_SIZE_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/scenario.size-risk-spot-time-decay.LDN.QIS-NY.SOD 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_IDX_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_STOP_PROD_EUS ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Stop-PROD-EUS 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_STOP_PROD_EUS
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_STOP_PROD_EUS = DummyOperator(
        task_id='JOB_LDN_EXO_EOD_RS_STOP_PROD_EUS',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_START_PROD_EUS ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Start-PROD-EUS 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_START_PROD_EUS
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_START_PROD_EUS = DummyOperator(
        task_id='JOB_LDN_EXO_EOD_RS_START_PROD_EUS',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_STOP_PRE_ATT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Stop-PRE-ATT 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_STOP_PRE_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_STOP_PRE_ATT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_STOP_PRE_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_IDX_EOD_PROD.sh;sleep 120",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_RS_START_PRE_ATT ------
	#
	# Control-M Job Name: LDN-EXO-EOD-RS-Start-PRE-ATT 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_RS_START_PRE_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_RS_START_PRE_ATT = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_RS_START_PRE_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_IDX_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RS_START_PROD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RS_START_PROD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_RS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_RS_LDN_EXO_SS_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RS_START_PROD_EUS ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RS-Start-PROD-EUS 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RS_START_PROD_EUS
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RS_START_PROD_EUS = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_RS_START_PROD_EUS',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_RS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_RS_LDN_EXO_SS_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_RS_STOP_PROD_EUS ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-RS-Stop-PROD-EUS 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_RS_STOP_PROD_EUS
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_RS_STOP_PROD_EUS = DummyOperator(
        task_id='JOB_LDN_SSEXO_EOD_RS_STOP_PROD_EUS',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_VS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-VS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_VS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_VS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_VS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_LDN_EXO_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_VS_START_PROD ------
	#
	# Control-M Job Name: LDN-EXO-EOD-VS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_VS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_VS_START_PROD = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_VS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_LDN_EXO_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_VS_START_PROD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-VS-Start-PROD 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_VS_START_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_VS_START_PROD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_VS_START_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/start_VS_LDN_SSEXO_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_VS_STOP_PROD ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-VS-Stop-PROD 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_VS_STOP_PROD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_VS_STOP_PROD = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_VS_STOP_PROD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/stop_VS_LDN_SSEXO_EOD_PROD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_ATT_11AM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-Att-11AM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_ATT_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_ATT_11AM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_ATT_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_ATT_1530PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-Att-1530PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_ATT_1530PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_ATT_1530PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_ATT_1530PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_ATT_1640PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-Att-1640PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_ATT_1640PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_ATT_1640PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_ATT_1640PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att-idxexo 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_INTRADAY_ATT_11AM ------
	#
	# Control-M Job Name: NY-LDN-EXO-Intraday-Att-11AM 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_INTRADAY_ATT_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_INTRADAY_ATT_11AM = SSHOperator(
        task_id='JOB_NY_LDN_EXO_INTRADAY_ATT_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/intraday-att-reduced 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_INTRADAY_ATT_1530PM ------
	#
	# Control-M Job Name: NY-LDN-EXO-Intraday-Att-1530PM 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_INTRADAY_ATT_1530PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_INTRADAY_ATT_1530PM = SSHOperator(
        task_id='JOB_NY_LDN_EXO_INTRADAY_ATT_1530PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/intraday-att-reduced 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_INTRADAY_ATT_1640PM ------
	#
	# Control-M Job Name: NY-LDN-EXO-Intraday-Att-1640PM 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_INTRADAY_ATT_1640PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_INTRADAY_ATT_1640PM = SSHOperator(
        task_id='JOB_NY_LDN_EXO_INTRADAY_ATT_1640PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/intraday-att-reduced 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_FLASH_11AM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-flash-11AM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_FLASH_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_FLASH_11AM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_FLASH_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-idxexotics-flash",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_FLASH_17PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-flash-17PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_FLASH_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_FLASH_17PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_FLASH_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-idxexotics-flash",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_ATT_11AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-Att-11AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_ATT_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_ATT_11AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_ATT_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_ATT_1530PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-Att-1530PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_ATT_1530PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_ATT_1530PM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_ATT_1530PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_ATT_1635PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-Att-1635PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_ATT_1635PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_ATT_1635PM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_ATT_1635PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_INTRADAY_ATT_11AM ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-Intraday-Att-11AM 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_INTRADAY_ATT_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_INTRADAY_ATT_11AM = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_INTRADAY_ATT_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_INTRADAY_ATT_1530PM ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-Intraday-Att-1530PM 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_INTRADAY_ATT_1530PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_INTRADAY_ATT_1530PM = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_INTRADAY_ATT_1530PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_GRIMIS_CACHE_10AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Grimis-Cache-10AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_GRIMIS_CACHE_10AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_GRIMIS_CACHE_10AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_GRIMIS_CACHE_10AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/populate-grimis-eod-cache",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_GRIMIS_CACHE_16PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Grimis-Cache-16PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_GRIMIS_CACHE_16PM
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_GRIMIS_CACHE_16PM = DummyOperator(
        task_id='JOB_LDN_SSEXO_GRIMIS_CACHE_16PM',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_FLASH_20PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-flash-20PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_FLASH_20PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_FLASH_20PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_FLASH_20PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -Dhost=rs-ldn-prod-qis-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-idxexotics-flash",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_GRIMIS_CACHE_16PM ------
	#
	# Control-M Job Name: LDN-IDXEXO-Grimis-Cache-16PM 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_GRIMIS_CACHE_16PM
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_GRIMIS_CACHE_16PM = DummyOperator(
        task_id='JOB_LDN_IDXEXO_GRIMIS_CACHE_16PM',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_GRIMIS_CACHE_8PM ------
	#
	# Control-M Job Name: LDN-IDXEXO-Grimis-Cache-8PM 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_GRIMIS_CACHE_8PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_GRIMIS_CACHE_8PM = SSHOperator(
        task_id='JOB_LDN_IDXEXO_GRIMIS_CACHE_8PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/populate-grimis-eod-cache",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_GRIMIS_CACHE_8AM ------
	#
	# Control-M Job Name: LDN-IDXEXO-Grimis-Cache-8AM 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_GRIMIS_CACHE_8AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_GRIMIS_CACHE_8AM = SSHOperator(
        task_id='JOB_LDN_IDXEXO_GRIMIS_CACHE_8AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/populate-grimis-eod-cache",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HYBRID_INTRADAY_ATT_11AM ------
	#
	# Control-M Job Name: LDN-Hybrid-Intraday-Att-11AM 	-->	 Airflow Job Name: JOB_LDN_HYBRID_INTRADAY_ATT_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HYBRID_INTRADAY_ATT_11AM = SSHOperator(
        task_id='JOB_LDN_HYBRID_INTRADAY_ATT_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att-3718-reduced 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HYBRID_INTRADAY_ATT_17PM ------
	#
	# Control-M Job Name: LDN-Hybrid-Intraday-Att-17PM 	-->	 Airflow Job Name: JOB_LDN_HYBRID_INTRADAY_ATT_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HYBRID_INTRADAY_ATT_17PM = SSHOperator(
        task_id='JOB_LDN_HYBRID_INTRADAY_ATT_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att-3718-reduced 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_PRIIPS_11AM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-PRIIPS-11AM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_PRIIPS_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_PRIIPS_11AM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_PRIIPS_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh  -DserverReport=true -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches-idxexo date=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` time=1100",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_11AM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-COPY-PRIIPS-11AM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_11AM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -copy -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches-idxexo date=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` time=1100",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_PRIIPS_17PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-PRIIPS-17PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_PRIIPS_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_PRIIPS_17PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_PRIIPS_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -DserverReport=true -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE` time=1700",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_17PM ------
	#
	# Control-M Job Name: LDN-EXO-Intraday-COPY-PRIIPS-17PM 	-->	 Airflow Job Name: JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_17PM = SSHOperator(
        task_id='JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -copy -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/idxexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE` time=1700",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EXO_PNL_FLASH_TRACKER ------
	#
	# Control-M Job Name: LDN-IDX-EXO-PnL-Flash-Tracker 	-->	 Airflow Job Name: JOB_LDN_IDX_EXO_PNL_FLASH_TRACKER
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EXO_PNL_FLASH_TRACKER = SSHOperator(
        task_id='JOB_LDN_IDX_EXO_PNL_FLASH_TRACKER',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_tools/exo_attribution_tracker.py '`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_ERROR_REPORT_1545PM ------
	#
	# Control-M Job Name: LDN-EXO-Error-Report-15:45PM 	-->	 Airflow Job Name: JOB_LDN_EXO_ERROR_REPORT_1545PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_ERROR_REPORT_1545PM = SSHOperator(
        task_id='JOB_LDN_EXO_ERROR_REPORT_1545PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'index_exotics' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_ERROR_REPORT_730AM ------
	#
	# Control-M Job Name: LDN-EXO-Error-Report-7:30AM 	-->	 Airflow Job Name: JOB_LDN_EXO_ERROR_REPORT_730AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_ERROR_REPORT_730AM = SSHOperator(
        task_id='JOB_LDN_EXO_ERROR_REPORT_730AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'index_exotics' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_ERROR_REPORT_730AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Error-Report-7:30AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_ERROR_REPORT_730AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_ERROR_REPORT_730AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_ERROR_REPORT_730AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'single_stock_exotics' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_ERROR_REPORT_730AM ------
	#
	# Control-M Job Name: LDN-CORP-Error-Report-7:30AM 	-->	 Airflow Job Name: JOB_LDN_CORP_ERROR_REPORT_730AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_ERROR_REPORT_730AM = SSHOperator(
        task_id='JOB_LDN_CORP_ERROR_REPORT_730AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'corporates' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_ERROR_REPORT_1545PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Error-Report-15:45PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_ERROR_REPORT_1545PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_ERROR_REPORT_1545PM = SSHOperator(
        task_id='JOB_LDN_SSEXO_ERROR_REPORT_1545PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'single_stock_exotics' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_ERROR_REPORT_1545PM ------
	#
	# Control-M Job Name: LDN-CORP-Error-Report-15:45PM 	-->	 Airflow Job Name: JOB_LDN_CORP_ERROR_REPORT_1545PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_ERROR_REPORT_1545PM = SSHOperator(
        task_id='JOB_LDN_CORP_ERROR_REPORT_1545PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_error_automation/intraday_checks.py '-region' 'uk' '-desk' 'corporates' '-business' 'Ged' '-reports' 'FO'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_KICK_OFF ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Kick-Off 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_KICK_OFF
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_KICK_OFF = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_KICK_OFF',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_PNL ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Pnl 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_PNL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_PNL = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_PNL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: LDN-WASH-EOD-FairValue 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_FAIRVALUE
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_FAIRVALUE = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_FAIRVALUE',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: LDN-WASH-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_FAIRVALUECOPY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_FAIRVALUECOPY = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_FAIRVALUECOPY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_XCCY ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Xccy 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_XCCY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_XCCY = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_XCCY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_NOTIFY_PNL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_NOTIFY_PNL = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_NOTIFY_PNL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_STATIC ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Static 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_STATIC
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_STATIC = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_STATIC',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COMBINED ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Combined 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COMBINED
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COMBINED = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COMBINED',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-WASH-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_RATEFIXING
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_RATEFIXING = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_RATEFIXING',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_ATT ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Att 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_ATT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_ATT = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_ATT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_COMBINED ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Combined 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_COMBINED
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_COMBINED = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_COMBINED',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_PERSISTRISK ------
	#
	# Control-M Job Name: LDN-WASH-PersistRisk 	-->	 Airflow Job Name: JOB_LDN_WASH_PERSISTRISK
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_PERSISTRISK = DummyOperator(
        task_id='JOB_LDN_WASH_PERSISTRISK',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_PERSISTSOD ------
	#
	# Control-M Job Name: LDN-WASH-PersistSod 	-->	 Airflow Job Name: JOB_LDN_WASH_PERSISTSOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_PERSISTSOD = DummyOperator(
        task_id='JOB_LDN_WASH_PERSISTSOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_NOTIFY_RISK
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_NOTIFY_RISK = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_NOTIFY_RISK',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_NOTIFY_RISK
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_NOTIFY_RISK = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_NOTIFY_RISK',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_TOD ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Tod 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_TOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_TOD = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_TOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_TOD ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Tod 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_TOD
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_TOD = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_TOD',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-WASH-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_IPV_DAILY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_IPV_DAILY = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_IPV_DAILY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_IPV_MONTHEND ------
	#
	# Control-M Job Name: LDN-WASH-EOD-IPV-Monthend 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_IPV_MONTHEND
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_IPV_MONTHEND = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_IPV_MONTHEND',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Ipv-daily 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_IPV_DAILY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_IPV_DAILY = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_IPV_DAILY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_IPV_MONTHLY ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Ipv-monthly 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_IPV_MONTHLY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_IPV_MONTHLY = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_IPV_MONTHLY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_MODEL_INFO ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Model-Info 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_MODEL_INFO
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_MODEL_INFO = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_MODEL_INFO',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_DBAX ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Dbax 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_DBAX
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_DBAX = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_DBAX',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_DBAX ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Dbax 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_DBAX
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_DBAX = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_DBAX',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_ATT ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Att 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_ATT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_ATT = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_ATT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RUNLDNWASHJARTOGRIMISPNL ------
	#
	# Control-M Job Name: runLdnWashJarToGrimisPnl 	-->	 Airflow Job Name: JOB_RUNLDNWASHJARTOGRIMISPNL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RUNLDNWASHJARTOGRIMISPNL = DummyOperator(
        task_id='JOB_RUNLDNWASHJARTOGRIMISPNL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNWASHJARTOGRIMISATT ------
	#
	# Control-M Job Name: LdnWashJarToGrimisAtt 	-->	 Airflow Job Name: JOB_LDNWASHJARTOGRIMISATT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNWASHJARTOGRIMISATT = DummyOperator(
        task_id='JOB_LDNWASHJARTOGRIMISATT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_PNL2 ------
	#
	# Control-M Job Name: LDN-WASH-Pnl2 	-->	 Airflow Job Name: JOB_LDN_WASH_PNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_PNL2 = DummyOperator(
        task_id='JOB_LDN_WASH_PNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RUNLDNWASHJARTOGRIMISPNL2 ------
	#
	# Control-M Job Name: runLdnWashJarToGrimisPnl2 	-->	 Airflow Job Name: JOB_RUNLDNWASHJARTOGRIMISPNL2
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RUNLDNWASHJARTOGRIMISPNL2 = DummyOperator(
        task_id='JOB_RUNLDNWASHJARTOGRIMISPNL2',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNWASHJARTOGRIMISYE ------
	#
	# Control-M Job Name: LdnWashJarToGrimisYE 	-->	 Airflow Job Name: JOB_LDNWASHJARTOGRIMISYE
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNWASHJARTOGRIMISYE = DummyOperator(
        task_id='JOB_LDNWASHJARTOGRIMISYE',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_MCC ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Mcc 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_MCC
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_MCC = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_MCC',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COPY_MCC ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Copy-Mcc 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COPY_MCC
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COPY_MCC = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COPY_MCC',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_COMBINED_PILOT ------
	#
	# Control-M Job Name: LDN-WASH-EOD-Combined-Pilot 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_COMBINED_PILOT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_COMBINED_PILOT = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_COMBINED_PILOT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-WASH-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_PVMANIFEST
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_PVMANIFEST = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_PVMANIFEST',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-ipv-att-daily date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_DAILY_COPY ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Daily-Copy 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_DAILY_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_DAILY_COPY = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_DAILY_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-ipv-att-daily date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_MONTHLY ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Monthly 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_MONTHLY = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_MONTHLY_COPY ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Monthly-Copy 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_MONTHLY_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_MONTHLY_COPY = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_MONTHLY_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-ipv-att-daily date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_DAILY_COPY ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Daily-Copy 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_DAILY_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_DAILY_COPY = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_DAILY_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod -copy ldn/idx/t0-ipv-att-daily date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_MONTHLY ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Monthly 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_MONTHLY = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_MONTHLY_COPY ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Monthly-Copy 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_MONTHLY_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_MONTHLY_COPY = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_MONTHLY_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod -copy ldn/idx/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EOD_IPV_SEED_VAR_KICKOFF ------
	#
	# Control-M Job Name: LDN-EOD-IPV-Seed-Var-Kickoff 	-->	 Airflow Job Name: JOB_LDN_EOD_IPV_SEED_VAR_KICKOFF
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EOD_IPV_SEED_VAR_KICKOFF = SSHOperator(
        task_id='JOB_LDN_EOD_IPV_SEED_VAR_KICKOFF',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="echo kicking off seed var",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_SEED_VAR ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Seed-Var 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_SEED_VAR
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_SEED_VAR = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_SEED_VAR',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-ipv-att-numerical-limitation date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_SEED_VAR ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Seed-Var 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_SEED_VAR
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_SEED_VAR = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_SEED_VAR',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod ldn/idx/t0-ipv-att-numerical-limitation date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_IPV_SEED_VAR_COPY ------
	#
	# Control-M Job Name: LDN-CORP-EOD-IPV-Seed-Var-Copy 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_IPV_SEED_VAR_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_IPV_SEED_VAR_COPY = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_IPV_SEED_VAR_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-ipv-att-numerical-limitation date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_IPV_SEED_VAR_COPY ------
	#
	# Control-M Job Name: LDN-IDX-EOD-IPV-Seed-Var-Copy 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_IPV_SEED_VAR_COPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_IPV_SEED_VAR_COPY = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_IPV_SEED_VAR_COPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idx.prod -copy ldn/idx/t0-ipv-att-numerical-limitation date=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_QIS_PNL_0700 ------
	#
	# Control-M Job Name: LDN-EXO-QIS-Pnl-0700 	-->	 Airflow Job Name: JOB_LDN_EXO_QIS_PNL_0700
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_QIS_PNL_0700 = SSHOperator(
        task_id='JOB_LDN_EXO_QIS_PNL_0700',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/t0-pnl-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_QIS_PNL_0915 ------
	#
	# Control-M Job Name: LDN-EXO-QIS-Pnl-0915 	-->	 Airflow Job Name: JOB_LDN_EXO_QIS_PNL_0915
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_QIS_PNL_0915 = SSHOperator(
        task_id='JOB_LDN_EXO_QIS_PNL_0915',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/idxexotics/t0-pnl-qis 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_PRIIPS_11AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-PRIIPS-11AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_PRIIPS_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_PRIIPS_11AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_PRIIPS_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -DserverReport=true -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` time=1100",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_11AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-COPY-PRIIPS-11AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_11AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_11AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_11AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -copy -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` time=1100",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_PRIIPS_17PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-PRIIPS-17PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_PRIIPS_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_PRIIPS_17PM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_PRIIPS_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -DserverReport=true -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE` time=1700",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_17PM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-COPY-PRIIPS-17PM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_17PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_17PM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_17PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%EXO_RT %%APP_DIR/bin/report/runReport.sh -copy -Dhost=rs-ldn-prod-ssexo-rt.dk0149-l.ukp2f.paas.intranet.db.com -Dport=19090 ldn/ssexotics/intraday-barrier-breaches date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE` time=1700",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_QIS_SPOT_SCENARIO ------
	#
	# Control-M Job Name: LDN-EXO-QIS-Spot-Scenario 	-->	 Airflow Job Name: JOB_LDN_EXO_QIS_SPOT_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_QIS_SPOT_SCENARIO = SSHOperator(
        task_id='JOB_LDN_EXO_QIS_SPOT_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT ldn.eod.idxexo.prod ldn/scenario.spot.LDN.INDEX-EXOTICS.QIS.SOD 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_LUMRISK_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QIS-LumRisk-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QIS_LUMRISK_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_LUMRISK_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QIS_LUMRISK_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/scenario.stress.lumRisk.QIS 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_PST_SBETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QIS-PST-SBeta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QIS_PST_SBETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_PST_SBETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QIS_PST_SBETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/scenario.stress.pst-sbeta.QIS 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_PST_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QIS-PST-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QIS_PST_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_PST_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QIS_PST_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/scenario.stress.pst-beta.QIS 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_COMBINED_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QIS-Combined-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QIS_COMBINED_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_COMBINED_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QIS_COMBINED_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/ScenarioStressBetaMerge 'date=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_QIS_SPOT_SCENARIO ------
	#
	# Control-M Job Name: NY-LDN-EXO-QIS-Spot-Scenario 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_QIS_SPOT_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_QIS_SPOT_SCENARIO = SSHOperator(
        task_id='JOB_NY_LDN_EXO_QIS_SPOT_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT ldn.eod.idxexo.ny.prod ldn/scenario.spot.LDN.NY.QIS.SOD 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPDBRSSPOTEODPROD1 ------
	#
	# Control-M Job Name: LDNCORPDBRSSPOTEODPROD1 	-->	 Airflow Job Name: JOB_LDNCORPDBRSSPOTEODPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPDBRSSPOTEODPROD1 = SSHOperator(
        task_id='JOB_LDNCORPDBRSSPOTEODPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/dbriskstore.scenarios.report.spot.corp",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPSPOTSODPROD1 ------
	#
	# Control-M Job Name: LDNCORPSPOTSODPROD1 	-->	 Airflow Job Name: JOB_LDNCORPSPOTSODPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPSPOTSODPROD1 = SSHOperator(
        task_id='JOB_LDNCORPSPOTSODPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.spot.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_SPOTVOL ------
	#
	# Control-M Job Name: LDN-CORP-SpotVol 	-->	 Airflow Job Name: JOB_LDN_CORP_SPOTVOL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_SPOTVOL = SSHOperator(
        task_id='JOB_LDN_CORP_SPOTVOL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.MRM.spot-piv-tw.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXDBRSSPOTEODPROD1 ------
	#
	# Control-M Job Name: LDNIDXDBRSSPOTEODPROD1 	-->	 Airflow Job Name: JOB_LDNIDXDBRSSPOTEODPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXDBRSSPOTEODPROD1 = SSHOperator(
        task_id='JOB_LDNIDXDBRSSPOTEODPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/dbriskstore.scenarios.report.spot.idx",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNSPOTVOLPROD1 ------
	#
	# Control-M Job Name: LDNSPOTVOLPROD1 	-->	 Airflow Job Name: JOB_LDNSPOTVOLPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNSPOTVOLPROD1 = SSHOperator(
        task_id='JOB_LDNSPOTVOLPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runAllReports.MRM.EOD.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTPIVTWSODPROD1 ------
	#
	# Control-M Job Name: LDNIDXSPOTPIVTWSODPROD1 	-->	 Airflow Job Name: JOB_LDNIDXSPOTPIVTWSODPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTPIVTWSODPROD1 = SSHOperator(
        task_id='JOB_LDNIDXSPOTPIVTWSODPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.MRM.spot-piv-tw.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTSODPROD1 ------
	#
	# Control-M Job Name: LDNIDXSPOTSODPROD1 	-->	 Airflow Job Name: JOB_LDNIDXSPOTSODPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTSODPROD1 = SSHOperator(
        task_id='JOB_LDNIDXSPOTSODPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.spot.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_SPOTVOL_DAILY ------
	#
	# Control-M Job Name: LDN-CORP-SpotVol-Daily 	-->	 Airflow Job Name: JOB_LDN_CORP_SPOTVOL_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_SPOTVOL_DAILY = SSHOperator(
        task_id='JOB_LDN_CORP_SPOTVOL_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.CORP.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNCORPDBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.corp",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_GAP_RISK ------
	#
	# Control-M Job Name: LDN-CORP-GAP-Risk 	-->	 Airflow Job Name: JOB_LDN_CORP_GAP_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_GAP_RISK = SSHOperator(
        task_id='JOB_LDN_CORP_GAP_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport1.sh ldn/scenario.MRM.spot-div.LDN.CORP.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXSPOTPIVTWSODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNIDXSPOTPIVTWSODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNIDXSPOTPIVTWSODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXSPOTPIVTWSODDAILYPROD1 = SSHOperator(
        task_id='JOB_LDNIDXSPOTPIVTWSODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.INDEX.SOD",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD1 ------
	#
	# Control-M Job Name: LDNIDXDBRSSPOTPIVTWEODDAILYPROD1 	-->	 Airflow Job Name: JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD1 = SSHOperator(
        task_id='JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/dbriskstore.scenarios.report.spot-pivtw.DAILY.idx",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_GAP_RISK ------
	#
	# Control-M Job Name: LDN-IDX-GAP-Risk 	-->	 Airflow Job Name: JOB_LDN_IDX_GAP_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_GAP_RISK = SSHOperator(
        task_id='JOB_LDN_IDX_GAP_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runReport2.sh ldn/scenario.MRM.spot-div.LDN.INDEX.BASKETCONSTITUENT.SOD 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_GLOBAL_GRID_ENGINE_START ------
	#
	# Control-M Job Name: Global-Grid-Engine-Start 	-->	 Airflow Job Name: JOB_GLOBAL_GRID_ENGINE_START
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_GLOBAL_GRID_ENGINE_START = SSHOperator(
        task_id='JOB_GLOBAL_GRID_ENGINE_START',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/prod_flowrisk_all_engine_start.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FABRIC_CHECK ------
	#
	# Control-M Job Name: Fabric-Check 	-->	 Airflow Job Name: JOB_FABRIC_CHECK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FABRIC_CHECK = SSHOperator(
        task_id='JOB_FABRIC_CHECK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.spot.Fabric-Check  'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LONDON_GED_SLA_REPORT ------
	#
	# Control-M Job Name: London-GED-SLA-Report 	-->	 Airflow Job Name: JOB_LONDON_GED_SLA_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LONDON_GED_SLA_REPORT = SSHOperator(
        task_id='JOB_LONDON_GED_SLA_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_tools/batch_slas.py '-region' 'uk' '-mode' 'EOD' '-desk' 'index_exotics' '-business' 'Ged' '-statusType' 'EOD' '-cobDate' '`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FFT_GED_SLA_REPORT ------
	#
	# Control-M Job Name: FFT-GED-SLA-Report 	-->	 Airflow Job Name: JOB_FFT_GED_SLA_REPORT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FFT_GED_SLA_REPORT = SSHOperator(
        task_id='JOB_FFT_GED_SLA_REPORT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python -u %%SCRIPT_DIR/fr_tools/batch_slas.py '-region' 'eu' '-mode' 'EOD' '-desk' 'index' '-business' 'Ged' '-statusType' 'EOD' '-cobDate' '`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_APAC_GED_SLA_REPORT ------
	#
	# Control-M Job Name: APAC-GED-SLA-Report 	-->	 Airflow Job Name: JOB_APAC_GED_SLA_REPORT
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_APAC_GED_SLA_REPORT = DummyOperator(
        task_id='JOB_APAC_GED_SLA_REPORT',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FLOWRISK_OPEN_POSITIONS_PUSH ------
	#
	# Control-M Job Name: Flowrisk-Open-Positions-Push 	-->	 Airflow Job Name: JOB_FLOWRISK_OPEN_POSITIONS_PUSH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FLOWRISK_OPEN_POSITIONS_PUSH = SSHOperator(
        task_id='JOB_FLOWRISK_OPEN_POSITIONS_PUSH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python %%SCRIPT_DIR/scripts/open_positions/send_open_positions.py '`/data/flowrisk/prodldn/fr-scripts/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FLOWRISK_DBALLOCATOR_OPEN_POSITIONS ------
	#
	# Control-M Job Name: Flowrisk-dbAllocator-Open-Positions 	-->	 Airflow Job Name: JOB_FLOWRISK_DBALLOCATOR_OPEN_POSITIONS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FLOWRISK_DBALLOCATOR_OPEN_POSITIONS = SSHOperator(
        task_id='JOB_FLOWRISK_DBALLOCATOR_OPEN_POSITIONS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python %%SCRIPT_DIR/scripts/dballoc_positions/allocator_open_positions_sysarg.py '`/data/flowrisk/prodldn/fr-scripts/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FLOWRISK_DBALLOCATOR_DURATIONS ------
	#
	# Control-M Job Name: Flowrisk-dbAllocator-Durations 	-->	 Airflow Job Name: JOB_FLOWRISK_DBALLOCATOR_DURATIONS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FLOWRISK_DBALLOCATOR_DURATIONS = SSHOperator(
        task_id='JOB_FLOWRISK_DBALLOCATOR_DURATIONS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python %%SCRIPT_DIR/scripts/dballoc_durations/allocator_durations_sysarg.py '`/data/flowrisk/prodldn/fr-scripts/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FLOWRISK_DBALLOCATOR_EOD_HW_COST ------
	#
	# Control-M Job Name: Flowrisk-dbAllocator-EOD-HW-Cost 	-->	 Airflow Job Name: JOB_FLOWRISK_DBALLOCATOR_EOD_HW_COST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FLOWRISK_DBALLOCATOR_EOD_HW_COST = SSHOperator(
        task_id='JOB_FLOWRISK_DBALLOCATOR_EOD_HW_COST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python %%SCRIPT_DIR/scripts/dbAllocator_eod/eod_hw_cost_per_account_main.py '`/data/flowrisk/prodldn/fr-scripts/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FLOWRISK_DBALLOCATOR_FABRIC_HW_COST ------
	#
	# Control-M Job Name: Flowrisk-dbAllocator-FABRIC-HW-Cost 	-->	 Airflow Job Name: JOB_FLOWRISK_DBALLOCATOR_FABRIC_HW_COST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FLOWRISK_DBALLOCATOR_FABRIC_HW_COST = SSHOperator(
        task_id='JOB_FLOWRISK_DBALLOCATOR_FABRIC_HW_COST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%PYTHONSERVER /apps/flowrisk/conda/conda/bin/python %%SCRIPT_DIR/scripts/dbAllocator_fabric/fabric_hw_cost_per_account_main.py",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_CORRSKEW ------
	#
	# Control-M Job Name: LDN-SSEXO-SOD-Scenario-Spot-CORRSKEW 	-->	 Airflow Job Name: JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_CORRSKEW
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_CORRSKEW = DummyOperator(
        task_id='JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_CORRSKEW',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_STOCHVOL ------
	#
	# Control-M Job Name: LDN-SSEXO-SOD-Scenario-Spot-STOCHVOL 	-->	 Airflow Job Name: JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_STOCHVOL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_STOCHVOL = SSHOperator(
        task_id='JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_STOCHVOL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.spot.LDN-SS-EXOTICS.SOD.STOCHVOL  'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_PRICE ------
	#
	# Control-M Job Name: LDN-SSEXO-SOD-Scenario-Spot-PRICE 	-->	 Airflow Job Name: JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_PRICE
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_PRICE = DummyOperator(
        task_id='JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_PRICE',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_CORRSKEW ------
	#
	# Control-M Job Name: LDN-IDXEXO-SOD-Scenario-Spot-CORRSKEW 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_CORRSKEW
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_CORRSKEW = SSHOperator(
        task_id='JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_CORRSKEW',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.spot.LDN-INDEX-EXOTICS.SOD.CORRSKEW 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_STOCHVOL ------
	#
	# Control-M Job Name: LDN-IDXEXO-SOD-Scenario-Spot-STOCHVOL 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_STOCHVOL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_STOCHVOL = DummyOperator(
        task_id='JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_STOCHVOL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_PRICE ------
	#
	# Control-M Job Name: LDN-IDXEXO-SOD-Scenario-Spot-PRICE 	-->	 Airflow Job Name: JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_PRICE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_PRICE = SSHOperator(
        task_id='JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_PRICE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/scenario.spot.LDN-INDEX-EXOTICS.SOD.PRICE 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`' 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_COMBINE_SUCCESSEMAIL ------
	#
	# Control-M Job Name: LDN-EXO-EOD-Combine-SuccessEmail 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_COMBINE_SUCCESSEMAIL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_COMBINE_SUCCESSEMAIL = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_COMBINE_SUCCESSEMAIL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/mail_report.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NU_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL ------
	#
	# Control-M Job Name: NU-LDN-SSEXO-EOD-Scenario-DivSpotVol 	-->	 Airflow Job Name: JOB_NU_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NU_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL = DummyOperator(
        task_id='JOB_NU_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL ------
	#
	# Control-M Job Name: LDN-IND-EXO-Scenario-Spot-Vol 	-->	 Airflow Job Name: JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL = DummyOperator(
        task_id='JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RESTART_RS_SS_LDN_EXO_RT ------
	#
	# Control-M Job Name: Restart-RS-SS-LDN-EXO-RT 	-->	 Airflow Job Name: JOB_RESTART_RS_SS_LDN_EXO_RT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RESTART_RS_SS_LDN_EXO_RT = SSHOperator(
        task_id='JOB_RESTART_RS_SS_LDN_EXO_RT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-RT.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_START_RS_SS_LDN_EXO_RT ------
	#
	# Control-M Job Name: start-RS-SS-LDN-EXO-RT 	-->	 Airflow Job Name: JOB_START_RS_SS_LDN_EXO_RT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_START_RS_SS_LDN_EXO_RT = SSHOperator(
        task_id='JOB_START_RS_SS_LDN_EXO_RT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-RT.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_ATT_0730AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-Att-0730AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_ATT_0730AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_ATT_0730AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_ATT_0730AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_INTRADAY_ATT_0930AM ------
	#
	# Control-M Job Name: LDN-SSEXO-Intraday-Att-0930AM 	-->	 Airflow Job Name: JOB_LDN_SSEXO_INTRADAY_ATT_0930AM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_INTRADAY_ATT_0930AM = SSHOperator(
        task_id='JOB_LDN_SSEXO_INTRADAY_ATT_0930AM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_INTRADAY_ATT_1635PM ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-Intraday-Att-1635PM 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_INTRADAY_ATT_1635PM
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_INTRADAY_ATT_1635PM = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_INTRADAY_ATT_1635PM',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod ldn/ssexoticsus/intraday-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_FABRIC_POD_LOGS_LDN_CLEANUP ------
	#
	# Control-M Job Name: Fabric-pod-logs-LDN-cleanup 	-->	 Airflow Job Name: JOB_FABRIC_POD_LOGS_LDN_CLEANUP
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_FABRIC_POD_LOGS_LDN_CLEANUP = SSHOperator(
        task_id='JOB_FABRIC_POD_LOGS_LDN_CLEANUP',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SSH 'cd /data/flowrisk/fabric && find . -name *log*.tar.gz -mmin +1200 -print -exec rm {} \; '",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_UK_SYNC_REFDB_KANNON ------
	#
	# Control-M Job Name: UK-SYNC-REFDB-KANNON 	-->	 Airflow Job Name: JOB_UK_SYNC_REFDB_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_UK_SYNC_REFDB_KANNON = SSHOperator(
        task_id='JOB_UK_SYNC_REFDB_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_SCRIPT",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_EU_SYNC_REFDB_KANNON ------
	#
	# Control-M Job Name: EU-SYNC-REFDB-KANNON 	-->	 Airflow Job Name: JOB_EU_SYNC_REFDB_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_EU_SYNC_REFDB_KANNON = SSHOperator(
        task_id='JOB_EU_SYNC_REFDB_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_SCRIPT",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-CORP-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk corp --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK ------
	#
	# Control-M Job Name: LDN-CORP-EOD-kannon-ratefixingrisk 	-->	 Airflow Job Name: JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK = SSHOperator(
        task_id='JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleRateFixing.sh --date %%FRDATE --region uk --desk corp-ratefixingrisk --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_IDX_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-IDX-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_IDX_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_IDX_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_IDX_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk idx --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_WASH_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-WASH-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_WASH_EOD_KANNON
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_WASH_EOD_KANNON = DummyOperator(
        task_id='JOB_LDN_WASH_EOD_KANNON',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_KANNON ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-kannon 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_KANNON = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk ssexoticsus --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK ------
	#
	# Control-M Job Name: NY-LDN-SSEXO-EOD-kannon-ratefixingrisk 	-->	 Airflow Job Name: JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK = SSHOperator(
        task_id='JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleRateFixing.sh --date %%FRDATE --region uk --desk ssexoticsus-ratefixingrisk --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_NY_LDN_EXO_EOD_KANNON ------
	#
	# Control-M Job Name: NY-LDN-EXO-EOD-kannon 	-->	 Airflow Job Name: JOB_NY_LDN_EXO_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_NY_LDN_EXO_EOD_KANNON = SSHOperator(
        task_id='JOB_NY_LDN_EXO_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk idxexoticsus --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk ssexotics --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK ------
	#
	# Control-M Job Name: LDN-SSEXO-EOD-kannon-ratefixingrisk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleRateFixing.sh --date %%FRDATE --region uk --desk ssexotics-ratefixingrisk --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-EXO-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_EXO_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_EXO_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk index_exotics --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-QIS-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleWithoutFRTB.sh --date %%FRDATE --region uk --desk qis --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK ------
	#
	# Control-M Job Name: LDN-QIS-EOD-kannon-ratefixingrisk 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleRateFixing.sh --date %%FRDATE --region uk --desk qis-ratefixingrisk --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_EOD_KANNON_FRTB ------
	#
	# Control-M Job Name: LDN-QIS-EOD-kannon-frtb 	-->	 Airflow Job Name: JOB_LDN_QIS_EOD_KANNON_FRTB
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_EOD_KANNON_FRTB = SSHOperator(
        task_id='JOB_LDN_QIS_EOD_KANNON_FRTB',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleFRTB.sh --date %%FRDATE --region uk --desk qis-saccr --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_KANNON ------
	#
	# Control-M Job Name: LDN-FIC-EOD-kannon 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_KANNON = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsule.sh --date %%FRDATE --region uk --desk fic --business Ged --nfs /data/flowrisk/prodldn/kannon/",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_MANUAL_UK_KANNON ------
	#
	# Control-M Job Name: MANUAL-UK-kannon 	-->	 Airflow Job Name: JOB_MANUAL_UK_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_MANUAL_UK_KANNON = SSHOperator(
        task_id='JOB_MANUAL_UK_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /data/flowriskuat/uatny2/kannon/run.kaapsule.manual.sh %%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_MANUAL_DE_KANNON ------
	#
	# Control-M Job Name: MANUAL-DE-kannon 	-->	 Airflow Job Name: JOB_MANUAL_DE_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_MANUAL_DE_KANNON = SSHOperator(
        task_id='JOB_MANUAL_DE_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /data/flowriskuat/uatny/kannon/run.kaapsule.manual.sh %%FRDATE",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_APAC_EOD_PORTCALC_GED_KANNON ------
	#
	# Control-M Job Name: APAC-EOD-PORTCALC-GED-kannon 	-->	 Airflow Job Name: JOB_APAC_EOD_PORTCALC_GED_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_APAC_EOD_PORTCALC_GED_KANNON = SSHOperator(
        task_id='JOB_APAC_EOD_PORTCALC_GED_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsulePortCalc.sh --date %%FRDATE --region apac --desk all --business Ged",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_EU_EOD_PORTCALC_GED_KANNON ------
	#
	# Control-M Job Name: EU-EOD-PORTCALC-GED-kannon 	-->	 Airflow Job Name: JOB_EU_EOD_PORTCALC_GED_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_EU_EOD_PORTCALC_GED_KANNON = SSHOperator(
        task_id='JOB_EU_EOD_PORTCALC_GED_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsulePortCalc.sh --date %%FRDATE --region eu --desk all --business Ged",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_UK_EOD_PORTCALC_GED_KANNON ------
	#
	# Control-M Job Name: UK-EOD-PORTCALC-GED-kannon 	-->	 Airflow Job Name: JOB_UK_EOD_PORTCALC_GED_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_UK_EOD_PORTCALC_GED_KANNON = SSHOperator(
        task_id='JOB_UK_EOD_PORTCALC_GED_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsulePortCalc.sh --date %%FRDATE --region uk --desk all --business Ged",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_UK_EOD_PORTCALC_GPF_KANNON ------
	#
	# Control-M Job Name: UK-EOD-PORTCALC-GPF-kannon 	-->	 Airflow Job Name: JOB_UK_EOD_PORTCALC_GPF_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_UK_EOD_PORTCALC_GPF_KANNON = SSHOperator(
        task_id='JOB_UK_EOD_PORTCALC_GPF_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsulePortCalc.sh --date %%FRDATE --region uk --desk all --business Gpf",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_US_EOD_PORTCALC_GED_KANNON ------
	#
	# Control-M Job Name: US-EOD-PORTCALC-GED-kannon 	-->	 Airflow Job Name: JOB_US_EOD_PORTCALC_GED_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_US_EOD_PORTCALC_GED_KANNON = SSHOperator(
        task_id='JOB_US_EOD_PORTCALC_GED_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsulePortCalc.sh --date %%FRDATE --region us --desk all --business Ged",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_SFTP_KANNON ------
	#
	# Control-M Job Name: SFTP-kannon 	-->	 Airflow Job Name: JOB_SFTP_KANNON
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_SFTP_KANNON = SSHOperator(
        task_id='JOB_SFTP_KANNON',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%KANNONSERVER /apps/flowrisk/prodldn/kannon/runKaapsuleSFTPKeys.sh --date %%FRDATE --region us eu uk apac",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_SENS_UK_NFS ------
	#
	# Control-M Job Name: LDN-Hubble-Sens-UK-nfs 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_SENS_UK_NFS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_SENS_UK_NFS = SSHOperator(
        task_id='JOB_LDN_HUBBLE_SENS_UK_NFS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnSensUkNfs controlFile=/data/flowrisk/common/hubble.ldn.sens.uk-nfs.csv jarDate=%%FRDATE uploadDate=%%FRDATE uploadFolder=%%FRDATE/uk svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_SENS_MARKER ------
	#
	# Control-M Job Name: LDN-Hubble-Sens-Marker 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_SENS_MARKER
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_SENS_MARKER = SSHOperator(
        task_id='JOB_LDN_HUBBLE_SENS_MARKER',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnSensMarker uploadFolder=%%FRDATE/uk uploadMarker=sensetivities-done.txt svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_STRESS ------
	#
	# Control-M Job Name: LDN-Hubble-Stress 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_STRESS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_STRESS = SSHOperator(
        task_id='JOB_LDN_HUBBLE_STRESS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnStress controlFile=/data/flowrisk/common/hubble.ldn.stress.csv jarDate=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` uploadDate=`%%FR_SCRIPT_DIR/T-zero %%FRDATE` uploadFolder=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`/uk svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_STRESS_MARKER ------
	#
	# Control-M Job Name: LDN-Hubble-Stress-Marker 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_STRESS_MARKER
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_STRESS_MARKER = SSHOperator(
        task_id='JOB_LDN_HUBBLE_STRESS_MARKER',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnStressMarker uploadFolder=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`/uk uploadMarker=stress-done.txt svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_STRESS_WEEKLY ------
	#
	# Control-M Job Name: LDN-Hubble-Stress-Weekly 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_STRESS_WEEKLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_STRESS_WEEKLY = SSHOperator(
        task_id='JOB_LDN_HUBBLE_STRESS_WEEKLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnStressWeekly controlFile=/data/flowrisk/common/hubble.ldn.stress.weekly.csv jarDate=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE` uploadDate=`%%FR_SCRIPT_DIR/T-zero %%FRDATE` uploadFolder=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`/uk svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_HUBBLE_STRESS_WEEKLY_MARKER ------
	#
	# Control-M Job Name: LDN-Hubble-Stress-Weekly-Marker 	-->	 Airflow Job Name: JOB_LDN_HUBBLE_STRESS_WEEKLY_MARKER
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_HUBBLE_STRESS_WEEKLY_MARKER = SSHOperator(
        task_id='JOB_LDN_HUBBLE_STRESS_WEEKLY_MARKER',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_util.sh ldn.eod.idxexo.prod com.db.ged.report.client.copyreport.HubbleUpload -Dlog4j.logFileName=hubbleLdnStressWeeklyMarker uploadFolder=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`/uk uploadMarker=stress-weekly-done.txt svc_flowrisk_prod@sftpgateway.uk.db.com:/svc_flowrisk_prod-hubble-1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_HUBBLE_MONDAYDUMMY ------
	#
	# Control-M Job Name: Hubble-MondayDummy 	-->	 Airflow Job Name: JOB_HUBBLE_MONDAYDUMMY
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_HUBBLE_MONDAYDUMMY = DummyOperator(
        task_id='JOB_HUBBLE_MONDAYDUMMY',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RESTART_RS_SS_LDN_EXO_RT1 ------
	#
	# Control-M Job Name: Restart-RS-SS-LDN-EXO-RT1 	-->	 Airflow Job Name: JOB_RESTART_RS_SS_LDN_EXO_RT1
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RESTART_RS_SS_LDN_EXO_RT1 = SSHOperator(
        task_id='JOB_RESTART_RS_SS_LDN_EXO_RT1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-RT1.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RESTART_RS_SS_LDN_EXO_RT2 ------
	#
	# Control-M Job Name: Restart-RS-SS-LDN-EXO-RT2 	-->	 Airflow Job Name: JOB_RESTART_RS_SS_LDN_EXO_RT2
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RESTART_RS_SS_LDN_EXO_RT2 = SSHOperator(
        task_id='JOB_RESTART_RS_SS_LDN_EXO_RT2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-RT2.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RESTART_RS_SS_LDN_EXO_ORCH ------
	#
	# Control-M Job Name: Restart-RS-SS-LDN-EXO-ORCH 	-->	 Airflow Job Name: JOB_RESTART_RS_SS_LDN_EXO_ORCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RESTART_RS_SS_LDN_EXO_ORCH = SSHOperator(
        task_id='JOB_RESTART_RS_SS_LDN_EXO_ORCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-ORCH.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_RESTART_RS_SS_LDN_EXO_ORCH ------
	#
	# Control-M Job Name: restart-RS-SS-LDN-EXO-ORCH 	-->	 Airflow Job Name: JOB_RESTART_RS_SS_LDN_EXO_ORCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_RESTART_RS_SS_LDN_EXO_ORCH = SSHOperator(
        task_id='JOB_RESTART_RS_SS_LDN_EXO_ORCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/restart-RS-SS-LDN-EXO-ORCH.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_COMBINE_LDN_QIS_EOD ------
	#
	# Control-M Job Name: Copy-Combine-LDN-QIS-EOD 	-->	 Airflow Job Name: JOB_COPY_COMBINE_LDN_QIS_EOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_COMBINE_LDN_QIS_EOD = SSHOperator(
        task_id='JOB_COPY_COMBINE_LDN_QIS_EOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_COMBINE_NY_LDN_EXO_EOD ------
	#
	# Control-M Job Name: Copy-Combine-NY-LDN-EXO-EOD 	-->	 Airflow Job Name: JOB_COPY_COMBINE_NY_LDN_EXO_EOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_COMBINE_NY_LDN_EXO_EOD = SSHOperator(
        task_id='JOB_COPY_COMBINE_NY_LDN_EXO_EOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod -copy ldn/qisus/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_COMBINE_LDN_SSEXO_EOD ------
	#
	# Control-M Job Name: Copy-Combine-LDN-SSEXO-EOD 	-->	 Airflow Job Name: JOB_COPY_COMBINE_LDN_SSEXO_EOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_COMBINE_LDN_SSEXO_EOD = SSHOperator(
        task_id='JOB_COPY_COMBINE_LDN_SSEXO_EOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_COMBINE_NY_LDN_SSEXO_EOD ------
	#
	# Control-M Job Name: Copy-Combine-NY-LDN-SSEXO-EOD 	-->	 Airflow Job Name: JOB_COPY_COMBINE_NY_LDN_SSEXO_EOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_COMBINE_NY_LDN_SSEXO_EOD = SSHOperator(
        task_id='JOB_COPY_COMBINE_NY_LDN_SSEXO_EOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.ny.prod -copy ldn/ssexoticsus/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_QIS_SPOT_SCENARIO_DAILY ------
	#
	# Control-M Job Name: LDN-EXO-QIS-Spot-Scenario-Daily 	-->	 Airflow Job Name: JOB_LDN_EXO_QIS_SPOT_SCENARIO_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_QIS_SPOT_SCENARIO_DAILY = SSHOperator(
        task_id='JOB_LDN_EXO_QIS_SPOT_SCENARIO_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-piv-tw.DAILY.LDN.QIS.SOD 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_DISCONTINUITY ------
	#
	# Control-M Job Name: LDN-QIS-Discontinuity 	-->	 Airflow Job Name: JOB_LDN_QIS_DISCONTINUITY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_DISCONTINUITY = SSHOperator(
        task_id='JOB_LDN_QIS_DISCONTINUITY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-discontinuity 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_EXO_QIS_SPOT_SCENARIO_WEEKLY ------
	#
	# Control-M Job Name: LDN-EXO-QIS-Spot-Scenario-Weekly 	-->	 Airflow Job Name: JOB_LDN_EXO_QIS_SPOT_SCENARIO_WEEKLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_EXO_QIS_SPOT_SCENARIO_WEEKLY = SSHOperator(
        task_id='JOB_LDN_EXO_QIS_SPOT_SCENARIO_WEEKLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.MRM.spot-piv-tw.LDN.QIS.SOD.WEEKLY 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_SPOT_SCENARIO ------
	#
	# Control-M Job Name: LDN-QIS-Spot-Scenario 	-->	 Airflow Job Name: JOB_LDN_QIS_SPOT_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_SPOT_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QIS_SPOT_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/scenario.spot.LDN.QIS.SOD 'date2=`%%FR_SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_PREBATCH_STOP_EOD_RS ------
	#
	# Control-M Job Name: LDN-FIC-EOD-PREBATCH-STOP-EOD-RS 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_PREBATCH_STOP_EOD_RS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_PREBATCH_STOP_EOD_RS = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_PREBATCH_STOP_EOD_RS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%LDNFICEOD %%SCRIPT_DIR/stop_RS_EOD.sh ldn.eod.fic.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_PREBATCH_START_EOD_RS ------
	#
	# Control-M Job Name: LDN-FIC-EOD-PREBATCH-START-EOD-RS 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_PREBATCH_START_EOD_RS
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_PREBATCH_START_EOD_RS = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_PREBATCH_START_EOD_RS',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%LDNFICEOD %%SCRIPT_DIR/start_RS_EOD.sh ldn.eod.fic.prod1",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_COMBINED ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Combined 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_COMBINED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_COMBINED = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_COMBINED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_COMBINED ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-Combined 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_COMBINED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_COMBINED = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_COMBINED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-combined 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_ATT ------
	#
	# Control-M Job Name: LDN-FIC-Att 	-->	 Airflow Job Name: JOB_LDN_FIC_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_ATT = SSHOperator(
        task_id='JOB_LDN_FIC_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_ATT ------
	#
	# Control-M Job Name: Copy-LDN-FIC-Att 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_ATT = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-att 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: LDN-FIC-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-ipv-att-modelswitch 'date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_IPV_MODELSWITCH ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-IPV-ModelSwitch 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_IPV_MODELSWITCH
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_IPV_MODELSWITCH = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_IPV_MODELSWITCH',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-ipv-att-modelswitch 'date=`%%FR_SCRIPT_DIR/PreviousMonthEnd`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_STATIC ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Static 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_STATIC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_STATIC = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_STATIC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-static-data 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_PERSIST_RISKPNL ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Persist-RiskPnl 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_PERSIST_RISKPNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_PERSIST_RISKPNL = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_PERSIST_RISKPNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/jar-to-grimis-riskpnl 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_ATT_PERSIST ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Att-Persist 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_ATT_PERSIST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_ATT_PERSIST = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_ATT_PERSIST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/jar-to-grimis-att 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_TOD ------
	#
	# Control-M Job Name: LDN-FIC-EOD-TOD 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_TOD = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_TOD ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-TOD 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_TOD
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_TOD = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_TOD',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-tradesOnDay 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_NOTIFY_RISK ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Notify-Risk 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_NOTIFY_RISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_NOTIFY_RISK = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_NOTIFY_RISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod mis3-notification 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`' 'portfolio=LD.FIC' 'jobType=Risk'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_NOTIFY_PNL ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Notify-Pnl 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_NOTIFY_PNL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_NOTIFY_PNL = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_NOTIFY_PNL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod mis3-notification 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`' 'portfolio=LD.FIC' 'jobType=Pnl'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_NOTIFY_ATT ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Notify-Att 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_NOTIFY_ATT
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_NOTIFY_ATT = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_NOTIFY_ATT',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod mis3-notification 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`' 'portfolio=LD.FIC' 'jobType=Att'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_MCC ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Mcc 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_MCC = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_MCC ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-Mcc 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_MCC
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_MCC = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_MCC',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-mcc 'date1=`%%FR_SCRIPT_DIR/T-minus-1 %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_PERSIST_DBAX ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Persist-Dbax 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_PERSIST_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_PERSIST_DBAX = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_PERSIST_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-latest-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_PERSIST_DBAX ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-Persist-Dbax 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_PERSIST_DBAX
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_PERSIST_DBAX = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_PERSIST_DBAX',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-latest-position-and-dbax-dated 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_MODELINFO ------
	#
	# Control-M Job Name: LDN-FIC-EOD-Modelinfo 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_MODELINFO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_MODELINFO = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_MODELINFO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/modelinfo mode=anyrule 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_RATEFIXING ------
	#
	# Control-M Job Name: LDN-FIC-EOD-RateFixing 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_RATEFIXING ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-RateFixing 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_RATEFIXING
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_RATEFIXING = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_RATEFIXING',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-rate-fixing-risk 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: LDN-FIC-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_IPV_DAILY ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-IPV-Daily 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_IPV_DAILY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_IPV_DAILY = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_IPV_DAILY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-ipv-att-daily 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_IPV_MONTHLY ------
	#
	# Control-M Job Name: LDN-FIC-EOD-IPV-Monthly 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_IPV_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_IPV_MONTHLY = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_IPV_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_IPV_MONTHLY ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-IPV-Monthly 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_IPV_MONTHLY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_IPV_MONTHLY = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_IPV_MONTHLY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/runCmdForFirstDays.sh `%%FR_SCRIPT_DIR/T-Zero %%FRDATE` '%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-ipv-att-monthly date=`'%%FR_SCRIPT_DIR/PreviousMonthEnd'`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_PVMANIFEST ------
	#
	# Control-M Job Name: LDN-FIC-EOD-PVManifest 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_PVMANIFEST
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_PVMANIFEST = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_PVMANIFEST',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/pvmanifest 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_IPV_SEED ------
	#
	# Control-M Job Name: LDN-FIC-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_IPV_SEED ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-IPV-Seed 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_IPV_SEED
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_IPV_SEED = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_IPV_SEED',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-ipv-att-numerical-limitation 'date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_EOD_FAIRVALUE ------
	#
	# Control-M Job Name: LDN-FIC-EOD-FairValue 	-->	 Airflow Job Name: JOB_LDN_FIC_EOD_FAIRVALUE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_EOD_FAIRVALUE = SSHOperator(
        task_id='JOB_LDN_FIC_EOD_FAIRVALUE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-fair-value-modelswitch date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_EOD_FAIRVALUECOPY ------
	#
	# Control-M Job Name: Copy-LDN-FIC-EOD-FairValueCopy 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_EOD_FAIRVALUECOPY
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_EOD_FAIRVALUECOPY = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_EOD_FAIRVALUECOPY',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-fair-value-modelswitch date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNFICJARTOGRIMISYE ------
	#
	# Control-M Job Name: LdnFicJarToGrimisYE 	-->	 Airflow Job Name: JOB_LDNFICJARTOGRIMISYE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNFICJARTOGRIMISYE = SSHOperator(
        task_id='JOB_LDNFICJARTOGRIMISYE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/jar-to-grimis-ye 'date=`%%FR_SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_SACCR_NOTIONAL ------
	#
	# Control-M Job Name: LDN-QIS-SACCR-Notional 	-->	 Airflow Job Name: JOB_LDN_QIS_SACCR_NOTIONAL
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_SACCR_NOTIONAL = SSHOperator(
        task_id='JOB_LDN_QIS_SACCR_NOTIONAL',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-saccr 'date1=`%%FR_SCRIPT_DIR/T-minus-1-previous %%FRDATE`' 'date2=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QISNY_LUMRISK_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QISNY-LumRisk-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QISNY_LUMRISK_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QISNY_LUMRISK_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QISNY_LUMRISK_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/scenario.stress.lumRisk.QISNY 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QISNY_PST_SBETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QISNY-PST-SBeta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QISNY_PST_SBETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QISNY_PST_SBETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QISNY_PST_SBETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/scenario.stress.pst-sbeta.QISNY 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QISNY_PST_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QISNY-PST-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QISNY_PST_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QISNY_PST_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QISNY_PST_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/scenario.stress.pst-beta.QISNY 'date2=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`' 'date1=`%%SCRIPT_DIR/T-zero %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QISNY_COMBINED_BETA_SCENARIO ------
	#
	# Control-M Job Name: LDN-QISNY-Combined-Beta-Scenario 	-->	 Airflow Job Name: JOB_LDN_QISNY_COMBINED_BETA_SCENARIO
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QISNY_COMBINED_BETA_SCENARIO = SSHOperator(
        task_id='JOB_LDN_QISNY_COMBINED_BETA_SCENARIO',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/qisus/ScenarioStressBetaMerge-QISNY 'date=`%%SCRIPT_DIR/T-plus-1 %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_UPDATE_FUSE_FUNDINGNAME_CACHE ------
	#
	# Control-M Job Name: Update-Fuse-FundingName-Cache 	-->	 Airflow Job Name: JOB_UPDATE_FUSE_FUNDINGNAME_CACHE
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_UPDATE_FUSE_FUNDINGNAME_CACHE = SSHOperator(
        task_id='JOB_UPDATE_FUSE_FUNDINGNAME_CACHE',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/updateFuseFundingNameCache.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNQISFIXINGRERUN ------
	#
	# Control-M Job Name: LdnQisFixingRerun 	-->	 Airflow Job Name: JOB_LDNQISFIXINGRERUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNQISFIXINGRERUN = SSHOperator(
        task_id='JOB_LDNQISFIXINGRERUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/qis-fixing-rerun 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDNQISUSFIXINGRERUN ------
	#
	# Control-M Job Name: LdnQisUSFixingRerun 	-->	 Airflow Job Name: JOB_LDNQISUSFIXINGRERUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDNQISUSFIXINGRERUN = SSHOperator(
        task_id='JOB_LDNQISUSFIXINGRERUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.ny.prod ldn/idxexotics/qis-us-fixing-rerun 'date=`%%FR_SCRIPT_DIR/T-zero-previous %%FRDATE`'",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_ADHOCSCRIPTRUN ------
	#
	# Control-M Job Name: AdhocScriptRun 	-->	 Airflow Job Name: JOB_ADHOCSCRIPTRUN
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_ADHOCSCRIPTRUN = SSHOperator(
        task_id='JOB_ADHOCSCRIPTRUN',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%RUN_REPORT %%FR_SCRIPT_DIR/adhocScript.sh",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_SLA_TEST_NY_COMBINED ------
	#
	# Control-M Job Name: SLA-Test-Ny-Combined 	-->	 Airflow Job Name: JOB_SLA_TEST_NY_COMBINED
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_SLA_TEST_NY_COMBINED = DummyOperator(
        task_id='JOB_SLA_TEST_NY_COMBINED',
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_CORP_FVARISK ------
	#
	# Control-M Job Name: Ldn-Corp-FVARisk 	-->	 Airflow Job Name: JOB_LDN_CORP_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_CORP_FVARISK = SSHOperator(
        task_id='JOB_LDN_CORP_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod ldn/corp/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_CORP_FVARISK ------
	#
	# Control-M Job Name: Copy-Ldn-Corp-FVARisk 	-->	 Airflow Job Name: JOB_COPY_LDN_CORP_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_CORP_FVARISK = SSHOperator(
        task_id='JOB_COPY_LDN_CORP_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.corp.prod -copy ldn/corp/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_FIC_FVARISK ------
	#
	# Control-M Job Name: Ldn-FIC-FVARisk 	-->	 Airflow Job Name: JOB_LDN_FIC_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_FIC_FVARISK = SSHOperator(
        task_id='JOB_LDN_FIC_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod ldn/fic/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_FIC_FVARISK ------
	#
	# Control-M Job Name: Copy-Ldn-FIC-FVARisk 	-->	 Airflow Job Name: JOB_COPY_LDN_FIC_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_FIC_FVARISK = SSHOperator(
        task_id='JOB_COPY_LDN_FIC_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.fic.prod -copy ldn/fic/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_QIS_FVARISK ------
	#
	# Control-M Job Name: Ldn-QIS-FVARisk 	-->	 Airflow Job Name: JOB_LDN_QIS_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_QIS_FVARISK = SSHOperator(
        task_id='JOB_LDN_QIS_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod ldn/qis/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_QIS_FVARISK ------
	#
	# Control-M Job Name: Copy-Ldn-QIS-FVARisk 	-->	 Airflow Job Name: JOB_COPY_LDN_QIS_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_QIS_FVARISK = SSHOperator(
        task_id='JOB_COPY_LDN_QIS_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.idxexo.prod -copy ldn/qis/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_LDN_SSEXO_FVARISK ------
	#
	# Control-M Job Name: LDN-SSEXO-FVARisk 	-->	 Airflow Job Name: JOB_LDN_SSEXO_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_LDN_SSEXO_FVARISK = SSHOperator(
        task_id='JOB_LDN_SSEXO_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod ldn/ssexotics/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_COPY_LDN_SSEXO_FVARISK ------
	#
	# Control-M Job Name: Copy-LDN-SSEXO-FVARisk 	-->	 Airflow Job Name: JOB_COPY_LDN_SSEXO_FVARISK
	# Control-M Job Type: Command 	-->	  Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_COPY_LDN_SSEXO_FVARISK = SSHOperator(
        task_id='JOB_COPY_LDN_SSEXO_FVARISK',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="%%FR_SCRIPT_DIR/run_report.sh ldn.eod.ssexo.prod -copy ldn/ssexotics/t0-funding-valuation-adj-risk date=`%%FR_SCRIPT_DIR/T-Zero %%FRDATE`",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_SLA_LDN_QIS_EOD_COMBINED ------
	#
	# Control-M Job Name: SLA-LDN-QIS-EOD-Combined 	-->	 Airflow Job Name: JOB_SLA_LDN_QIS_EOD_COMBINED
	# Control-M Job Type: Dummy 	-->	  Airflow Operator Type: DummyOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_SLA_LDN_QIS_EOD_COMBINED = DummyOperator(
        task_id='JOB_SLA_LDN_QIS_EOD_COMBINED',
        dag=dag
    )


# Task Dependencies


    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_RS_INTRADAY_PNL_CPY_1]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPDBRSSPOTEODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPSPOTPIVTWSODDAILYPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD2, JOB_LDNCORPSPOTPIVTWSODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPDBRSSPOTPIVTWEODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNSPOTVOLPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXDBRSSPOTEODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXSPOTPIVTWSODDAILYPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD2, JOB_LDNIDXSPOTPIVTWSODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXDBRSSPOTPIVTWEODPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNSPOTVOLPROD2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNT0POSSIGNOFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_DBP_REPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_SA_EOD_DBP_REPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_BOOK_TABLE_UPDATE, JOB_LDN_GPF_BOOK_TABLE_UPDATE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_BOOK_TABLE_UPDATE, JOB_LDN_GPF_BOOK_TABLE_UPDATE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_COPY_DBAX, JOB_LDNCORPEODMODELINFO, JOB_LDN_EOD_COPY_DBAX, JOB_LDN_CORP_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_FR_EOD_T0_POS_SIGNOFF_CHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNIDXRISKPNLPILOTRECON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_PNL_LATEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KICKOFF, JOB_LDN_EOD_KICKOFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_PNL_LATEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_FLOW_EOD_ERROR_CHECKS, JOB_LDN_CORP_EOD_KANNON, JOB_LDN_CORP_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_PERSIST_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_PERSIST_DBAX, JOB_LDN_CORP_COPY_TOD_OLD, JOB_LDN_CORP_EOD_COPY_TOD, JOB_LDN_CORP_EOD_COPY_ALL_REPORTS, JOB_LDNLEGACYEODCOPYXCCYADJREPORTNARROW]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KANNON_STATIC, JOB_LDNIDXMIS3NOTIFICATIONRISK, JOB_LDNCORPMIS3NOTIFICATIONATT, JOB_LDNIDXMIS3NOTIFICATIONATT, JOB_LDNCORPMIS3NOTIFICATIONRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNIDXRISKPNLPILOT, JOB_LNCORPRISKPNLPILOT, JOB_LDN_EOD_CORP_RS_RESTART_PROD2, JOB_LDN_EOD_IDX_RS_RESTART_PROD2, JOB_LDN_EOD_OD_RS_RESTART_PROD2, JOB_LDN_EOD_SS_RS_RESTART_PROD2, JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXMIS3NOTIFICATIONPNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNIDXRISKPNLPILOT, JOB_LDN_EOD_RAG_STATUS_REPORT, JOB_LNCORPRISKPNLPILOT, JOB_LDN_EOD_CORP_RS_RESTART_PROD2, JOB_LDN_EOD_IDX_RS_RESTART_PROD2, JOB_LDN_EOD_OD_RS_RESTART_PROD2, JOB_LDN_EOD_SS_RS_RESTART_PROD2, JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_RATEFIXING]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_RATEFIXING, JOB_LDN_EOD_MODELNFO_DQEMAIL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_PERSIST_ATT, JOB_LDN_HUBBLE_SENS_UK_NFS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXEODCOPYTRADESONDAYREPORT, JOB_LDN_IDX_EOD_PERSIST_DBAX]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_COPY_ALL_REPORTS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNIDXRISKPNLPILOT, JOB_LNCORPRISKPNLPILOT, JOB_LDN_EOD_CORP_RS_RESTART_PROD2, JOB_LDN_EOD_IDX_RS_RESTART_PROD2, JOB_LDN_EOD_OD_RS_RESTART_PROD2, JOB_LDN_EOD_SS_RS_RESTART_PROD2, JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXEODMODELINFO, JOB_LDN_EOD_COPY_DBAX, JOB_LDN_IDX_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_YE_BS_DUMMY, JOB_LDN_EOD_YE_BS, JOB_LDN_EOD_YE_BS_GPF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_YE_BS_DUMMY, JOB_LDN_EOD_YE_BS, JOB_LDN_EOD_YE_BS_GPF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_YE_BS2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KICKOFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KICKOFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_FLOW_EOD_ERROR_CHECKS, JOB_LDN_IDX_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_MODELNFO_DQEMAIL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNCORPRISKPNLPILOTRECON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPRISKPNLPILOTCOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LNIDXRISKPNLPILOTCOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_IDX_RS_RESTART_PROD1]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_CORP_RS_RESTART_PROD1]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPMIS3NOTIFICATIONPNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPMIS3NOTIFICATIONRISK, JOB_LDN_CORP_EOD_PERSIST_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPMIS3NOTIFICATIONATT, JOB_LDN_CORP_EOD_PERSIST_SOD, JOB_LDN_CORP_EOD_PERSIST_YE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_TOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXMIS3NOTIFICATIONRISK, JOB_LDN_IDX_EOD_PERSIST_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXMIS3NOTIFICATIONATT, JOB_LDN_IDX_EOD_PERSIST_SOD, JOB_LDN_IDX_EOD_PERSIST_YE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXEODTRADESONDAYREPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPCOPYRPICOMREPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXCOPYRPICOMREPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_EUS_REPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_GRIMIS_ADDUP]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_EUS_YEBS_DUMMY, JOB_LDN_EOD_YE_ADDUP]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KICKOFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_EUS_YE_BS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_EUS_YE_BS2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_KICKOFF, JOB_LDN_EOD_YE_BSMERGE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_YE_COPY_FRPYPL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_RS_DB_LUX_INTRADAY_PNL, JOB_LDN_IDX_GET_FUTURE_PRICE, JOB_LDNIDXPOPULATEGRIMISEODCACHE, JOB_LDNCORPPOPULATEGRIMISEODCACHE, JOB_LDNCORPRPICOMREPORT, JOB_LDN_EOD_STATICDATA, JOB_LDNIDXRPICOMREPORT, JOB_LDN_EOD_OD_RS_RESTART_PROD2, JOB_LDN_EOD_IDX_RS_RESTART_PROD2, JOB_LDN_EOD_CORP_RS_RESTART_PROD2, JOB_LDN_EOD_CORP_RS_RESTART_PROD1, JOB_LDN_EOD_IDX_RS_RESTART_PROD1, JOB_LDN_QIS_EOD_KICK_OFF, JOB_LDN_SSEXO_EOD_KICK_OFF, JOB_LDN_EXO_EOD_RS_STOP_PROD_EUS, JOB_LDN_SSEXO_EOD_RS_STOP_PROD_EUS, JOB_LDN_FIC_EOD_PREBATCH_STOP_EOD_RS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXCOPYMCCREPORT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPCOPYMCCREPORT, JOB_LDN_ECM_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_ECM_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXGRIMISATT, JOB_LDN_IDX_EOD_RISK_IPV_MODELSWITCH, JOB_LDN_IDX_EOD_PERSIST_RISK, JOB_LDN_IDX_EOD_COPY_XCCY_ADJ_REPORT, JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPGRIMISATT, JOB_LDN_CORP_EOD_RISK_IPV_MODELSWITCH, JOB_LDN_CORP_EOD_PERSIST_RISK, JOB_LDN_CORP_EOD_COPY_XCCY_ADJ_REPORT, JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT, JOB_LDN_HUBBLE_SENS_UK_NFS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPCOPYSOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXCOPYSOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_CORP_RS_STOP_PROD1_PILOT, JOB_LDN_EOD_IDX_RS_STOP_PROD1_PILOT, JOB_LDN_EXO_EOD_RS_STOP_PROD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_VS_START_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_IDX_RS_START_PROD1_PILOT, JOB_LDN_EOD_CORP_RS_START_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_DBA_UPGRADE_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_VS_START_PROD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_RS_START_PROD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_VS_STOP_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EOD_VS_STOP_PROD1_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_VS_STOP_PROD_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKSNAP_LDN_COPY_GPFAIT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKSNAP_LDN_COPY_GPFDEVEUR]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKPROFILE_LDN_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKPROFILE_LDN_GPF_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDN_GPF_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKMERGELDNGEDLEGACY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISKMERGELDNGEDLEGACY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYRISK_LDNGEDLEGACY_BREACHCHECK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_DEVEUR_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHERETF_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHEREMSS_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHERWASH_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHERB2BSYD_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHERINVTRADING_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_OTHERSEF_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_INTRADAYFLASHSNAP_LDN_AIT_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_DAILY_HOUSEKEEPING_LONDON_SERVERS_NFS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_PNL, JOB_LDN_QIS_EOD_STATIC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_FAIRVALUE, JOB_LDN_QIS_EOD_PNL_ERROR_CHECKS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_FAIRVALUE, JOB_NY_LDN_EXO_EOD_DBAX, JOB_NY_LDN_EXO_EOD_PNL_ERROR_CHECKS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_NOTIFY_RISK, JOB_LDN_QIS_EOD_NOTIFY_PNL, JOB_LDN_QIS_EOD_NOTIFY_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_NOTIFY_RISK, JOB_NY_LDN_EXO_EOD_NOTIFY_PNL, JOB_NY_LDN_EXO_EOD_NOTIFY_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS, JOB_LDN_QIS_EOD_KANNON, JOB_COPY_COMBINE_LDN_QIS_EOD, JOB_LDN_QIS_SACCR_NOTIONAL, JOB_UPDATE_FUSE_FUNDINGNAME_CACHE, JOB_LDN_QIS_FVARISK, JOB_SLA_LDN_QIS_EOD_COMBINED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_IDX_RT1_RS_START_PROD, JOB_LDN_EXO_IDX_RT2_RS_START_PROD, JOB_NY_LDN_EXO_EOD_RISK_PNL_ERROR_CHECKS, JOB_NY_LDN_EXO_EOD_KANNON, JOB_COPY_COMBINE_NY_LDN_EXO_EOD, JOB_SLA_TEST_NY_COMBINED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_IPV_SEED, JOB_LDNQISJARTOGRIMISATT, JOB_LDN_EXO_QIS_SPOT_SCENARIO, JOB_LDN_QIS_SPOT_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDNEXOJARTOGRIMISATT, JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_MODEL_INFO, JOB_LDN_QIS_EOD_COPY_TOD, JOB_LDN_EXO_EOD_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_QIS_TOD, JOB_NY_LDN_EXO_EOD_COPY_TOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_QIS_COPY_TOD, JOB_NY_LDN_EXO_EOD_MODEL_INFO, JOB_NY_LDN_EXO_EOD_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_RATEFIXING]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_RATEFIXING]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COPY_DBAX, JOB_LDN_QIS_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_DBAX, JOB_NY_LDN_EXO_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COPY_IPV_DAILY, JOB_LDN_EXO_EOD_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_IPV_DAILY, JOB_NY_LDN_EXO_EOD_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_COPY_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_COPY_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_PNL, JOB_LDN_SSEXO_EOD_STATIC, JOB_LDN_WASH_EOD_KICK_OFF]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_FAIRVALUE, JOB_LDN_SSEXO_EOD_PNL_ERROR_CHECKS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_FAIRVALUE, JOB_NY_LDN_SSEXO_EOD_PNL_ERROR_CHECKS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_NOTIFY_ATT, JOB_LDN_IDXEXO_EOD_NOTIFY_ATT, JOB_LDN_SSEXO_EOD_NOTIFY_PNL, JOB_LDN_IDXEXO_EOD_NOTIFY_PNL, JOB_LDN_SSEXO_EOD_NOTIFY_RISK, JOB_LDN_IDXEXO_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT, JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL, JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS, JOB_LDN_SSEXO_EOD_KANNON, JOB_LDN_EXO_EOD_KANNON, JOB_COPY_COMBINE_LDN_SSEXO_EOD, JOB_LDN_SSEXO_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_RISK_PNL_ERROR_CHECKS, JOB_NY_LDN_SSEXO_EOD_KANNON, JOB_COPY_COMBINE_NY_LDN_SSEXO_EOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_MODEL_INFO, JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_TOD, JOB_LDNSSEXOJARTOGRIMISATT, JOB_LDN_EXO_EOD_SCENARIO_SPOT, JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_CORRSKEW, JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_PRICE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_TOD, JOB_NY_LDNSSEXOJARTOGRIMISATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_DBAX, JOB_LDN_IDXEXO_EOD_DBAX, JOB_LDN_SSEXO_EOD_IPV_SEED, JOB_LDN_SSEXO_EOD_PVMANIFEST, JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_COPY_DBAX, JOB_LDN_EXO_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_DBAX, JOB_NY_LDN_SSEXO_EOD_IPV_SEED, JOB_NY_LDN_SSEXO_EOD_PVMANIFEST, JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_IPV_DAILY, JOB_LDN_SSEXO_EOD_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_IPV_DAILY, JOB_NY_LDN_SSEXO_EOD_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_IPV_MONTHEND, JOB_LDN_IDXEXO_EOD_IPV_MONTHEND, JOB_LDN_WASH_EOD_IPV_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_COPY_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MONTHEND]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_MODEL_INFO, JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_RATEFIXING]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_TOD, JOB_LDN_SSEXO_EOD_DBAX, JOB_LDN_SSEXO_EOD_MODEL_INFO, JOB_LDN_IDXEXO_EOD_TOD, JOB_LDN_EXO_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_COPY_TOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_TOD, JOB_NY_LDN_SSEXO_EOD_DBAX, JOB_NY_LDN_SSEXO_EOD_MODEL_INFO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_RECON_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COPY_PILOT, JOB_LDN_QIS_EOD_DBAX_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_RISKPNL_PILOT, JOB_LDN_SSEXO_EOD_PILOT_RECON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_EMAIL_RISK_PNL_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_NOTIFY_RISK, JOB_LDN_QIS_PERSISTSOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_NOTIFY_RISK, JOB_LDN_IDXEXO_EOD_NOTIFY_RISK, JOB_LDN_SSEXO_PERSISTSOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_NOTIFY_PNL, JOB__LDNQISJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_NOTIFY_ATT, JOB_LDNQISJARTOGRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_NOTIFY_ATT, JOB_NYLDNIDXEXOJAR2GRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_NOTIFY_ATT, JOB_LDN_IDXEXO_EOD_NOTIFY_ATT, JOB_LDNSSEXOJARTOGRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_NOTIFY_ATT, JOB_NYLDNSSEXOJAR2GRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COMBINE, JOB__LDNQISJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COMBINE, JOB__LDNSSEXOJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_NOTIFY_PNL, JOB_LDN_IDXEXO_EOD_NOTIFY_PNL, JOB__LDNSSEXOJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_NOTIFY_PNL, JOB_LDN_IDXEXO_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COPY_MCC, JOB_NY_QIS_LDN_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_QIS_LDN_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_MCC, JOB_LDN_SSEXO_EOD_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_EOD_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_RECON_WEEKLY_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_EMAIL_RISK_PNL_WEEKLY_PILOT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_COPY_XCCY, JOB_LDN_QIS_EOD_DBAX, JOB_LDNQISJARTOGRIMISPNL, JOB__LDN_QIS_EOD_PNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_COMBINE, JOB_NY_LDN_EXO_EOD_COPY_XCCY, JOB_NY_LDNEXOJARTOGRIMISPNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_FAIRVALUE, JOB_LDN_QIS_EOD_ATT, JOB_LDN_QIS_EOD_TOD, JOB_LDN_QIS_EOD_RISKPNL_MERGE, JOB_LDN_EXO_EOD_IPV_MODELSWITCH, JOB_LDN_QIS_PERSISTRISK, JOB_LDN_EXO_EOD_COMBINE_SUCCESSEMAIL, JOB_LDN_EXO_EOD_CORRRISK_WEEKLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_FAIRVALUE, JOB_NY_LDN_EXO_EOD_ATT, JOB_NY_LDN_EXO_EOD_TOD, JOB_NY_LDN_EXO_EOD_IPV_MODELSWITCH, JOB_NY_LDN_EXO_PERSISTRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_COPY_XCCY, JOB_LDNSSEXOJARTOGRIMISPNL, JOB__LDN_SSEXO_EOD_PNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_COMBINE, JOB_NY_LDN_SSEXO_EOD_COPY_XCCY, JOB_NY_LDNSSEXOJARTOGRIMISPNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_FAIRVALUE, JOB_LDN_SSEXO_EOD_ATT, JOB_LDN_SSEXO_EOD_RISKPNL_MERGE, JOB_LDN_SSEXO_EOD_IPV_MODELSWITCH, JOB_LDN_SSEXO_PERSISTRISK, JOB_RESTART_RS_SS_LDN_EXO_RT, JOB_LDN_HUBBLE_SENS_UK_NFS, JOB_RESTART_RS_SS_LDN_EXO_RT1, JOB_RESTART_RS_SS_LDN_EXO_RT2, JOB_RESTART_RS_SS_LDN_EXO_ORCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_FAIRVALUE, JOB_NY_LDN_SSEXO_EOD_ATT, JOB_NY_LDN_SSEXO_EOD_IPV_MODELSWITCH, JOB_NY_LDN_SSEXO_PERSISTRISK, JOB_RESTART_RS_SS_LDN_EXO_RT, JOB_RESTART_RS_SS_LDN_EXO_RT1, JOB_RESTART_RS_SS_LDN_EXO_RT2, JOB_RESTART_RS_SS_LDN_EXO_ORCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY, JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE, JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY, JOB_NY_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNEXODBRSSPOTPIVTWEODDAILYPROD1, JOB_LDN_EXO_EOD_SCENARIO_DIV_SPOT, JOB_LDN_EXO_SPOTVOL_BASKETCONST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDNEXODBRSSPOTPIVTWEODDAILYPROD1, JOB_NY_LDN_EXO_EOD_SCENARIO_DIV_SPOT, JOB_NY_LDN_EXO_EOD_SCENARIO_GAP_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE, JOB_LDN_EXO_DISCONTINUITY, JOB_NY_LDN_EXO_DISCONTINUITY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY, JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY, JOB_NY_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO3707_SOD_SCENARIO_SPOT_VOL_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDNSSEXODBRSSPOTPIVTWEODDAILYPROD1, JOB_NY_LDN_SSEXO_EOD_SCENARIO_GAP_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNSSEXO3707DBRSSPOTPIVTWEODDAILYPROD1, JOB_LDN_WASHEXO_SOD_SCENARIO_SPOT_VOL_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNWASHEXODBRSSPOTPIVTWEODDAILYPROD1, JOB_LDN_SSEXO_EOD_SCENARIO_GAP_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_NU]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW, JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_FAST_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_SCENARIO_WEEKLY_SPOT_VOL_SLOW_DBRISKSTORE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_LUMRISK_BETA_SCENARIO, JOB_LDN_QIS_PST_SBETA_SCENARIO, JOB_LDN_QIS_PST_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QISNY_LUMRISK_BETA_SCENARIO, JOB_LDN_QISNY_PST_SBETA_SCENARIO, JOB_LDN_QISNY_PST_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_SPOTVOL_BASKETCONST, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_TERM_STRUCTURE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL, JOB_NU_LDN_SSEXO_EOD_SCENARIO_DIVSPOTVOL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_DISCONTINUITY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_DISCONTINUITY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_SIZE_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_SIZE_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_SIZE_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_EXO_SIZE_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_IPV_DAILY, JOB_LDN_EXO_EOD_IPV_MONTHEND, JOB_LDN_IDXEXO_GRIMIS_CACHE_8PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_RS_START_PROD_EUS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_GRIMIS_CACHE_16PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_RS_START_PRE_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_GRIMIS_CACHE_16PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_RS_START_PROD_EUS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HYBRID_INTRADAY_ATT_11AM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HYBRID_INTRADAY_ATT_17PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HYBRID_INTRADAY_ATT_17PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_INTRADAY_ATT_11AM, JOB_NY_LDN_SSEXO_INTRADAY_ATT_11AM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_11AM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_INTRADAY_COPY_PRIIPS_17PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COPY_XCCY, JOB_LDN_WASH_EOD_STATIC, JOB_LDN_WASH_EOD_FAIRVALUE, JOB_RUNLDNWASHJARTOGRIMISPNL, JOB_LDN_WASH_PNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_NOTIFY_PNL, JOB_LDN_WASH_EOD_NOTIFY_RISK, JOB_LDN_WASH_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_ATT, JOB_LDN_WASH_EOD_KANNON, JOB_LDN_WASH_EOD_COPY_COMBINED, JOB_LDN_WASH_PERSISTRISK, JOB_LDN_WASH_EOD_FAIRVALUE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_TOD, JOB_LDN_WASH_EOD_COPY_ATT, JOB_LDNWASHJARTOGRIMISATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_PERSISTSOD, JOB_LDN_WASH_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COPY_TOD, JOB_LDN_WASH_EOD_RATEFIXING, JOB_LDN_WASH_EOD_MODEL_INFO, JOB_LDN_WASH_EOD_DBAX]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_IPV_MONTHEND, JOB_LDN_WASH_EOD_COPY_IPV_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COPY_IPV_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COPY_DBAX, JOB_LDN_WASH_EOD_COMBINED_PILOT, JOB_LDN_WASH_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_NOTIFY_PNL, JOB_RUNLDNWASHJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_NOTIFY_RISK, JOB_LDNWASHJARTOGRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COMBINED, JOB_RUNLDNWASHJARTOGRIMISPNL2]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_WASH_EOD_COPY_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_IPV_DAILY_COPY, JOB_LDN_CORP_EOD_IPV_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_IPV_MONTHLY_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_IPV_DAILY_COPY, JOB_LDN_IDX_EOD_IPV_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_IPV_MONTHLY_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_IPV_SEED_VAR, JOB_LDN_IDX_EOD_IPV_SEED_VAR]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_IPV_SEED_VAR_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDX_EOD_IPV_SEED_VAR_COPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_11AM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_INTRADAY_COPY_PRIIPS_17PM]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPDBRSSPOTEODPROD1, JOB_LDN_CORP_SPOTVOL_DAILY, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNSPOTVOLPROD1, JOB_LDN_HUBBLE_STRESS_WEEKLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNSPOTVOLPROD1, JOB_LDN_HUBBLE_STRESS_WEEKLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXDBRSSPOTEODPROD1, JOB_LDNIDXSPOTPIVTWSODDAILYPROD1, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNCORPDBRSSPOTPIVTWEODDAILYPROD1, JOB_LDN_CORP_GAP_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_SPOTVOL, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXDBRSSPOTPIVTWEODDAILYPROD1, JOB_LDN_IDX_GAP_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDNIDXSPOTPIVTWSODPROD1, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_STOCHVOL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_PRICE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_IDXEXO_SOD_SCENARIO_SPOT_STOCHVOL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_EOD_SCENARIO_HYBRID_SOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_CORP_EOD_KANNON_RATEFIXINGRISK, JOB_LDN_IDX_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_NY_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK, JOB_NY_LDN_EXO_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_SSEXO_EOD_KANNON_RATEFIXINGRISK, JOB_LDN_EXO_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_KANNON_RATEFIXINGRISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_KANNON_FRTB]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_EU_EOD_PORTCALC_GED_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_UK_EOD_PORTCALC_GED_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_UK_EOD_PORTCALC_GPF_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_US_EOD_PORTCALC_GED_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_SFTP_KANNON]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_SENS_MARKER]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_STRESS_MARKER]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_STRESS_WEEKLY_MARKER]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_HUBBLE_STRESS, JOB_LDN_HUBBLE_STRESS, JOB_LDN_EXO_EOD_SCENARIO_SPOT_VOL_DAILY, JOB_LDN_EXO_EOD_SCENARIO_SPOT_DBRISKSTORE, JOB_LDN_IND_EXO_SCENARIO_SPOT_VOL, JOB_LDN_HUBBLE_STRESS, JOB_LDN_SSEXO_SOD_SCENARIO_SPOT_VOL_DAILY, JOB_LDN_SSEXO_EOD_SCENARIO_SPOT_FAST_DBRISKSTORE, JOB_LDN_HUBBLE_STRESS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_EXO_QIS_SPOT_SCENARIO_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_PREBATCH_START_EOD_RS]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_COMBINED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_KANNON, JOB_COPY_LDN_FIC_EOD_COMBINED, JOB_LDN_FIC_ATT, JOB_LDN_FIC_EOD_IPV_MODELSWITCH, JOB_LDN_FIC_EOD_STATIC, JOB_LDN_FIC_EOD_PERSIST_RISKPNL, JOB_LDN_FIC_EOD_FAIRVALUE, JOB_LDN_FIC_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_ATT, JOB_LDN_FIC_EOD_ATT_PERSIST, JOB_LDN_FIC_EOD_TOD]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_IPV_MODELSWITCH]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_NOTIFY_RISK, JOB_LDN_FIC_EOD_NOTIFY_ATT]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_ATT_PERSIST, JOB_LDN_FIC_EOD_NOTIFY_RISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_NOTIFY_ATT, JOB_LDNFICJARTOGRIMISYE]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_TOD, JOB_LDN_FIC_EOD_PERSIST_DBAX]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_NOTIFY_PNL]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_MCC]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_PERSIST_DBAX, JOB_LDN_FIC_EOD_MODELINFO, JOB_LDN_FIC_EOD_PVMANIFEST]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_FIC_EOD_RATEFIXING, JOB_LDN_FIC_EOD_IPV_DAILY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_RATEFIXING]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_IPV_DAILY, JOB_LDN_FIC_EOD_IPV_MONTHLY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_IPV_MONTHLY, JOB_LDN_FIC_EOD_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_IPV_SEED]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_EOD_FAIRVALUECOPY]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QIS_EOD_KANNON_FRTB]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QISNY_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QISNY_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_LDN_QISNY_COMBINED_BETA_SCENARIO]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_CORP_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_FIC_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_QIS_FVARISK]

    JOB_SLA_LDN_QIS_EOD_COMBINED >> [JOB_COPY_LDN_SSEXO_FVARISK]
