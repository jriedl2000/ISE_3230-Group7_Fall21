import cvxpy as cp

x = cp.Variable(75, boolean  = True) # vector variable

constraints = []

#First set of constraints: 
    #Ensure each person goes on 3 dates (because there are 3 rounds)

    #For males
constraints.append((x[0]) + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9] + x[10] + x[11] + x[12] + x[13] + x[14] == 3)
constraints.append((x[15]) + x[16] + x[17] + x[18] + x[19] + x[20] + x[21] + x[22] + x[23] + x[24] + x[25] + x[26] + x[27] + x[28] + x[29] == 3)
constraints.append((x[30]) + x[31] + x[32] + x[33] + x[34] + x[35] + x[36] + x[37] + x[38] + x[39] + x[40] + x[41] + x[42] + x[43] + x[44] == 3)
constraints.append((x[45]) + x[46] + x[47] + x[48] + x[49] + x[50] + x[51] + x[52] + x[53] + x[54] + x[55] + x[56] + x[57] + x[58] + x[59] == 3)
constraints.append((x[60]) + x[61] + x[62] + x[63] + x[64] + x[65] + x[66] + x[67] + x[68] + x[69] + x[70] + x[71] + x[72] + x[73] + x[74] == 3)

    #For females
constraints.append((x[0]) + x[1] + x[2] + x[15] + x[16] + x[17] + x[30] + x[31] + x[32] + x[45] + x[46] + x[47] + x[60] + x[61] + x[62] == 3)
constraints.append((x[3]) + x[4] + x[5] + x[18] + x[19] + x[20] + x[33] + x[34] + x[35] + x[48] + x[49] + x[50] + x[63] + x[64] + x[65] == 3)
constraints.append((x[6]) + x[7] + x[8] + x[21] + x[22] + x[23] + x[36] + x[37] + x[38] + x[51] + x[52] + x[53] + x[66] + x[67] + x[68] == 3)
constraints.append((x[9]) + x[10] + x[11] + x[24] + x[25] + x[26] + x[39] + x[40] + x[41] + x[54] + x[55] + x[56] + x[69] + x[70] + x[71] == 3)
constraints.append((x[12]) + x[13] + x[14] + x[27] + x[28] + x[29] + x[42] + x[43] + x[44] + x[57] + x[58] + x[59] + x[72] + x[73] + x[74] == 3)

#Second set of constraints:
    #Choose 5 pairings for each round

    #Round 1
constraints.append((x[0]) + x[3] + x[6] + x[9] + x[12] + x[15] + x[18] + x[21] + x[24] + x[27] + x[30] + x[33] + x[36] + x[39]
                   + x[42] + x[45] + x[48] + x[51] + x[54] + x[57] + x[60] + x[63] + x[66] + x[69] + x[72] == 5)

    #Round 2
constraints.append((x[1]) + x[4] + x[7] + x[10] + x[13] + x[16] + x[19] + x[22] + x[25] + x[28] + x[31] + x[34] + x[37] + x[40]
                   + x[43] + x[46] + x[49] + x[52] + x[55] + x[58] + x[61] + x[64] + x[67] + x[70] + x[73] == 5)

    #Round 3
constraints.append((x[2]) + x[5] + x[8] + x[11] + x[14] + x[17] + x[20] + x[23] + x[26] + x[29] + x[32] + x[35] + x[38] + x[41]
                   + x[44] + x[47] + x[50] + x[53] + x[56] + x[59] + x[62] + x[65] + x[68] + x[71] + x[74] == 5)



#Third set of constraints:
    #Avoid redundancy between rounds for pairings(i.e. can not have the same pairing more than once between rounds)
constraints.append((x[0]) + x[1] + x[2] <= 1)
constraints.append((x[3]) + x[4] + x[5] <= 1)
constraints.append((x[6]) + x[7] + x[8] <= 1)
constraints.append((x[9]) + x[10] + x[11] <= 1)
constraints.append((x[12]) + x[13] + x[14] <= 1)
constraints.append((x[15]) + x[16] + x[17] <= 1)
constraints.append((x[18]) + x[19] + x[20] <= 1)
constraints.append((x[21]) + x[22] + x[23] <= 1)
constraints.append((x[24]) + x[25] + x[26] <= 1)
constraints.append((x[27]) + x[28] + x[29] <= 1)
constraints.append((x[30]) + x[31] + x[32] <= 1)
constraints.append((x[33]) + x[34] + x[35] <= 1)
constraints.append((x[36]) + x[37] + x[38] <= 1)
constraints.append((x[39]) + x[40] + x[41] <= 1)
constraints.append((x[42]) + x[43] + x[44] <= 1)
constraints.append((x[45]) + x[46] + x[47] <= 1)
constraints.append((x[48]) + x[49] + x[50] <= 1)
constraints.append((x[51]) + x[52] + x[53] <= 1)
constraints.append((x[54]) + x[55] + x[56] <= 1)
constraints.append((x[57]) + x[58] + x[59] <= 1)
constraints.append((x[60]) + x[61] + x[62] <= 1)
constraints.append((x[63]) + x[64] + x[65] <= 1)
constraints.append((x[66]) + x[67] + x[68] <= 1)
constraints.append((x[69]) + x[70] + x[71] <= 1)
constraints.append((x[72]) + x[73] + x[74] <= 1)

#Fourth set of constraints:
    #Ensures each person dates exactly one person per round
    #Male 1
constraints.append((x[0]) + x[3] + x[6] + x[9] + x[12] == 1)
constraints.append((x[1]) + x[4] + x[7] + x[10] + x[13] == 1)
constraints.append((x[2]) + x[5] + x[8] + x[11] + x[14] == 1)

    #Male 2
constraints.append((x[15]) + x[18] + x[21] + x[24] + x[27] == 1)
constraints.append((x[16]) + x[19] + x[22] + x[25] + x[28] == 1)
constraints.append((x[17]) + x[20] + x[23] + x[26] + x[29] == 1)

    #Male 3
constraints.append((x[30]) + x[33] + x[36] + x[39] + x[42] == 1)
constraints.append((x[31]) + x[34] + x[37] + x[40] + x[43] == 1)
constraints.append((x[32]) + x[35] + x[38] + x[41] + x[44] == 1)

    #Male 4
constraints.append((x[45]) + x[48] + x[51] + x[54] + x[57] == 1)
constraints.append((x[46]) + x[49] + x[52] + x[55] + x[58] == 1)
constraints.append((x[47]) + x[50] + x[53] + x[56] + x[59] == 1)

    #Male 5
constraints.append((x[60]) + x[63] + x[66] + x[69] + x[72] == 1)
constraints.append((x[61]) + x[64] + x[67] + x[70] + x[73] == 1)
constraints.append((x[62]) + x[65] + x[68] + x[71] + x[74] == 1)

    #Female 1
constraints.append((x[0]) + x[15] + x[30] + x[45] + x[60] == 1)
constraints.append((x[1]) + x[16] + x[31] + x[46] + x[61] == 1)
constraints.append((x[2]) + x[17] + x[32] + x[47] + x[62] == 1)

    #Female 2
constraints.append((x[3]) + x[18] + x[33] + x[48] + x[63] == 1)
constraints.append((x[4]) + x[19] + x[34] + x[49] + x[64] == 1)
constraints.append((x[5]) + x[20] + x[35] + x[50] + x[65] == 1)

    #Female 3
constraints.append((x[6]) + x[21] + x[36] + x[51] + x[66] == 1)
constraints.append((x[7]) + x[22] + x[37] + x[52] + x[67] == 1)
constraints.append((x[8]) + x[23] + x[38] + x[53] + x[68] == 1)

    #Female 4
constraints.append((x[9]) + x[24] + x[39] + x[54] + x[69] == 1)
constraints.append((x[10]) + x[25] + x[40] + x[55] + x[70] == 1)
constraints.append((x[11]) + x[26] + x[41] + x[56] + x[71] == 1)

    #Female 5
constraints.append((x[12]) + x[27] + x[42] + x[57] + x[72] == 1)
constraints.append((x[13]) + x[28] + x[43] + x[58] + x[73] == 1)
constraints.append((x[14]) + x[29] + x[44] + x[59] + x[74] == 1)


#assuming same probabilities between rounds
obj_func= (0.323 * x[0] + 0.323 * x[1] + 0.323 * x[2] + 0.394 * x[3] + 0.394 * x[4] + 0.394 * x[5] + 0.763 * x[6] + 0.763 * x[7]
           + 0.763 * x[8] + 0.664 * x[9] + 0.664 * x[10] + 0.664 * x[11] + 0.271 * x[12] + 0.271 * x[13] + 0.271 * x[14] 
           + 0.354 * x[15] + 0.354 * x[16] + 0.354 * x[17] + 0.318 * x[18] + 0.318 * x[19] + 0.318 * x[20] + 0.455 * x[21] + 
           0.455 * x[22] + 0.455 * x[23] + 0.331 * x[24] + 0.331 * x[25]
           + 0.331 * x[26] + 0.625 * x[27] + 0.625 * x[28] + 0.625 * x[29] + 0.628 * x[30] + 0.628 * x[31] + 0.628 * x[32] 
           + 0.364 * x[33] + 0.364 * x[34] + 0.364 * x[35] + 0.376 * x[36] + 0.376 * x[37] +
           0.376 * x[38] + 0.266 * x[39] + 0.266 * x[40] + 0.266 * x[41] + 0.268 * x[42] + 0.268 * x[43]
           + 0.268 * x[44] + 0.724 * x[45] + 0.724 * x[46] + 0.724 * x[47] + 0.388 * x[48] + 0.388 * x[49] + 0.388 * x[50] 
           + 0.409 * x[51] + 0.409 * x[52] + 0.409 * x[53] + 1.042 * x[54] + 1.042 * x[55] + 1.042 * x[56] + 0.577 * x[57] + 
           0.577 * x[58] + 0.577 * x[59] + 0.324 * x[60] + 0.324 * x[61]
           + 0.324 * x[62] + 0.658 * x[63] + 0.658 * x[64] + 0.658 * x[65] + 0.392 * x[66] + 0.392 * x[67] + 0.392 * x[68] 
           + 0.636 * x[69] + 0.636 * x[70] + 0.636 * x[71] + 0.264 * x[72] + 0.264 * x[73] 
           + 0.264 * x[74])

problem = cp.Problem(cp.Maximize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True) #verbose parameter determines showing/not showing the output
problem.solve(solver=cp.GUROBI,verbose = True)


print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
