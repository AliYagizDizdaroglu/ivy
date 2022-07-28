# global
from typing import Optional, Union, Tuple
import abc

# local
import ivy

# ToDo: implement all methods here as public instance methods


class ArrayWithStatistical(abc.ABC):
    def min(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        """
        Examples
        --------
        With: code:`ivy.Array`
        input:

        >> > x = ivy.array([1, 2, 3])
        >> > z = x.min()
        >> > print(z)
        ivy.array(3)

        >> > x = ivy.array([0, 1, 2])
        >> > z = ivy.array([0, 0, 0])
        >> > y = ivy.min(x, out=z)
        >> > print(z)
        ivy.array(2)

        >> > x = ivy.array([[0, 1, 2], [4, 6, 10]])
        >> > y = ivy.min(x, 0, True)
        >> > print(y)
        ivy.array([[4, 6, 10]])

        >> > x = ivy.native_array([[0, 1, 2], [4, 6, 10]])
        >> > y = ivy.min(x)
        >> > print(y)
        ivy.array(10)

        With: code:`ivy.Container`
        input:

        >> > x = ivy.Container(a=ivy.array([0., 1., 2.]), b=ivy.array([3., 4., 5.]))
        >> > y = ivy.min(x)
        >> > print(y)
        {
            a: ivy.array(2.),
            b: ivy.array(5.)
        }

        >> > x = ivy.Container(a=ivy.array([1, 2, 3]), \
                               b=ivy.array([2, 3, 4]))
        >> > z = x.min()
        >> > print(z)
        {
            a: ivy.array(3),
            b: ivy.array(4)
        }
        """
        return ivy.min(self._data, axis, keepdims, out=out)

    def max(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.max(self._data, axis, keepdims, out=out)

    def mean(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.mean(self._data, axis, keepdims, out=out)

    def var(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        correction: Union[int, float] = 0.0,
        keepdims: bool = False,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.var(self._data, axis, correction, keepdims, out=out)

    def prod(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False,
        *,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.prod(self._data, axis, keepdims, dtype=dtype, out=out)

    def sum(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        keepdims: bool = False,
        *,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.sum(self._data, axis=axis, dtype=dtype, keepdims=keepdims, out=out)

    def std(
        self: ivy.Array,
        axis: Union[int, Tuple[int]] = None,
        correction: Union[int, float] = 0.0,
        keepdims: bool = False,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.std(self._data, axis, correction, keepdims, out=out)

    def einsum(
        self: ivy.Array,
        equation: str,
        *,
        out: Optional[ivy.Array] = None,
    ) -> ivy.Array:
        return ivy.einsum(equation, self._data, out=out)
