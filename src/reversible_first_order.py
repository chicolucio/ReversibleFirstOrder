import numpy as np
import matplotlib.pyplot as plt


class ReversibleFirstOrder:
    def __init__(self, rate_cte_forward, rate_cte_backward, reactant_initial_concentration,
                 product_initial_concentration, time=10, points=100):
        self.kf = rate_cte_forward
        self.kb = rate_cte_backward
        self.A0 = reactant_initial_concentration
        self.B0 = product_initial_concentration
        self.t = np.linspace(0, time, points)

    @property
    def reactant_time(self):
        return -((self.kb * self.B0 - self.kf * self.A0) *
                 np.exp(-self.t * (self.kf + self.kb)) -
                 self.kb * (self.A0 + self.B0)) / (self.kf + self.kb)

    @property
    def product_time(self):
        return self.A0 + self.B0 - self.reactant_time

    @property
    def reaction_quotient(self):
        return self.product_time / self.reactant_time

    @staticmethod
    def _plot_params(ax=None, time_unit='s', ylabel='Concentration', concentration_unit='mol/l',
                     title=True, title_text=''):
        """Internal function for plot parameters.
        Parameters
        ----------
        ax : Matplotlib axes, optional
            axes where the graph will be plotted, by default None.
        """
        linewidth = 2
        size = 12

        # grid and ticks settings
        ax.minorticks_on()
        ax.grid(b=True, which='major', linestyle='--',
                linewidth=linewidth - 0.5)
        ax.grid(b=True, which='minor', axis='both',
                linestyle=':', linewidth=linewidth - 1)
        ax.tick_params(which='both', labelsize=size + 2)
        ax.tick_params(which='major', length=6, axis='both')
        ax.tick_params(which='minor', length=3, axis='both')

        # labels and size
        ax.xaxis.label.set_size(size + 4)
        ax.yaxis.label.set_size(size + 4)

        ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        ax.yaxis.major.formatter._useMathText = True
        ax.figure.canvas.draw()  # Update the text
        order_magnitude = ax.yaxis.get_offset_text().get_text().replace('\\times', '')
        ax.yaxis.offsetText.set_visible(False)
        if order_magnitude == concentration_unit == '':
            ax.set_ylabel(f'{ylabel}')
        else:
            ax.set_ylabel(f'{ylabel} / {order_magnitude} {concentration_unit}')
        ax.set_xlabel(f'Time / {time_unit}')
        if not title:
            pass
        elif title_text == '':
            ax.set_title(r'Concentration vs time for Reactant $\rightleftarrows$ Product', fontsize=18)
        else:
            ax.set_title(title_text, fontsize=18)

        return ax

    def plot_reaction_time(self, size=(10, 8), ax=None, time_unit='s', concentration_unit='mol/l',
                           title=True, title_text=''):
        if ax is None:
            fig, ax = plt.subplots(figsize=size, facecolor=(1.0, 1.0, 1.0))

        ax.plot(self.t, self.reactant_time, label='Reactant')
        ax.plot(self.t, self.product_time, label='Product')

        self._plot_params(ax, time_unit, 'Concentration', concentration_unit, title, title_text)

        ax.legend(loc='best', fontsize=14)

        return ax

    def plot_reaction_quotient_time(self, size=(10, 8), ax=None, time_unit='s', q='Q',
                                    title=True,
                                    title_text=r'Reaction Quotient vs Time for Reactant $\rightleftarrows$ Product'):
        if ax is None:
            fig, ax = plt.subplots(figsize=size, facecolor=(1.0, 1.0, 1.0))

        ax.plot(self.t, self.reaction_quotient)

        self._plot_params(ax, time_unit, q, '', title, title_text)

        return ax
