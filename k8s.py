import logging
import grpc
import crud_pb2_grpc, crud_pb2
import sys

def run_create(argv):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.ConfigMngmntStub(channel)
        with open(argv[2], 'r') as fin:
            response = stub.CreateConfig(crud_pb2.createRequest(service_name=argv[0][:3], config_body=fin.read()))
    print("Client Received version number: " + response.version)

def run_delete(argv):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.ConfigMngmntStub(channel) 
        response = stub.DeleteConfig(crud_pb2.deleteRequest(service_name=argv[0][:3], version=argv[2]))
        if response.result == '0':
            print("Sucsses: version " + argv[2] + " DELETED")
            return 0
        else:
            print("Error delete this version")
            return 1

def run_update(argv):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.ConfigMngmntStub(channel)
        with open(argv[3], 'r') as fin:
            response = stub.UpdateConfig(crud_pb2.updateRequest(service_name=argv[0][:3], version=argv[2], config_body=fin.read()))
        if response.result == '0':
            print("Sucsses: version " + argv[2] + " UPDATED")
            return 0
        else:
            print("Error update this version")
            return 1

def run_read(argv):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.ConfigMngmntStub(channel)
        response = stub.GetConfig(crud_pb2.deleteRequest(service_name=argv[0][:3], version=argv[2]))
        if response.result == '0':
            print("Client Received config of version: " + argv[2])
            print(response.config_body.replace("\\n", '\n'))
            return 0
        else:
            print("Error read this version")   
            return 1   
        


if __name__ == '__main__':
    if len(sys.argv) > 1:
        logging.basicConfig()
        if sys.argv[1].lower() == "create":
            if len(sys.argv) == 3:
                run_create(sys.argv)
            else:
                print("Wrong quantity of args!")
        elif sys.argv[1].lower() == "read":
            if len(sys.argv) == 3:
                run_read(sys.argv)
            else:
                print("Wrong quantity of args!")
        elif sys.argv[1].lower() == "delete":
            if len(sys.argv) == 3:
                run_delete(sys.argv)
            else:
                print("Wrong quantity of args!")
        elif sys.argv[1].lower() == "update":
            if len(sys.argv) == 4:
                run_update(sys.argv)
            else:
                print("Wrong quantity of args!")
    else:
        print("Wrong quantity of args!")