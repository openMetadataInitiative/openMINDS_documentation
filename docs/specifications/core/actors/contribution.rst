############
Contribution
############

https://openminds.ebrains.eu/core/Contribution
----------------------------------------------

Structured information on the contribution made to a research product.

------------

------------

**********
Properties
**********

:Required: `contributionType <contributionType_heading_>`_, `contributor <contributor_heading_>`_
:Optional:

------------

.. _contributionType_heading:

contributionType
----------------

Distinct class of what was given or supplied as a part or share.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contributionType
   :value type: | linked object array \(1-N\) of type
                | `ContributionType <https://openminds.ebrains.eu/controlledTerms/ContributionType>`_
   :instructions: Add one or several type of contributions made by the stated contributor.

`BACK TO TOP <Contribution_>`_

------------

.. _contributor_heading:

contributor
-----------

Legal person that gave or supplied something as a part or share.

.. admonition:: specifications

   :semantic name: https://openminds.ebrains.eu/vocab/contributor
   :value type: | linked object of type
                | `Organization <https://openminds.ebrains.eu/core/Organization>`_ or `Person <https://openminds.ebrains.eu/core/Person>`_
   :instructions: Add the contributing person or organization.

`BACK TO TOP <Contribution_>`_

------------

