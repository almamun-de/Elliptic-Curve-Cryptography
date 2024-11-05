# Elliptic Curve Cryptography (ECC)

## Overview
This project explores the basic properties of elliptic curves, especially in the context of elliptic curve cryptography (ECC). It includes an implementation of point addition and point doubling on an elliptic curve over a finite field.

## Files
- `elliptic_curve.py`: Python script implementing basic elliptic curve operations over a finite field.

## Visualization with JCrypTool
JCrypTool can be used to visualize elliptic curves over both the real numbers and finite fields. This helps in understanding:
- **Point Addition**: How points on a curve can be added geometrically.
- **Point Doubling**: The process of doubling a point on the curve.
- **Finite vs. Continuous Fields**: Differences between curves in finite (discrete) fields and continuous fields.

### Key Concepts
- **Point Addition**: The sum of two points on an elliptic curve.
- **Point Doubling**: Adding a point to itself.
- **Finite Fields**: Calculations are done modulo a prime number, leading to a finite set of points.

## Usage
### Running the Script
The script can be run directly from the command line. It demonstrates:
- Checking if points lie on the curve.
- Performing point addition and doubling.

```bash
python elliptic_curve.py


