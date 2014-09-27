
from renal import models
from opal import models as omodels
#from infectioncontrol import models as icmodels

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

detail_columns = [
    # models.Demographics,
    # models.ContactDetails,
    # models.Carers,
    # models.Location,
    # omodels.Tagging,
    # models.Diagnosis,
    # models.PresentingComplaint,
    # obsmodels.Observation,
    # models.PastMedicalHistory,
    # models.Antimicrobial,
    # models.Allergies,
    # models.MicrobiologyTest,
    # models.Line,
    # models.OPATLineAssessment,
    # models.MicrobiologyInput,
    # models.OPATReview,
    # models.Travel,
    # models.Appointment,
    # models.Todo,
    # models.OPATOutstandingIssues,
    # models.GeneralNote,
 ]

extract_columns = [
    # omodels.Tagging,
    # models.Demographics,
    # models.Location,
    # models.Diagnosis,
    # models.Antimicrobial,
    # models.Allergies,
    # models.PastMedicalHistory,
    # models.MicrobiologyInput,
    # models.MicrobiologyTest,
    # models.Travel,
    # models.Todo,
    # models.GeneralNote,
    ]

