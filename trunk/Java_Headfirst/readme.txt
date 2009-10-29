创建可执行的JAR
    1 确定所有的类文件都在classes目录下
    2 创建manifest.txt来描述哪个类带有main()方法
        该文件带有下面这一行：
        Main-Class: MySpp //后面没有.class
        在次行后面都要换行，否则有可能出错。将此文件放在classes目录下
    3 执行jar工具来创建带有所有类以及manifest的jar文件
        %cd MiniProject/classes
        %jar -cvmf manifest.txt app1.jar *.class
        或
        %jar -cvmf manifest.txt app1.jar MyApp.class
执行jar
    %java -jar app1.jar
