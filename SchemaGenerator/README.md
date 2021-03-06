# Schema generator
## Defining extensions and generating schemas
The [Open Knowledge Foundation tabular data package](https://raw.githubusercontent.com/openreferral/specification/master/datapackage.json) machine readable representation of Open Referral’s [Human Services Data Specification (HSDS) Objects and fields reference](https://openreferral.readthedocs.io/en/latest/hsds/reference/#objects-and-fields) has been updated to denote extensions and application profile constraints.

From the revised data model we generate JSON schemas for web method responses extending [those defined by Open Referral](https://openreferral.readthedocs.io/en/latest/_static/swagger/?url=../openapi-hsda.yaml#). We  also generate CSV schemas which define tabular views on the data but will not provide a complete directory. The diagram below shows the process of refining the data package and then generating machine readable schemas. Links to code and resources generate are given - these are subject to refinement in consultation with software developers.

![Going from the tabular data package to schemas](https://github.com/esd-org-uk/human-services/blob/master/Resources/FromTabularDataPackageToEverything.PNG)

1.  [Existing Open Referral tabular data package](https://raw.githubusercontent.com/openreferral/specification/master/datapackage.json)
2.  [Tabular data package with extensions and application profile](https://raw.githubusercontent.com/esd-org-uk/human-services/master/SchemaGenerator/Generator/ExtendedDataPackage.json)
3.  [Tabular data package with extensions and application profile](https://raw.githubusercontent.com/esd-org-uk/human-services/master/SchemaGenerator/Generator/ExtendedDataPackage.json)
4.  [Code to generate ERDs](https://github.com/esd-org-uk/human-services/tree/master/SchemaGenerator)
5.  ERD for:
  - [Open Referral data package](https://github.com/esd-org-uk/human-services/raw/master/Resources/OpenReferralERD.png) [Graphviz Dot File](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Resources/OpenReferralERD.gv) [Lucid Charts ERD File](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Resources/OpenReferralERD.csv)
  - [Extended data package](https://github.com/esd-org-uk/human-services/raw/master/Resources/AllERD.png) [Graphviz Dot File](https://github.com/esd-org-uk/human-services/raw/master/Resources/AllERD.gv) [Lucid Charts ERD File](https://github.com/esd-org-uk/human-services/raw/master/Resources/AllERD.csv)
  - [Application profile](https://github.com/esd-org-uk/human-services/raw/master/Resources/ApplicationProfileERD.png) [Graphviz Dot File](https://github.com/esd-org-uk/human-services/raw/master/Resources/ApplicationProfileERD.gv). Manually generated tidied up version of the [Application profile ERD](https://github.com/esd-org-uk/human-services/raw/master/Resources/LGA_ApplicationProfileBasicEntityRelationshipDiagram.png). [Lucid Charts ERD File](https://github.com/esd-org-uk/human-services/raw/master/Resources/ApplicationProfileERD.csv)
6. [Code to generate JSON schema](https://github.com/esd-org-uk/human-services/tree/master/SchemaGenerator) for “get” for any class
7. JSON schema for:
  - Service - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/service.schema.json) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/service.schema.verbose.json)
  - Organization - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/organization.schema.json) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/organization.schema.verbose.json)
  - Location - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/location.schema.json) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/location.schema.verbose.json)
  - Review - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/review.schema.json) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/review.schema.verbose.json)
8. [Code to generate CSV schema](https://github.com/esd-org-uk/human-services/tree/master/SchemaGenerator) for any class
9.  CSV schema for:
  - Service - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/service.schema.csv) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/service.schema.verbose.csv)
  - Organization - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/organization.schema.csv) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/organization.schema.verbose.csv)
  - Location - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/location.schema.csv) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/location.schema.verbose.csv)
  - Review - [simple](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/review.schema.csv) [verbose](https://raw.githubusercontent.com/esd-org-uk/human-services/master/Schemas/review.schema.verbose.csv)

*Simple* schemas define the properties of a class (eg a service) and any other class associated via a many-to-one relationship (eg the organization delivering a service). *Verbose* schemas also include classes associated via a one-to-many relationship (eg service reviews). The “many” properties are expressed as arrays in JSON and expected to be pipe-delimited in CSV.

We also provide pluralised versions of the JSON schemas defining the structure of responses to web methods like getServices.

CSV schemas are expressed in the [CSV format](https://validator.opendata.esd.org.uk/csvschema) used by the LGA’s data validator. We’ll also provide [CSV on the Web](https://www.w3.org/TR/tabular-data-primer/) format schemas if there is much demand for them.

## Human Services LGA Application profile documentation
The [auto-generated documentation for the application profile](http://htmlpreview.github.io/?https://github.com/esd-org-uk/human-services/blob/master/Schemas/documentation.html) gives the names and descriptions of the objects and fields, our extensions and application profile details such as allowed values and required/optional taxonomies.

## The schema generator
Documentation is generated using this command: 
>Generator.exe --type=html --filter=2 --verbose=1 --title=documentation

The parameters  can have the following values.

- type
  - gv = ERD in Graphviz format
  - erd = ERD in LucidChart CSV format
  - json = JSON Schema
  - table = JSON Table Schema
  - csv = CSV Schema
  - sql = Create Table Statements
  - html = HTML documentation
- filter
  - 0 = All
  - 1 = Open Referral
  - 2 = Service Directory
- verbose - 1 if the output should be verbose
- title - the title of the output file
- multiple - 1 if the initial object should represented as an array
- datapackage - the location of the data package to process. If none is provided the default data package is used.

To get all the available parameters along with help call: 
>Generator.exe --help 

You can get the latest version of the generator software [here](https://github.com/esd-org-uk/human-services/blob/master/SchemaGenerator/Releases/Generator.1.0.0.zip).
