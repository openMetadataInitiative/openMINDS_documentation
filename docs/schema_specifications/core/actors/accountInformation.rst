##################
AccountInformation
##################

:Semantic name: core:AccountInformation

:Display as: Core:account information


------------

------------

Properties
##########

:Required: `service <service_heading_>`_, `userName <userName_heading_>`_
:Optional:

------------

.. _service_heading:

*******
service
*******

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/service
   :value type: | linked object of type
                | core:WebService \[TYPE_ERROR\]
   :instructions: Add the web service of this account.

`BACK TO TOP <AccountInformation_>`_

------------

.. _userName_heading:

********
userName
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.ebrains.eu/vocab/userName
   :value type: | string
                | formatting: text/plain; singleline
   :instructions: Enter the user name for this account.

`BACK TO TOP <AccountInformation_>`_

------------

