from fastapi import APIRouter
from .flow1 import flow1_router
# from .shray_demo_flow import asit_router
# from .shray_demo_flow2 import asit_router2
# from .shray_demo_flow3 import asit_router3
# from .shray_demo_flow_4 import asit_router4
# from .shray_demo_flow_5 import asit_router5
# from .shray_demo_flow_6 import asit_router6
# from .shray_dynamic_flow import asit_db_dynamic_router
# from .database_operation_flow import crud_with_db
# from .demo_practice import demo_router
from .sign_in import shray_router

flow_router = APIRouter()
# flow_router.include_router(flow1_router,prefix="/flow1")
# flow_router.include_router(shray_router,prefix="/asit")
# flow_router.include_router(shray_router2,prefix="/asit2")
# flow_router.include_router(shray_router3,prefix="/asit3")
# flow_router.include_router(shray_router4,prefix="/asit4")
# flow_router.include_router(shray_router5,prefix="/asit5")
# flow_router.include_router(shray_router6,prefix="/asit6")
# flow_router.include_router(shray_db_dynamic_router,prefix="/asit7")
# flow_router.include_router(crud_with_db,prefix="/asit8")
# flow_router.include_router(demo_router,prefix="/asit9")
flow_router.include_router(shray_router,prefix="/shray")
