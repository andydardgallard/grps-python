from concurrent import futures
import logging
import grpc
import crud_pb2, crud_pb2_grpc
import pandas as pd

class ConfigDB():
    df = pd.DataFrame()

    def read_csv(self):
        try:
            with open("configDB.csv", 'r') as fin:
                self.df = pd.read_csv(fin, sep=';')
        except:
            file = open("configDB.csv", 'w')
            file.write("service;version;config_body;status")
            file.close()
            with open("configDB.csv", 'r') as fin:
                self.df = pd.read_csv(fin, sep=';')
        return self.df

class ConfigMngmnt(crud_pb2_grpc.ConfigMngmntServicer):
    db = ConfigDB()
    
    def GetConfig(self, request, context):
        config_body = ""
        result_out = '1'
        try:
            df = self.db.read_csv()
            filtr_serv = df.service == request.service_name
            filtr_version =  df.version == int(request.version)
            index =  df[filtr_serv & filtr_version].index[0]
            config_body = df.iloc[index, 2]
            result_out = '0'
        except:
            print("Error read")
        return crud_pb2.getResponse(config_body=config_body, result=result_out)
    
    def CreateConfig(self, request, context):
        df = self.db.read_csv()
        version_out = '0'
        try:
            filtr_serv = df.service == request.service_name
            filtr_status = df.status == "active"
            index = df[filtr_serv & filtr_status].index[0]
            df.iloc[index, 3:] = "notactive"
            body_config = request.config_body.replace("\n", "\\n")
            df.loc[len(df.index)] = [request.service_name, df.iloc[index].version + 1, body_config, "active"] 
            df.to_csv("configDB.csv", sep=';', index=False)
            version_out = str(df.iloc[index].version + 1)
        except:
            body_config = request.config_body.replace("\n", "\\n")
            df.loc[len(df.index)] = [request.service_name, '0', body_config, "active"] 
            df.to_csv("configDB.csv", sep=';', index=False)
        return crud_pb2.createResponse(version=version_out)

    def DeleteConfig(self, request, context):
        result_out = '1'
        try:
            df = self.db.read_csv()
            filtr_serv = df.service == request.service_name
            filtr_version =  df.version == int(request.version)
            index =  df[filtr_serv & filtr_version].index[0]
            if  df.iloc[index, 3] == "notactive":
                df.drop(index=index, inplace=True)
                df.to_csv("configDB.csv", sep=';', index=False)
                result_out = '0'
            else:
                print("Active version cannot be deleted")
        except:
            print("No such version")
        return crud_pb2.deleteResponse(result=result_out)

    def UpdateConfig(self, request, context):
        result_out = '1'
        try:
            df = self.db.read_csv()
            filtr_serv = df.service == request.service_name
            filtr_version =  df.version == int(request.version)
            index = df[filtr_serv & filtr_version].index[0]
            body_config = request.config_body.replace("\n", "\\n")
            df.iloc[index, 2] = body_config
            df.to_csv("configDB.csv", sep=';', index=False)
            result_out = '0'
        except:
            print("Error Update")
        return crud_pb2.updateResponse(result=result_out)

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crud_pb2_grpc.add_ConfigMngmntServicer_to_server(ConfigMngmnt(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()