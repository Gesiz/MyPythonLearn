# TODO 导入模块下的所有资源
# 不管是from导入还是import导入效果是一样的
# 当第一导入模块的时候，这个模块会从上到下的执行
# 以后导入就不会执行了

import module1

# 只在第一导入的时候会执行
# import module1
# import module1
# import module1
# import module1

print('main的代码在执行')


