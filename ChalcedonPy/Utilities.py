import matplotlib.pyplot as plt
from cycler import cycler 
from pathlib import Path # to work with paths
import matplotlib.colors  # all related to colours

def init(save_path, display_mode):
   """Generates variables for use in the module

   Parameters
   ----------
   save_path : string
       The folder in which the images would be saved
   display_mode: string
       Sets the display and save type for the images
   
   Examples
   --------
   cp.init(save_path="Mathematical-Fundamentals", display_mode="web")

   """
   global SAVE_PATH, style
   SAVE_PATH = save_path
   style = display_mode

   # Set style for use in supplemental website
   if style == "web":
      plt.style.use('dusk')

   # Set style for use in ipython and lecture slide
   elif style == "slide":
      plt.style.use('dawn')
   

def store_fig(fig_id,
              tight_layout=True,
              fig_extension="png",
              resolution=400,
              close=None):
   """Function to save a figure

   Parameters
   ----------
   fig_id : string
       name of the figure
   tight_layout : bool
       Set whether figure is tight
   fig_extension : string
       set the figure extension
   resolution : int
       Set the DPI
   close : bool
       Set to close the figure or not

   Examples
   --------
   cp.store_fig("An Example", close=True)
   """
    
    if tight_layout:
        plt.tight_layout()
        
    if style == "web":
        fig_extension = "png"
        
    elif style == 'slide':
        fig_extension = "pdf"

    IMAGES_PATH = Path() / "images" / SAVE_PATH
        
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    plt.savefig(path, format=fig_extension, dpi=resolution)

    if close:
        plt.close()


class Plotting:
    # Set the colour parameter for plots to fit beamer metropolis theme
    plt.rcParams["figure.facecolor"] = "(0.98, 0.98, 0.98)"
    plt.rcParams.update({'axes.facecolor': '(0.98, 0.98, 0.98)'})
    matplotlib.colors.ColorConverter.colors['bg1'] = (0.98, 0.98, 0.98)

    @staticmethod
    def image_subplot_style(row, column, image_array, publish=None, show=None, rgb=None, title=None,
                            cmap_array=None, set_cmap=False):
        """Presents a set of images in a grid of subplots.

        :param figsize: Figure size for your subplot.
        :param title: Add title to your plot. Treated as array.
        :param cmap_array: colormap array, if none entered it is treated as None.
        :param row: Number of rows in an image.
        :param column: Number of columns in an image.
        :param image_array: Write here the images in an array you want in the plot in the order you want it to show.
        :param publish: Write the name of the file you want to save it as (.eps, 200 dpi).
        :param show: Just activates plt.show().
        :param rgb: Sets print colour to true.
        """

        # noinspection PyTypeChecker
        fig_plot, axes_plot = plt.subplots(row, column, sharex=True, sharey=True)

        for ind, ax_loop in enumerate(axes_plot.flatten()):

            Plotting.remove_borders(ax_loop)  # remove unnecessary borders

            ax_loop.tick_params(left=False, right=False, labelleft=False, labelbottom=False, bottom=False)

            ax_loop.imshow(image_array[ind][:][:])  # print image for subplot

            if rgb:  # convert image bgr to rgb
                if set_cmap is True:
                    ax_loop.imshow(Plotting.bgr2rgb(image_array[ind][:][:]), cmap=cmap_array[ind])
                else:
                    ax_loop.imshow(Plotting.bgr2rgb(image_array[ind][:][:]))

            if title is None:

                # Determine where to put the title on the image
                if ind < column:
                    ax_loop.set_title("(" + str(chr(ord('a') + ind)) + ")", fontsize=12)
                else:
                    ax_loop.set_xlabel("(" + str(chr(ord('a') + ind)) + ")", fontsize=12)

            else:
                # Determine where to put the title on the image
                if ind < column:
                    ax_loop.set_title(title[ind], fontsize=12)
                else:
                    ax_loop.set_xlabel(title[ind], fontsize=12)

        Plotting.printer(show, publish)

    @staticmethod
    def plot_subplot_style(fig_subplot, axes_subplot):
        """Some standard aesthetics for the matplotlib function

        :param fig_subplot: figure for the subplot.
        :param axes_subplot: axes for the subplot.
        """

        axes_subplot.spines['top'].set_visible(False)
        axes_subplot.spines['right'].set_visible(False)
        axes_subplot.xaxis.set_tick_params(width=2)
        axes_subplot.yaxis.set_tick_params(width=2)
        plt.rcParams['axes.linewidth'] = 2
        fig_subplot.tight_layout()

    @staticmethod
    def bgr2rgb(image_in_bgr):
        """Converts an image from BGR space to RGB.

        :param image_in_bgr: image in BGR format.
        :return: image in RGB format.
        """
        return cv.cvtColor(image_in_bgr, cv.COLOR_BGR2RGB)

    @classmethod
    def compare_images(cls, original, altered):
        """Creates two individual windows to showcase the filters effect

        :param original: Original unaltered image
        :param altered: Output altered image
        """
        # A static function to showcase both the original and the altered image
        cv.imshow('Original Image', original)
        cv.imshow("Output Image", altered)

        # Wait and close all windows
        cv.waitKey(0)
        cv.destroyAllWindows()

    @classmethod
    def printer(cls, show=None, publish=None):

        # To print the plot in a nice .eps file in 200 dpi format.
        if publish:
            plt.savefig(publish + ".png", format='png', dpi=300, bbox_inches='tight')

        # To lazy to write plt.show()
        if show:
            plt.show()

    @classmethod
    def color_loop(cls):
        prop_cycle = plt.rcParams['axes.prop_cycle']
        colors = prop_cycle.by_key()['color']
        return colors

    @classmethod
    def remove_borders(cls, axes_rm_borders):
        axes_rm_borders.spines['top'].set_visible(False)
        axes_rm_borders.spines['right'].set_visible(False)
        axes_rm_borders.spines['bottom'].set_visible(False)
        axes_rm_borders.spines['left'].set_visible(False)
        axes_rm_borders.tick_params(which='both', size=0, labelsize=0)
        axes_rm_borders.grid(which='major', color='#DDDDDD', linewidth=0.05)
        axes_rm_borders.grid(which='minor', color='#DDDDDD', linewidth=0.05)
