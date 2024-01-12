import re
import replicate
import json

def transcribe(input_filename):
    # model = replicate.models.get("zeke/zisper")
    # version = model.versions.get("d64f0cf852b8ce01cfbd532ef8c00f4e8384bf56759de097edb22e27cdc512bd")
    # prediction = replicate.predictions.create(
    #     version=version,
    #     input={"audio":open(input_filename, "rb")})
    
    deployment = replicate.deployments.get("zeke/zesty-zisper")
    prediction = deployment.predictions.create(
        input={"audio":open(input_filename, "rb")})

    prediction.wait()
    output_json = json.loads(prediction.output)
    joined_text = ' '.join(item['text'].strip() for item in output_json)

    return(joined_text)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
        print(transcribe(input_filename))
    else:
        print("File name missing, must have file name passed as argument")
