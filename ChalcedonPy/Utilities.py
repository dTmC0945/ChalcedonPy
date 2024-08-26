import matplotlib.pyplot as plt
from cycler import cycler 
from pathlib import Path # to work with paths
import matplotlib.colors  # all related to colours

def init(save_path):
   global SAVE_PATH
   SAVE_PATH = save_path
   

# define a function to store matplotlib style information
def plot_settings(style, size):

   # define custom default colors for generating image with
   # consisten color cycling
   new_colours = ['#326199',
                 '#4fb1a1',
                 '#fcc055',
                 '#eb8d50',
                 '#df6e5b',
                 '#9a031e',
                 '#984ea3']
   
   # define the styles for generating web compatible images.
   if style == "web":
      style = {
         'axes.edgecolor': '1e1e2e',
         'axes.facecolor': '363a4f',
         'axes.axisbelow' : True,
         'axes.labelcolor' : 'cad3f5',
         'axes.grid': True,
         'axes.grid.which': 'both',
         'axes.spines.left': False,
         'axes.spines.right': False,
         'axes.spines.top': False,
         'axes.spines.bottom': False,
         'axes.prop_cycle': cycler(color=new_colours),

         'grid.color': '5b6078',
         'grid.linewidth': '1.2',
         
         'xtick.color': 'cad3f5',
         'xtick.major.bottom': True,
         'xtick.labelsize': 10,
         'xtick.minor.bottom': True,
         'xtick.minor.bottom': True,
         'xtick.minor.visible': True,
         'xtick.minor.width': 0.5,
         
         'ytick.color': 'cad3f5',
         'ytick.major.left': True,
         'ytick.minor.left': False,
         'ytick.minor.visible': True,
         'ytick.labelsize': 10,

         'savefig.facecolor': '363a4f',

         'text.color': 'cad3f5',
         
         'lines.linewidth': 4,

         'font.size': 16,
         
         'legend.fancybox' : False,
         'legend.facecolor' : '6c7086',
         
         'figure.facecolor': '838ba7',
      }

      # Define the font dictionary to store label formatting
      font = {'color':  '#cad3f5',
              'weight': 'normal',
              'size': 16,
              }   

   elif style == "slide":
      style = {
         'axes.edgecolor': 'f0f0f0',
         'axes.facecolor': 'fafafa',
         'axes.axisbelow' : True,
         'axes.labelcolor' : '1e1e1e',
         'axes.grid': True,
         'axes.grid.which': 'both',
         'axes.spines.left': False,
         'axes.spines.right': False,
         'axes.spines.top': False,
         'axes.spines.bottom': False,
         'axes.prop_cycle': cycler(color=new_colours),

         'grid.color': 'f0f0f0',
         'grid.linewidth': '1.2',
         
         'xtick.color': '1e1e1e',
         'xtick.major.bottom': True,
         'xtick.labelsize': 10,
         'xtick.minor.bottom': True,
         'xtick.minor.bottom': True,
         'xtick.minor.visible': True,
         'xtick.minor.width': 0.5,
         
         'ytick.color': '1e1e1e',
         'ytick.major.left': True,
         'ytick.minor.left': False,
         'ytick.labelsize': 10,

         'savefig.facecolor': 'fafafa',

         'text.color': '1e1e1e',
         
         'lines.linewidth': 4,

         'font.size': 12,
         
         'legend.fancybox' : False,
         'legend.facecolor' : '6c7086',
         
         'figure.facecolor': 'fafafa',
      }

      # Define the font dictionary to store label formatting
      font = {'color':  '#1e1e1e',
              'weight': 'normal',
              'size': 16,
              }   

   # Apply style sheet for use in matplotlib
   plt.rcParams.update(style)
   
   # Define figure size based on the number of figures
   if size == 1:
      plt.figure(figsize=(10,6))
   elif size == 2:
      plt.figure(figsize=(12,5))
   elif size == None:
      return 0

def grid_settings(style):
   """
   Sets the grid settings for the matplotlib plotting

   variables:

   style: sets the output type takes either "web" or "slides"
   """

   if style == "web":
      plt.grid(which='minor', color='#5b6078', linestyle=':', linewidth=0.5)
      plt.grid(which='major', color='#5b6078', linestyle=':', linewidth=0.8)
      
   elif style == "slide": 
      plt.grid(which='minor', color='#c8c8c8', linestyle=':', linewidth=0.5)
      plt.grid(which='major', color='#c8c8c8', linestyle=':', linewidth=0.8)

   plt.minorticks_on()

def store_fig(fig_id,
              tight_layout=True,
              fig_extension="png",
              resolution=400,
              style=None,
              close=None):
    
    if tight_layout:
        plt.tight_layout()
        
    if style == "web":
        plot_settings(size = None, style = "web")
        plt.grid(which='minor', color='#5b6078', linestyle=':', linewidth=0.5)
        plt.grid(which='major', color='#5b6078', linestyle=':', linewidth=0.8)
        fig_extension = "png"
        
    elif style == 'slide':
        plot_settings(size = None, style = "slide")
        plt.grid(which='minor', color='#c8c8c8', linestyle=':', linewidth=0.5)
        plt.grid(which='major', color='#c8c8c8', linestyle=':', linewidth=0.8)
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
