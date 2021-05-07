from concurrent import futures
import grpc

import job_status_pb2
import job_status_pb2_grpc

class JobStatusServicer(job_status_pb2_grpc.JobStatusServicer):

    def __init__(self):
        self.status = "This is the job status message!"

    def GetStatus(self, request, context):
        bucketname, job_name, job_type = request.bucketname, request.job_name, request.job_type
        print(f"bucketname: {bucketname} job_name: {job_name} job_type: {job_type}")
        return job_status_pb2.StatusResponse(job_status=self.status)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  job_status_pb2_grpc.add_JobStatusServicer_to_server(
      JobStatusServicer(), server
  )
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    serve()