TEMPLATE = app
TARGET = accelbubble
QT += quick sensors svg xml
SOURCES = main.cpp

RESOURCES += \
    accelbubble.qrc

OTHER_FILES = \
    $$files(*.qml) \
    content \
    images

target.path = $$[QT_INSTALL_EXAMPLES]/sensors/accelbubble
INSTALLS += target
