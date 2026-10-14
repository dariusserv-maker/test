# Two-pump rotation FBD

IEC FBD review diagram based on the two-pump specification: nine ordered networks, named signal connectors, and directional wires.

- [Editable diagrams.net diagram](pump_rotation_fbd.drawio)
- [SVG diagram](pump_rotation_fbd.svg)
- [PDF: one network per page](pump_rotation_fbd.pdf)
- [All formats in a ZIP archive](pump_rotation_fbd.zip)

Download the ZIP through GitHub's **Raw / Download raw file** action. Open the `.drawio` file in diagrams.net with **File > Open From > Device**.

Legend: `LeadPump = 1` selects Pump1; `LeadPump = 2` selects Pump2. `LeadPump` is RETAIN; `RotationTime` is adjustable. The cyclic task period is 100 ms.

Validation: XML parsing, nine mxGraph pages, edge references, SVG parsing, and PDF rendering passed. An abstract block-graph evaluator checked 50,000 randomized scans without simultaneous RUN commands. This is not Schneider compilation or PLC simulation. Live diagrams.net import was not tested because network access to that site was blocked.

This package is a visual design artifact, not a Machine Expert HVAC project or a verified TM172PDG42R executable. No physical I/O mapping or PLC download was performed.
