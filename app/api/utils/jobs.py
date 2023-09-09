
def job_formatted(job):
    response = {
        "uuid": job.uuid if job else None,
        "type": job.type if job else None,
        "status": job.status,
        "status_message": job.status_message,
        "project_uuid": job.project_uuid,
        "client_uuid": job.client_uuid,
        "application_uuid": job.application_uuid,
        "params": job.params,
        "error": job.error,
        "output": job.output,
        "created_at": job.created_at,
        "updated_at": job.updated_at
    }
    return response
