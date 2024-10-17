############
Contribution
############

:Semantic name: core:Contribution

:Display as: Core:contribution


------------

------------

Properties
##########

:Required: `contributor <contributor_heading_>`_, `type <type_heading_>`_
:Optional:

------------

.. _contributor_heading:

***********
contributor
***********

Legal person that gave or supplied something as a part or share.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contributor
   :value type: | linked object of type
                | core:Consortium \[TYPE_ERROR\], core:Organization \[TYPE_ERROR\] or core:Person \[TYPE_ERROR\]
   :instructions: Add all types of contribution made by the stated 'contributor'.

`BACK TO TOP <Contribution_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object array \(1-N\) of type
                | controlledTerms:ContributionType \[TYPE_ERROR\]
   :instructions: Add the party that performed the contribution.

`BACK TO TOP <Contribution_>`_

------------

