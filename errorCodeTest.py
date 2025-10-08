def translateErrorCode(errorCode):
    if errorCode == "401 Unauthorized":
        translation = "Server received an authenticated request"

    elif errorCode == "404 Not Found":
        translation = "Requested web page not found on server"

    elif errorCode == "408 Request Timeout":
        translation = "Server request to close unused connection"

    else:
        translation = "Unknown error code"

    print(translation)

translateErrorCode("401 Unauthorized")
translateErrorCode("404 Not Found")
translateErrorCode("408 Request Timeout")
translateErrorCode("403 Whatever")