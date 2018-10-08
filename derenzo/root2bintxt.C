/////////////////////////////////////////////////////   
//                                                 //
//			S.JAN - sjan@cea.fr - March 2007	   //
//			updated by							   //
//			U. Pietrzyk - u.pietrzyk@fz-juelich.de //
//			March 2010							   //
//                                                 //
//   Example of a ROOT C++ code-macro to:          // 
//   -----------------------------------           //
//   1/ read an output root data file              //
//   2/ create a loop on each event which are      //
//      stored during the simulation               //
//   3/ perform data processing                    //
//   4/ plot the results                           //
//                                                 //
/////////////////////////////////////////////////////
#include <fstream>
#include <iomanip>
#include <stdio.h>
void root2bintxt()
{
 //const char* filename = "polyCyl"
   gROOT->Reset();
	TFile *f = new TFile("result.root");
   //output the true coincidence event(position) into a .txt file
	std::ofstream out("result.txt", std::ios_base::out|std::ios_base::binary);//
	std::ofstream outhdr("result.txt.hdr");

	TTree *Coincidences = (TTree*)gDirectory->Get("Coincidences");
   //TTree *Gate = (TTree*)gDirectory->Get("Gate");
   //TTree *Hits = (TTree*)gDirectory->Get("Hits");
   // TTree *Singles = (TTree*)gDirectory->Get("Singles");
   

   
//creation of a histo 1 Dim.
TH1F *gamma1 = new TH1F("gamma1","",50,0.2,.8);  
TH1F *gamma2 = new TH1F("gamma2","",50,0.2,.8);  

 
//creation of histo 3 Dim. 
TH3F *position1 = new TH3F("position1","",200,-300,300,200,-300,300,200,-300,300);  

TH3F *position2 = new TH3F("position2","",200,-300,300,200,-300,300,200,-300,300);
//
//Declaration of leaves types - TTree Coincidences
//  
   Int_t           RayleighCrystal1;
   Int_t           RayleighCrystal2;
   Int_t           RayleighPhantom1;
   Int_t           RayleighPhantom2;
   Float_t         axialPos;
   Char_t          comptVolName1[40];
   Char_t          comptVolName2[40];
   Int_t           comptonPhantom1;
   Int_t           comptonPhantom2;
   Int_t           comptonCrystal1;
   Int_t           comptonCrystal2;   
   Int_t           crystalID1;
   Int_t           crystalID2;
   //Int_t           blockID1;
   //Int_t           blockID2;
   Float_t         energy1;
   Float_t         energy2;   
   Int_t           eventID1;
   Int_t           eventID2;
   Float_t         globalPosX1;
   Float_t         globalPosX2;
   Float_t         globalPosY1;
   Float_t         globalPosY2;      
   Float_t         globalPosZ1;
   Float_t         globalPosZ2;
   Int_t           layerID1;
   Int_t           layerID2;
   Int_t           moduleID1;
   Int_t           moduleID2;
   Float_t         rotationAngle;
   Int_t           rsectorID1;
   Int_t           rsectorID2;
   Int_t           runID;
   Float_t         sinogramS;
   Float_t         sinogramTheta;
   Int_t           sourceID1;
   Int_t           sourceID2;
   Float_t        sourcePosX1;
   Float_t        sourcePosX2;
   Float_t        sourcePosY1;
   Float_t        sourcePosY2;
   Float_t        sourcePosZ1;
   Float_t        sourcePosZ2;
   Int_t           submoduleID1;
   Int_t           submoduleID2;
   Double_t         time1;
   Double_t         time2;
   
//   
//Set branch addresses - TTree Coincicences
//  
   Coincidences->SetBranchAddress("axialPos",&axialPos);
   Coincidences->SetBranchAddress("RayleighCrystal1",&RayleighCrystal1);
   Coincidences->SetBranchAddress("RayleighCrystal2",&RayleighCrystal2);
   Coincidences->SetBranchAddress("RayleighPhantom1",&RayleighPhantom1);
   Coincidences->SetBranchAddress("RayleighPhantom2",&RayleighPhantom2);
   Coincidences->SetBranchAddress("comptVolName1",&comptVolName1);
   Coincidences->SetBranchAddress("comptVolName2",&comptVolName2);
   Coincidences->SetBranchAddress("comptonPhantom1",&comptonPhantom1);
   Coincidences->SetBranchAddress("comptonPhantom2",&comptonPhantom2);
   Coincidences->SetBranchAddress("comptonCrystal1",&comptonCrystal1);
   Coincidences->SetBranchAddress("comptonCrystal2",&comptonCrystal2);
   Coincidences->SetBranchAddress("crystalID1",&crystalID1);
   Coincidences->SetBranchAddress("crystalID2",&crystalID2);
  // Coincidences->SetBranchAddress("blockID1",&blockID1);
  // Coincidences->SetBranchAddress("blockID2",&blockID2);
   Coincidences->SetBranchAddress("energy1",&energy1);
   Coincidences->SetBranchAddress("energy2",&energy2);   
   Coincidences->SetBranchAddress("eventID1",&eventID1);
   Coincidences->SetBranchAddress("eventID2",&eventID2);
   Coincidences->SetBranchAddress("globalPosX1",&globalPosX1);
   Coincidences->SetBranchAddress("globalPosX2",&globalPosX2);
   Coincidences->SetBranchAddress("globalPosY1",&globalPosY1);
   Coincidences->SetBranchAddress("globalPosY2",&globalPosY2);      
   Coincidences->SetBranchAddress("globalPosZ1",&globalPosZ1);
   Coincidences->SetBranchAddress("globalPosZ2",&globalPosZ2);
   Coincidences->SetBranchAddress("layerID1",&layerID1);
   Coincidences->SetBranchAddress("layerID2",&layerID2);
   Coincidences->SetBranchAddress("moduleID1",&moduleID1);
   Coincidences->SetBranchAddress("moduleID2",&moduleID2);
   Coincidences->SetBranchAddress("rotationAngle",&rotationAngle);
   Coincidences->SetBranchAddress("level1ID1",&rsectorID1);
   Coincidences->SetBranchAddress("level1ID2",&rsectorID2);
   Coincidences->SetBranchAddress("runID",&runID);
   Coincidences->SetBranchAddress("sinogramS",&sinogramS);
   Coincidences->SetBranchAddress("sinogramTheta",&sinogramTheta);
   Coincidences->SetBranchAddress("sourceID1",&sourceID1);
   Coincidences->SetBranchAddress("sourceID2",&sourceID2);
   Coincidences->SetBranchAddress("sourcePosX1",&sourcePosX1);
   Coincidences->SetBranchAddress("sourcePosX2",&sourcePosX2);
   Coincidences->SetBranchAddress("sourcePosY1",&sourcePosY1);
   Coincidences->SetBranchAddress("sourcePosY2",&sourcePosY2);
   Coincidences->SetBranchAddress("sourcePosZ1",&sourcePosZ1);
   Coincidences->SetBranchAddress("sourcePosZ2",&sourcePosZ2);
   Coincidences->SetBranchAddress("submoduleID1",&submoduleID1);
   Coincidences->SetBranchAddress("submoduleID2",&submoduleID2);
   Coincidences->SetBranchAddress("time1",&time1);
   Coincidences->SetBranchAddress("time2",&time2);
   
   Int_t nentries = Coincidences->GetEntries();
  // Int_t nSingles = Singles->GetEntries();
	cout<<" Coincidences:   "<<  nentries <<endl;
  //	cout<<" Singles     :   "<<  nSingles <<endl;
   Int_t nbytes = 0;
    
//
//loop on the events in the TTree Coincidences
//

Int_t Nbr_Coinc_Prompt = 0. ;
Float_t Nbr_Coinc_Random = 0. ;
Float_t Nbr_Coinc_Scatter = 0. ;
Int_t Nbr_Coinc_Trues = 0. ;
Float_t Ntot = 100000. ;
Float_t meanE1 = 0;
Float_t meanE2 = 0;

int *matrix = new int[128*128*12];
for(int i=0; i<128*128*12;i++){
	*(matrix+i) = 0;
}

if(out.is_open())
{
	for (Int_t i=0; i<nentries;i++) {
   	nbytes += Coincidences->GetEntry(i);
   
   
   // Fill gamma1 histo without condition
   gamma1->Fill(energy1);
   
   // Fill the gamma2 histo with condition
   //if(energy2>0.4)
   gamma2->Fill(energy2);
   
   // Fill the 3D Histo without condition
   //position->Fill(globalPosZ1,globalPosX1,globalPosY1);
   
   meanE1 += energy1;
   meanE2 += energy2;
   ///////////////////////////////////////////////////////////////////////////////////////////
   //      						                                        //	
   // E V A L U A T I O N   O F   :   P R O M P T S   ;   T R U E S   ;   R A N D O M   ;   //
   //                                                                                       //
   // S E N S I T I V I T Y                                                                 //                           
   //									                //
   ///////////////////////////////////////////////////////////////////////////////////////////
	
	Nbr_Coinc_Prompt++;
	
	if ( eventID1 != eventID2 ) Nbr_Coinc_Random++;		
	if ( eventID1 == eventID2 && comptonPhantom1 == 0 && comptonPhantom2 == 0 && RayleighPhantom1 == 0 && RayleighPhantom2 == 0) 
	{	
		//if(i<10) cout<<globalPosX1<<endl;
	    Nbr_Coinc_Trues++;
		// position1->Fill(globalPosZ1,globalPosX1,globalPosY1);
		// position2->Fill(globalPosZ2,globalPosX2,globalPosY2);
		// int nx = (int)((sourcePosX1+80.0)/1.25);
		// int ny = (int)((sourcePosY1+80.0)/1.25);
		// int nz = (int)((sourcePosZ1+72.0)/12.0);
		// int nIndex = nz+ny*12+nx*12*128;
		// *(matrix+nIndex) += 1;
		float* buffer = new float[7];
		buffer[0] = (float)globalPosX1;
		buffer[1] = (float)globalPosY1;
		buffer[2] = (float)globalPosZ1;
		buffer[3] = (float)globalPosX2;
		buffer[4] = (float)globalPosY2;
		buffer[5] = (float)globalPosZ2;
		//buffer[6] = (float)(time2-time1)*3e11/2;
		//cout<<globalPosX1<<' '<<globalPosY1;
		buffer[6] = 0;
		out.write((char*) buffer, sizeof(float)*7);
		//buffer[0] = (float)sourcePosX1;
		//buffer[1] = (float)sourcePosY1;
		//buffer[2] = (float)sourcePosZ1;
		//cout<<buffer[0]<<' '<<buffer[1]<<endl;
		//out.write((char*) buffer, sizeof(float)*3);
				//out<<setw(20)<<rsectorID1;
				//out<<setw(20)<<eventID2;
				//out<< std::endl;
		}
	}
}
// if(out.is_open())
// {
// 	for(int i = 0;i<128;i++){
// 		for(int j = 0;j<128;j++){
// 			for(int k = 0;k<12;k++)
// 				out<<*(matrix+k+j*12+i*12*128)<<std::endl;
// 		}
// 	}
// }
delete[] matrix;
out.close();

if(outhdr.is_open()){
	outhdr<<Nbr_Coinc_Trues<<std::endl;
}
outhdr.close();

Float_t Sensi = Nbr_Coinc_Trues/Ntot*100.;
Float_t SF = (Nbr_Coinc_Prompt-Nbr_Coinc_Random-Nbr_Coinc_Trues)/(Nbr_Coinc_Prompt-Nbr_Coinc_Random)*100;

cout<<""<<endl;
cout<<""<<endl;
cout<<""<<endl;
cout<<"#   M E A N E 1       =   "<<meanE1/Nbr_Coinc_Prompt      <<"   keV"<<endl;
cout<<"#   M E A N E 2       =   "<<meanE2/Nbr_Coinc_Prompt      <<"   keV"<<endl;
cout<<"#   N T O T A L S     =   "<<Ntot             <<"   ps"<<endl;
cout<<"#   P R O M P T S     =   "<<Nbr_Coinc_Prompt <<"   Cps"<<endl;
cout<<"#   T R U E S         =   "<<Nbr_Coinc_Trues  <<"   Cps"<<endl;
cout<<"#   R A N D O M S     =   "<<Nbr_Coinc_Random <<"   Cps"<<endl;
cout<<" ______________________________________"<<endl;
cout<<"|                                      "<<endl;
cout<<"|  T O T A L   S E N S I T I V I T Y   :   "<<  Sensi <<"  %"<<endl;
cout<<"|______________________________________"<<endl;
cout<<"|                                      "<<endl;
cout<<"|  S C A T T E R   F R A C T I O N     :   "<<  SF <<"  %"<<endl;
cout<<"|______________________________________"<<endl;
cout<<""<<endl;
cout<<""<<endl;
cout<<""<<endl; 


//
// Plot the results
//

//    gStyle->SetPalette(1);
   
   
//    c1 = new TCanvas("Reco","Reco",200,10,500,600);
//    c1->SetFillColor(0);
//    c1->SetBorderMode(0);   
       
//    gamma1->Draw();
//    gamma1->SetFillColor(2);
//    //gamma2->Draw("same");  
//    gamma2->SetFillColor(9);
   
   
//    tex = new TLatex(0.255919,600,"GAMMA 1");
//    tex->SetTextColor(2);
//    tex->SetTextSize(0.05);
//    tex->SetLineWidth(2);
//    //tex->Draw();
//    tex2 = new TLatex(0.620151,300,"GAMMA 2");
//    tex2->SetTextColor(9);
//    tex2->SetTextSize(0.05);
//    tex2->SetLineWidth(2);
//    tex2->Draw();
     
//    c1->Update(); 

// //////////////////////////////////////////////////////////////////////////////
// //////////////////////////////////////////////////////////////////////////////
//    c2 = new TCanvas("Reco_true1","Reco_true1",200,10,500,600);
//    c2->SetFillColor(0);
//    c2->SetGrid();
//    c2->SetBorderMode(0); 

//    position1->Draw();

//    c2->Update(); 
// /////////////////////////////////////////////////////////////////   
//    c3 = new TCanvas("Reco_true2","Reco_true2",200,10,500,600);
//    c3->SetFillColor(0);
//    c3->SetGrid();
//    c3->SetBorderMode(0); 

//    position2->Draw();

//    c3->Update();   
   
}
