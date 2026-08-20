#!/usr/bin/env python3
"""generate 1:1 printable badux board templates as PDF.

the board is a triangular lattice (the dual of the hexagonal cells drawn by the web client):
three families of straight parallel lines at 60 degrees, stones on the intersections.

geometry matches variationalgo/web/src/variationalgo/view/board/PixelPointConversions.ts:
axial coords (q, r) with s = -q - r, x = pitch * (q + r/2), y = pitch * (sqrt(3)/2) * r.
"""

import argparse
import math
import cairo

MM = 72.0 / 25.4          # postscript points per mm
SQRT3 = math.sqrt(3.0)

PAGES = {                 # name: (width mm, height mm)
    'letter': (215.9, 279.4),
    'a4': (210.0, 297.0),
}

PAGE_MARGIN = 12.0        # unprintable-border allowance on left/right/top
FOOTER = 18.0             # bottom strip for the sheet label and calibration bar
OVERLAP = 10.0            # shared band between adjacent tiles


def board_points(radius):
    for q in range(-radius, radius + 1):
        for r in range(-radius, radius + 1):
            if max(abs(q), abs(r), abs(q + r)) <= radius:
                yield q, r


def star_points(radius):
    """mirrors HexBoardFeatures.starPoints"""
    points = [(0, 0)]
    if radius < 4:
        return points
    if radius < 7:
        d = radius - 2
    else:
        d = radius - 3
    points += [(d, 0), (-d, 0), (0, d), (0, -d), (d, -d), (-d, d)]
    if radius >= 7 and radius > 10:
        side = math.ceil((radius - 3) / 2)
        if radius % 2 == 1:
            points += [(side, -d), (-side, d), (d, -side),
                       (-d, side), (side, side), (-side, -side)]
        else:
            fifth = radius - 4
            points += [(side - 1, -fifth), (-side + 1, fifth), (fifth, -side + 1),
                       (-fifth, side - 1), (side - 1, side - 1), (-side + 1, -side + 1)]
    return points


def grid_lines(radius):
    """one segment per grid line: 3 families of 2*radius+1 parallel lines"""
    def span(fixed_axis, k):
        pts = [p for p in board_points(radius) if fixed_axis(p) == k]
        return min(pts), max(pts)

    lines = []
    for k in range(-radius, radius + 1):
        lines.append(span(lambda p: p[0], k))                    # constant q
        lines.append(span(lambda p: p[1], k))                    # constant r
        lines.append(span(lambda p: -p[0] - p[1], k))            # constant s
    return lines


class Board:
    def __init__(self, cells_per_edge, pitch, border):
        self.n = cells_per_edge
        self.radius = cells_per_edge - 1
        self.pitch = pitch
        self.border = border
        self.point_width = 2 * self.radius * pitch
        self.point_height = SQRT3 * self.radius * pitch
        # the drawing area is the point hexagon offset outward by `border` on every side
        self.outer_radius = self.radius * pitch + border * 2 / SQRT3
        self.width = 2 * self.outer_radius
        self.height = SQRT3 * self.outer_radius

    @property
    def name(self):
        return f'{self.n}x{self.n}x{self.n}'

    def xy(self, point):
        """lattice point to mm, origin at the top left of the drawing area"""
        q, r = point
        return (self.width / 2 + self.pitch * (q + 0.5 * r),
                self.height / 2 + self.pitch * (SQRT3 / 2) * r)

    def draw(self, ctx, line_width=0.5):
        ctx.set_source_rgb(0, 0, 0)
        ctx.set_line_width(line_width * MM)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        for a, b in grid_lines(self.radius):
            ax, ay = self.xy(a)
            bx, by = self.xy(b)
            ctx.move_to(ax * MM, ay * MM)
            ctx.line_to(bx * MM, by * MM)
            ctx.stroke()
        dot = 0.0625 * self.pitch                                # ~3mm diameter at 24mm pitch
        for p in star_points(self.radius):
            x, y = self.xy(p)
            ctx.arc(x * MM, y * MM, dot * MM, 0, 2 * math.pi)
            ctx.fill()

    def draw_edge_hint(self, ctx):
        """dashed hexagon at the border offset: a suggested finished board edge"""
        if self.border <= 0:
            return
        ctx.save()
        ctx.set_source_rgb(0.6, 0.6, 0.6)
        ctx.set_line_width(0.3 * MM)
        ctx.set_dash([3 * MM, 3 * MM])
        r_out = self.outer_radius
        for i in range(7):
            angle = math.pi / 180 * (60 * i)                     # flat sides top/bottom
            x = self.width / 2 + r_out * math.cos(angle)
            y = self.height / 2 + r_out * math.sin(angle)
            (ctx.move_to if i == 0 else ctx.line_to)(x * MM, y * MM)
        ctx.stroke()
        ctx.restore()


def footer(ctx, page_w, page_h, label, note):
    ctx.save()
    ctx.set_source_rgb(0.35, 0.35, 0.35)
    ctx.select_font_face('sans-serif', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    ctx.set_font_size(7.5)
    ctx.move_to(PAGE_MARGIN * MM, (page_h - 12.0) * MM)
    ctx.show_text(label)

    if note:
        ctx.set_font_size(6.5)
        ctx.move_to(PAGE_MARGIN * MM, (page_h - 6.0) * MM)
        ctx.show_text(note)

    bar_right = page_w - PAGE_MARGIN
    bar_left = bar_right - 100.0
    y = page_h - 10.0
    ctx.set_line_width(0.3 * MM)
    ctx.move_to(bar_left * MM, y * MM)
    ctx.line_to(bar_right * MM, y * MM)
    for x in (bar_left, bar_right):
        ctx.move_to(x * MM, (y - 2.0) * MM)
        ctx.line_to(x * MM, (y + 2.0) * MM)
    for i in range(1, 10):
        x = bar_left + 10.0 * i
        ctx.move_to(x * MM, y * MM)
        ctx.line_to(x * MM, (y + 1.5) * MM)
    ctx.stroke()

    ctx.set_font_size(6.5)
    ctx.move_to(bar_left * MM, (page_h - 12.5) * MM)
    ctx.show_text('print at 100%, no scaling — this bar must measure exactly 100mm')
    ctx.restore()


def trim_marks(ctx, x0, y0, x1, y1, trim_left, trim_top):
    ctx.save()
    ctx.set_source_rgb(0.7, 0.7, 0.7)
    ctx.set_line_width(0.25 * MM)
    ctx.set_dash([2 * MM, 2 * MM])
    if trim_left:
        ctx.move_to(x0 * MM, y0 * MM)
        ctx.line_to(x0 * MM, y1 * MM)
    if trim_top:
        ctx.move_to(x0 * MM, y0 * MM)
        ctx.line_to(x1 * MM, y0 * MM)
    ctx.stroke()
    ctx.restore()


def render_tiled(board, page, path):
    page_w, page_h = PAGES[page]
    content_w = page_w - 2 * PAGE_MARGIN
    content_h = page_h - PAGE_MARGIN - FOOTER
    step_x = content_w - OVERLAP
    step_y = content_h - OVERLAP
    cols = max(1, math.ceil((board.width - OVERLAP) / step_x))
    rows = max(1, math.ceil((board.height - OVERLAP) / step_y))

    # centre the board across the whole tiled sheet area
    span_x = OVERLAP + cols * step_x
    span_y = OVERLAP + rows * step_y
    off_x = (span_x - board.width) / 2
    off_y = (span_y - board.height) / 2

    surface = cairo.PDFSurface(path, page_w * MM, page_h * MM)
    ctx = cairo.Context(surface)
    for row in range(rows):
        for col in range(cols):
            ctx.save()
            ctx.rectangle(PAGE_MARGIN * MM, PAGE_MARGIN * MM, content_w * MM, content_h * MM)
            ctx.clip()
            ctx.translate((PAGE_MARGIN - col * step_x + off_x) * MM,
                          (PAGE_MARGIN - row * step_y + off_y) * MM)
            board.draw_edge_hint(ctx)
            board.draw(ctx)
            ctx.restore()
            trim_marks(ctx, PAGE_MARGIN, PAGE_MARGIN,
                       page_w - PAGE_MARGIN, page_h - FOOTER,
                       trim_left=col > 0, trim_top=row > 0)
            label = (f'badux {board.name} — {board.pitch:g}mm pitch — 1:1 — '
                     f'sheet row {row + 1}/{rows}, col {col + 1}/{cols}')
            note = ('trim on the dashed edges, then lap each sheet over the one above and to its '
                    'left, matching grid lines through the 10mm overlap') if (rows * cols) > 1 else None
            footer(ctx, page_w, page_h, label, note)
            ctx.show_page()
    surface.finish()
    return rows, cols


def render_full(board, path):
    surface = cairo.PDFSurface(path, board.width * MM, board.height * MM)
    ctx = cairo.Context(surface)
    board.draw_edge_hint(ctx)
    board.draw(ctx)
    surface.finish()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--size', type=int, default=12, help='cells per board edge (6, 8, 12)')
    ap.add_argument('--pitch', type=float, default=24.0, help='mm between adjacent points')
    ap.add_argument('--border', type=float, default=18.0, help='mm of board beyond the outer points')
    ap.add_argument('--page', choices=list(PAGES) + ['full'], default='a4')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    board = Board(args.size, args.pitch, args.border)
    if args.page == 'full':
        render_full(board, args.out)
        print(f'{args.out}: single page {board.width:.0f} x {board.height:.0f} mm')
    else:
        rows, cols = render_tiled(board, args.page, args.out)
        print(f'{args.out}: {rows * cols} sheets ({cols} x {rows}) of {args.page}, '
              f'board {board.width:.0f} x {board.height:.0f} mm '
              f'(points {board.point_width:.0f} x {board.point_height:.0f})')


if __name__ == '__main__':
    main()
