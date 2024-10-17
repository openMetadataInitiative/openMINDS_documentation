#######
Funding
#######

:Semantic name: core:Funding

:Display as: Core:funding


------------

------------

Properties
##########

:Required: `funder <funder_heading_>`_
:Optional: `acknowledgement <acknowledgement_heading_>`_, `awardNumber <awardNumber_heading_>`_, `awardTitle <awardTitle_heading_>`_

------------

.. _acknowledgement_heading:

***************
acknowledgement
***************

Official declaration or avowal of appreciation of an act or achievement.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/acknowledgement
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the acknowledgement that should be used with this funding.

`BACK TO TOP <Funding_>`_

------------

.. _awardNumber_heading:

***********
awardNumber
***********

Machine-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/awardNumber
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the associated award number of this funding.

`BACK TO TOP <Funding_>`_

------------

.. _awardTitle_heading:

**********
awardTitle
**********

Human-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/awardTitle
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the award title of this funding.

`BACK TO TOP <Funding_>`_

------------

.. _funder_heading:

******
funder
******

Legal person that provides money for a particular purpose.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/funder
   :value type: | linked object of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add the party that provided this funding.

`BACK TO TOP <Funding_>`_

------------

