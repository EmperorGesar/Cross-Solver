import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from hand import Default
from piece import Center, Edge, Corner
from params import Color, Position
from scrambler import Scrambler
from solver import Solver


class Cube:
    def __init__(self, opacity=0.8):
        self.fig = plt.figure()
        self.fig.canvas.manager.set_window_title('Cross Solver')
        self.ax = self.fig.add_subplot(projection='3d')

        self.opacity = opacity

        self.ax_Rand = self.fig.add_axes((0.01, 0.92, 0.07, 0.07))
        self.b_Rand = Button(self.ax_Rand, 'Rand')
        self.b_Rand.on_clicked(self.scramble)

        self.ax_Cross = self.fig.add_axes((0.01, 0.84, 0.07, 0.07))
        self.b_Cross = Button(self.ax_Cross, 'Cross')
        self.b_Cross.on_clicked(self.solve)

        self.ax_R = self.fig.add_axes((0.01, 0.01, 0.07, 0.07))
        self.ax_Rp = self.fig.add_axes((0.09, 0.01, 0.07, 0.07))
        self.ax_U = self.fig.add_axes((0.17, 0.01, 0.07, 0.07))
        self.ax_Up = self.fig.add_axes((0.25, 0.01, 0.07, 0.07))
        self.ax_F = self.fig.add_axes((0.33, 0.01, 0.07, 0.07))
        self.ax_Fp = self.fig.add_axes((0.41, 0.01, 0.07, 0.07))
        self.ax_L = self.fig.add_axes((0.49, 0.01, 0.07, 0.07))
        self.ax_Lp = self.fig.add_axes((0.57, 0.01, 0.07, 0.07))
        self.ax_D = self.fig.add_axes((0.65, 0.01, 0.07, 0.07))
        self.ax_Dp = self.fig.add_axes((0.73, 0.01, 0.07, 0.07))
        self.ax_B = self.fig.add_axes((0.81, 0.01, 0.07, 0.07))
        self.ax_Bp = self.fig.add_axes((0.89, 0.01, 0.07, 0.07))

        self.b_R = Button(self.ax_R, 'R')
        self.b_Rp = Button(self.ax_Rp, 'R\'')
        self.b_U = Button(self.ax_U, 'U')
        self.b_Up = Button(self.ax_Up, 'U\'')
        self.b_F = Button(self.ax_F, 'F')
        self.b_Fp = Button(self.ax_Fp, 'F\'')
        self.b_L = Button(self.ax_L, 'L')
        self.b_Lp = Button(self.ax_Lp, 'L\'')
        self.b_D = Button(self.ax_D, 'D')
        self.b_Dp = Button(self.ax_Dp, 'D\'')
        self.b_B = Button(self.ax_B, 'B')
        self.b_Bp = Button(self.ax_Bp, 'B\'')

        self.b_R.on_clicked(self.R)
        self.b_Rp.on_clicked(self.Rp)
        self.b_U.on_clicked(self.U)
        self.b_Up.on_clicked(self.Up)
        self.b_F.on_clicked(self.F)
        self.b_Fp.on_clicked(self.Fp)
        self.b_L.on_clicked(self.L)
        self.b_Lp.on_clicked(self.Lp)
        self.b_D.on_clicked(self.D)
        self.b_Dp.on_clicked(self.Dp)
        self.b_B.on_clicked(self.B)
        self.b_Bp.on_clicked(self.Bp)

        self.center_w = Center(Color.WHITE, Position.d)
        self.center_b = Center(Color.BLUE, Position.f)
        self.center_r = Center(Color.RED, Position.r)
        self.center_g = Center(Color.GREEN, Position.b)
        self.center_o = Center(Color.ORANGE, Position.l)
        self.center_y = Center(Color.YELLOW, Position.u)

        self.edge_wb = Edge(Color.WHITE, Color.BLUE, Position.df)
        self.edge_wr = Edge(Color.WHITE, Color.RED, Position.dr)
        self.edge_wg = Edge(Color.WHITE, Color.GREEN, Position.db)
        self.edge_wo = Edge(Color.WHITE, Color.ORANGE, Position.dl)

        self.edge_br = Edge(Color.BLUE, Color.RED, Position.fr)
        self.edge_gr = Edge(Color.GREEN, Color.RED, Position.br)
        self.edge_go = Edge(Color.GREEN, Color.ORANGE, Position.bl)
        self.edge_bo = Edge(Color.BLUE, Color.ORANGE, Position.fl)

        self.edge_yb = Edge(Color.YELLOW, Color.BLUE, Position.uf)
        self.edge_yr = Edge(Color.YELLOW, Color.RED, Position.ur)
        self.edge_yg = Edge(Color.YELLOW, Color.GREEN, Position.ub)
        self.edge_yo = Edge(Color.YELLOW, Color.ORANGE, Position.ul)

        self.corner_wbr = Corner(Color.WHITE, Color.BLUE, Color.RED, Position.dfr)
        self.corner_wgr = Corner(Color.WHITE, Color.GREEN, Color.RED, Position.dbr)
        self.corner_wgo = Corner(Color.WHITE, Color.GREEN, Color.ORANGE, Position.dbl)
        self.corner_wbo = Corner(Color.WHITE, Color.BLUE, Color.ORANGE, Position.dfl)

        self.corner_ybr = Corner(Color.YELLOW, Color.BLUE, Color.RED, Position.ufr)
        self.corner_ygr = Corner(Color.YELLOW, Color.GREEN, Color.RED, Position.ubr)
        self.corner_ygo = Corner(Color.YELLOW, Color.GREEN, Color.ORANGE, Position.ubl)
        self.corner_ybo = Corner(Color.YELLOW, Color.BLUE, Color.ORANGE, Position.ufl)

        self.pieces = [self.corner_wbo, self.edge_wb, self.corner_wbr,
                       self.edge_wo, self.center_w, self.edge_wr,
                       self.corner_wgo, self.edge_wg, self.corner_wgr,
                       self.edge_bo, self.center_b, self.edge_br,
                       self.center_o, None, self.center_r,
                       self.edge_go, self.center_g, self.edge_gr,
                       self.corner_ybo, self.edge_yb, self.corner_ybr,
                       self.edge_yo, self.center_y, self.edge_yr,
                       self.corner_ygo, self.edge_yg, self.corner_ygr]

        self.hand = Default()
        self.scrambler = Scrambler()
        self.solver = Solver()

    def reset(self):
        self.edge_wb.set_colors(Color.WHITE, Color.BLUE)
        self.edge_wb.set_pos(Position.df)
        self.edge_wr.set_colors(Color.WHITE, Color.RED)
        self.edge_wr.set_pos(Position.dr)
        self.edge_wg.set_colors(Color.WHITE, Color.GREEN)
        self.edge_wg.set_pos(Position.db)
        self.edge_wo.set_colors(Color.WHITE, Color.ORANGE)
        self.edge_wo.set_pos(Position.dl)

        self.edge_br.set_colors(Color.BLUE, Color.RED)
        self.edge_br.set_pos(Position.fr)
        self.edge_gr.set_colors(Color.GREEN, Color.RED)
        self.edge_gr.set_pos(Position.br)
        self.edge_go.set_colors(Color.GREEN, Color.ORANGE)
        self.edge_go.set_pos(Position.bl)
        self.edge_bo.set_colors(Color.BLUE, Color.ORANGE)
        self.edge_bo.set_pos(Position.fl)

        self.edge_yb.set_colors(Color.YELLOW, Color.BLUE)
        self.edge_yb.set_pos(Position.uf)
        self.edge_yr.set_colors(Color.YELLOW, Color.RED)
        self.edge_yr.set_pos(Position.ur)
        self.edge_yg.set_colors(Color.YELLOW, Color.GREEN)
        self.edge_yg.set_pos(Position.ub)
        self.edge_yo.set_colors(Color.YELLOW, Color.ORANGE)
        self.edge_yo.set_pos(Position.ul)

        self.corner_wbr.set_colors(Color.WHITE, Color.BLUE, Color.RED)
        self.corner_wbr.set_pos(Position.dfr)
        self.corner_wgr.set_colors(Color.WHITE, Color.GREEN, Color.RED)
        self.corner_wgr.set_pos(Position.dbr)
        self.corner_wgo.set_colors(Color.WHITE, Color.GREEN, Color.ORANGE)
        self.corner_wgo.set_pos(Position.dbl)
        self.corner_wbo.set_colors(Color.WHITE, Color.BLUE, Color.ORANGE)
        self.corner_wbo.set_pos(Position.dfl)

        self.corner_ybr.set_colors(Color.YELLOW, Color.BLUE, Color.RED)
        self.corner_ybr.set_pos(Position.ufr)
        self.corner_ygr.set_colors(Color.YELLOW, Color.GREEN, Color.RED)
        self.corner_ygr.set_pos(Position.ubr)
        self.corner_ygo.set_colors(Color.YELLOW, Color.GREEN, Color.ORANGE)
        self.corner_ygo.set_pos(Position.ubl)
        self.corner_ybo.set_colors(Color.YELLOW, Color.BLUE, Color.ORANGE)
        self.corner_ybo.set_pos(Position.ufl)

        self.pieces = [self.corner_wbo, self.edge_wb, self.corner_wbr,
                       self.edge_wo, self.center_w, self.edge_wr,
                       self.corner_wgo, self.edge_wg, self.corner_wgr,
                       self.edge_bo, self.center_b, self.edge_br,
                       self.center_o, None, self.center_r,
                       self.edge_go, self.center_g, self.edge_gr,
                       self.corner_ybo, self.edge_yb, self.corner_ybr,
                       self.edge_yo, self.center_y, self.edge_yr,
                       self.corner_ygo, self.edge_yg, self.corner_ygr]

    def R(self, event):
        self.hand.R(self.pieces)
        self.show()

    def Rp(self, event):
        self.hand.Rp(self.pieces)
        self.show()

    def U(self, event):
        self.hand.U(self.pieces)
        self.show()

    def Up(self, event):
        self.hand.Up(self.pieces)
        self.show()

    def F(self, event):
        self.hand.F(self.pieces)
        self.show()

    def Fp(self, event):
        self.hand.Fp(self.pieces)
        self.show()

    def L(self, event):
        self.hand.L(self.pieces)
        self.show()

    def Lp(self, event):
        self.hand.Lp(self.pieces)
        self.show()

    def D(self, event):
        self.hand.D(self.pieces)
        self.show()

    def Dp(self, event):
        self.hand.Dp(self.pieces)
        self.show()

    def B(self, event):
        self.hand.B(self.pieces)
        self.show()

    def Bp(self, event):
        self.hand.Bp(self.pieces)
        self.show()

    def get_cross_state(self):
        state = [None, None, None, None,
                 None, None, None, None,
                 None, None, None, None]
        edge_index = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        for i in range(12):
            color_t = self.pieces[edge_index[i]].get_colors()
            if color_t[0] is Color.WHITE:
                state[i] = (color_t[1].name[0], 0)
            elif color_t[1] is Color.WHITE:
                state[i] = (color_t[0].name[0], 1)

        return state

    def solve(self, event):
        if len(self.fig.texts) == 2:
            self.fig.texts.pop()
        cross_text = self.solver.search()
        self.fig.text(0.09, 0.865, cross_text)
        plt.draw()
        plt.show()

    def scramble(self, event):
        self.reset()
        turns, rand_text = self.scrambler.generate()
        self.hand.scramble(self.pieces, turns)

        self.fig.texts = []
        self.fig.text(0.09, 0.945, rand_text)
        self.show()

    def show(self):
        self.ax.clear()
        self.ax.set_axis_off()

        for p in self.pieces:
            if p is not None:
                self.ax.add_collection3d(
                    Poly3DCollection(p.get_pos().value[0],
                                     edgecolors=Color.BLACK.value,
                                     facecolors=p.get_colors()[0].value,
                                     linewidths=1, alpha=self.opacity))
                if p.__class__ is not Center:
                    self.ax.add_collection3d(
                        Poly3DCollection(p.get_pos().value[1],
                                         edgecolors=Color.BLACK.value,
                                         facecolors=p.get_colors()[1].value,
                                         linewidths=1, alpha=self.opacity))
                if p.__class__ is Corner:
                    self.ax.add_collection3d(
                        Poly3DCollection(p.get_pos().value[2],
                                         edgecolors=Color.BLACK.value,
                                         facecolors=p.get_colors()[2].value,
                                         linewidths=1, alpha=self.opacity))

        state = self.get_cross_state()
        self.solver.set_state(state)

        self.ax.set_box_aspect([1, 1, 1])
        # ax.set_proj_type('ortho')

        limits = np.array([
            self.ax.get_xlim3d(),
            self.ax.get_ylim3d(),
            self.ax.get_zlim3d(),
        ])
        origin = np.mean(limits, axis=1)
        radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))

        x, y, z = origin
        self.ax.set_xlim3d([x - radius, x + radius])
        self.ax.set_ylim3d([y - radius, y + radius])
        self.ax.set_zlim3d([z - radius, z + radius])

        plt.draw()
        plt.show()
