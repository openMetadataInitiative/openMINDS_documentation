Example-02
==========

Let us become more scientific in our next example and demonstrate for two fictional case scenarios how information on research subjects stored in a tabular format (e.g., as CSV) can be extracted into openMINDS compliant graph structured metadata instances.

For the first case scenario, we assume that five adult research subjects, each of a different species, were imaged once while awake, and (at least for some) were imaged a second time while asleep. The metadata structurally describing this information is stored in the following CSV file: 

.. csv-table:: subjects_case01.csv
   :file: ../../_static/test-data/subjects_case01.csv
   :widths: 10, 10, 10, 10, 10
   :header-rows: 1

Based on this information, we know that we will have to create five "Subject" instances and one to two "SubjectState" instances. In addition, we know that we will not have to create instances for defining the species, the age category or the subject attribute describing the state of the subject when it was imaged, because these instances are already available through the openMINDS libraries. Translating this tabular information into a graph structured openMINDS metadata collection using Python could look like this:

.. code-block:: python

   # import packages
   from openminds import Collection
   import csv
   import openminds.latest.core as omcore

   # Create an empty metadata collection
   collection = Collection()

   # read csv file to a list of dictionaries
   with open('subjects_case01.csv', 'r') as f:
       csv_reader = csv.DictReader(f)
       data = [row for row in csv_reader]
   f.close()

   # create subject instances with their respective states
   subjects = {}
   for d in data:
      subjects[d["subject_ID"]] = omcore.Subject(
         internal_identifier = d["subject_ID"]
         )

   # adding instances to collection
   # (remember: linked instances are automatically added)
   for s in subjects: 
       collection.add(s) 

   failures = collection.validate()

   if not failures:
       collection.save("my_collection.jsonld")

For the second case scenario, we assume that another five adult research subjects, where we pretend to have the general knowledge that all subjects are rhesus macaques (Macaca mulatta), and participated in a behavioral experiment while being an infant, a juvenile and an adult. Instead of the exact age of each monkey, the body weight was measured before each behavioral experiment:   

.. csv-table:: subjects_case02.csv
   :file: ../../_static/test-data/subjects_case02.csv
   :widths: 10, 10, 10, 10, 10
   :header-rows: 1

Based on this information, we know that we will have again to create five "Subject" instances, each with three "SubjectState" instances. In addition, we know that we will not have to create instances for defining the species, the age category or the unit of measurement of the subject's body weight, because these instances are already available through the openMINDS libraries. Translating this tabular information into a graph structured openMINDS metadata collection using Python could look like this:

.. code-block:: python

   # import packages
   from openminds import Collection
   import csv
   import openminds.latest.core as omcore

   # Create an empty metadata collection
   collection = Collection()

   # read csv file to a list of dictionaries
   with open('subjects_case02.csv', 'r') as f:
       csv_reader = csv.DictReader(f)
       data = [row for row in csv_reader]
   f.close()

   # create subject instances with their respective states
   subjects = {}
   for d in data:
      subjects[d["subject_ID"]] = omcore.Subject(
         internal_identifier = d["subject_ID"]
         )

   # adding instances to collection
   # (remember: linked instances are automatically added)
   for s in subjects: 
       collection.add(s) 

   failures = collection.validate()

   if not failures:
       collection.save("my_collection.jsonld")
