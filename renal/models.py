"""
ELCID implementation specific models!
"""
from django.db import models

from opal.models import (Subrecord,
                         option_models,
                         EpisodeSubrecord, PatientSubrecord, GP, CommunityNurse)
from opal.utils.fields import ForeignKeyOrFreeText
from opal.utils.models import lookup_list



class Demographics(PatientSubrecord):
    _is_singleton = True

    name             = models.CharField(max_length=255, blank=True)
    hospital_number  = models.CharField(max_length=255, blank=True)
    nhs_number       = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth    = models.DateField(null=True, blank=True)
    country_of_birth = ForeignKeyOrFreeText(option_models['destination'])
    ethnicity        = models.CharField(max_length=255, blank=True, null=True)
    gender           = models.CharField(max_length=255, blank=True, null=True)


class Location(EpisodeSubrecord):
    _is_singleton = True

    category                   = models.CharField(max_length=255, blank=True)
    ward                       = models.CharField(max_length=255, blank=True)
    bed                        = models.CharField(max_length=255, blank=True)
    consultant                 = models.CharField(max_length=255, blank=True)


class PresentingComplaint(EpisodeSubrecord):
    _title = 'Presenting Complaint'

    symptom = ForeignKeyOrFreeText(option_models['symptom'])
    duration = ForeignKeyOrFreeText(option_models['duration'])
    details = models.CharField(max_length=255, blank=True)


class Diagnosis(EpisodeSubrecord):
    _title = 'Active Diagnosis'
    _sort = 'date_of_diagnosis'

    condition = ForeignKeyOrFreeText(option_models['condition'])
    provisional = models.BooleanField()
    details = models.CharField(max_length=255, blank=True)
    date_of_diagnosis = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u'Diagnosis for {0}: {1} - {2}'.format(
            self.episode.patient.demographics_set.get().name,
            self.condition,
            self.date_of_diagnosis
            )


class PastMedicalHistory(EpisodeSubrecord):
    _title = 'PMH'
    _sort = 'year'

    condition = ForeignKeyOrFreeText(option_models['condition'])
    year      = models.CharField(max_length=4, blank=True)
    details   = models.CharField(max_length=255, blank=True)


class Todo(EpisodeSubrecord):
    _title = 'To Do'
    details = models.TextField(blank=True)
    

class Investigation(EpisodeSubrecord):
    _sort = 'date_ordered'

    test                  = models.CharField(max_length=255)
    date_ordered          = models.DateField(null=True, blank=True)
    details               = models.CharField(max_length=255, blank=True)
    microscopy            = models.CharField(max_length=255, blank=True)
    organism              = models.CharField(max_length=255, blank=True)
    sensitive_antibiotics = models.CharField(max_length=255, blank=True)
    resistant_antibiotics = models.CharField(max_length=255, blank=True)
    result                = models.CharField(max_length=255, blank=True)
    igm                   = models.CharField(max_length=20, blank=True)
    igg                   = models.CharField(max_length=20, blank=True)
    vca_igm               = models.CharField(max_length=20, blank=True)
    vca_igg               = models.CharField(max_length=20, blank=True)
    ebna_igg              = models.CharField(max_length=20, blank=True)
    hbsag                 = models.CharField(max_length=20, blank=True)
    anti_hbs              = models.CharField(max_length=20, blank=True)
    anti_hbcore_igm       = models.CharField(max_length=20, blank=True)
    anti_hbcore_igg       = models.CharField(max_length=20, blank=True)
    rpr                   = models.CharField(max_length=20, blank=True)
    tppa                  = models.CharField(max_length=20, blank=True)
    viral_load            = models.CharField(max_length=20, blank=True)
    parasitaemia          = models.CharField(max_length=20, blank=True)
    hsv                   = models.CharField(max_length=20, blank=True)
    vzv                   = models.CharField(max_length=20, blank=True)
    syphilis              = models.CharField(max_length=20, blank=True)
    c_difficile_antigen   = models.CharField(max_length=20, blank=True)
    c_difficile_toxin     = models.CharField(max_length=20, blank=True)
    species               = models.CharField(max_length=20, blank=True)
    hsv_1                 = models.CharField(max_length=20, blank=True)
    hsv_2                 = models.CharField(max_length=20, blank=True)
    enterovirus           = models.CharField(max_length=20, blank=True)
    cmv                   = models.CharField(max_length=20, blank=True)
    ebv                   = models.CharField(max_length=20, blank=True)
    influenza_a           = models.CharField(max_length=20, blank=True)
    influenza_b           = models.CharField(max_length=20, blank=True)
    parainfluenza         = models.CharField(max_length=20, blank=True)
    metapneumovirus       = models.CharField(max_length=20, blank=True)
    rsv                   = models.CharField(max_length=20, blank=True)
    adenovirus            = models.CharField(max_length=20, blank=True)
    norovirus             = models.CharField(max_length=20, blank=True)
    rotavirus             = models.CharField(max_length=20, blank=True)
    giardia               = models.CharField(max_length=20, blank=True)
    entamoeba_histolytica = models.CharField(max_length=20, blank=True)
    cryptosporidium       = models.CharField(max_length=20, blank=True)


AccessSiteLookupList = type(*lookup_list('access_site', module=__name__))    

class RRT(EpisodeSubrecord):
    _is_singleton = True
    
    haemodialysis = models.BooleanField(default=False)
    access_site = ForeignKeyOrFreeText(AccessSiteLookupList)
    day_mon = models.BooleanField(default=False)
    day_tue = models.BooleanField(default=False)
    day_wed = models.BooleanField(default=False)
    day_thu = models.BooleanField(default=False)
    day_fri = models.BooleanField(default=False)
    day_sat = models.BooleanField(default=False)
    day_sun = models.BooleanField(default=False)
    regional_unit = models.CharField(max_length=200, blank=True, null=True)
    peritonealdialysis = models.BooleanField(default=False)
    no_rrt = models.BooleanField(default=False)
    transplant = models.BooleanField(default=False)
    donor_type = models.CharField(max_length=200, blank=True, null=True)


class NextBlood(EpisodeSubrecord):
    date = models.DateField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    other  = models.TextField(blank=True, null=True)


class DNR(EpisodeSubrecord):
    _title = 'Resuscitation'
    _is_singleton = True

    dnr = models.CharField(max_length=200, blank=True, null=True)


class Allergies(PatientSubrecord):
    drug        = ForeignKeyOrFreeText(option_models['antimicrobial'])
    details     = models.CharField(max_length=255, blank=True)


class DischargePlan(EpisodeSubrecord):
    date_of_discharge = models.DateField(blank=True, null=True)
    date_of_medical_fitness = models.DateField(blank=True, null=True)
    date_of_outpatient_appt = models.DateField(blank=True, null=True)
    outpatient_tests  = models.TextField(blank=True, null=True)


class NursingNeeds(EpisodeSubrecord):
    needs = models.TextField(blank=True, null=True)


class Risk(EpisodeSubrecord):
    risk = models.TextField(blank=True, null=True)


class InfectionStatus(EpisodeSubrecord):
    infection = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)
    status  = models.CharField(max_length=255, blank=True)


class MDTNeeds(EpisodeSubrecord):
    needs = models.TextField(blank=True, null=True)
    
