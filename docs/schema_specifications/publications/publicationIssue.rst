################
PublicationIssue
################

:Semantic name: publications:PublicationIssue

:Display as: Publications:publication issue


------------

------------

Properties
##########

:Required: `isPartOf <isPartOf_heading_>`_, `issueNumber <issueNumber_heading_>`_
:Optional:

------------

.. _isPartOf_heading:

********
isPartOf
********

Reference to the ensemble of multiple things or beings.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/isPartOf
   :value type: | linked object of type
                | publications:PublicationVolume \[TYPE_ERROR\]
   :instructions: Add the publication volume this publication issue is part of.

`BACK TO TOP <PublicationIssue_>`_

------------

.. _issueNumber_heading:

***********
issueNumber
***********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/issueNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the issue number of this publication issue.

`BACK TO TOP <PublicationIssue_>`_

------------

