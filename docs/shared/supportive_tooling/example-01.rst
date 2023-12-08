Example-01
==========

Let use pick up again the example we used in getting started and assume we locally stored information about the Heart of Gold Spacecraft Crew as Comma Separated Values:

.. csv-table:: persons.csv
   :file: ../../_static/test-data/persons.csv
   :widths: 10, 10, 10, 10, 10
   :header-rows: 1

We will now guide you through the process of how to represent this data table as linked data in openMINDS using the openMINDS Python library.

Let us start by importing the necessary packages, initiating an empty openMINDS linked data collection, and loading the rows of the data table as a list of Python dictionaries whose keys are given by the table header:

.. code-block:: python

   # import packages
   from openminds import Collection
   import csv
   import openminds.latest.core as omcore

   # Create an empty metadata collection
   collection = Collection()

   # read csv file to a list of dictionaries
   with open('persons.csv', 'r') as f:
       csv_reader = csv.DictReader(f)
       data = [row for row in csv_reader]
   f.close()

Next let us map the data to the matching linked data instances. For this we will create for each dictionary in data:
+ a "Person" instance with the provided "givenName" and "familyName"
+ a "ContactInformation" instance with "email" (if provided) and link it to the respective "Person" instance
+ an "Affiliation" instance which is embeded into the respective "Person" instance
+ link in each "Affiliation" instance the respective "Consortium" instance which full name is provided in "memberOf" 

Note: we need to assume that the persons may be members of the same consortium, therefore we start creating a unique set of "Consortium" instances (following the logic: same full name, same consortium).

.. code-block:: python

   # extract data to create dictionary with unique "Consortium" instances
   consortia = {}
   for d in data:
       if d['memberOf'] not in consortia:
           consortia[d['memberOf']] = omcore.Consortium(
               id = f"_:{d['memberOf'].replace(' ', '-').lower()}",
               full_name = d['memberOf']
           )

   # extract data to create dictionary with "ContactInformation" instances
   contacts = {}
   for d in data:
       if d['email'] not in contacts and d['email'] != '':
           contacts[d['email']] = omcore.ContactInformation(
               id = f"_:{d['email']}",
               email = d['email']
           )

   # extract data to create dictionary with "Person" instances where each "Person" instance
   # will link to their respective "ContactInformation" instance
   # embed an "Affiliation" instance that links to the respective "Consortium" instance
   persons = []
   for d in data:
       full_name = " ".join([d['givenName'], d['familyName']
       persons.append(omcore.Person(
           id = f"_:{full_name.replace(' ', '-').lower()}",
           given_name = d['givenName'],
           family_name = d['familyName'],
           alternate_name = d['alternateName'] if d['alternateName'] != '' else None,
           contactInformation = contacts[d'email'],
           affiliations = omcore.Affiliation(member_of=consortia[d['memberOf']])
       )

   

