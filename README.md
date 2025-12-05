# nuttx-testing

This repository contains test cases compatible with the NTFC tool for
Apache NuttX RTOS. For details, please visit the NTFC repository.

### Preparing the image for testing

NuttX image requirements for tests:

- ``CONFIG_DEBUG_SYMBOLS`` must be set.

- NSH must be enabled and set as entry point

- ``CONFIG_DEBUG_FEATURES=y`` and ``CONFIG_DEBUG_ASSERTIONS=y``
  are recommended.
