/*
 * Copyright 2000, Regents of the University of Minnesota
 * tstsuggest.c
 *
 * This file tests the various routines of the Suggest library
 *
 * Started 11/6/00
 * George
 *
 * $Id: tstsuggest.c,v 1.2 2000/11/08 04:03:35 karypis Exp $
 *
 */


#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>
#include <time.h>
#include <suggest.h>


/*-------------------------------------------------------------
 * Timing macros
 *-------------------------------------------------------------*/
#define cleartimer(tmr) (tmr = 0.0)
#define starttimer(tmr) (tmr -= getseconds())
#define stoptimer(tmr) (tmr += getseconds())
#define gettimer(tmr) (tmr)


/*************************************************************************
* This function returns the seconds
**************************************************************************/
double getseconds(void)
{
  return((double) clock()/CLOCKS_PER_SEC);
}



/*************************************************************************
* This function reads in the transactions from a file and hides one of 
* them for testing.
**************************************************************************/
void ReadTransactions(char *fname, int *r_nusers, int *r_nitems, int *r_ntrans, 
                      int **r_userids, int **r_itemids, int **r_hidden)
{
  int i, j, k, nusers, nitems, ntrans;
  int *userids, *itemids, *hidden;
  FILE *fp;

  if ((fp = fopen(fname, "r")) == NULL) {
    printf("Error opening file %s\n", fname);
    exit(0);
  }

  fscanf(fp, "%d %d %d", &nusers, &nitems, &ntrans);

  userids = (int *)malloc(sizeof(int)*ntrans+1);
  itemids = (int *)malloc(sizeof(int)*ntrans+1);
  hidden  = (int *)malloc(sizeof(int)*nusers+1);

  for (i=0; i<ntrans; i++) 
    fscanf(fp, "%d %d", userids+i, itemids+i);
  userids[i] = nusers;  /* makes coding easier! */

  fclose(fp);

  for (i=0; i<ntrans; i++) {
    if (userids[i+1] != userids[i]) {
      hidden[userids[i]] = itemids[i];
      userids[i] = -1;
    }
  }
    
  for (j=0, i=0; i<ntrans; i++) {
    if (userids[i] != -1) {
      userids[j] = userids[i];
      itemids[j] = itemids[i];
      j++;
    }
  }
  userids[j] = nusers;  /* makes coding easier! */


  *r_nusers  = nusers;
  *r_nitems  = nitems;
  *r_ntrans  = ntrans-nusers;
  *r_userids = userids;
  *r_itemids = itemids;
  *r_hidden  = hidden;

/*
  for (i=0; i<ntrans-nusers; i++)
    printf("%d %d\n", userids[i], itemids[i]);
  exit(0);
*/
}



/*************************************************************************
* This function tests the SUGGEST recommendation library
**************************************************************************/
int main(int argc, char *argv[])
{
  int i, j, k, nusers, nitems, ntrans;
  int *userids, *itemids, *hidden;
  int *model, rcmds[10], nrcmd, nhits;
  float alpha;
  float tmr1, tmr2;


  if (argc != 2) {
    printf("Usage: %s <fname>\n", argv[0]);
    exit(0);
  }


  ReadTransactions(argv[1], &nusers, &nitems, &ntrans, &userids, &itemids, &hidden);

  printf("Dataset Statistics: Nusers: %d, Nitems: %d, Ntrans; %d\n", nusers, nitems, ntrans);


  printf("-----------------------------------------------------------------------------\n");
  printf("Testing RType=1...\n");
  printf("  Bulding model [NNbr=20]...\n");

  cleartimer(tmr1);
  cleartimer(tmr2);
  starttimer(tmr1);

  model = SUGGEST_Init(nusers, nitems, ntrans, userids, itemids, 1, 20, 0.0);

  stoptimer(tmr1);

  starttimer(tmr2);
  printf("  Computing top-10 recommendations...\n");
  for (nhits=0, k=0, i=0; i<ntrans; i++) {
    if (userids[i+1] != userids[i]) {
      nrcmd = SUGGEST_TopN(model, i-k+1, itemids+k, 10, rcmds);
      for (j=0; j<nrcmd; j++) {
        if (rcmds[j] == hidden[userids[i]]) {
          nhits++;
          break;
        }
      }
      k = i+1;
    }
  }
  stoptimer(tmr2);

  printf("    Nhits: %d, InitTime: %.2f secs, TopN-Rate: %.2f rcmds/sec\n\n", nhits, tmr1, nusers/tmr2);

  SUGGEST_Clean(model);



  printf("-----------------------------------------------------------------------------\n");
  printf("Testing RType=2...\n");
  printf("  Estimating Alpha..."); fflush(stdout);

  alpha = SUGGEST_EstimateAlpha(nusers, nitems, ntrans, userids, itemids, 20, 10);

  printf("  Alpha=%.2f\n", alpha);

  printf("  Bulding model [NNbr=20]...\n");

  cleartimer(tmr1);
  cleartimer(tmr2);
  starttimer(tmr1);

  model = SUGGEST_Init(nusers, nitems, ntrans, userids, itemids, 2, 20, alpha);

  stoptimer(tmr1);

  starttimer(tmr2);
  printf("  Computing top-10 recommendations...\n");
  for (nhits=0, k=0, i=0; i<ntrans; i++) {
    if (userids[i+1] != userids[i]) {
      nrcmd = SUGGEST_TopN(model, i-k+1, itemids+k, 10, rcmds);
      for (j=0; j<nrcmd; j++) {
        if (rcmds[j] == hidden[userids[i]]) {
          nhits++;
          break;
        }
      }
      k = i+1;
    }
  }
  stoptimer(tmr2);

  printf("    Nhits: %d, InitTime: %.2f secs, TopN-Rate: %.2f rcmds/sec\n\n", nhits, tmr1, nusers/tmr2);

  SUGGEST_Clean(model);

    

  printf("-----------------------------------------------------------------------------\n");
  printf("Testing RType=3...\n");
  printf("  Bulding model [NNbr=50]...\n");

  cleartimer(tmr1);
  cleartimer(tmr2);
  starttimer(tmr1);

  model = SUGGEST_Init(nusers, nitems, ntrans, userids, itemids, 3, 50, 0.0);

  stoptimer(tmr1);

  starttimer(tmr2);
  printf("  Computing top-10 recommendations...\n");
  for (nhits=0, k=0, i=0; i<ntrans; i++) {
    if (userids[i+1] != userids[i]) {
      nrcmd = SUGGEST_TopN(model, i-k+1, itemids+k, 10, rcmds);
      for (j=0; j<nrcmd; j++) {
        if (rcmds[j] == hidden[userids[i]]) {
          nhits++;
          break;
        }
      }
      k = i+1;
    }
  }
  stoptimer(tmr2);

  printf("    Nhits: %d, InitTime: %.2f secs, TopN-Rate: %.2f rcmds/sec\n\n", nhits, tmr1, nusers/tmr2);

  SUGGEST_Clean(model);


  free(userids);
  free(itemids);
  free(hidden);

}
