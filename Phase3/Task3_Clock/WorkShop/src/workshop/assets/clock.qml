import QtQuick
import QtQuick.Shapes

Item {
    id: root

    width: 500
    height: 500

    required property var clockData

    property int hours: clockData.hours
    property int minutes: clockData.mins
    property int seconds: clockData.secs

    Rectangle {
        id: clockFace

        anchors.centerIn: parent

        width: Math.min(parent.width, parent.height) * 0.92
        height: width
        radius: width / 2

        color: "black"

        border.width: 12
        border.color: "#555555"



        Repeater {
            model: 60

            delegate: Item {
                required property int index

                width: clockFace.width
                height: clockFace.height

                anchors.centerIn: parent

                rotation: index * 6

                Rectangle {
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 12

                    width: index % 5 === 0 ? 5 : 2
                    height: index % 5 === 0 ? 17 : 9

                    color: "white"
                }
            }
        }


        Repeater {
            model: 12

            delegate: Item {
                required property int index

                width: clockFace.width
                height: clockFace.height

                anchors.centerIn: parent

                rotation: index * 30

                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 18

                    text: index === 0 ? 12 : index

                    color: "white"

                    font.pixelSize: 22
                    font.bold: true

                    rotation: -index * 30

                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
        }


        Item {
            id: hourHand

            width: 8
            height: clockFace.height * 0.24

            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.verticalCenter

            transformOrigin: Item.Bottom

            rotation: (root.hours + root.minutes / 60) * 30

            Shape {
                anchors.fill: parent

                ShapePath {
                    strokeColor: "white"
                    strokeWidth: 8

                    startX: hourHand.width / 2
                    startY: hourHand.height

                    PathLine {
                        x: hourHand.width / 2
                        y: 0
                    }
                }
            }
        }


        Item {
            id: minuteHand

            width: 5
            height: clockFace.height * 0.36

            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.verticalCenter

            transformOrigin: Item.Bottom

            rotation: root.minutes * 6

            Shape {
                anchors.fill: parent

                ShapePath {
                    strokeColor: "white"
                    strokeWidth: 5

                    startX: minuteHand.width / 2
                    startY: minuteHand.height

                    PathLine {
                        x: minuteHand.width / 2
                        y: 0
                    }
                }
            }
        }



        Item {
            id: secondHand

            width: 3
            height: clockFace.height * 0.42

            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.verticalCenter

            transformOrigin: Item.Bottom

            rotation: root.seconds * 6

            Shape {
                anchors.fill: parent

                ShapePath {
                    strokeColor: "red"
                    strokeWidth: 3

                    startX: secondHand.width / 2
                    startY: secondHand.height

                    PathLine {
                        x: secondHand.width / 2
                        y: 0
                    }
                }
            }
        }



        Rectangle {
            anchors.centerIn: parent

            width: 22
            height: 22
            radius: 11

            color: "white"
        }
    }
}