############
Contribution
############

:Semantic name:: https://openminds.ebrains.eu/core/Contribution

Structured information on the contribution made to a research product.


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

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contributor
   :value type: | linked object of type
                | `Consortium <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/consortium.html>`_, `Organization <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/organization.html>`_ or `Person <https://openminds-documentation.readthedocs.io/en/latest/specifications/core/actors/person.html>`_
   :instructions: Add all types of contribution made by the stated 'contributor'.

`BACK TO TOP <Contribution_>`_

------------

.. _type_heading:

****
type
****

Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/type
   :value type: | linked object array \(1-N\) of type
                | `ContributionType <https://openminds-documentation.readthedocs.io/en/latest/specifications/controlledTerms/contributionType.html>`_
   :instructions: Add the party that performed the contribution.

`BACK TO TOP <Contribution_>`_

------------

