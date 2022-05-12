import json
def getRequestData(request,dataType = False):
    """
    Get request data from request object
    """
    data = {}
    data['GET'] = request.GET
    data['POST'] = request.POST
    data['COOKIES'] = request.COOKIES
    data['META'] = request.META
    data['FILES'] = request.FILES
    data['BODY'] = request.body
    data['SESSION'] = request.session
    data['HEADERS'] = request.headers
    data['ENCODING'] = request.encoding
    data['CONTENT_TYPE'] = request.content_type
    data['CONTENT_PARAMS'] = request.content_params
    data['SCHEME'] = request.scheme
    data['METHOD'] = request.method
    data['PATH'] = request.path
    data['PATH_INFO'] = request.path_info
    if (dataType):
        formedData = {}
        compiledData = json.loads(data['BODY'])
        for key in dataType:
            try:
                if (compiledData[key] and compiledData[key]['type'] and dataType[key]['type'] == compiledData[key]['type']):
                    formedData[key] = compiledData[key]['value']
                else:
                    raise Exception('Missing data type or value for ' + key + ' in ' + dataType[key]['type'] + ' format.')
            except:
                raise Exception('Missing data type or value for ' + key + ' in ' + dataType[key]['type'] + ' format.')
        data['FORMED_DATA'] = formedData
    return data