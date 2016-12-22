#define RUNONDATA 0
#define LOGSCALE 0
#define NORMALIZE 1
#define POISSON 0
#define SAVEPLOTS 1
#define MAXEVENTS 100000
#define NMAXJETS 30
#define CUT_HT -500.0
#define CSVM 0.89
#define LUMI 10.0  //Just for now

#include <fstream>

float deltaR(float eta1, float phi1, float eta2, float phi2);

float deltaEta(float eta1, float eta2);

float deltaPhi(float phi1, float phi2);

float deltaD(float eta1, float phi1, float eta2, float phi2);

int checkreps(int e);

void Control_plots(){

  TStopwatch* clock = new TStopwatch();
  clock->Start();

  float xmin  = 0;
  float xmax  = 6.0;

  string folder = "/scratch/dsalerno/TTH_MEM_74X/V14/crab_151222/";

  string variable;
  //variable = "leadjet_pt";
  //variable = "num_btag";
  //variable = "leadjet_eta";
  //variable = "btagLR";     xmin=-1.0;  xmax=2.0;     //xmin sets the bLR cut
  
  //variable = "DR1j";     xmin=0.0;  xmax=2.0;
  //variable = "DR2j";     xmin=0.0;  xmax=3.5;
  //variable = "DR3j";     xmin=0.5;  xmax=4.5;
  //variable = "DR4j";     xmin=1.0;  xmax=5.0;
  //variable = "DR5j";     xmin=1.0;  xmax=5.5;
  //variable = "DR6j";     xmin=1.0;  xmax=5.5;

  //variable = "Deta1j";     xmin=0.0;  xmax=1.0;
  //variable = "Deta2j";     xmin=0.0;  xmax=1.6;
  //variable = "Deta3j";     xmin=0.0;  xmax=2.5;
  //variable = "Deta4j";     xmin=0.0;  xmax=3.5;
  //variable = "Deta5j";     xmin=0.0;  xmax=4.5;
  //variable = "Deta6j";     xmin=0.0;  xmax=4.5;

  //variable = "Dphi1j";     xmin=0.0;  xmax=1.0;
  //variable = "Dphi2j";     xmin=0.0;  xmax=2.0;
  //variable = "Dphi3j";     xmin=0.0;  xmax=3.0;
  //variable = "Dphi4j";     xmin=0.5;  xmax=3.2;
  //variable = "Dphi5j";     xmin=1.0;  xmax=3.2;
  //variable = "Dphi6j";     xmin=1.5;  xmax=3.2;

  //variable = "Deta1j2";     xmin=0.0;  xmax=4.0;
  //variable = "Deta2j3";     xmin=0.0;  xmax=4.0;
  //variable = "Deta3j4";     xmin=0.0;  xmax=4.5;
  //variable = "Deta4j5";     xmin=0.0;  xmax=4.5;
  //variable = "Deta5j6";     xmin=0.0;  xmax=5.0;
  //variable = "Deta6j7";     xmin=0.0;  xmax=5.0;

  //variable = "DD1j";     xmin=0.0;  xmax=2.1;
  //variable = "DD2j";     xmin=0.0;  xmax=2.1;
  //variable = "DD3j";     xmin=0.0;  xmax=2.1;
  //variable = "DD4j";     xmin=0.0;  xmax=2.1;
  //variable = "DD5j";     xmin=0.0;  xmax=2.1;
  //variable = "DD6j";     xmin=0.0;  xmax=2.0;

  //variable = "DD1j2";     xmin=0.0;  xmax=2.0;
  //variable = "DD2j3";     xmin=0.0;  xmax=12.0;
  variable = "DD3j4";     xmin=0.0;  xmax=5.0;
  //variable = "DD4j5";     xmin=0.0;  xmax=2.0;
  //variable = "DD5j6";     xmin=0.0;  xmax=2.0;
  //variable = "DD6j7";     xmin=0.0;  xmax=2.0;

  string tag = "_withtrig";
  if(CUT_HT>0) tag += Form("_HT%.0f",CUT_HT);  
  if(variable == "btagLR") tag += Form("bLR_%f",xmin);
  if(RUNONDATA) tag += "_data";
  if(LOGSCALE)  tag += "_log";  

  std::ofstream outfile( ("./logs/log_Control_"+variable+tag+".txt").c_str() ); 

  outfile << "Plotting variable " << variable << endl << endl;

  gStyle->SetOptStat(0);
  gStyle->SetTitleFillColor(0);
  gStyle->SetCanvasBorderMode(0);
  gStyle->SetCanvasColor(0);
  gStyle->SetPadBorderMode(0);
  gStyle->SetPadColor(0);
  gStyle->SetTitleFillColor(0);
  gStyle->SetTitleBorderSize(0);
  gStyle->SetTitleH(0.04);
  //gStyle->SetTitleFontSize(0.025);
  gStyle->SetTitleStyle(0);
  gStyle->SetTitleOffset(1.3,"y");

  TCanvas *c1 = new TCanvas("c1","",5,30,640,580);
  TPad *p1 = new TPad("p1","",0,0,1,1);
  
  if( tag.find("ratio") != string::npos ){
    c1 = new TCanvas("c1","",5,30,640,580/0.85);
    p1 = new TPad("p1","",0,0.155,1,1);
  }

  p1->SetGrid(0,0);
  p1->SetFillStyle(4000);
  p1->SetFillColor(10);
  p1->SetTicky();
  p1->SetTicks(0,0);
  p1->SetObjectStat(0);
  p1->Draw();
  p1->cd();

  p1->SetTopMargin(0.05);

  TString cmsinfo = "";
  if(RUNONDATA==0) cmsinfo = Form("Simulation                                                  %.1f fb^{-1} (13 TeV)",LUMI);
  else cmsinfo =             Form("CMS Preliminary                                     %.1f fb^{-1} (13 TeV)",LUMI);

  TPaveText *pt_title = new TPaveText(0.1, 0.952, 0.9, 1.0,"brNDC");
  pt_title->SetFillStyle(1001);
  pt_title->SetBorderSize(0);
  pt_title->SetFillColor(0);
  pt_title->SetTextFont(42); 
  pt_title->SetTextSize(0.04); 
  pt_title->AddText(cmsinfo);

  TLegend* leg = new TLegend(0.12,0.54,0.37,0.91,NULL,"brNDC"); // right:0.62-0.87, left:0.12-0.37
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetFillColor(10);
  leg->SetTextSize(0.04);

  THStack* hStack = new THStack("hStack","Title; x-axis ; events ");

  // set samples here
  vector<string> samples;
  //samples.push_back("dummy");
  //samples.push_back("QCDMultijet");
  samples.push_back("QCD");
  //samples.push_back("TTJets");
  samples.push_back("TTH");
  if(RUNONDATA)  samples.push_back("Data");

  TH1F* hS    = 0;
  TH1F* hData = 0;
  TH1F* hErr  = 0;

  TH1F* httH  = 0;
  TH1F* hQCD  = 0;
  TH1F* httjj = 0;
  TH1F* httcc = 0;
  TH1F* httb  = 0;
  TH1F* httbb = 0;

  // determine plot parameters for different variables
  TString title = "Histogram title";
  int   nbins = 30;
  TString xaxis = "m";

  if(variable=="leadjet_pt"){
    title = "seventh jet pT";
    nbins = 30;
    xmin = 20;
    xmax = 8000;
    xaxis = "p_{T}";
  }
  if(variable=="num_btag"){
    title = "number of CSVM";
    nbins = 9;
    xmin = 0;
    xmax = 9;
    xaxis = "no. b";
  }
  if(variable=="leadjet_eta"){
    title = "leading jet #eta";
    nbins = 30;
    xmin = -3.0;
    xmax = 3.0;
    xaxis = "leading jet #eta";
  }
  if(variable.find("btagLR")==0){
    title = ("b_{LR}: "+variable).c_str();
    nbins = 30;
    xaxis = "b_{LR}";
  }
  if(variable.find("DR")==0){
    title = variable;
    nbins = 60;
    xaxis = "#DeltaR_{nj}";
  }
  if(variable.find("Deta")==0){
    title = variable;
    nbins = 60;
    xaxis = "#Delta#eta_{nj}";
  }
  if(variable.find("DD")==0){
    title = variable;
    nbins = 60;
    xaxis = "distance_{nj}";
  }
  if(variable.find("Dphi")==0){
    title = variable;
    nbins = 60;
    xaxis = "#Delta#phi_{nj}";
  }

  // master histogram (all other histograms are a clone of this one)
  TH1F* h1 = new TH1F("h1",""+title+"; "+xaxis+"; Events", nbins , xmin, xmax );

  h1->GetXaxis()->SetTitleFont(62);
  h1->GetXaxis()->SetTitleSize(0.04);
  h1->GetXaxis()->SetLabelFont(62);
  h1->GetXaxis()->SetLabelSize(0.038);

  h1->GetYaxis()->SetTitleFont(62);
  h1->GetYaxis()->SetTitleSize(0.039);
  h1->GetYaxis()->SetLabelFont(62);
  h1->GetYaxis()->SetLabelSize(0.038);

  // clone histograms
  httH  = (TH1F*)h1->Clone("httH" );
  hQCD  = (TH1F*)h1->Clone("hQCD" );
  httjj = (TH1F*)h1->Clone("httjj");
  httcc = (TH1F*)h1->Clone("httcc");
  httb  = (TH1F*)h1->Clone("httb" );
  httbb = (TH1F*)h1->Clone("httbb");
  hErr  = (TH1F*)h1->Clone("Err");
  hData = (TH1F*)h1->Clone("hData");
  hS    = (TH1F*)h1->Clone("hS");

  // set histogram styles
  hS   ->SetLineWidth( 4 );
  hS   ->SetLineColor( kBlue+2 );
  hS   ->Sumw2();
  httH ->SetLineColor( kBlue+2 );
  httH ->SetFillColor( kBlue+2 );
  httH ->SetFillStyle( 3002 );
  httH ->SetMarkerColor( kBlue+2 );
  httH ->SetMarkerStyle( 20 );
  httH ->SetMarkerSize( 1.5 );
  httH ->Sumw2();
  hQCD ->SetLineColor( kGreen+3 );
  hQCD ->SetFillColor( kGreen+3 );
  hQCD ->SetMarkerColor( kGreen+3 );
  hQCD ->SetMarkerStyle( 21 );
  hQCD ->SetMarkerSize( 1.5 );
  hQCD ->Sumw2();
  httjj->SetLineColor( kRed-7 );
  httjj->SetFillColor( kRed-7 );
  httjj->SetMarkerColor( kRed-7 );
  httjj->SetMarkerStyle( 22 );
  httjj->SetMarkerSize( 1.5 );
  httjj->Sumw2();
  httcc->SetLineColor( kRed+1 );
  httcc->SetFillColor( kRed+1 );
  httcc->SetMarkerColor( kRed+1 );
  httcc->SetMarkerStyle( 33 );
  httcc->SetMarkerSize( 1.5 );
  httcc->Sumw2();
  httb ->SetLineColor( kRed-2 );
  httb ->SetFillColor( kRed-2 );
  httb ->SetMarkerColor( kRed-2 );
  httb ->SetMarkerStyle( 34 );
  httb ->SetMarkerSize( 1.5 );
  httb ->Sumw2();
  httbb->SetLineColor( kRed+3 );
  httbb->SetFillColor( kRed+3 );
  httbb->SetMarkerColor( kRed+3 );
  httbb->SetMarkerStyle( 29 );
  httbb->SetMarkerSize( 1.5 );
  httbb->Sumw2();
  hErr ->SetLineColor( kBlack );
  hErr ->SetFillColor( kBlack );
  hErr ->SetFillStyle( 3654 );
  hData->SetMarkerStyle( 20 );
  hData->SetMarkerSize( 1.5 );
  hData->SetMarkerColor( kBlack );
  hData->SetLineColor( kBlack );
  hData->SetLineWidth( 2 );

  // loop over samples
  for(unsigned int s=0; s<samples.size(); s++){

    outfile << endl << "Running sample " << samples[s] << endl;
    cout << endl << "Running sample " << samples[s] << endl;

    vector<string> fname;
    
    if( samples[s] == "QCD" ){
      //fname.push_back(folder+"QCD300/tree_QCD300.root");      
      fname.push_back(folder+"QCD500/tree_QCD500.root");
      fname.push_back(folder+"QCD700/tree_QCD700.root");
      fname.push_back(folder+"QCD1000/tree_QCD1000.root");
      fname.push_back(folder+"QCD1500/tree_QCD1500.root");
      fname.push_back(folder+"QCD2000/tree_QCD2000.root");
    }
    else if( samples[s].find("Data") != string::npos ){
      fname.push_back(folder+"ME_data.root");
    }
    else if( samples[s] == "TTH" ){
      fname.push_back(folder+"TTH/tree_TTH_part.root");
    }
    else{
      fname.push_back(folder+samples[s]+"/tree_"+samples[s]+".root");
    }
    // loop over input files
    for(unsigned int f=0; f<fname.size(); f++){
      
      outfile << endl << "Running file " << fname[f] << endl;

      float nGen_fac = 1.0;
      if( fname[f].find("/TTH/") != string::npos ) nGen_fac = 3933404.0/(3933404.0-3089.0);
      // else if( fname[f].find("TTJets") != string::npos ) nGen_fac = 19757190.0/14278690.0;
      // else if( fname[f].find("QCD300") != string::npos ) nGen_fac = 19466760.0/18282047.0;
      // else if( fname[f].find("QCD500") != string::npos ) nGen_fac = 19664159.0/17830047.0;
      // else if( fname[f].find("QCD700") != string::npos ) nGen_fac = 15165288.0/13441279.0;
      // else if( fname[f].find("QCD1000") != string::npos ) nGen_fac = 4963895.0/4461516.0;
      // else if( fname[f].find("QCD1500") != string::npos ) nGen_fac = 3691495.0/3415737.0;
      // else if( fname[f].find("QCD2000") != string::npos ) nGen_fac = 1912529.0/1862522.0

      // load file
      TFile* file = TFile::Open( fname[f].c_str() );
      if(file==0 || file->IsZombie() ) continue;
      
      // load tree
      TTree *tree = (TTree*)file->Get("tree");

      // Declare calculated variables
      int numEvents = 0;
      int numSelected = 0;
      int numttbb = 0;
      int numttbj = 0;
      int numttcc = 0;
      int numttjj = 0;
      float eval;
      int MCweight = 0;

      // Declare leaf types
      int    evt;
      int    numJets;
      int    nBCSVM;
      int    cat;
      int    njets;
      double ht;
      double jets_pt      [NMAXJETS];  //jets sorted by decreasing pT
      double jets_eta     [NMAXJETS];
      double jets_phi     [NMAXJETS];
      double jets_mass    [NMAXJETS];
      double jets_btagCSV [NMAXJETS];
      double jets_qgl     [NMAXJETS];
      
      int   nleps;
      // float leps_pt     [99];  //loose leptons
      // float leps_eta    [99];
      // float leps_phi    [99];
      // float leps_mass      [99];
      // float lepton_charge [99];
      // float lepton_rIso   [99];
      // int   lepton_type   [99];

      // float MET_pt;
      // float MET_phi;
      // float MET_sumEt;
 
      // int       Vtype;
      // EventInfo EVENT;
      // UChar_t   triggerFlags[70];
      double    weight_xs;
      // float     QCDweight;
      // float     Trigweight;
      int       cat_gen;        //-1=unknown, 0=SL, 1=DL, 2=FH
      double    puWeight;
      double    genWeight;
      double    btag_LR;
      double    mem_tth_p[13];
      double    mem_ttbb_p[13];
      int       triggerDecision;
      
      //float p4H       [4];    //generator level 4-vectors: 0=pT, 1=eta, 2=phi, 3=m
      //float p4T       [4];
      //float p4Tbar    [4];
      
      //int   nSimBs;
      int   nMatchSimB;    //use for tt+jets subsample: ttbb, ttbj, or ttjj
      int   nMatchSimC;    //use for tt+jets subsample: ttcc or ttjj

      // Connect the branches with their member variables.
      if(!tree) return;
      tree->SetBranchAddress("evt",           &evt);
      tree->SetBranchAddress("numJets",       &numJets);
      tree->SetBranchAddress("nBCSVM",        &nBCSVM);
      tree->SetBranchAddress("cat",           &cat);
      tree->SetBranchAddress("njets",         &njets);
      tree->SetBranchAddress("ht",            &ht);     
      tree->SetBranchAddress("jets_pt",       jets_pt);
      tree->SetBranchAddress("jets_eta",      jets_eta);
      tree->SetBranchAddress("jets_phi",      jets_phi);
      tree->SetBranchAddress("jets_mass",     jets_mass);
      tree->SetBranchAddress("jets_btagCSV",  jets_btagCSV);
      tree->SetBranchAddress("jets_qgl",      jets_qgl);

      tree->SetBranchAddress("nleps",        &nleps);
      //tree->SetBranchAddress("leps_pt",      leps_pt);
      //tree->SetBranchAddress("leps_eta",     leps_eta);
      //tree->SetBranchAddress("leps_phi",     leps_phi);
      //tree->SetBranchAddress("leps_mass",    leps_mass);
      //tree->SetBranchAddress("lepton_charge",lepton_charge);
      //tree->SetBranchAddress("lepton_rIso",  lepton_rIso);
      //tree->SetBranchAddress("lepton_type",  lepton_type);

      //tree->SetBranchAddress("MET_pt",       &MET_pt);
      //tree->SetBranchAddress("MET_phi",      &MET_phi);
      //tree->SetBranchAddress("MET_sumEt",    &MET_sumEt);
      
      //tree->SetBranchAddress("Vtype",         &Vtype);
      //tree->SetBranchAddress("EVENT",        &EVENT);
      //tree->SetBranchAddress("triggerFlags",  triggerFlags);
      tree->SetBranchAddress("weight_xs",        &weight_xs);
      //tree->SetBranchAddress("QCDweight",     &QCDweight);
      //tree->SetBranchAddress("Trigweight",    &Trigweight);
      
      tree->SetBranchAddress("cat_gen",          &cat_gen);
      tree->SetBranchAddress("puWeight",         &puWeight);
      tree->SetBranchAddress("genWeight",        &genWeight);
      tree->SetBranchAddress("btag_LR_4b_2b",    &btag_LR);
      tree->SetBranchAddress("mem_tth_p",        mem_tth_p);
      tree->SetBranchAddress("mem_ttbb_p",       mem_ttbb_p);
      tree->SetBranchAddress("triggerDecision",  &triggerDecision);
      
      //tree->SetBranchAddress("p4H",          p4H);
      //tree->SetBranchAddress("p4T",          p4T);
      //tree->SetBranchAddress("p4Tbar",       p4Tbar);
      
      //tree->SetBranchAddress("nSimBs",       &nSimBs);
      tree->SetBranchAddress("nMatchSimB",  &nMatchSimB);
      tree->SetBranchAddress("nMatchSimC",  &nMatchSimC);
      
      int totalEntries = tree->GetEntries();
      outfile << totalEntries << endl;
      
      int nEvents = 0;
      if( (MAXEVENTS<0) || (MAXEVENTS>totalEntries)  ) nEvents = totalEntries;
      else nEvents = MAXEVENTS;
      if(samples[s]=="TTJets")  nEvents = totalEntries;

      float scalefac = float(totalEntries)/float(nEvents) * nGen_fac;
      float lumi = LUMI*1000.0; //weight_xs scales to 1 pb-1 or 0.001 fb-1
     
      // no rescaling for all hadronic ttbar decay gen filter

      int repeated = 0;
      //////////////////////////////////////////////////// loop over events
      for(int entry=0; entry < nEvents; entry++){
	tree->GetEntry(entry);
	numEvents++;
	eval = -99.;
	
	// print the processed event number
	if(entry%(totalEntries/20)==0){
	  cout << entry << " (" << float(entry)/float(totalEntries)*100 << " %)" << endl;
	}
	// lepton veto
	if( nleps > 0 ) continue;

	// event selection - category and correct tt+jets subsample
	bool pass = true;

	// gen filter on all hadronic ttbar decay
	// if( (samples[s]== "TTH" || samples[s]== "TTJets") && cat_gen!=2 ) continue;
	
	// Trigger selection
	if( triggerDecision<=0 ) continue;

	// HT cut
	if( ht < CUT_HT) continue;
	
	// remove repeated events
	int rep = 0;
	if(evt==repeated) continue;
	rep = checkreps(evt);
	if(rep){
	  repeated = rep;
	  cout << "repeated event " << evt << endl;
	}

	// selection
	if( pass ){

	  int limit = njets<NMAXJETS ? njets : NMAXJETS;
	  
	  // calculate number of b-tag medium and save indices	
	  int n_btag = nBCSVM;
	  if( (samples[s].find("QCDMultijet") != string::npos) && n_btag == 2 ) n_btag = 4;
	  
	  // calculate HT
	  // already in tree as "ht"
	  
	  MCweight = genWeight/abs(genWeight);  //either +1 or -1

	  // calculate variable to be plotted
	  /*if(variable=="leadjet_pt"){
	    float maxpt = 0.0;
	    for(int i=0; i<limit; i++){
	      if(jet_pt[i]>maxpt) maxpt = jet_pt[i];
	    }
	    eval = maxpt;
	    numSelected += MCweight;
	  }
	  if(variable=="num_btag"){
	    eval = float(n_btag);
	    numSelected += MCweight;
	  }
	  if(variable=="leadjet_eta"){
	    float maxpt = 0.0;
	    float leadeta = -99.0;
	    for(int i=0; i<limit; i++){
	      if(jet_pt[i]>maxpt){
		maxpt = jet_pt[i];
		leadeta = jet_eta[i];
	      }
	    }
	    eval = leadeta;
	    numSelected += MCweight;
	  }
	  if(variable=="btagLR"){
	    if(btagLR >= xmin){
	      eval = btag_LR;
	      numSelected += MCweight;
	    }
	  }
	  */
	  if(variable.find("DR")==0){
	    float dR = 99.0;
	    float DRj = 0.0;
	    //loop over jets
	    for(int i=0; i<limit; i++){
	      float dR1min = 99.0;
	      float dR2min = 99.0;
	      float dR3min = 99.0;
	      float dR4min = 99.0;
	      float dR5min = 99.0;
	      float dR6min = 99.0;
	      for(int j=0; j<limit; j++){
		if( i == j) continue;
		dR = deltaR(jets_eta[i], jets_phi[i], jets_eta[j], jets_phi[j]);
		if(dR < dR1min){
		  dR6min = dR5min;
		  dR5min = dR4min;
		  dR4min = dR3min;
		  dR3min = dR2min;
		  dR2min = dR1min;
		  dR1min = dR;
		}
		else if(dR < dR2min){
		  dR6min = dR5min;
		  dR5min = dR4min;
		  dR4min = dR3min;
		  dR3min = dR2min;
		  dR2min = dR;		  
		}
		else if(dR < dR3min){
		  dR6min = dR5min;
		  dR5min = dR4min;
		  dR4min = dR3min;
		  dR3min = dR;
		}
		else if(dR < dR4min){
		  dR6min = dR5min;
		  dR5min = dR4min;
		  dR4min = dR;
		}
		else if(dR < dR4min){
		  dR6min = dR5min;
		  dR5min = dR;
		}
		else if(dR < dR5min){
		  dR6min = dR;
		}
	      }
	      if(variable=="DR1j") DRj += dR1min;
	      else if(variable=="DR2j") DRj += dR2min;
	      else if(variable=="DR3j") DRj += dR3min;
	      else if(variable=="DR4j") DRj += dR4min;
	      else if(variable=="DR5j") DRj += dR5min;
	      else if(variable=="DR6j") DRj += dR6min;
	    }
	    eval = DRj / limit;
	    numSelected += MCweight;
	  }
	  else if(variable.find("Deta")==0){
	    float deta = 99.0;
	    float Detaj = 0.0;
	    int numjet = 0;
	    if(variable=="Deta1j2") numjet = 2;
	    else if(variable=="Deta2j3") numjet = 3;
	    else if(variable=="Deta3j4") numjet = 4;
	    else if(variable=="Deta4j5") numjet = 5;
	    else if(variable=="Deta5j6") numjet = 6;
	    else if(variable=="Deta6j7") numjet = 7;
	    else numjet = limit;
	    //loop over jets
	    for(int i=0; i<numjet; i++){
	      float deta1min = 99.0;
	      float deta2min = 99.0;
	      float deta3min = 99.0;
	      float deta4min = 99.0;
	      float deta5min = 99.0;
	      float deta6min = 99.0;
	      for(int j=0; j<numjet; j++){
		if( i == j) continue;
		deta = deltaEta(jets_eta[i], jets_eta[j]);
		if(deta < deta1min){
		  deta6min = deta5min;
		  deta5min = deta4min;
		  deta4min = deta3min;
		  deta3min = deta2min;
		  deta2min = deta1min;
		  deta1min = deta;
		}
		else if(deta < deta2min){
		  deta6min = deta5min;
		  deta5min = deta4min;
		  deta4min = deta3min;
		  deta3min = deta2min;
		  deta2min = deta;		  
		}
		else if(deta < deta3min){
		  deta6min = deta5min;
		  deta5min = deta4min;
		  deta4min = deta3min;
		  deta3min = deta;
		}
		else if(deta < deta4min){
		  deta6min = deta5min;
		  deta5min = deta4min;
		  deta4min = deta;
		}
		else if(deta < deta4min){
		  deta6min = deta5min;
		  deta5min = deta;
		}
		else if(deta < deta5min){
		  deta6min = deta;
		}
	      }
	      if(variable.find("Deta1j")==0) Detaj += deta1min;
	      else if(variable.find("Deta2j")==0) Detaj += deta2min;
	      else if(variable.find("Deta3j")==0) Detaj += deta3min;
	      else if(variable.find("Deta4j")==0) Detaj += deta4min;
	      else if(variable.find("Deta5j")==0) Detaj += deta5min;
	      else if(variable.find("Deta6j")==0) Detaj += deta6min;
	    }
	    eval = Detaj / numjet;
	    numSelected += MCweight;
	  }
	  else if(variable.find("DD")==0){
	    float dD = 99.0;
	    float DDj = 0.0;
	    int numjet = 0;
	    if(variable=="DD1j2") numjet = 2;
	    else if(variable=="DD2j3") numjet = 3;
	    else if(variable=="DD3j4") numjet = 4;
	    else if(variable=="DD4j5") numjet = 5;
	    else if(variable=="DD5j6") numjet = 6;
	    else if(variable=="DD6j7") numjet = 7;
	    else numjet = limit;
	    //loop over jets
	    for(int i=0; i<numjet; i++){
	      float dD1min = 99.0;
	      float dD2min = 99.0;
	      float dD3min = 99.0;
	      float dD4min = 99.0;
	      float dD5min = 99.0;
	      float dD6min = 99.0;
	      for(int j=0; j<numjet; j++){
		if( i == j) continue;
		dD = deltaD(jets_eta[i], jets_phi[i], jets_eta[j], jets_phi[j]);
		if(dD < dD1min){
		  dD6min = dD5min;
		  dD5min = dD4min;
		  dD4min = dD3min;
		  dD3min = dD2min;
		  dD2min = dD1min;
		  dD1min = dD;
		}
		else if(dD < dD2min){
		  dD6min = dD5min;
		  dD5min = dD4min;
		  dD4min = dD3min;
		  dD3min = dD2min;
		  dD2min = dD;		  
		}
		else if(dD < dD3min){
		  dD6min = dD5min;
		  dD5min = dD4min;
		  dD4min = dD3min;
		  dD3min = dD;
		}
		else if(dD < dD4min){
		  dD6min = dD5min;
		  dD5min = dD4min;
		  dD4min = dD;
		}
		else if(dD < dD4min){
		  dD6min = dD5min;
		  dD5min = dD;
		}
		else if(dD < dD5min){
		  dD6min = dD;
		}
	      }
	      if(variable.find("DD1j")==0) DDj += dD1min;
	      else if(variable.find("DD2j")==0) DDj += dD2min;
	      else if(variable.find("DD3j")==0) DDj += dD3min;
	      else if(variable.find("DD4j")==0) DDj += dD4min;
	      else if(variable.find("DD5j")==0) DDj += dD5min;
	      else if(variable.find("DD6j")==0) DDj += dD6min;
	    }
	    eval = DDj / numjet;
	    numSelected += MCweight;
	  }
	  else if(variable.find("Dphi")==0){
	    float dphi = 99.0;
	    float Dphij = 0.0;
	    //loop over jets
	    for(int i=0; i<limit; i++){
	      float dphi1min = 99.0;
	      float dphi2min = 99.0;
	      float dphi3min = 99.0;
	      float dphi4min = 99.0;
	      float dphi5min = 99.0;
	      float dphi6min = 99.0;
	      for(int j=0; j<limit; j++){
		if( i == j) continue;
		dphi = deltaPhi(jets_phi[i], jets_phi[j]);
		if(dphi < dphi1min){
		  dphi6min = dphi5min;
		  dphi5min = dphi4min;
		  dphi4min = dphi3min;
		  dphi3min = dphi2min;
		  dphi2min = dphi1min;
		  dphi1min = dphi;
		}
		else if(dphi < dphi2min){
		  dphi6min = dphi5min;
		  dphi5min = dphi4min;
		  dphi4min = dphi3min;
		  dphi3min = dphi2min;
		  dphi2min = dphi;		  
		}
		else if(dphi < dphi3min){
		  dphi6min = dphi5min;
		  dphi5min = dphi4min;
		  dphi4min = dphi3min;
		  dphi3min = dphi;
		}
		else if(dphi < dphi4min){
		  dphi6min = dphi5min;
		  dphi5min = dphi4min;
		  dphi4min = dphi;
		}
		else if(dphi < dphi4min){
		  dphi6min = dphi5min;
		  dphi5min = dphi;
		}
		else if(dphi < dphi5min){
		  dphi6min = dphi;
		}
	      }
	      if(variable=="Dphi1j") Dphij += dphi1min;
	      else if(variable=="Dphi2j") Dphij += dphi2min;
	      else if(variable=="Dphi3j") Dphij += dphi3min;
	      else if(variable=="Dphi4j") Dphij += dphi4min;
	      else if(variable=="Dphi5j") Dphij += dphi5min;
	      else if(variable=="Dphi6j") Dphij += dphi6min;
	    }
	    eval = Dphij / limit;
	    numSelected += MCweight;
	  }



	  // determine tt+jets subsample
	  int ttjets = 0;
	  if( samples[s].find("TTJets") != string::npos ){	  
	    if( nMatchSimB >= 2 ){
	      ttjets = 1; //ttbb
	    }
	    else if( nMatchSimB == 1 ){
	      ttjets = 2; //ttb
	    }
	    else if( nMatchSimB == 0 && nMatchSimC >= 1 ){
	      ttjets = 3; //ttcc
	    }
	    else if( nMatchSimB == 0 && nMatchSimC == 0 ){
	      ttjets = 4; //ttjj
	    }
	    else cout << "Error determining tt+jets subsample" << endl;
	  }

	  // fill the historams
	  if( samples[s].find("TTJets") != string::npos ){
	    if( ttjets == 1 ){
	      httbb->Fill(eval,MCweight*weight_xs*scalefac*lumi); //need Trigweight
	      numttbb++;
	    }	    
	    if( ttjets == 2 ){
	      httb ->Fill(eval,MCweight*weight_xs*scalefac*lumi);
	      numttbj++;
	    }
	    if( ttjets == 3 ){
	     httcc->Fill(eval,MCweight*weight_xs*scalefac*lumi);
	     numttcc++;
	    }
	    if( ttjets == 4 ){
	      httjj->Fill(eval,MCweight*weight_xs*scalefac*lumi);
	      numttjj++;
	    }
	  }
	  else if( samples[s].find("TTH") != string::npos ){
	    httH->Fill(eval,MCweight*weight_xs*scalefac*lumi);  //need Trigweight
	  }
	  else if( samples[s] == "QCD" ){
	    hQCD->Fill(eval,MCweight*weight_xs*scalefac*lumi);
	  }
	  else if( samples[s].find("QCDMultijet") != string::npos ){
	    //hQCD->Fill(eval,QCDweight*scalefac);
	  }
	  else if( samples[s].find("Data") != string::npos ){
	    hData->Fill(eval,MCweight*weight_xs*scalefac);
	  }
	  else{
	    outfile << "sample not found!" << endl;
	  }

	} //end selection
	
      } //end loop over events    

      outfile << "Total number of events " << numEvents << endl;
      outfile << "Number of selected events " << numSelected << endl;
      if( samples[s].find("TTJets") != string::npos ){
	outfile << "Number of ttbb events " << numttbb << " integral " << httbb->Integral() << endl;
	outfile << "Number of ttb  events " << numttbj << " integral " << httb ->Integral() << endl;
	outfile << "Number of ttcc events " << numttcc << " integral " << httcc->Integral() << endl;
	outfile << "Number of ttjj events " << numttjj << " integral " << httjj->Integral() << endl;
	outfile << "Bin integral " << httbb->Integral()+httb->Integral()+httcc->Integral()+httjj->Integral() << endl;
      }
      if( samples[s].find("TTH") != string::npos ){
	outfile << "Bin integral " << httH->Integral() << endl;
      }
      if( samples[s].find("QCD") != string::npos ){
	outfile << "Bin integral " << hQCD->Integral() << endl;
      }

    } //end loop over files
    
  } //end loop over samples

  
  if( RUNONDATA){
    if( POISSON ) hData->SetBinErrorOption(TH1::kPoisson);
    else hData->Sumw2();
  }
  
  // add histrograms to background error
  hErr->Add(hQCD, 1.0);
  hErr->Add(httbb, 1.0);
  hErr->Add(httb , 1.0);
  hErr->Add(httcc, 1.0);
  hErr->Add(httjj, 1.0);

  hS  ->Add(httH , 100.0);
  
  // add histrograms to stack
  hStack->Add(hQCD);
  hStack->Add(httbb);
  hStack->Add(httb);
  hStack->Add(httcc);
  hStack->Add(httjj);
  hStack->Add(httH);
  
  // add histograms to legend
  leg->AddEntry(httH,  "t#bar{t}H (125)", "F");
  leg->AddEntry(httjj, "t#bar{t} + lf", "F");
  leg->AddEntry(httcc, "t#bar{t} + c#bar{c}", "F");
  leg->AddEntry(httb,  "t#bar{t} + b", "F");
  leg->AddEntry(httbb, "t#bar{t} + b#bar{b}", "F");
  leg->AddEntry(hQCD,  "QCD Multijet", "F");
  if(RUNONDATA) leg->AddEntry(hData, "Data", "LPE");
  leg->AddEntry(hErr,  "Bkg. Unc.", "F");
  leg->AddEntry(hS,    "t#bar{t}H (125) x 100", "L");
 
  // set y-axis range
  float max =  TMath::Max( hErr->GetMaximum()*1.15,(hData!=0 ? hData->GetMaximum()*1.45 : -1.));
  if(LOGSCALE){
    hErr->GetYaxis()->SetRangeUser(1, max*8.0 );
    p1->SetLogy(1);
  }
  else hErr->GetYaxis()->SetRangeUser(0, max );
  cout << "max range is " << max << endl;
  // draw histograms
  hErr  ->Draw("HIST");
  hStack->Draw("HISTSAME");
  hS    ->Draw("HISTSAME");
  hErr  ->Draw("E2SAME");
  if(hData!=0) hData->Draw("PE1SAME");
  leg->Draw();

  pt_title->Draw();

    
  //-----------------------ratio plot-------------------
  if( tag.find("ratio") != string::npos ){
    
    c1->cd();
    TPad *p2 = new TPad("p1","",0,0,1,0.175);
    p2->SetGrid(0,0);
    p2->SetFillStyle(4000);
    p2->SetFillColor(10);
    p2->SetTicky();
    p2->SetObjectStat(0);
    p2->Draw();
    p2->cd();
    
    TF1* one = new TF1("one","1",0,1);

    TH1F* one_error = 0;
    one_error = (TH1F*)h1->Clone("one_error");
    
    TH1F* h_ratio = 0;
    h_ratio = (TH1F*)h1->Clone("h_ratio");

    TGraphAsymmErrors* g_ratio = new TGraphAsymmErrors(h1);
    if( g_ratio->GetN() != h_ratio->GetNbinsX() ){
      outfile << "g_ratio has different number of bins to h_ratio. return!" << endl;
      return;
    }

    // loop over bins
    for(int b=1; b<= h_ratio->GetNbinsX() ; b++){

      float nbkg     = hErr->GetBinContent(b);
      float nbkg_up  = hErr->GetBinContent(b) + hErr->GetBinError(b);
      float nbkg_low = hErr->GetBinContent(b) - hErr->GetBinError(b);
    
      float ndata      = hErr->GetBinContent(b);
      float ndataErr   = hErr->GetBinError(b);  
      if(RUNONDATA){
	ndata      = hData->GetBinContent(b);
	ndataErr   = hData->GetBinError(b);
      }

      float r       = nbkg>0 ? ndata/nbkg      : 0;
      float rErr    = nbkg>0 ? ndataErr/nbkg   : 0;

      float one_up  = nbkg_low >0 ? nbkg/nbkg_low : 0;
      float one_low = nbkg_up  >0 ? nbkg/nbkg_up  : 0;

      float xPoint  = h1->GetBinCenter(b);
      float xWidth  = 0.5*h1->GetBinWidth(b);

      h_ratio->SetBinContent(b, r);
      h_ratio->SetBinError(b,rErr);

      if(RUNONDATA && POISSON){

	float dataErrLow = hData->GetBinErrorLow(b);
	float dataErrUp  = hData->GetBinErrorUp(b);
	float rErrUp     = nbkg>0 ? dataErrUp/nbkg  : 0;
	float rErrLow    = nbkg>0 ? dataErrLow/nbkg : 0;

	g_ratio->SetPoint(b-1, xPoint, r);
	g_ratio->SetPointEYlow(b-1, rErrLow);
	g_ratio->SetPointEYhigh(b-1, rErrUp);
	g_ratio->SetPointEXlow(b-1, xWidth);
	g_ratio->SetPointEXhigh(b-1, xWidth);
      }

      one_error->SetBinContent(b, 1.0);
      one_error->SetBinError(b, (one_up-one_low)/2 );
    
    } //end loop over bins

    // set ratio histogram styles
    one_error->SetTitle(0);
    one_error->GetYaxis()->SetRangeUser(0.0,2.0);

    one_error->GetXaxis()->SetTitle(0);
    one_error->GetXaxis()->SetLabelSize(0);
    one_error->GetXaxis()->SetNdivisions(0);
    one_error->GetXaxis()->SetTickLength(0.1);

    one_error->GetYaxis()->SetTitleSize(0.18);
    one_error->GetYaxis()->SetTitleOffset(0.24);
    one_error->GetYaxis()->SetTitle("Data/MC  ");
    one_error->GetYaxis()->SetNdivisions(202);
    one_error->GetYaxis()->SetLabelSize(0.16);

    one_error->SetFillColor(kGreen);

    h_ratio->SetMarkerStyle(20);
    h_ratio->SetMarkerSize(1.5);
    h_ratio->SetMarkerColor(kBlack);
    h_ratio->SetLineColor(kBlack);
    h_ratio->SetLineWidth(2);

    g_ratio->SetMarkerStyle(20);
    g_ratio->SetMarkerSize(1.5);
    g_ratio->SetMarkerColor(kBlack);
    g_ratio->SetLineColor(kBlack);
    g_ratio->SetLineWidth(2);

    one->SetLineColor(kBlack);
    one->SetLineStyle(kDashed);
    one->SetLineWidth(1);

    one_error->Draw("E2");
    one->Draw("SAME");
    if(RUNONDATA && POISSON) g_ratio->Draw("PE1SAME");
    else h_ratio->Draw("PE1SAME");

  } //end ratio plot
  
  
  // save plots
  if( SAVEPLOTS ){
    c1->SaveAs(  ("./Control_plots/AH_"+variable+tag+"_temp.pdf").c_str() ); 
  }

  // Normalized plot
  if( NORMALIZE ){
    TCanvas *c2 = new TCanvas("c2","",5,30,640,580);
    TPad *p2 = new TPad("p2","",0,0,1,1);
  
    p2->SetGrid(0,0);
    p2->SetFillStyle(4000);
    p2->SetFillColor(10);
    p2->SetTicky();
    p2->SetTicks(0,0);
    p2->SetObjectStat(0);
    p2->Draw();
    p2->cd();
    
    p2->SetTopMargin(0.05);

    httH ->SetLineWidth( 3 );
    httH ->SetFillStyle( 0 );

    hQCD ->SetLineWidth( 3 );
    hQCD ->SetFillStyle( 0 );

    httjj ->SetLineWidth( 3 );
    httjj ->SetFillStyle( 0 );

    httcc ->SetLineWidth( 3 );
    httcc ->SetFillStyle( 0 );

    httb ->SetLineWidth( 3 );
    httb ->SetFillStyle( 0 );

    httbb ->SetLineWidth( 3 );
    httbb ->SetFillStyle( 0 );

    hQCD ->GetYaxis()->SetTitle("Normalized units");
    hQCD ->SetMaximum( hQCD->GetMaximum()*2.0 );   //CHANGE HERE
    hQCD ->DrawNormalized("PE");
    httbb->DrawNormalized("PESAME");
    httb ->DrawNormalized("PESAME");
    httcc->DrawNormalized("PESAME");
    httjj->DrawNormalized("PESAME");
    httH ->DrawNormalized("PESAME");
    leg->Draw();
    pt_title->Draw();

    if( SAVEPLOTS ){
      c2->SaveAs(  ("./Control_plots/AH_"+variable+tag+"_norm_temp.pdf").c_str() ); 
    }
  }

  float time1 = clock->CpuTime();
  outfile << endl << "*** Plot done in " << time1/60.0 << " min." << endl;

  outfile.close();
  
  return;
}

float deltaR(float eta1, float phi1, float eta2, float phi2 ){
  
  return  sqrt( (eta1-eta2)*(eta1-eta2) + acos( cos(phi1-phi2) )*acos( cos(phi1-phi2) ) );
}

float deltaEta(float eta1, float eta2 ){
  
  return  abs(eta1-eta2);
}
float deltaPhi(float phi1, float phi2 ){
  
  return  acos( cos(phi1-phi2) );
}

float deltaD(float eta1, float phi1, float eta2, float phi2 ){
  
  //float theta1 = 2*atan(exp(-eta1));
  //float theta2 = 2*atan(exp(-eta1));

  //return  sqrt(2-2*(sin(theta1)*sin(theta2)*cos(phi1-phi2)+cos(theta1)*cos(theta2) ) );

  float n = 2.2;

  return sqrt( (eta1-eta2)*(eta1-eta2)*(1 + (n-abs(eta1))*(n-abs(eta2))/n/n*acos(cos(phi1-phi2))*acos(cos(phi1-phi2)) ) );

}

int checkreps(int e){

  int reps[87]{13200666,
      17688290,
      11508769,
      18778520,
      17391282,
      6247723,
      17619188,
      13768131,
      19954503,
      16169148,
      16867517,
      16166548,
      18263706,
      11821277,
      7343852,
      17211627,
      15771487,
      5888013,
      12252188,
      18135453,
      17427233,
      15886940,
      18273806,
      19659095,
      3706202,
      15281673,
      19989054,
      16131597,
      15476179,
      19698846,
      14649206,
      15595631,
      6148270,
      9928025,
      17772792,
      18267306,
      12522797,
      19951003,
      17664039,
      12354241,
      18706018,
      12510597,
      16834566,
      18544114,
      11379365,
      15447728,
      16334103,
      18152553,
      14830161,
      18786771,
      18075251,
      15655834,
      17753892,
      15808638,
      17412582,
      3952654,
      2084970,
      3890658,
      613862,
      3170902,
      2933518,
      3508482,
      2919718,
      1134830,
      2753028,
      3985552,
      3498682,
      2807624,
      3668172,
      3973352,
      3649572,
      2928318,
      3891258,
      3942654,
      3123106,
      59862640,
      24392493,
      41965643,
      55226856,
      47123858,
      59362634,
      28605965,
      26053703,
      28688788,
      20965335,
      23310018,
      20449674,
      };

  for(int r=0; r<87; r++){
    if(e == reps[r]) return e;
  }
  return 0;
}
