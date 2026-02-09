class Shape:
    __shape_count = 0  # 类变量，记录所有图形创建数量

    def __init__(self):
        self.__area = 0
        Shape.__shape_count += 1

    def __calc_area(self):
        """私有方法：计算面积（基类默认实现）"""
        return 0

    def get_area(self):
        """公开方法：获取面积"""
        self.__area = self.__calc_area()
        return self.__area

    @classmethod
    def get_shape_count(cls):
        """类方法：获取图形总数"""
        return cls.__shape_count


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius  # 实例变量存储尺寸

    def __calc_area(self):
        """重写面积计算逻辑（多态）"""
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def __calc_area(self):
        """重写面积计算逻辑（多态）"""
        return self.width * self.height


# 测试代码
if __name__ == "__main__":
    # 创建图形实例
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    # 通过公开方法获取面积
    print(f"圆形面积: {circle.get_area():.2f}")
    print(f"矩形面积: {rectangle.get_area()}")
    print(f"图形总数: {Shape.get_shape_count()}")

    # 验证封装性
    try:
        print(circle.__area)  # 会报错
    except AttributeError as e:
        print(f"封装验证: 无法直接访问私有属性 - {e}")