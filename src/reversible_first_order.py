import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class ReversibleFirstOrder:
    """
    A reversible process in kinetics means the backward reaction is significant.

    The software considers the equilibrium Reactant <=> Product also expressed A <=> B.
    """

    def __init__(self, rate_cte_forward, rate_cte_backward, reactant_initial_concentration,
                 product_initial_concentration, time=10, points=100):
        """
        Parameters
        ----------
        rate_cte_forward : float
            rate constant of the forward reaction, usually expressed as kf.
        rate_cte_backward : float
            rate constant of the backward reaction, usually expressed as kb.
        reactant_initial_concentration : float
            being the reactant/left-side compound A, usually expressed as [A]0.
        product_initial_concentration : float
            being the product/right-side compound B, usually expressed as [B]0.
        time : int
            the final time, in arbitrary units.
        points : int
            the number of simulated points to be created.
        """

        self.kf = rate_cte_forward
        self.kb = rate_cte_backward
        self.A0 = reactant_initial_concentration
        self.B0 = product_initial_concentration
        self.t = np.linspace(0, time, points)

    @property
    def reactant_time(self):
        """
        Reactant A concentration evolution with time.
        Returns
        -------
        np.array
            numpy array with n points corresponding to [A].
        """
        return -((self.kb * self.B0 - self.kf * self.A0) *
                 np.exp(-self.t * (self.kf + self.kb)) -
                 self.kb * (self.A0 + self.B0)) / (self.kf + self.kb)

    @property
    def product_time(self):
        """
        Product B concentration evolution with time.
        Returns
        -------
        np.array
            numpy array with n points corresponding to [B].
        """
        return self.A0 + self.B0 - self.reactant_time

    @property
    def reaction_quotient(self):
        """
        Reaction quotient Q evolution with time.
        Returns
        -------
        np.array
            numpy array with n points corresponding to Q.
        """
        return self.product_time / self.reactant_time

    @staticmethod
    def _plot_params(ax=None, time_unit='s', ylabel='Concentration', concentration_unit='mol/l',
                     title=True, title_text=''):
        """
        Plot customization.
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
                           title=True, title_text='', label_reactant='Reactant', label_product='Product'):
        """
        Plots concentration vs time

        Parameters
        ----------
        size : tuple, optional
            plot size. Ignored if an axis object is passed through ax parameter.
        ax : Matplotlib.axes, optional
            axis for the plot. If None, one will be created
        time_unit : str, optional
            time unit to be displayed at the label
        concentration_unit : str, optional
            concentration unit to be displayed at the label
        title : bool, optional
            title toggle
        title_text : str, optional
            title text. If '' a default will be displayed unless title=False
        label_reactant : str, optional
            label for the reactant A
        label_product : str, optional
            label for the product B

        Returns
        -------
        Matplotlib.axes
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=size, facecolor=(1.0, 1.0, 1.0))

        ax.plot(self.t, self.reactant_time, label=label_reactant)
        ax.plot(self.t, self.product_time, label=label_product)

        self._plot_params(ax, time_unit, 'Concentration', concentration_unit, title, title_text)

        handles, labels = ax.get_legend_handles_labels()
        patch_kf = mpatches.Patch(color='white', label=' '.join(['$k_f =$', f'{self.kf}']))
        patch_kb = mpatches.Patch(color='white', label=' '.join(['$k_b =$', f'{self.kb}']))
        patch_A0 = mpatches.Patch(color='white', label=' '.join(['$[A]_0 =$', f'{self.A0}']))
        patch_BO = mpatches.Patch(color='white', label=' '.join(['$[B]_0 =$', f'{self.B0}']))

        handles.extend([patch_A0, patch_BO, patch_kf, patch_kb])

        xbbox = 0.5
        ybbox = -0.15
        ax.legend(handles=handles, loc='upper center', fontsize=14, shadow=True, fancybox=True,
                  bbox_to_anchor=(xbbox, ybbox), ncol=len(handles), columnspacing=0.2)

        return ax

    def plot_reaction_quotient_time(self, size=(10, 8), ax=None, time_unit='s', q='Q',
                                    title=True,
                                    title_text=r'Reaction Quotient vs Time for Reactant $\rightleftarrows$ Product'):
        """
        Plots reaction quotient vs time
        Parameters
        ----------
        size : tuple, optional
            plot size. Ignored if an axis object is passed through ax parameter.
        ax : Matplotlib.axes, optional
            axis for the plot. If None, one will be created
        time_unit : str, optional
            time unit to be displayed at the label
        q : str, optional
            Vertical axis label
        title : bool, optional
            title toggle
        title_text : str, optional
            title text. A default will be displayed unless title=False

        Returns
        -------
        Matplotlib.axes
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=size, facecolor=(1.0, 1.0, 1.0))

        ax.plot(self.t, self.reaction_quotient, color='red')

        self._plot_params(ax, time_unit, q, '', title, title_text)

        return ax
