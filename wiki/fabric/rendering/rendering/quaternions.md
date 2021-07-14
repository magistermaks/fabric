## Quaternions
[Back](rendering.md)

Quaternions are used to represent rotation in 3D space, they avoid the [Gimbal Lock](https://en.wikipedia.org/wiki/Gimbal_lock) problem that can occur when using roll, pitch and yaw. Quaternions rely on some fairly complicated math, because of that most people treat them as "black-boxes", and use them without understanding the math involved.

```java
// to rotate around the Y axis:
Vec3f.POSITIVE_Y.getDegreesQuaternion(degrees); // or:
Vec3f.POSITIVE_Y.getRadialQuaternion(radians);
```

The same can be done for `POSITIVE_X` axis, and `POSITIVE_Z` axis.

Example:
```java
// rotate matrix on all 3 axis
matrices.multiply( Vec3f.POSITIVE_X.getDegreesQuaternion(60) );
matrices.multiply( Vec3f.POSITIVE_Y.getDegreesQuaternion(60) );
matrices.multiply( Vec3f.POSITIVE_Z.getDegreesQuaternion(60) );
```

Learn about matrices here: [Matrices](matrices.md)
