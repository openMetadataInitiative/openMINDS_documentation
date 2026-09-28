#######################################
Terminologies: MRIPulseSequence library
#######################################

Related schema specification: `MRIPulseSequence <https://openminds-documentation.readthedocs.io/en/v5.0/schema_specifications/controlledTerms/MRIPulseSequence.html>`_

------------

------------

T2-starPulseSequence
--------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/T2-starPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence that is optimized to measure the effective spin-spin relaxation time (T2-star).
   :name: T2-star pulse sequence
   :synonym: T2* pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

T2PulseSequence
---------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/T2PulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence that is optimized to measure the spin-spin relaxation time (T2).
   :name: T2 pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

echoPlanarPulseSequence
-----------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/echoPlanarPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance image pulse sequence that is composed of multiple echoes at different phase steps (often collected blocks of 64 or 128 phase steps), which are acquired using rephasing gradients where rephasing is achieved by rapidly reversing the readout or frequency-encoding gradient.
   :name: echo planar pulse sequence
   :synonym: echo-planar imaging

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

fastLowAngleShotPulseSequence
-----------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/fastLowAngleShotPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A gradient echo pulse sequence that combines a low-flip angle radio-frequency excitation of the nuclear magnetic resonance signal (recorded as a spatially encoded gradient echo) with a short repetition time. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Fast_low_angle_shot_magnetic_resonance_imaging)]
   :name: fast low angle shot pulse sequence
   :synonym: FLASH, FLASH pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

fastSpinEchoPulseSequence
-------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/fastSpinEchoPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance image pulse sequence that collects multiple echos instead of a single echo during a spin echo pulse sequence, multiple echos are recorded for each 90-degree pulse by using multiple 180-degree inversion pulses with slightly different phase encoding gradients.
   :name: fast spin echo pulse sequence
   :synonym: FSE, FSE imaging, FSE pulse sequence, TSE, TSE imaging, TSE pulse sequence, fast spin-echo imaging, turbo spin echo, turbo spin-echo imaging

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

fluidAttenuatedInversionRecoveryPulseSequence
---------------------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/fluidAttenuatedInversionRecoveryPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A special inversion recovery pulse sequence where the inversion time is adjusted such that at equilibrium there is no net transverse magnetization of fluid in order to null the signal from fluid in the resulting image.
   :name: fluid attenuated inversion recovery pulse sequence
   :synonym: FLAIR, FLAIR pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

gradientEchoPulseSequence
-------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/gradientEchoPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence composed of one or more radio frequency pulses that are usually less than 90 degrees interleaved with the application of a spatial magnetic field gradient.
   :name: gradient-echo pulse sequence
   :synonym: GRE pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

inversionRecoveryPulseSequence
------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/inversionRecoveryPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence composed of a 180-degree radiofrequency pulse, followed by a spin echo pulse sequence.
   :name: inversion recovery pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

magnetizationTransferPulseSequence
----------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/magnetizationTransferPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A combination of two radiofrequency pulses, the first off-resonance, the second in resonance with the Larmor frequency of free-water protons.
   :name: magnetization transfer pulse sequence
   :synonym: MT pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

multi-echoPulseSequence
-----------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/multi-echoPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence composed of multiple gradient reversals following a single radiofrequency pulse.
   :name: multi-echo pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

saturationRecoveryPulseSequence
-------------------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/saturationRecoveryPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence composed of multiple slice selective 90-degree radiofrequency pulses at regular intervals delayed to allow the recovery of all the longitudinal magnetization before another pulse is applied.
   :name: saturation recovery pulse sequence
   :otherOntologyIdentifier: http://uri.interlex.org/base/ilx_0110354
   :preferredOntologyIdentifier: http://uri.interlex.org/base/ilx_0110354
   :synonym: SR pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

spinEchoPulseSequence
---------------------

.. admonition:: metadata sheet

   :@context: @vocab: <https://openminds.om-i.org/props/>
   :@id: https://openminds.om-i.org/instances/MRIPulseSequence/spinEchoPulseSequence
   :@type: https://openminds.om-i.org/types/MRIPulseSequence
   :definition: A magnetic resonance imaging pulse sequence composed of a slice selective 90-degree pulse followed by one or more (for fast spin echo sequences) 180-degree refocusing pulses.
   :name: spin echo pulse sequence
   :synonym: SE pulse sequence

`BACK TO TOP <Terminologies: MRIPulseSequence library_>`_

------------

