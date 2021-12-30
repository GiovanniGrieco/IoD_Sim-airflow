from PySide2.QtCore import Qt, QPointF, QRectF
from PySide2.QtGui import QColor, QPainter, QBrush, QRadialGradient, QLinearGradient, QPen, QPainterPath, QFont
from PySide2.QtWidgets import QStyle

from custom_src.global_tools.math import pythagoras


class NIPainter:

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        pass

    def paint_NI_title_label_default(painter, design_style, title_str, c, pen_w, font, bounding_rect):
        pen = QPen(c)
        pen.setWidth(pen_w)

        painter.setPen(pen)
        painter.setFont(font)

        text_rect = bounding_rect
        text_rect.setTop(text_rect.top()-7)

        if design_style == 'extended':
            painter.drawText(text_rect, Qt.AlignLeft | Qt.AlignVCenter, title_str)
        elif design_style == 'minimalistic':
            painter.drawText(text_rect, Qt.AlignTop | Qt.AlignHCenter, title_str)

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        pass

    def paint_PI_label_default(painter, label_str, c, font, bounding_rect):
        painter.setBrush(Qt.NoBrush)
        pen = QPen(c)
        painter.setPen(pen)
        painter.setFont(font)
        painter.drawText(bounding_rect, Qt.AlignCenter, label_str)


    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        pass

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):
        pass

    def get_header_rect(w, h, title_rect):
        """
        :param w: width
        :param h: height
        """

        header_height = 1.4 * title_rect.height()  # 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-w / 2, -h / 2))
        header_rect.setWidth(w)
        header_rect.setHeight(header_height)
        return header_rect

    def interpolate_color(c1, c2, val):
        r1 = c1.red()
        g1 = c1.green()
        b1 = c2.blue()
        a1 = c1.alpha()

        r2 = c2.red()
        g2 = c2.green()
        b2 = c2.blue()
        a2 = c2.alpha()

        r = (r2 - r1) * val + r1
        g = (g2 - g1) * val + g1
        b = (b2 - b1) * val + b1
        a = (a2 - a1) * val + a1

        return QColor(r, g, b, a)


class NIPainter_Light(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            painter.setPen(QPen(QColor(node_color.name())))
            painter.setFont(QFont('Roboto', 13))
            painter.drawText(bounding_rect, Qt.AlignLeft | Qt.AlignVCenter, title_str)
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('Roboto', 15, QFont.Thin),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#797e82')
        else:
            if exec_type == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Roboto Mono", 10, QFont.Normal), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        color = None
        if not connected:
            color = QColor('#797e82')
        else:
            if exec_type == 'exec':
                color = QColor('#dddddd')
            else:
                color = node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Light.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Light.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect: QRectF, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#ffffff')
        header_color = c

        header_height = NIPainter.get_header_rect(w, h, title_rect).height()
        rel_header_height = header_height/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(QRectF(
            QPointF(bounding_rect.left(), bounding_rect.top()+header_height),
            bounding_rect.bottomRight()
        ), 6, 6)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor('#3c3c3c')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)


class NIPainter_Dark(NIPainter):

    def paint_NI_title_label(painter, option, hovering, design_style, title_str, node_color, bounding_rect):
        if design_style == 'extended':
            painter.setPen(QPen(QColor(node_color.name())))
            painter.setFont(QFont('Roboto', 13))
            painter.drawText(bounding_rect, Qt.AlignLeft | Qt.AlignVCenter, title_str)
        else:
            NIPainter.paint_NI_title_label_default(
                painter, design_style, title_str, node_color,
                2,
                QFont('Roboto', 15, QFont.Thin),
                bounding_rect
            )

    def paint_PI_label(painter, option, exec_type, connected, label_str, node_color, bounding_rect):
        c = None
        if not connected:
            c = QColor('#797e82')
        else:
            if exec_type == 'exec':
                c = QColor('#cccccc')
            else:
                c = node_color
        NIPainter.paint_PI_label_default(painter, label_str, c, QFont("Roboto Mono", 10, QFont.Normal), bounding_rect)

    def paint_PI(painter, option, node_color, exec_type, connected, padding, w, h):
        color = None
        if not connected:
            color = QColor('#797e82')
        else:
            if exec_type == 'exec':
                color = QColor('#dddddd')
            else:
                color = node_color

        if exec_type == 'exec':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                brush = QBrush(QColor(255, 255, 255, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        elif exec_type == 'data':
            if connected or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                r = node_color.red()
                g = node_color.green()
                b = node_color.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

        brush = QBrush(QColor(color))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(QRectF(padding+w/8, padding+h/8, 3*w/4, 3*h/4))

    def paint_NI(design_style,
                 painter, option,
                 c: QColor, w: int, h: int, bounding_rect, title_rect):

        painter.setRenderHint(QPainter.Antialiasing)

        if design_style == 'extended':
            NIPainter_Dark.draw_NI_extended_background(painter, c, w, h, bounding_rect, title_rect)
        elif design_style == 'minimalistic':
            NIPainter_Dark.draw_NI_minimalistic(painter, c, w, h, bounding_rect)

    def draw_NI_extended_background(painter, c, w, h, bounding_rect: QRectF, title_rect):
        """
        :param painter: painter from paint event
        :param c: NodeInstance's theme color
        :param w: width
        :param h: height
        :param bounding_rect: NodeInstance's bounding rect
        :param title_rect: NI's title label's bounding rect
        """

        background_color = QColor('#3c3c3c')
        header_color = c

        header_height = NIPainter.get_header_rect(w, h, title_rect).height()
        rel_header_height = header_height/h
        gradient = QLinearGradient(bounding_rect.topLeft(), bounding_rect.bottomLeft())
        gradient.setColorAt(0, header_color)
        gradient.setColorAt(rel_header_height, header_color)
        gradient.setColorAt(rel_header_height+0.0001, background_color)
        gradient.setColorAt(1, background_color)

        painter.setBrush(QBrush(background_color))
        painter.setPen(Qt.NoPen)  # QPen(c.darker()))
        painter.drawRoundedRect(QRectF(
            QPointF(bounding_rect.left(), bounding_rect.top()+header_height),
            bounding_rect.bottomRight()
        ), 6, 6)

    def draw_NI_minimalistic(painter, c, w, h, bounding_rect, background_color=QColor('#3c3c3c')):
        """
        :param painter: painter from paint event
        :param c_s: corner size/corner radius
        :param c: color
        :param w: width
        :param h: height
        :param background_color: std background color
        """
        c_s = 10
        painter.setBrush(NIPainter.interpolate_color(c, background_color, 0.97))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bounding_rect, c_s, c_s)
