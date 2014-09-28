"""
Schema for OPAL Renal implementation
"""

from renal import models
from opal import models as omodels

list_columns = [
    models.Demographics,
    models.Location,
    models.PastMedicalHistory,
    models.Diagnosis,
    models.RRT,
    models.Investigation,
    models.Todo,
    models.NextBlood,
    models.DNR,
    models.DischargePlan
]

nursing_columns = [
    models.Demographics,
    models.Location,
    models.PastMedicalHistory,
    models.Diagnosis,
    models.RRT,
    models.DNR,
    models.NursingNeeds,
    models.Risk,
    models.InfectionStatus,
    models.MDTNeeds
]

all_columns = [
    models.Demographics,
    models.Location,
    models.PastMedicalHistory,
    models.Diagnosis,
    models.RRT,
    models.Investigation,
    models.Todo,
    models.NextBlood,
    models.DNR,
    models.DischargePlan,
    models.NursingNeeds,
    models.Risk,
    models.InfectionStatus,
    models.MDTNeeds
]

list_schemas = {
    'default': list_columns,
    'patients': {
        'nursing': nursing_columns,
        'renal_all': all_columns
        }
}

detail_columns = all_columns = [
    models.Demographics,
    models.Location,
    models.Allergies,
    models.PastMedicalHistory,
    models.Diagnosis,
    models.RRT,
    models.Investigation,
    models.Todo,
    models.NextBlood,
    models.DNR,
    models.DischargePlan,
    models.NursingNeeds,
    models.Risk,
    models.InfectionStatus,
    models.MDTNeeds
]
extract_columns = all_columns
