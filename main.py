from console import (
    Boolean,
    Complex,
    Dictionary,
    Float,
    Integer,
    List,
    NoneValue,
    Set,
    String,
    Tuple,
)


def main() -> None:
    print(Boolean(True))
    print(Integer(10) + Integer(5))
    print(Float(3.5) * Float(2))
    print(String("hola").upper())
    print(List([1, 2, 3]))
    print(Dictionary({"name": "Python"}))
    print(Set({1, 2, 3}))
    print(Tuple((1, 2, 3)))
    print(Complex(2 + 3j).magnitude())
    print(NoneValue())


if __name__ == "__main__":
    main()
