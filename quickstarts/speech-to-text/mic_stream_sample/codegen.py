from grpc.tools import protoc


protoc.main(
    (
        "",
        "-I.",
        "--python_out=./",
        "--grpc_python_out=./",
        "./protos/yysystem.proto",
    )
)
