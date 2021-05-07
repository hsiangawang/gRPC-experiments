from concurrent import futures
import grpc

import job_status_pb2
import job_status_pb2_grpc


def getJobStatus(stub, StatusRequest):
    response = stub.GetStatus(StatusRequest)
    print(response.job_status)


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = job_status_pb2_grpc.JobStatusStub(channel)
        print("-------------- JobStatus --------------")
        getJobStatus(stub, job_status_pb2.StatusRequest(bucketname="adamw", job_name="model_v1", job_type="NLP"))

if __name__ == '__main__':
    run()