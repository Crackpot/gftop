class ClothingException extends Exception {
    // ClothingException    衣服异常总类
    //      UniformException    制服异常
    //      PantsException    裤子异常
    //      LingerieException    女士内衣异常
    //      ShirtException    衬衫异常总类
    //          TeeShirtException    短袖圆领男衫异常
    //          DressShirtException    衣服衬衫异常
}
class UniformException extends ClothingException{// 制服
}
class PantsException extends ClothingException {// 裤子
}
class LingerieException extends ClothingException {// 女士内衣
}
class ShirtException extends ClothingException {// Shirt
}
class TeeShirtException extends ShirtException {// TeeShirt
}
class DressShirtException extends ShirtException {// DressShirt
}
