**Note**: This is a draft for text to be added to the ReadTheDocs documentation pages

openMINDS pipelines
===================

openMINDS pipelines are specialized branches within a subset of the repositories in the openMetadataInitiative organization. The purpose of these branches is to build an up-to-date version of schemas or derived schema representations. Pipelines are triggered by a set of GitHub Actions workflows whose job it is to ensure the continual synchronization of interdependent repositories.

We’ll first outline the different repository types in the openMetadataInitiative organization before we describe the existing workflows and the pipeline branches in more detail.

Repository types
----------------

There are three types of repositories in the Open Metadata Initiative Organization:
  
1. "Module" repositories
2. "Central" repository
3. "Target" repositories

Module Repositories
~~~~~~~~~~~~~~~~~~~

These repositories represent individual openMINDS metadata modules, for example `openMINDS_core`_ or `openMINDS_SANDS`_. It also includes the `openMINDS_instances`_ repository which is a library of controlled metadata instances for metadata schemas/types of the various openMINDS modules. Development of openMINDS schemas (and instances) will happen on these module repositories, and any suggestion for a schema modification should happen through a Pull Request to the respective repository.

.. _openMINDS_core: https://github.com/openMetadataInitiative/openMINDS_core
.. _openMINDS_SANDS: https://github.com/openMetadataInitiative/openMINDS_SANDS
.. _openMINDS_instances: https://github.com/openMetadataInitiative/openMINDS_instances

Central repository
~~~~~~~~~~~~~~~~~~

The **central** repository (`openMINDS`_) contains schemas for the full openMINDS model in the omi.json format. These schemas are extended and “resolved” [link to description of the tpl.json and omi.json formats] variants of the schema templates found in the respective **module** repositories. The **central** repository should be considered the ground truth for schemas.

.. _openMINDS: https://github.com/openMetadataInitiative/openMINDS

Target repositories
~~~~~~~~~~~~~~~~~~~

**Target** repositories are repositories that depend on the ground truth schemas in the **central** repository. Examples include `openMINDS_Python`_, `openMINDS_MATLAB`_, `openMINDS_Java`_, and `openMINDS_documentation`_. These repositories should be updated whenever changes are made to the ground truth schemas, i.e., the **central** `openMINDS`_ repository.

.. _openMINDS_Python: https://github.com/openMetadataInitiative/openMINDS_Python
.. _openMINDS_MATLAB: https://github.com/openMetadataInitiative/openMINDS_MATLAB
.. _openMINDS_Java: https://github.com/openMetadataInitiative/openMINDS_Java
.. _openMINDS_documentation: https://github.com/openMetadataInitiative/openMINDS_documentation

Repository dependencies
-----------------------

The **central** repository depends on each of the **module** repositories, and the **target** repositories all depend on the **central** repository. Once any of the **module** repositories have a new commit (push), they trigger the build process of **central** which aggregates the information across all of those **modules** and merges them in a single (versioned) view. Once this is done, the **target** build pipelines are triggered to then consume the centrally provided information to build their "language-specific" products.

Overview of Workflows
---------------------

There are currently two types of GitHub Actions workflows, ``openMINDS_upstream``, and ``build``.

openMINDS_upstream (module repositories)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each of the module repositories has a workflow called ``openMINDS_upstream``. This workflow is triggered whenever something is pushed to the respective repository (todo: mention version branches), and it has a single job which is to trigger the build pipeline of the **central** repository. An example of such a workflow is found `here`_.

.. _here: https://github.com/openMetadataInitiative/openMINDS_core/blob/e873947bd8cae1de08aebd3ecc59a1c81d218cb3/.github/workflows/openMINDS_upstream.yml

openMINDS_upstream (central repository)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a push is made on the ``main`` branch of the **central** `openMINDS`_ repository, the **central** ``openMINDS_upstream`` workflow is triggered. This workflow has a single job which is to trigger the ``build`` workflow of each of the **target** repositories.

Suggestion: rename ``openMINDS_upstream`` of **central** repo to ``openMINDS_trigger_targets``

Build (central and target repositories)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **central** repository (`openMINDS`_) and the **target** repositories have a branch called ``pipeline`` that contains the ``build`` workflow and the build routines for that repository. When the ``build`` workflow is triggered, the build routines will execute and the built product is pushed to the ``main`` branch of the respective repository.

Workflow example flow
---------------------

Let's say a modification of a schema in the core module is pushed onto `openMINDS_core`_. This will trigger the following series of workflows:

1. The ``openMINDS_upstream`` workflow of the `openMINDS_core`_ repository is triggered, which in turn triggers the ``build`` workflow of the **central** `openMINDS`_ repository’s ``pipeline`` branch.
2. The ``build`` workflow of the **central** repository executes and pushes an updated version onto the ``main`` branch.
3. The ``openMINDS_upstream`` workflow of the **central** repository is triggered, which in turn triggers the ``build`` workflows of each of the **target** repositories.
4. The ``build`` workflows of the **target** repositories execute and the changes are pushed onto the ``main`` repository branches.

The result of this series of workflows is that both the **central** and the **target** repositories are updated with the latest change from the core module.

For target repository developers
--------------------------------

1. All **target** repositories should have a ``pipeline`` branch whose responsibility it is to build schema representations from the ground-truth schemas of the **central** repository. At the moment the best way to get started is to explore the pipeline branches of one or more existing **target** repositories.
2. The `openMINDS_upstream.yml`_ of the **central** `openMINDS`_ repository must be updated to trigger the ``build`` workflow on the ``pipeline`` branch of the **target** repository.

.. _openMINDS_upstream.yml: https://github.com/openMetadataInitiative/openMINDS/blob/main/.github/workflows/openMINDS_upstream.yml

For module repository developers
----------------------------------------

There must be an ``openMINDS_upstream`` workflow (todo: add link to example from one of the module repositories).
