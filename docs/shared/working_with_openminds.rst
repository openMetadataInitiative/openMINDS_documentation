######################
Working with openMINDS
######################

openMINDS provides a flexible and modular metadata framework that combines general, cross-domain graph structures with domain-specific schemas describing various aspects of scientific research.

Due to this breadth, it is neither practical nor necessary to consider the full schema model at once. Instead, openMINDS is typically approached through smaller, logically coherent substructures.

This section introduces the terminology and concepts needed to navigate the openMINDS schema model and to identify such substructures for representing different types of research objects as linked metadata graphs.

Terminology
###########

To work effectively with openMINDS, it is important to distinguish between the following concepts:

- **openMINDS schema model**: the complete set of schemas forming a fully connected logical graph (schema graph)  
- **openMINDS schema submodel**: a subset of schemas forming a coherent logical subgraph of the overall model  
- **openMINDS schema module**: a group of thematically related schemas maintained together (in a GitHub repository), structured according to openMINDS dependency rules  
- **openMINDS instance**: an instantiation of a specific schema type representing a node in the metadata graph  
- **openMINDS metadata collection**: a set of interconnected instances forming a metadata graph  

The relationship between these concepts can be summarized as follows:

The openMINDS schema model defines the schema graph, i.e., the logical structure of schema types and their relations.

Metadata collections represent metadata graphs composed of concrete instances that follow and realize this structure.

Modular application of openMINDS
################################

Rather than working with the full schema model, openMINDS is typically applied through submodels. Each submodel is defined by an entry-point schema and its associated dependency tree, i.e., the chain of all schemas linked or embedded through required properties.

This approach allows users to construct metadata graphs tailored to a specific use case without requiring implementation of the entire model.

To support this modular application, the openMINDS schema model is organized into modules that group schemas according to their role and dependencies.

At a high level, two types of modules can be distinguished:

- **essential modules**: define the general structure of metadata descriptions. The core module provides the main entry points for general research product descriptions, while the controlledTerms module provides standardized terminologies that typically serve as descriptive endpoints of the model  
- **extension modules**: provide modality- or technique-specific detail. They build on the core module and make use of controlledTerms to extend metadata descriptions for specific domains  

The set of available extension modules is version-dependent and expands over time as new domains and use cases are covered.

----

The following pages introduce selected openMINDS submodels and demonstrate how they are applied in practice to represent different types of research objects as linked metadata graphs.
