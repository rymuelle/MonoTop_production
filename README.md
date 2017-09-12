# MonoTop_production

## Installing Delphes and PY8

You must use MadGraph 2.6 or greater, 2.5 has some compatibility issues. This will take some time and you will also need pythia8 if not installed.

1. Navigate to your Madgraph directory run 

        ./bin/mg5_aMC

2. In the madgraph terminal, run 


        install Delphes 

3. After some time, Delphes and pythia will be installed.

Alternativly, you can download Delphes, make them and point to their install path. In your prefered place to install run:

    wget -q http://cp3.irmp.ucl.ac.be/downloads/Delphes-3.4.1.tar.gz
    tar -zxf Delphes-3.4.1.tar.gz
    cd Delphes-3.4.1
    make

In the MG command line, run:

    set delphes_path <path to Delphes>/Delphes-3.4.1
