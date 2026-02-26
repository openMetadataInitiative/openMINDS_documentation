#################
DeployedInterface
#################

:Semantic name: https://openminds.om-i.org/types/DeployedInterface

:Display as: Deployed interface


------------

------------

Properties
##########

:Required: `accessibility <accessibility_heading_>`_, `interface <interface_heading_>`_, `location <location_heading_>`_
:Optional:

------------

.. _accessibility_heading:

*************
accessibility
*************

Level to which something is accessible to someone or something.

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/accessibility
   :value type: | linked object of type
                | `Accessibility <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/accessibility.html>`_
   :instructions: Add the accessibility of this deployed interface.

`BACK TO TOP <DeployedInterface_>`_

------------

.. _interface_heading:

*********
interface
*********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/interface
   :value type: | linked object of type
                | `InterfaceVersion <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/products/interfaceVersion.html>`_
   :instructions: Enter the interface version that is deployed.

`BACK TO TOP <DeployedInterface_>`_

------------

.. _location_heading:

********
location
********

.. admonition:: schema_specifications

   :semantic name: https://openminds.om-i.org/props/location
   :value type: | linked object of type
                | `Location <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/location.html>`_ or `WebResource <https://openminds-documentation.readthedocs.io/en/latest/schema_specifications/core/miscellaneous/webResource.html>`_
   :instructions: Add the location (for physical services) or URL (for digital services) where this deployed interface may be accessed.

`BACK TO TOP <DeployedInterface_>`_

------------

