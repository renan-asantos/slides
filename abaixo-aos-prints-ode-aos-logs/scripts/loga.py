from loguru import logger

feature = "f-string"
logger.info(f"Se você está usando Python {3.8} prefira {feature}")
print("\n")

# from loguru import logger
# import sys
# import json
#
# def serialize(record: dict):
#     subset = {
#         "timestamp": record["time"].timestamp(),
#         "message": record["message"],
#         "severity": record["level"].name,
#         "log.level": record["level"].name,
#         "file.name": record["file"].path,
#         "line.number": record["line"],
#         "func.name":record["function"]
#     }
#
#     if extra_values := record["extra"]:
#         subset.update(
#             {f"extra.{key}": value for key, value in extra_values.items()},
#         )
#
#     return json.dumps(subset)
#
# logger.remove(0)
# logger = logger.patch(lambda record: record["extra"].update({"serialized": serialize(record)} ))
# logger.add(sys.stderr, format="{extra[serialized]}")
# logger.bind(valor="topper").info("Ola")
# logger.info("Ola2")
# print("\n")


# import sys
# import json
# from loguru import logger
#
#
# def serialize(record):
#     subset = {
#         "timestamp": record["time"].timestamp(),
#         "message": record["message"],
#         "level": record["level"].name,
#     }
#     return json.dumps(subset)
#
#
# def patching(record):
#     record["extra"]["serialized"] = serialize(record)
#
# logger = logger.patch(patching)
# logger.add(sys.stderr, format="{extra}")
# logger.bind(coisa="legal").info("Ola")
# print("\n")


# import sys
#
# from loguru import logger
#
# logger.add(sys.stderr, serialize=True)
#
# logger.info(f"Ola")
# print("\n")



# import logging
#
# logging.basicConfig(
#     level = logging.INFO,
#     filename = "logs.txt",
#     filemode = "w",
#     format="%(asctime)s %(levelname)s:%(message)s",
#     datefmt='%d/%m/%Y %I:%M:%S %p'
# )
#
# logging.info("Informação")
# logging.warning("Aviso")
# logging.error("Erro")
