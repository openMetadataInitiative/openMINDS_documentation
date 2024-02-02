Example-02
==========

Let us become more scientific in our next example and demonstrate how information on research subjects that was stored in a tabular format (e.g., as CSV) can be extracted into openMINDS compliant graph structured metadata instances.

For the first case scenario, we assume that five adult research subjects, each of a different species, were imaged once while awake, and (at least for some) were imaged a second time while asleep. The metadata structurally describing this information is stored in the following CSV file: 

.. csv-table:: subjects_case01.csv
   :file: ../../_static/test-data/subjects_case01.csv
   :widths: 10, 10, 10, 10, 10
   :header-rows: 1

For the second case scenario, we assume that another five adult research subjects, where we pretend to have the general knowledge that all subjects are rhesus macaques (Macaca mulatta), and participated in a behavioral experiment while being an infant, a juvenile and an adult. Instead of the exact age of each monkey, the body weight was measured before each behavioral experiment at the respective age category:   

.. csv-table:: subjects_case02.csv
   :file: ../../_static/test-data/subjects_case02.csv
   :widths: 10, 10, 10, 10, 10
   :header-rows: 1
