Guidos Workbench
================

This document provides usage instructions for the image analysis module **GWB** (GuidosToolbox Workbench). **GWB** is a subset of the desktop software package GuidosToolbox (`GTB <https://forest.jrc.ec.europa.eu/en/activities/lpa/gtb/>`_) designed as Jupyter dashboard. More information is available at the **GWB** `homepage <https://forest.jrc.ec.europa.eu/en/activities/lpa/gwb/>`_. 

Introduction
------------

the GuidosToolbox (`GTB <https://forest.jrc.ec.europa.eu/en/activities/lpa/gtb/>`_) was developed as a graphical user interface to morphological spatial pattern analysis of raster data (`Soille and Vogt 2009 <https://doi.org/10.1016/j.patrec.2008.10.015>`_). The GTB has since been enhanced with numerous modules for analysis of landscape objects, patterns, and networks, and specialized modules for assessing fragmentation and restoration (`Vogt and Riitters 2017 <https://doi.org/10.1080/22797254.2017.1330650>`_). The GTB has gained global acceptance as a free, intuitive, interactive, and generic stand-alone image analysis platform on several popular operating systems. Here we implemented the most popular GTB modules inside the SEPAL platform as a Jupyter dashboard using the `GWB CLI tool <https://docs.sepal.io/en/latest/cli/gwb.html>`_. 

Presentation
^^^^^^^^^^^^

To launch the app please follow the SEPAL registration steps and then move to the SEPAL apps' dashboard.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dashboard.png
    :alt: SEPAL dashboard 
    
The application should launch itself in the About section, allowing to select the tool you want to use. 

.. note::
    
    If this is the first time you use the app, you will actually face the following popup:
    
    .. image:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/licence.png
        :alt: licence
        
    This licence needs to be accepted to use the **GWB** tools. It is reminded in the section :code:`Licence` of the app. 
    If you don't want to accept this Licence, just close the app tab.

General structure
^^^^^^^^^^^^^^^^^

The application is strucured as followed: 

On the left side you will find a navigation drawer that you can open and close using the `hamburger button <https://en.wikipedia.org/wiki/Hamburger_button>`_. 

.. tip:: 

    On small devices such as tablet or phones, the navigation drawer will be hidden by default. click on the button and it will overlay the rest of the app 
    
    .. image:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/small_device_without_menu.png
        :alt: small screen without drawer
        :width: 40%
        
    .. image:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/small_device_with_menu.png
        :alt: small screen with drawer
        :width: 40%
        
Each name in the list correspond to a tool of the **GWB** module, they will be prensented individually in the next sections. By clicking on it you will display the panels relative to the function you want to use. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/landing.png
    :alt: presentation of the structure

.. danger:: 

    All the tools in this module use a categorical raster as input. This raster need to use discrete integer value to be manipulated. Any raster with continuous values will raise an error.

Modules
-------

Every module is presented independantely, you can directly jump to the tool you are intersted and this documentation will guide you trough the full process.

ACC
^^^

This module will conduct the **Accounting** analysis. Accounting will label and calculate the area of all foreground objects (coded with 2 byte). The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Accounting <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Objects-Accounting.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes)
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :alt: upload 4 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background. If you sepcify sepcial background they will be treated separately in the analysis (e.g. water, buildings).
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_params.png
    :alt: acc params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   spatial pixel resolution: 25
    -   area thresholds: 200 2000 20000 100000 200000
    -   options: default

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%
    
spatial pixel resolution
########################

Set the spatial pixel resolution of your image in meters. It is only use for the summary.

area thresholds
###############

Set up to 5 area thresholds in pixels. 

options
#######

Two computation options are available: 

-   stats + image of viewport (default)
-   stats + images of ID, area, viewport (detailed)

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you informations about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/acc/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_acc.tif`
-   :code:`<raster_name>_bin_map_acc.csv`
-   :code:`<raster_name>_bin_map_acc.txt`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance your using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. figure:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_acc.tif
    :width: 50%
    :align: center


DIST
^^^^

This module will conduct the **Euclidean Distance** analysis. Each pixel will show the shortest distance to the foreground (coded with 2 byte) boundary. Pixels inside a foreground object have a positive distance value while background pixels have a negative distance value. The result are spatially explicit maps and tabular summary statistics.
Details on the methodology and input/output options can be found in the `Distance <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Distance-Euclidean.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes)
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :alt: upload 2 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background.
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dist_params.png
    :alt: dist params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Options: Euclidian Distance only

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%

Options
#######

Two computation options are available: 

-   compute the Euclidian Distance only
-   compute the Euclidian Distance and the Hysometric Curve


run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you informations about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/dist_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/dist/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_dist.tif`
-   :code:`<raster_name>_bin_map_dist.txt`
-   :code:`<raster_name>_bin_map_dist_hist.png`
-   :code:`<raster_name>_bin_map_dist_viewport.tif`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_dist_hmc.png
    :width: 49%

.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_dist.tif
    :width: 49%

FAD
^^^

This module will conduct the **fragmentation** analysis at **five fixed observation scales**. Because forest fragmentation is scale-dependent, fragmentation is reported at five observation scales, which allows different observers to make their own choice about scales and threshold of concern. The change of fragmentation across different observation scales provides additional interesting information. Fragmentation is measured by determining the Forest Area Density (**FAD**) within a shifting, local neighborhood. It can be measured at pixel or patch level. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes)
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :alt: upload 4 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background. If you sepcify sepcial background they will be treated separately in the analysis (e.g. water, buildings)
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/fad_params.png
    :alt: acc params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Computation prescision: float-prescision
    -   Options: per-pixel density, color-coded into 6 fragmentation classes (FAD)

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%
    
Computation prescision
######################

Set the prescision used to compute you image. Float prescision (default) will give more accurate results that bytes but will also take more Ressource to compute.

Options
#######

Three computation options are available: 

-   FAD: per-pixel density, color-coded into 6 fragmentation classes
-   FAD-APP2: average per-patch density, color-coded into 2 classes
-   FAD-APP5: average per-patch density, color-coded into 5 classes

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/fad_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/fad/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_fad_<class_number>.tif`
-   :code:`<raster_name>_bin_map_fad_barplot.png`
-   :code:`<raster_name>_bin_map_fad_mscale.csv` 
-   :code:`<raster_name>_bin_map_fad_mscale.tif`
-   :code:`<raster_name>_bin_map_fad_mscale.txt`
-   :code:`<raster_name>_bin_map_fad_mscale.sav`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad_barplot.png
    :width: 49%

.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad_mscale.tif
    :width: 49%

FRAG
^^^^

This module will conduct the **fragmentation** analysis at a **user-selected observation scale**. This module and its option are similar to :ref:`gwb_fad` but allow the user to specify a single (or multiple) specific observation scale. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Fragmentation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Fragmentation-FADFOS.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background 1 (optional)
-   special background 2 (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/4_classes.png
    :alt: upload 4 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background. If you specify special background they will be treated separately in the analysis (e.g. water, buildings).
    
.. warning::

    the second special background is the non-fragmenting background (optional)
    
Select parameters
"""""""""""""""""

You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/frag_params.png
    :alt: acc params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8
    -   Spatial pixel resolution: 25
    -   Computation prescision: float-prescision
    -   Windows size: 23
    -   Pptions: average per-patch density, color-coded into 2 classes (FAD-APP2)

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%
    
spatial pixel resolution
########################

Set the spatial pixel resolution of your image in meters. Only use for the summary.

window size
###########

Set up to 10 observation windows size (in pixels).

options
#######

Three computation options are available: 

-   FAD: per-pixel density, color-coded into 6 fragmentation classes
-   FAD-APP2: average per-patch density, color-coded into 2 classes
-   FAD-APP5: average per-patch density, color-coded into 5 classes

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/frag_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/frag/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_frag_fad-<option>_<class>.tif`
-   :code:`<raster_name>_bin_map_frag.csv`
-   :code:`<raster_name>_bin_map_frag.txt`
-   :code:`<raster_name>_bin_map_frag.tif`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance your using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. figure:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_fad-app2_23.tif
    :width: 50%

LM
^^

This module will conduct the **Landscape Mosaic** analysis at a **user-selected observation scale**. The Landscape Mosaic measures land cover heterogeneity, or human influence, in a tri-polar classification of a location accounting for the relative contributions of the three land cover types **Agriculture**, **Natural**, **Developed** in the area surrounding that location. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Landscape Mosaic <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-LM.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/clc3classes.tif` file (3 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   dominant land cover 1
-   dominant land cover 2
-   dominant land cover 3

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/3_classes.png
    :alt: upload 3 classes
    
Select parameters
"""""""""""""""""

You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/lm_params.png
    :alt: lm params
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   window size: 23

window size
###########

Set the square window size (in pixels). It should be an odd number in [3, 5, ...501].
with :math:`kdim` beeing the window size you can calculate it from the observation scale using the following formula: 

..math::

    obs_scale = (pixres * kdim)^2 / 10000
    
with

-   :math:`obs_scale` in hectare
-   :math:`pixres` in meters
-   :math:`kdim` in pixels

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/lm_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/lm/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_lm_23.tif`
-   :code:`<raster_name>_bin_map_lm_23_103class.tif`
-   :code:`<raster_name>_bin_map_heatmap.csv`
-   :code:`<raster_name>_bin_map_heatmap.png`
-   :code:`<raster_name>_bin_map_heatmap.sav`
-   :code:`heatmap_legend.png`
-   :code:`lm103class_legend.png`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`clc3classes.tif` file.
    
.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/lm103class_legend.png
    :width: 49%

.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/clc3class_lm_23.tif
    :width: 49%

MSPA
^^^^

This module will conduct the **Morphological Spatial Pattern Analysis**. MSPA analyses shape and connectivity and conducts a segmentation of foreground patches in up to 25 feature classes. The result are spatially explicit maps and tabular summary statistics. Details on the methodology and input/output options can be found in the `Morphology <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-Morphology.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :alt: upload 2 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background.
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_params.png
    :alt: acc params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8 (default)
    -   Edge width: 1
    -   Transition: True
    -   Intext: True

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%
    
Edge width
##########

Define in pixel the width of the edges that will defin the cores of the MSPA analysis.

Transitions
###########

Select wether or not to use transitions.

Intext
######

Select wether or not to use intext.

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/mspa_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/mspa/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_<4 params>.tif`
-   :code:`<raster_name>_bin_map_<4 params>.txt`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.
    
Here is the result of the computation using the default parameters on the :code:`example.tif` file.
    
.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/mspalegend.gif
    :width: 49%

.. image:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_8_1_1_1.tif
    :width: 49%

P223
^^^^

This module will conduct the **Density** (P2), **Contagion** (P22) or **Adjacency** (P23) analysis of foreground (**FG**) objects at a user-selected observation scale (`Riitters et al. (2000) <https://www.srs.fs.usda.gov/pubs/ja/ja_riitters006.pdf>`_). The result are spatially explicit maps and tabular summary statistics. The classification is determined by measurements of forest amount (P2) and connectivity (P22) within the neighborhood that is centered on a subject forest pixel. P2 is the probability that a pixel in the neighborhood is forest, and P22 is the probability that a pixel next to a forest pixel is also forest.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground
-   special background (optional)

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/p223_classes.png
    :alt: upload 3 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background. If you sepcify a sepcial background it will be treated separately in the analysis (e.g. water, buildings)
    
Select parameters
"""""""""""""""""

You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/acc_params.png
    :alt: acc params
    
.. note::

    These parameters can be used to perform the default computation:
    
    -   Window size: 27
    -   Computation prescision: Float (default)
    -   Algorithm: FG-Density
    
Window size
###########

Set the square window size (in pixels) It should be an odd number in [3, 5, ...501].
with :math:`kdim` beeing the window size you can calculate it from the observation scale using the following formula: 

.. math::

    obs_scale = (pixres * kdim)^2 / 10000
    
with 

- :math:`obs_scale` in hectare
- :math:`pixres` in meters
- :math:`kdim` in pixels

Computation prescision
######################

Set the prescision used to compute you image. Float prescision (default) will give more accurate results that bytes but will also take more Ressource to compute.

Algorithm
#########

The P223 module can run: **FG-Density** (P2), **FG-Contagion** (P22), or **FG-Adjacency** (P23)

P223 will provide a color-coded image showing [0,100]% for either **FG-Density**, **FG-Contagion**, or **FG-Adjacency** masked for the Foreground cover. Use the alternative options to obtain the original spatcon output without normalisation, masking, or color-coding.

.. tip::

    For original spatcon output **ONLY**:
    Missing values are coded as 0 (rounded byte), or -0.01 (float precision). For all output types, missing indicates the input window contained only missing pixels.

.. tip::

    For FG-Contagion and FG-Adjacency output **ONLY**, missing also indicates the input window contained no foreground pixels (there was no information about foreground edge).

For all output types, :math:`rounded byte = (float precision * 254) + 1`
    
You'll find the options displayed with the following names in the dropdown:

-   FG-Density   (FG-masked and normalised)
-   FG-Contagion (FG-masked and normalised)
-   FG-Adjacency (FG-masked and normalised)
-   FG-Density   (original spatcon output)
-   FG-Contagion (original spatcon output)
-   FG-Adjacency (original spatcon output)
-   FG-Shannon   (original spatcon output)
-   FG-SumD      (original spatcon output)

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/p223_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/p223/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_p<option>_<window>.tif`
-   :code:`<raster_name>_bin_map_p<option>_<window>.txt`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. figure:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_p2_27.tif
    :width: 50%

PARC
^^^^

This module will conduct the **parcellation** analysis. This module provides a statistical summary file (txt/csv- format) with details for each unique class found in the image as well as the full image content: class value, total number of objects, total area, degree of parcellation.
Details on the methodology and input/output options can be found in the `Parcellation <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Objects-Parcellation.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/clc3classes.tif` file (3 classes).
    
The first step requires you to select your image in your SEPAL folder. The image need to be a categorical tif raster.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/0_classes.png
    :alt: upload 0 classes
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/parc_params.png
    :alt: parc params
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   Foreground connectivity: 8

Foreground connectivity
#######################

This set the foreground connectivity of your analysis:

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/parc_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/parc/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_parc.csv`
-   :code:`<raster_name>_bin_map_parc.txt`


.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`clc3classes.tif` file.

.. csv-table::
    :header: Class, Value, Count, Area[pixels], APS, AWAPS, AWAPS/data, DIVISION, PARC[%]

    1,1,45,2.44893e+06,54420.7,2.07660e+06,1.27136e+06,0.152039,1.19374
    2,2,164,957879.,5840.73,82557.6,19770.0,0.913812,17.7426
    3,3,212,593190.,2798.07,128177.,19008.4,0.783919,11.0897
    8-connected Parcels:, ,421, 4000000,9501.19, ,1310139.4,0.672465,8.07904

RSS
^^^

This module will conduct the **Restoration Status Summary analysis**. It will calculate key attributes of the current network status, composed of foreground (forest) patches and it provides the normalized degree of network coherence. The result are tabular summary statistics. Details on the methodology and input/output options can be found in the `Restoration Planner <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-RestorationPlanner.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :alt: upload 2 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background.
    
Select parameters
"""""""""""""""""
You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/rss_params.png
    :alt: rss params
    
.. note::

    This parameters can be used to perform the default computation:
    
    -   Foreground connectivity: 8

Foreground connectivity
#######################

This set the foreground connectivity of your analysis: 

-   8 neigbors (default) will use every pixel in the vincinity (including diagonals)
-   4 neigbors only use the vertical and horizontal one

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/connectivity.png
    :alt: connectivity image
    :width: 50%

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/rss_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/rss/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`rss<connectivity>.txt`
-   :code:`rss<connectivity>.csv`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. csv-table::
    :header: FNAME, AREA, RAC[%], NR_OBJ, LARG_OBJ, APS, CNOA, ECA, COH[%]
    
    example_bin_map.tif,428490.00,42.860572,2850,214811,150.34737,311712,221292.76,51.644789

SPA
^^^

This module will conduct the **Simplified Pattern Analysis**. SPA analyses shape and conducts a segmentation of foreground patches into 2, 3, 5, or 6 feature classes. The result are spatially explicit maps and tabular summary statistics. :code:`GWB_SPA` is a simpler version of :code:`GWB_MSPA`. Details on the methodology and input/output options can be found in the `Morphology <https://ies-ows.jrc.ec.europa.eu/gtb/GTB/psheets/GTB-Pattern-Morphology.pdf>`_ product sheet.

Set up image
""""""""""""

.. tip::

    You can use the default dataset to test the module. Click on the :code:`Download test dataset` button on the top of the second panel. By clicking on this button, 2 files will be added to your :code:`downloads` folder (:code:`example.tif` and :code:`clc3classes.tif`).
    
    .. figure::  https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/test_dataset.png
        :alt: download tes dataset
        :width: 45%
    
    Once the file is downloaded follow the normal process using the :code:`downloads/example.tif` file (2 classes).
    
The first step requires you to reclassify your image. Using the reclassifying panel, select your image in your SEPAL folder.

.. warning:: 

    If the image is not in your SEPAL folders but in your local computer consider reading the `exchange file with SEPAL <https://docs.sepal.io/en/latest/setup/filezilla.html>`_ page of this documentation.
    
The dropdowns menu will hydrate themselves with the discrete values of your raster. Select each class in your image and place them in one of the following categories: 

-   background
-   foreground

Every class that is not set to a reclassifying category will be considered as "missing data" (0 byte) and removed from the analysis.

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/2_classes.png
    :alt: upload 2 classes

.. tip::

    for forest analysis you will want to set forest as foreground and all the other classes in background.
    
Select parameters
"""""""""""""""""

You will need to select parameters for your computation: 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/spa_params.png
    :alt: spa params
    
.. note::

    This parameter can be used to perform the default computation:
    
    -   number of patterns class: SLF, Coherent (2)

number of patterns class
########################

Set the number of pattern class you want to compute:

-   SLF, Coherent (2)
-   Core, Core-Openings, Margin (3)
-   Core, Core-Openings, Edge, Perforation, Margin (5)
-   Core, Core-Openings, Edge, Perforation, Islet, Margin (6)

run analysis
""""""""""""

Once your parameters are all set you can launch the analysis. The blue rectangle will display you information about the computation. It will turn to green at the end and display some computation logs. 

.. figure:: https://raw.githubusercontent.com/12rambau/gwb/master/doc/img/spa_results.png
    :alt: information logs

The final files can be retreived in :code:`module_results/gwb/spa/` folder. it should include:

-   :code:`<raster_name>_bin_map.tif`
-   :code:`<raster_name>_bin_map_spa<nuber of class>.tif`
-   :code:`<raster_name>_bin_map_spa<number of class>.txt`

.. danger::

    If the rectangle become red, read attentively the instruction of the logs. Usually the instance you're using is too small to handle the file you want to analyse. If it's the case, close the app, open a bigger instance and run your analysis again.

Here is the result of the computation using the default parameters on the :code:`example.tif` file.

.. figure:: https://raw.githubusercontent.com/openforis/sepal-doc/master/docs/source/img/cli/gwb/example_spa2.tif
    :width: 50%