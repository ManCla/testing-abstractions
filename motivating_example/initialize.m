clear all

% process matrices
A=[-0.12 0; 5 0];
B=[2.25; 0];
C=eye(2);
D=[0;0];

% sampling time of control loop
st=0.05; % 50[ms]

% square wave reference signal
ramp=255;  % amplitude
rfq=0.1;   % [Hz]

% number of bits A/D and D/A
n_bits=10;
max_int10=2^(n_bits-1);

% volts of the power source
volts=10;

% conversion from int16_t in [+511,-512] to Volt in [+10,-10]
int_to_volt=volts/max_int10;
% conversion from Volt in [+10,-10] to int16_t in [+511,-512] 
volt_to_int=max_int10/volts;

% frequency of triangular wave for PWM
Tpwm=0.05;     %[Hz]
TfilterPWM=140; % time constant of analog filter
fo=[1/TfilterPWM 1];
afDen=conv(fo,fo);