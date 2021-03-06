import csv
import os
import uuid
import re
import datetime
import ApplyEsdTags as esdTags
from utils.stripFormatting import stripAll
from SetUUID import AddUUID

objUuid = AddUUID("")

if not os.path.isdir("../OpenReferral"):
    os.mkdir("../OpenReferral")

try:
    csv_in_Organisations = open('../WellAwareData/utf8Organisations.csv', encoding="utf8")
except IOError:
    raise FileNotFoundError("Error: Organisations.csv does not exist.")

csv_reader_Organisations = csv.DictReader(csv_in_Organisations)
count_in_Organisations = 0

try:
    csv_in_Projects = open('../WellAwareData/utf8Projects.csv', encoding="utf8")
except IOError:
    raise FileNotFoundError("Error: Projects.cvs does not exist.")

csv_reader_Projects = csv.DictReader(csv_in_Projects)
count_in_Projects = 0

try:
    csv_in_Events = open('../WellAwareData/utf8Events.csv', encoding="utf8")
except IOError:
    raise FileNotFoundError("Error: Events.csv does not exist.")

csv_reader_Events = csv.DictReader(csv_in_Events)
count_in_Events = 0

try:
    csv_in_Groups = open('../WellAwareData/utf8Groups.csv', encoding="utf8")
except IOError:
    raise FileNotFoundError("Error: Groups.csv does not exist.")

csv_reader_Groups = csv.DictReader(csv_in_Groups)
count_in_Groups = 0

try:
    csv_in_Activities = open('../WellAwareData/utf8Activities.csv', encoding="utf8")
except IOError:
    raise FileNotFoundError("Error: Activities.csv does not exist.")

csv_reader_Activities = csv.DictReader(csv_in_Activities)
count_in_Activities = 0

try:
    csv_out_organization = open('../OpenReferral/organization.csv', mode='w')
except IOError:
    raise PermissionError("Error: organization.csv cannot be opened.")

fields_organization = [
    'id',
    'name',
    'description',
    'url',
    'logo',
    'uri'
]
writer_organization = csv.DictWriter(csv_out_organization, fieldnames=fields_organization, quoting=csv.QUOTE_ALL)
writer_organization.writeheader()
count_out_organization = 0

try:
    csv_out_service = open('../OpenReferral/service.csv', mode='w')
except IOError:
    raise PermissionError("Error: service.csv cannot be opened.")

fields_service = [
    'id',
    'organization_id',
    'name',
    'description',
    'url',
    'email',
    'status',
    'fees',
    'accreditations',
    'deliverable_type'
]
writer_service = csv.DictWriter(csv_out_service, fieldnames=fields_service, quoting=csv.QUOTE_ALL)
writer_service.writeheader()
count_out_service = 0

try:
    csv_out_service_taxonomy = open('../OpenReferral/service_taxonomy.csv', mode='w')
except IOError:
    raise PermissionError("Error: service_taxonomy.csv cannot be opened.")

fields_service_taxonomy = [
    'id',
    'service_id',
    'taxonomy_id'
]
writer_service_taxonomy = csv.DictWriter(csv_out_service_taxonomy,
                                         fieldnames=fields_service_taxonomy,
                                         quoting=csv.QUOTE_ALL)
writer_service_taxonomy.writeheader()
count_out_service_taxonomy = 0

try:
    csv_out_link_taxonomy = open('../OpenReferral/link_taxonomy.csv', mode='w')
except IOError:
    raise PermissionError("Error: link_taxonomy.csv cannot be opened.")

fields_link_taxonomy = [
    'id',
    'link_type',
    'link_id',
    'taxonomy_id'
]
writer_link_taxonomy = csv.DictWriter(csv_out_link_taxonomy, fieldnames=fields_link_taxonomy, quoting=csv.QUOTE_ALL)
writer_link_taxonomy.writeheader()
count_out_link_taxonomy = 0

try:
    csv_out_service_at_location = open('../OpenReferral/service_at_location.csv', mode='w')
except IOError:
    raise PermissionError("Error: service_at_location.csv cannot be opened.")

fields_service_at_location = [
    'id',
    'service_id',
    'location_id'
]
writer_service_at_location = csv.DictWriter(csv_out_service_at_location, fieldnames=fields_service_at_location,
                                            quoting=csv.QUOTE_ALL)
writer_service_at_location.writeheader()
count_out_service_at_location = 0

try:
    csv_out_location = open('../OpenReferral/location.csv', mode='w')
except IOError:
    raise PermissionError("Error: location.csv cannot be opened.")

fields_location = [
    'id',
    'name',
    'description',
    'latitude',
    'longitude'
]
writer_location = csv.DictWriter(csv_out_location, fieldnames=fields_location, quoting=csv.QUOTE_ALL)
writer_location.writeheader()
count_out_location = 0

try:
    csv_out_phone = open('../OpenReferral/phone.csv', mode='w')
except IOError:
    raise PermissionError("Error: phone.csv cannot be opened.")

fields_phone = [
    'id',
    'contact_id',
    'number',
    'language'
]
writer_phone = csv.DictWriter(csv_out_phone, fieldnames=fields_phone, quoting=csv.QUOTE_ALL)
writer_phone.writeheader()
count_out_phone = 0

try:
    csv_out_contact = open('../OpenReferral/contact.csv', mode='w')
except IOError:
    raise PermissionError("Error: contact.csv cannot be opened.")

fields_contact = [
    'id',
    'service_id',
    'name',
    'title'
]
writer_contact = csv.DictWriter(csv_out_contact, fieldnames=fields_contact, quoting=csv.QUOTE_ALL)
writer_contact.writeheader()
count_out_contact = 0

try:
    csv_out_physical_address = open('../OpenReferral/physical_address.csv', mode='w')
except IOError:
    raise PermissionError("Error: physical_address.csv cannot be opened.")

fields_physical_address = [
    'id',
    'location_id',
    'address_1',
    'city',
    'state_province',
    'postal_code',
    'country'
]
writer_physical_address = csv.DictWriter(csv_out_physical_address, fieldnames=fields_physical_address,
                                         quoting=csv.QUOTE_ALL)
writer_physical_address.writeheader()
count_out_physical_address = 0

try:
    csv_out_regular_schedule = open('../OpenReferral/regular_schedule.csv', mode='w')
except IOError:
    raise PermissionError("Error: regular_schedule.csv cannot be opened.")

fields_regular_schedule = [
    'id',
    'service_id',
    'service_at_location_id',
    'opens_at',
    'closes_at',
    'valid_from',
    'valid_to',
    'dtstart',
    'freq',
    'interval',
    'byday',
    'bymonthday',
    'description'
]
writer_regular_schedule = csv.DictWriter(csv_out_regular_schedule, fieldnames=fields_regular_schedule,
                                         quoting=csv.QUOTE_ALL)
writer_regular_schedule.writeheader()
count_out_regular_schedule = 0

try:
    csv_out_holiday_schedule = open('../OpenReferral/holiday_schedule.csv', mode='w')
except IOError:
    raise PermissionError("Error: holiday_schedule.csv cannot be opened.")

fields_holiday_schedule = [
    'id',
    'service_id',
    'service_at_location_id',
    'closed',
    'opens_at',
    'closes_at',
    'start_date',
    'end_date'
]
writer_holiday_schedule = csv.DictWriter(csv_out_holiday_schedule, fieldnames=fields_holiday_schedule,
                                         quoting=csv.QUOTE_ALL)
writer_holiday_schedule.writeheader()
count_out_holiday_schedule = 0

try:
    csv_out_funding = open('../OpenReferral/funding.csv', mode='w')
except IOError:
    raise PermissionError("Error: funding.csv cannot be opened.")

fields_funding = [
    'id',
    'service_id',
    'source'
]
writer_funding = csv.DictWriter(csv_out_funding, fieldnames=fields_funding, quoting=csv.QUOTE_ALL)
writer_funding.writeheader()
count_out_funding = 0

try:
    csv_out_eligibility = open('../OpenReferral/eligibility.csv', mode='w')
except IOError:
    raise PermissionError("Error: eligibility.csv cannot be opened.")

fields_eligibility = [
    'id',
    'service_id',
    'eligibility'
]
writer_eligibility = csv.DictWriter(csv_out_eligibility, fieldnames=fields_eligibility, quoting=csv.QUOTE_ALL)
writer_eligibility.writeheader()
count_out_eligibility = 0

try:
    csv_out_accessibility_for_disabilities = open('../OpenReferral/accessibility_for_disabilities.csv', mode='w')
except IOError:
    raise PermissionError("Error: accessibility_for_disabilities.csv cannot be opened.")

fields_accessibility_for_disabilities = [
    'id',
    'location_id',
    'accessibility'
]
writer_accessibility_for_disabilities = csv.DictWriter(csv_out_accessibility_for_disabilities,
                                                       fieldnames=fields_accessibility_for_disabilities,
                                                       quoting=csv.QUOTE_ALL)
writer_accessibility_for_disabilities.writeheader()
count_out_accessibility_for_disabilities = 0

try:
    csv_out_taxonomy = open('../OpenReferral/taxonomy.csv', mode='w')
except IOError:
    raise PermissionError("Error: taxonomy.csv cannot be opened.")

fields_taxonomy = [
    'id',
    'name',
    'vocabulary'
]
writer_taxonomy = csv.DictWriter(csv_out_taxonomy, fieldnames=fields_taxonomy, quoting=csv.QUOTE_ALL)
writer_taxonomy.writeheader()
count_out_taxonomy = 0

try:
    csv_out_service_area = open('../OpenReferral/service_area.csv', mode='w')
except IOError:
    raise PermissionError("Error: service_area.csv cannot be opened.")

fields_service_area = [
    'id',
    'service_id',
    'service_area',
    'description',
    'extent',
    'uri'
]
writer_service_area = csv.DictWriter(csv_out_service_area, fieldnames=fields_service_area, quoting=csv.QUOTE_ALL)
writer_service_area.writeheader()
count_out_service_area = 0

try:
    csv_out_cost_option = open('../OpenReferral/cost_option.csv', mode='w')
except IOError:
    raise PermissionError("Error: cost_option.csv cannot be opened.")

fields_cost_option = [
    'id',
    'service_id',
    'valid_from',
    'valid_to',
    'option',
    'amount'
]
writer_cost_option = csv.DictWriter(csv_out_cost_option, fieldnames=fields_cost_option, quoting=csv.QUOTE_ALL)
writer_cost_option.writeheader()
count_out_cost_option = 0

try:
    csv_out_review = open('../OpenReferral/review.csv', mode='w')
except IOError:
    raise PermissionError("Error: review.csv cannot be opened.")

fields_review = [
    'id',
    'service_id',
    'reviewer_organization_id',
    'title',
    'description',
    'date',
    'scrore',
    'url',
    'widget'
]
writer_review = csv.DictWriter(csv_out_review, fieldnames=fields_review, quoting=csv.QUOTE_ALL)
writer_review.writeheader()
count_out_review = 0


def FormatDate(inDate):
    outDate = inDate[:4] + '-' + inDate[4:6] + '-' + inDate[6:8]
    return outDate


def setupOrganization(row):
    global row_organization
    global idOrganization

    Name = ''

    if "Title" in row:
        if row["Title"].strip():
            Name = row["Title"].strip()

    if "OrganisationLink" in row:
        if row["OrganisationLink"].strip():
            Name = (row["OrganisationLink"].strip()).replace("&amp;", "&")

    row_organization.update({'name': Name})
    row_organization.update({'description': Name})

    if "ImageURL" in row:
        if row["ImageURL"].strip():
            row_organization.update({'logo': row["ImageURL"].strip()})

    if "Websiteurl" in row:
        if row["Websiteurl"].strip():
            row_organization.update({'url': row["Websiteurl"].strip()})


# could bring this back if we decide to allow email on the organization as well as the service
#        if "Email" in row:
#            if row["Email"].strip():
#                row_organization.update({'email': row["Email"].strip()})


def setupService(row):
    global row_service
    global idService

    global count_out_taxonomy
    global count_out_link_taxonomy
    global count_out_service_taxonomy
    global count_out_phone
    global count_out_contact
    global count_out_service_at_location
    global count_out_service_area
    global count_out_regular_schedule

    row_service.update({'status': 'active'})

    if "Title" in row:
        if row['Title'].strip():
            row_service.update({'name': (row["Title"].strip()).replace("&amp;", "&")})

    if "Content" in row:
        if row['Content'].strip():
            row_service.update({'description': stripAll(row["Content"].strip())})

    if "Contactdetails" in row:
        Description = ''
        if row["Contactdetails"].strip():
            if "Description" in row_service:
                Description = row_service["description"] + '\n'
            row_service.update({'description': stripAll(Description + row["Content"].strip())})

    if "Websiteurl" in row:
        if row['Websiteurl'].strip():
            row_service.update({'url': row["Websiteurl"].strip()})

    if "Email" in row:
        if row['Email'].strip():
            row_service.update({'email': row["Email"].strip()})

    if "Telephone" in row:
        if row['Telephone'].strip():
            row_contact = {}
            count_out_contact += 1
            idContact = count_out_contact
            row_contact.update({'id': idContact})
            row_contact.update({'service_id': idService})

            writer_contact.writerow(row_contact)

            row_phone = {}
            count_out_phone += 1
            idPhone = count_out_phone
            row_phone.update({'id': idPhone})
            row_phone.update({'contact_id': idContact})
            row_phone.update({'number': row['Telephone'].strip()})

            writer_phone.writerow(row_phone)

    if "PrimaryService" in row:
        if row["PrimaryService"]:

            PrimaryServices = row["PrimaryService"].split('|')
            for taxonomyLabel in PrimaryServices:
                taxonomyLabel = taxonomyLabel.strip()
                if taxonomyLabel in listPrimaryServiceLabels.keys():
                    idTaxonomy = listPrimaryServiceLabels[taxonomyLabel]['id']
                else:
                    count_out_taxonomy += 1
                    idTaxonomy = 'bccprimaryservicetype:' + str(count_out_taxonomy)
                    listPrimaryServiceLabels.update({taxonomyLabel: {'id': idTaxonomy}})

                row_service_taxonomy = {}
                count_out_service_taxonomy += 1
                idServiceTaxonomy = count_out_service_taxonomy
                row_service_taxonomy.update({'id': idServiceTaxonomy})
                row_service_taxonomy.update({'service_id': idService})
                row_service_taxonomy.update({'taxonomy_id': idTaxonomy})
                writer_service_taxonomy.writerow(row_service_taxonomy)

    if "Service" in row:
        if row["Service"]:

            Services = row["Service"].split('|')
            for taxonomyLabel in Services:
                taxonomyLabel = taxonomyLabel.strip()
                if taxonomyLabel in listServiceLabels.keys():
                    idTaxonomy = listServiceLabels[taxonomyLabel]['id']
                else:
                    count_out_taxonomy += 1
                    idTaxonomy = 'bccservicetype:' + str(count_out_taxonomy)
                    listServiceLabels.update({taxonomyLabel: {'id': idTaxonomy}})

                row_service_taxonomy = {}
                count_out_service_taxonomy += 1
                idServiceTaxonomy = count_out_service_taxonomy
                row_service_taxonomy.update({'id': idServiceTaxonomy})
                row_service_taxonomy.update({'service_id': idService})
                row_service_taxonomy.update({'taxonomy_id': idTaxonomy})
                writer_service_taxonomy.writerow(row_service_taxonomy)

    if "KeySearchTerms" in row:
        if row["KeySearchTerms"].strip():
            if ',' in row["KeySearchTerms"].strip():
                Terms = row["KeySearchTerms"].strip().split(',')
            else:
                Terms = row["KeySearchTerms"].strip().split(' ')

            for taxonomyLabel in Terms:

                if taxonomyLabel in listSearchLabels.keys():
                    idTaxonomy = listSearchLabels[taxonomyLabel]['id']
                else:
                    count_out_taxonomy += 1
                    idTaxonomy = 'bccsearchterm:' + str(count_out_taxonomy)
                    listSearchLabels.update({taxonomyLabel: {'id': idTaxonomy}})

                row_service_taxonomy = {}
                count_out_service_taxonomy += 1
                idServiceTaxonomy = count_out_service_taxonomy
                row_service_taxonomy.update({'id': idServiceTaxonomy})
                row_service_taxonomy.update({'service_id': idService})
                row_service_taxonomy.update({'taxonomy_id': idTaxonomy})
                writer_service_taxonomy.writerow(row_service_taxonomy)

    if "AgeGroup" in row:
        if row["AgeGroup"]:

            AgeGroups = row["AgeGroup"].split('|')
            for taxonomyLabel in AgeGroups:
                taxonomyLabel = taxonomyLabel.strip()
                if taxonomyLabel in listAgeGroupLabels.keys():
                    idTaxonomy = listAgeGroupLabels[taxonomyLabel]['id']
                else:
                    count_out_taxonomy += 1
                    idTaxonomy = 'bccagegroup:' + str(count_out_taxonomy)
                    listAgeGroupLabels.update({taxonomyLabel: {'id': idTaxonomy}})

                row_service_taxonomy = {}
                count_out_service_taxonomy += 1
                idServiceTaxonomy = count_out_service_taxonomy
                row_service_taxonomy.update({'id': idServiceTaxonomy})
                row_service_taxonomy.update({'service_id': idService})
                row_service_taxonomy.update({'taxonomy_id': idTaxonomy})
                writer_service_taxonomy.writerow(row_service_taxonomy)

    if "UserGroup" in row:
        if row["UserGroup"]:

            UserGroups = row["UserGroup"].split('|')
            for taxonomyLabel in UserGroups:
                taxonomyLabel = taxonomyLabel.strip()
                if taxonomyLabel in listUserGroupLabels.keys():
                    idTaxonomy = listUserGroupLabels[taxonomyLabel]['id']
                else:
                    count_out_taxonomy += 1
                    idTaxonomy = 'bccusergroup:' + str(count_out_taxonomy)
                    listUserGroupLabels.update({taxonomyLabel: {'id': idTaxonomy}})

                row_service_taxonomy = {}
                count_out_service_taxonomy += 1
                idServiceTaxonomy = count_out_service_taxonomy
                row_service_taxonomy.update({'id': idServiceTaxonomy})
                row_service_taxonomy.update({'service_id': idService})
                row_service_taxonomy.update({'taxonomy_id': idTaxonomy})
                writer_service_taxonomy.writerow(row_service_taxonomy)

    idServiceAtLocation = ''

    if "Address" in row:
        if row["Address"]:
            AddressPostcode = makeAddressPostcode(row['Address'])

            Postcode = AddressPostcode['Postcode']
            FirstLineOfAddress = AddressPostcode['FirstLineOfAddress']

            if not Postcode:
                if "Postcodeareawheretheorganisationworks" in row:
                    if row["Postcodeareawheretheorganisationworks"].strip():
                        Postcode = row["Postcodeareawheretheorganisationworks"].strip()

            # check if the address already exists

            idPhysicalAddress = getPhysicalAddressId(Postcode, '', FirstLineOfAddress)
            idLocation = idPhysicalAddress

            if not idPhysicalAddress:
                idLocation = writeLocation(AddressPostcode['AddressLines'], Postcode, row)

            row_service_at_location = {}
            count_out_service_at_location += 1
            idServiceAtLocation = count_out_service_at_location
            row_service_at_location.update({'id': idServiceAtLocation})
            row_service_at_location.update({'service_id': idService})
            row_service_at_location.update({'location_id': idLocation})
            writer_service_at_location.writerow(row_service_at_location)

    if "District" in row:
        if row["District"]:

            Districts = row["District"].split('|')
            for AreaName in Districts:
                AreaName = AreaName.strip()

                count_out_service_area += 1
                idArea = count_out_service_area

                row_service_area = {}
                row_service_area.update({'id': idArea})
                row_service_area.update({'service_id': idService})
                row_service_area.update({'service_area': AreaName})

                writer_service_area.writerow(row_service_area)

    if "AreasServed" in row:
        if (row["AreasServed"].strip()):
            Area = row["AreasServed"].strip()
            count_out_service_area += 1
            idArea = count_out_service_area

            row_service_area = {}
            row_service_area.update({'id': idArea})
            row_service_area.update({'service_id': idService})
            row_service_area.update({'service_area': Area})

            writer_service_area.writerow(row_service_area)

    Fees = ''
    if "CostInformation" in row:
        if Fees:
            Fees += "\n"
        if row["CostInformation"].strip():
            Fees += row["CostInformation"].strip()

    if "ConcessionsInformation" in row:
        if Fees:
            Fees += "\n"
        if row["ConcessionsInformation"].strip():
            Fees += row["CostInformation"].strip()

    if "Cost" in row:
        if Fees:
            Fees += "\n"
        if row["Cost"].strip():
            Fees += row["Cost"].strip()

    row_service['fees'] = Fees

    # schedule information

    row_schedule = {}

    if 'Startdate' in row:
        if row['Startdate'].strip():
            row_schedule.update({'valid_from': FormatDate(row['Startdate'].strip())})
            row_schedule.update({'dtstart': FormatDate(row['Startdate'].strip())})
    if 'Enddate' in row:
        if row['Enddate'].strip():
            row_schedule.update({'valid_to': FormatDate(row['Enddate'].strip())})

    Day = ''
    DayDD = ''

    AvailabilityDescription = ''

    if 'Startdate' in row:
        if row['Startdate']:
            objDate = datetime.datetime.strptime(row['Startdate'], '%Y%m%d')
            DayNum = objDate.weekday()
            Day = ''
            txtDay = ''
            if DayNum == 0:
                Day = 'MO'
                txtDay = 'Monday'
            if DayNum == 1:
                Day = 'TU'
                txtDay = 'Tuesday'
            if DayNum == 2:
                Day = 'WE'
                txtDay = 'Wednesday'
            if DayNum == 3:
                Day = 'TH'
                txtDay = 'Thursday'
            if DayNum == 4:
                Day = 'FR'
                txtDay = 'Friday'
            if DayNum == 5:
                Day = 'SA'
                txtDay = 'Saturday'
            if DayNum == 6:
                Day = 'SU'
                txtDay = 'Sunday'

            DayDD = objDate.day

    if 'Recurringoption' in row:
        #        if (row['Recurringoption'] == 'daily'):
        #            row_Session.update({'Frequency': 'daily'})
        #            AvailabilityDescription = 'Every Day'

        if row['Recurringoption'] == 'weekly':
            row_schedule.update({'freq': 'WEEKLY'})
            if Day:
                row_schedule.update({'byday': Day})
                AvailabilityDescription = txtDay + 's'

            if 'Whichoccurrenceofthedayofthemonth' in row:
                if row['Whichoccurrenceofthedayofthemonth'].strip():
                    row_schedule.update({'freq': 'MONTHLY'})
                    DayOffset = ''
                    if row['Whichoccurrenceofthedayofthemonth'].strip() == 'first':
                        DayOffset = 1
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'second':
                        DayOffset = 2
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'third':
                        DayOffset = 3
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'fourth':
                        DayOffset = 4
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'last':
                        DayOffset = -1

                    if Day:
                        if DayOffset:
                            Day = str(DayOffset) + Day
                        row_schedule.update({'byday': Day})

                        AvailabilityDescription = "On the " + row[
                            'Whichoccurrenceofthedayofthemonth'].strip() + ' ' + txtDay + " of each month"

        if row['Recurringoption'] == 'fortnightly':

            row_schedule.update({'freq': 'WEEKLY'})
            row_schedule.update({'interval': '2'})

            if Day:
                row_schedule.update({'byday': Day})

            AvailabilityDescription = "Fortnightly on a " + txtDay

        if row['Recurringoption'] == 'monthly':
            row_schedule.update({'bymonthday': DayDD})
            row_schedule.update({'freq': 'MONTHLY'})
            AvailabilityDescription = "On the " + str(DayDD) + " of each month"

            if 'Whichoccurrenceofthedayofthemonth' in row:
                if row['Whichoccurrenceofthedayofthemonth'].strip():

                    MonthOffset = ''
                    if row['Whichoccurrenceofthedayofthemonth'].strip() == 'first':
                        MonthOffset = 1
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'second':
                        MonthOffset = 2
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'third':
                        MonthOffset = 3
                    elif row['Whichoccurrenceofthedayofthemonth'].strip() == 'fourth':
                        MonthOffset = 4

                    row_schedule.update({'interval': MonthOffset})

                    AvailabilityDescription = "On the " + str(DayDD) + " of every " + row[
                        'Whichoccurrenceofthedayofthemonth'].strip() + " month"

    if 'Starttime' in row:
        if row['Starttime']:
            row_schedule.update({'opens_at': row['Starttime']})
            AvailabilityDescription += " from " + row['Starttime']
    if 'Endtime' in row:
        if row['Endtime']:
            row_schedule.update({'closes_at': row['Endtime']})
            AvailabilityDescription += " to " + row['Endtime']

    if AvailabilityDescription.strip():
        row_schedule.update({'description': stripAll(AvailabilityDescription)})

    if row_schedule:
        count_out_regular_schedule += 1
        idSchedule = count_out_regular_schedule
        row_schedule.update({'id': idSchedule})

        if idServiceAtLocation and idService:
            row_schedule.update({'service_at_location_id': idServiceAtLocation})
            row_schedule.update({'service_id': None})
        else:
            if idServiceAtLocation:
                row_schedule.update({'service_at_location_id': idServiceAtLocation})
                row_schedule.update({'service_id': None})
            else:
                row_schedule.update({'service_id': idService})
                row_schedule.update({'service_at_location_id': None})

        writer_regular_schedule.writerow(row_schedule)


def makeAddressPostcode(AddressLine):
    listAddress = re.split(',|\n', AddressLine)
    FirstLineOfAddress = ''
    LastLineOfAddress = ''

    if len(listAddress) > 0:
        FirstLineOfAddress = listAddress[0].strip()
        LastLineOfAddress = listAddress[len(listAddress) - 1].strip()

    Postcode = ''
    objMatch = re.search(
        r'(([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2}))$',
        LastLineOfAddress, re.M | re.I)
    if objMatch:
        Postcode = objMatch.group(0)
        listAddress[len(listAddress) - 1] = listAddress[len(listAddress) - 1].replace(Postcode, '')

    return {'AddressLines': listAddress, 'FirstLineOfAddress': FirstLineOfAddress, 'Postcode': Postcode}


def getPhysicalAddressId(Postcode, VenueName, Address1):
    try:
        csv_in_physical_address = open('../OpenReferral/physical_address.csv', encoding="utf8")
    except IOError:
        raise FileNotFoundError("Error: Can't open physical_address.csv to read.")

    csv_reader_physical_address = csv.DictReader(csv_in_physical_address)

    FoundId = False

    for row_Address in csv_reader_physical_address:

        idAddress = row_Address["id"]

        if row_Address["postal_code"].strip() == Postcode.strip():
            if (row_Address["address_1"].strip() == VenueName.strip()) or (
                    row_Address["address_1"].strip() == Address1.strip()):
                FoundId = idAddress
                break

    csv_in_physical_address.close()

    return FoundId


def getIdForOrgName(OrgName):
    try:
        csv_in_organization = open('../OpenReferral/organization.csv', encoding="utf8")
    except IOError:
        raise FileNotFoundError("Error: Can't open organization.csv to read.")

    csv_reader_organization = csv.DictReader(csv_in_organization)

    FoundId = False

    for row_organization in csv_reader_organization:

        idOrg = row_organization["id"]

        if row_organization["name"].strip() == OrgName.strip():
            FoundId = row_organization["id"]
            break

    csv_in_organization.close()

    return FoundId


def writeLocation(listAddressLines, Postcode, row):
    global count_out_location
    global count_out_accessibility_for_disabilities

    count_out_location += 1
    idLocation = objUuid.get_uuid(count_out_location, "location", "bristol")
    idPhysicalAddress = idLocation

    row_location = {}
    row_location.update({'id': idLocation})

    row_physical_address = {}
    row_physical_address.update({'id': idPhysicalAddress})
    row_physical_address.update({'location_id': idLocation})

    FirstLineOfAddress = ''
    if len(listAddressLines) > 0:
        row_physical_address.update({"address_1": listAddressLines[0].strip()})
        FirstLineOfAddress = listAddressLines[0].strip()

    RemainingAddress = ''

    if len(listAddressLines) > 1:
        RemainingAddress += ', ' + listAddressLines[1].strip()
    if len(listAddressLines) > 2:
        RemainingAddress += ', ' + listAddressLines[2].strip()
    if len(listAddressLines) > 3:
        RemainingAddress += ', ' + listAddressLines[3].strip()
    if len(listAddressLines) > 4:
        RemainingAddress += ', ' + listAddressLines[4].strip()

    row_physical_address.update({"city": RemainingAddress})
    row_physical_address.update({"postal_code": Postcode})
    row_physical_address.update({"state_province": ""})

    if 'lat' in row and 'lng' in row:
        if row['lat'] and row['lng']:
            row_location.update({'latitude': row['lat'].strip()})
            row_location.update({'longitude': row['lng'].strip()})

    if 'Accessibility' in row:
        if row['Accessibility']:
            Accessibilities = row['Accessibility'].split('|')
            for Label in Accessibilities:
                row_Accessibility = {}

                count_out_accessibility_for_disabilities += 1
                idAccessibility = count_out_accessibility_for_disabilities

                row_Accessibility.update({'id': idAccessibility})
                row_Accessibility.update({'location_id': idLocation})
                row_Accessibility.update({'accessibility': Label})

                writer_accessibility_for_disabilities.writerow(row_Accessibility)

    writer_location.writerow(row_location)
    writer_physical_address.writerow(row_physical_address)
    csv_out_physical_address.flush()

    return idLocation


listPrimaryServiceLabels = {}
listServiceLabels = {}
listAgeGroupLabels = {}
listUserGroupLabels = {}
listSearchLabels = {}

# Set up some taxonomy items

count_out_taxonomy += 1
row_taxonomy = {}
row_taxonomy.update({'id': 'bccsource:Organisation'})
row_taxonomy.update({'name': 'Organisation'})
row_taxonomy.update({'vocabulary': "BCC Data Sources"})
writer_taxonomy.writerow(row_taxonomy)

count_out_taxonomy += 1
row_taxonomy = {}
row_taxonomy.update({'id': 'bccsource:Project'})
row_taxonomy.update({'name': 'Project'})
row_taxonomy.update({'vocabulary': "BCC Data Sources"})
writer_taxonomy.writerow(row_taxonomy)

count_out_taxonomy += 1
row_taxonomy = {}
row_taxonomy.update({'id': 'bccsource:Event'})
row_taxonomy.update({'name': 'Event'})
row_taxonomy.update({'vocabulary': "BCC Data Sources"})
writer_taxonomy.writerow(row_taxonomy)

count_out_taxonomy += 1
row_taxonomy = {}
row_taxonomy.update({'id': 'bccsource:Group'})
row_taxonomy.update({'name': 'Group'})
row_taxonomy.update({'vocabulary': "BCC Data Sources"})
writer_taxonomy.writerow(row_taxonomy)

count_out_taxonomy += 1
row_taxonomy = {}
row_taxonomy.update({'id': 'bccsource:Activity'})
row_taxonomy.update({'name': 'Activity'})
row_taxonomy.update({'vocabulary': "BCC Data Sources"})
writer_taxonomy.writerow(row_taxonomy)

# Set up organizations

for row_in_Organisations in csv_reader_Organisations:
    if row_in_Organisations["ID"] in ["", None]:
        continue
    idOrganization = objUuid.get_uuid(row_in_Organisations["ID"], "organization", "bristol")

    if idOrganization:
        row_organization = {}

        count_out_organization += 1

        row_organization.update({'id': idOrganization})
        setupOrganization(row_in_Organisations)
        writer_organization.writerow(row_organization)
        csv_out_organization.flush()

        count_in_Organisations += 1
        print(f'Processing Organisation {count_in_Organisations}.')

print(f'Processed {count_in_Organisations} Organisations.')

# set up services from the Organisation Table

# so back to row 1 - which is after the header row

csv_in_Organisations.seek(0)
next(csv_in_Organisations)
count_in_Organisations = 0

for row_in_Organisations in csv_reader_Organisations:
    if row_in_Organisations["ID"] in [None, ""]:
        continue

    idOrganization = objUuid.get_uuid(row_in_Organisations["ID"], "organization", "bristol")

    if idOrganization:
        row_service = {}

        count_out_service += 1

        idService = objUuid.get_uuid(count_out_service, "service", "bristol")

        row_service.update({'id': idService})
        row_service.update({'organization_id': idOrganization})

        row_service_taxonomy = {}
        count_out_service_taxonomy += 1
        idServiceTaxonomy = count_out_service_taxonomy
        row_service_taxonomy.update({'id': idServiceTaxonomy})
        row_service_taxonomy.update({'service_id': idService})
        row_service_taxonomy.update({'taxonomy_id': 'bccsource:Organisation'})
        writer_service_taxonomy.writerow(row_service_taxonomy)

        setupService(row_in_Organisations)

        writer_service.writerow(row_service)

        count_in_Organisations += 1
        print(f'Processing Organisation {count_in_Organisations}.')

for row_in_Projects in csv_reader_Projects:

    if row_in_Projects['id']:

        row_service = {}

        count_out_service += 1

        idService = objUuid.get_uuid(count_out_service, "service", "bristol")

        row_service.update({'id': idService})

        idOrganization = False

        if row_in_Projects['OrganisationID'].strip():
            idOrganization = objUuid.get_uuid(row_in_Projects['OrganisationID'].strip(), "organization", "bristol")
        else:
            if row_in_Projects['OrganisationLink'].strip():
                idOrganization = getIdForOrgName(row_in_Projects['OrganisationLink'].strip())
            else:
                idOrganization = getIdForOrgName(row_in_Projects['Title'].strip())

            if not idOrganization:
                count_out_organization += 1
                idOrganization = 'activity:' + str(count_out_organization)
                idOrganization = objUuid.get_uuid(idOrganization, "organization", "bristol")
                row_organization = {}
                row_organization.update({'id': idOrganization})
                setupOrganization(row_in_Projects)
                writer_organization.writerow(row_organization)
                csv_out_organization.flush()

        row_service.update({'organization_id': idOrganization})

        row_service_taxonomy = {}
        count_out_service_taxonomy += 1
        idServiceTaxonomy = count_out_service_taxonomy
        row_service_taxonomy.update({'id': idServiceTaxonomy})
        row_service_taxonomy.update({'service_id': idService})
        row_service_taxonomy.update({'taxonomy_id': 'bccsource:Project'})
        writer_service_taxonomy.writerow(row_service_taxonomy)

        setupService(row_in_Projects)

        writer_service.writerow(row_service)

        count_in_Projects += 1
        print(f'Processing Project {count_in_Projects}.')

for row_in_Events in csv_reader_Events:

    if row_in_Events['id']:

        row_service = {}

        count_out_service += 1

        idService = objUuid.get_uuid(count_out_service, "service", "bristol")

        row_service.update({'id': idService})

        idOrganization = False

        if row_in_Events['OrganisationID'].strip():
            idOrganization = row_in_Events['OrganisationID'].strip()
        else:
            if row_in_Events['OrganisationLink'].strip():
                idOrganization = getIdForOrgName(row_in_Events['OrganisationLink'].strip())
            else:
                idOrganization = getIdForOrgName(row_in_Events['Title'].strip())

            if not idOrganization:
                count_out_organization += 1
                idOrganization = 'event:' + str(count_out_organization)
                idOrganization = objUuid.get_uuid(idOrganization, "organization", "bristol")
                row_organization = {}
                row_organization.update({'id': idOrganization})
                setupOrganization(row_in_Events)
                writer_organization.writerow(row_organization)
                csv_out_organization.flush()

        row_service.update({'organization_id': idOrganization})

        row_service_taxonomy = {}
        count_out_service_taxonomy += 1
        idServiceTaxonomy = count_out_service_taxonomy
        row_service_taxonomy.update({'id': idServiceTaxonomy})
        row_service_taxonomy.update({'service_id': idService})
        row_service_taxonomy.update({'taxonomy_id': 'bccsource:Event'})
        writer_service_taxonomy.writerow(row_service_taxonomy)

        setupService(row_in_Events)

        writer_service.writerow(row_service)

        count_in_Events += 1
        print(f'Processing Event {count_in_Events}.')

for row_in_Groups in csv_reader_Groups:

    if row_in_Groups['id']:

        row_service = {}

        count_out_service += 1

        idService = objUuid.get_uuid(count_out_service, "service", "bristol")

        row_service.update({'id': idService})

        idOrganization = False

        if row_in_Groups['OrganisationID'].strip():
            idOrganization = row_in_Groups['OrganisationID'].strip()
        else:
            if row_in_Groups['OrganisationLink'].strip():
                idOrganization = getIdForOrgName(row_in_Groups['OrganisationLink'].strip())
            else:
                idOrganization = getIdForOrgName(row_in_Groups['Title'].strip())

            if not idOrganization:
                count_out_organization += 1
                idOrganization = 'group:' + str(count_out_organization)
                idOrganization = objUuid.get_uuid(idOrganization, "organization", "bristol")
                row_organization = {}
                row_organization.update({'id': idOrganization})
                setupOrganization(row_in_Groups)
                writer_organization.writerow(row_organization)
                csv_out_organization.flush()

        row_service.update({'organization_id': idOrganization})

        row_service_taxonomy = {}
        count_out_service_taxonomy += 1
        idServiceTaxonomy = count_out_service_taxonomy
        row_service_taxonomy.update({'id': idServiceTaxonomy})
        row_service_taxonomy.update({'service_id': idService})
        row_service_taxonomy.update({'taxonomy_id': 'bccsource:Group'})
        writer_service_taxonomy.writerow(row_service_taxonomy)

        setupService(row_in_Groups)

        writer_service.writerow(row_service)

        count_in_Groups += 1
        print(f'Processing Group {count_in_Groups}.')

for row_in_Activities in csv_reader_Activities:

    if row_in_Activities['id']:

        row_service = {}

        count_out_service += 1

        idService = objUuid.get_uuid(count_out_service, "service", "bristol")

        row_service.update({'id': idService})

        idOrganization = False

        if row_in_Activities['OrganisationID'].strip():
            idOrganization = row_in_Activities['OrganisationID'].strip()
        else:
            if row_in_Activities['OrganisationLink'].strip():
                idOrganization = getIdForOrgName(row_in_Activities['OrganisationLink'].strip())
            else:
                idOrganization = getIdForOrgName(row_in_Activities['Title'].strip())

            if not idOrganization:
                count_out_organization += 1
                idOrganization = 'activity:' + str(count_out_organization)
                idOrganization = objUuid.get_uuid(idOrganization, "organization", "bristol")
                row_organization = {}
                row_organization.update({'id': idOrganization})
                setupOrganization(row_in_Activities)
                writer_organization.writerow(row_organization)
                csv_out_organization.flush()

        row_service.update({'organization_id': idOrganization})

        row_service_taxonomy = {}
        count_out_service_taxonomy += 1
        idServiceTaxonomy = count_out_service_taxonomy
        row_service_taxonomy.update({'id': idServiceTaxonomy})
        row_service_taxonomy.update({'service_id': idService})
        row_service_taxonomy.update({'taxonomy_id': 'bccsource:Activity'})
        writer_service_taxonomy.writerow(row_service_taxonomy)

        setupService(row_in_Activities)

        writer_service.writerow(row_service)

        count_in_Activities += 1
        print(f'Processing Activity {count_in_Activities}.')

print(f'Processed {count_in_Organisations} Organisations.')
print(f'Processed {count_in_Activities} Activivies.')

# write out the taxonomy rows that have been generated for the run

for key, value in listPrimaryServiceLabels.items():
    row_taxonomy = {}
    row_taxonomy.update({'id': value['id']})
    row_taxonomy.update({'name': key})
    row_taxonomy.update({'vocabulary': "BCC Primary Services"})
    writer_taxonomy.writerow(row_taxonomy)

for key, value in listServiceLabels.items():
    row_taxonomy = {}
    row_taxonomy.update({'id': value['id']})
    row_taxonomy.update({'name': key})
    row_taxonomy.update({'vocabulary': "BCC Services"})
    writer_taxonomy.writerow(row_taxonomy)

for key, value in listAgeGroupLabels.items():
    row_taxonomy = {}
    row_taxonomy.update({'id': value['id']})
    row_taxonomy.update({'name': key})
    row_taxonomy.update({'vocabulary': "BCC Age Groups"})
    writer_taxonomy.writerow(row_taxonomy)

for key, value in listUserGroupLabels.items():
    row_taxonomy = {}
    row_taxonomy.update({'id': value['id']})
    row_taxonomy.update({'name': key})
    row_taxonomy.update({'vocabulary': "BCC User Groups"})
    writer_taxonomy.writerow(row_taxonomy)

for key, value in listSearchLabels.items():
    row_taxonomy = {}
    row_taxonomy.update({'id': value['id']})
    row_taxonomy.update({'name': key})
    row_taxonomy.update({'vocabulary': "BCC Search Terms"})
    writer_taxonomy.writerow(row_taxonomy)

csv_in_Organisations.close()
csv_in_Projects.close()
csv_in_Events.close()
csv_in_Groups.close()

csv_out_organization.close()
csv_out_accessibility_for_disabilities.close()
csv_out_contact.close()
csv_out_cost_option.close()
csv_out_eligibility.close()
csv_out_funding.close()
csv_out_holiday_schedule.close()
csv_out_link_taxonomy.close()
csv_out_location.close()
csv_out_phone.close()
csv_out_physical_address.close()
csv_out_regular_schedule.close()
csv_out_taxonomy.close()
csv_out_service.close()
csv_out_service_area.close()
csv_out_service_at_location.close()
csv_out_service_taxonomy.close()
objUuid.insert_new_uuid()

esdTags.main()
