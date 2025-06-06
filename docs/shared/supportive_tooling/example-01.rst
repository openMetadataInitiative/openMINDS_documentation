Example-01
==========

.. raw:: html

   <a class="binder example-01" href="https://mybinder.org/v2/gh/openMetadataInitiative/openMINDS_documentation/main?urlpath=%2Fdoc%2Ftree%2F%2Fdocs%2Fshared%2Fsupportive_tooling%2Fexample-01.ipynb">
      <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
   </a>

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

"data" contains now a list of dictionaries that each contain the values of each cell in one row with the column header of each cell as keys. Next let us create from those data the representative linked data instances. 

Let us assume that "memberOf" provides the full name of a consortium each person is affiliated to.
Since members might be affiliated to the same consortium we assume further that the same full name means the same consortium. 
We can also assume that the "email" is unique for each person.

With these assumptions we will create :

* a unique set of "Consortium" instances based on the full name given under "memberOf" in all dictionaries in data
* a "ContactInformation" instance based on "email" for each dictionary in data
* a "Person" instance for each dictionary in data with:

  * the "givenName", "familyName", and "alternateName" (if available)
  * a link to the respective "ContactInformation" instance
  * a person-specific embedded "Affiliation" instance that links to the respective "Consortium" instance

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
       full_name = " ".join([d['givenName'], d['familyName']])
       persons.append(omcore.Person(
           id = f"_:{full_name.replace(' ', '-').lower()}",
           given_name = d['givenName'],
           family_name = d['familyName'],
           alternate_names = d['alternateName'] if d['alternateName'] != '' else None,
           contact_information = contacts[d['email']],
           affiliations = omcore.Affiliation(member_of=consortia[d['memberOf']])
       ))

As final step, we will add our linked data instances to the collection we initiated in the beginning, validate this collection against the openMINDS metadata models, and save the collection if the validation did not reveal any failures:

.. code-block:: python

   # adding instances to collection
   # we only need to add the "Person" instances, because ...
   # linked instances are added to the collection automatically
   for p in persons: 
       collection.add(p) 

   failures = collection.validate()

   if not failures:
       collection.save("my_collection.jsonld")
