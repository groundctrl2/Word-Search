def print_grid(grid):
    print("")
    count1=0
    string1=""
    for i in range(len(grid[0])+1):
        string1+=str(count1)
        if count1==0:
            string1+=" "
        if count1<9:
            string1+="  "
        else:
            string1+=" "
        count1=count1+1
    print(string1)
    count2=1
    for row in grid:
        new_row=""
        new_row+=str(count2)
        if count2<=9:
            new_row+="   "
        else:
            new_row+="  "
        count2=count2+1
        for letter in row:
            new_row+=letter
            new_row+="  "
        print(new_row)
    print("")
def is_valid(grid):
    row_length=0
    for row in grid:
        if row_length==0:
            row_length+=len(row)
        if len(row)!=row_length:
            return False
    return True

def get_col(grid):
    row_length=len(grid[0])
    list=[]
    for i in range(row_length):
        string=""
        for row in grid:
            string+=row[i]
        list.append(string)
    return list
def get_pos_diag(grid): #gives positive diagonals left to right
    cols=len(grid[0])
    rows=len(grid)
    pos_diags=[]
    for i in range(rows):
        pos_diag=""
        row=i
        for col in range(i+1):
            if col<=(cols-1):
                pos_diag+=grid[row][col]
                row=row-1
        pos_diags.append(pos_diag)
    for i in range(1,cols):
        pos_diag=""
        col=i
        for row in range(rows-1,0,-1):
            if col<=(cols-1):
                pos_diag+=grid[row][col]
                col=col+1
        pos_diags.append(pos_diag)
    return pos_diags
def get_neg_diag(grid): #gives negative diagonals left to right
    cols=len(grid[0])
    rows=len(grid)
    pos_diags=[]
    for i in range(rows-1,-1,-1):
        pos_diag=""
        row=i
        for col in range(rows-row):
            if col<=(cols-1):
                pos_diag+=grid[row][col]
                row=row+1
        pos_diags.append(pos_diag)
    for i in range(1,cols):
        pos_diag=""
        col=i
        for row in range(rows):
            if col<=(cols-1):
                pos_diag+=grid[row][col]
                col=col+1
        pos_diags.append(pos_diag)
    return pos_diags

def backwards(list):
    new_list=[]
    for string in list:
        new_list.append(string[::-1])
    return new_list

def check_row(grid,words):
    backwards_list=backwards(grid)
    for word in words:
        for row in range(len(grid)):
            if word in grid[row]:
                print(word," is in row ",str(row+1))
            if word in backwards_list[row]:
                print(word," is backwards in row ",str(row+1))
def check_col(grid,words):
    cols=get_col(grid)
    backwards_list=backwards(cols)
    for word in words:
        for col in range(len(cols)):
            if word in cols[col]:
                print(word," is in column ",str(col+1))
            if word in backwards_list[col]:
                print(word," is backwards in column ",str(col+1))
def check_pos_diag(grid,words):
    pos_diag=get_pos_diag(grid)
    backwards_list=backwards(pos_diag)
    positions=[[] for _ in range(len(grid)+len(grid[0])-1)]
    for row in range(len(grid)):
        positions[row].append(1)
        positions[row].append(row+1)
    for col in range(1,len(grid[0])):
        positions[len(grid)+col-1].append(col+1)
        positions[len(grid)+col-1].append(len(grid))
    for word in words:
        for positive in range(len(pos_diag)):
            if word in pos_diag[positive]:
                print(word," is in the positive diagonal starting in position ",str(positions[positive]))
            if word in backwards_list[positive]:
                print(word," is backwards in the positive diagonal starting in position ",str(positions[positive]))
def check_neg_diag(grid,words):
    neg_diag=get_neg_diag(grid)
    backwards_list=backwards(neg_diag)
    positions=[[] for _ in range(len(grid)+len(grid[0])-1)]
    bottom_start=len(grid)
    for row in range(len(grid)):
        positions[row].append(1)
        positions[row].append(bottom_start)
        bottom_start=bottom_start-1
    one_right=2
    for col in range(1,len(grid[0])):
        positions[len(grid)+col-1].append(one_right)
        one_right=one_right+1
        positions[len(grid)+col-1].append(1)
    for word in words:
        for negative in range(len(neg_diag)):
            if word in neg_diag[negative]:
                print(word," is in the negative diagonal starting in position ",str(positions[negative]))
            if word in backwards_list[negative]:
                print(word," is backwards in the negative diagonal starting in position ",str(positions[negative]))

def solve_grid(grid,words):
    if is_valid(grid)==False:
        print("Invalid Grid")
    else:
        check_row(grid,words)
        check_pos_diag(grid,words)
        check_col(grid,words)
        check_neg_diag(grid,words)

dog_types=["COAEHBDHADTN","ELURORSUATEO","GHRXRIESCSRR","OPEPCBTHARRO","DRUINETEUFIT","LDENAAEPHFET","LNLSIGRHAIRW","UUGCTLUEUTIE","BHNHAEDRHSCI","PSHEMIEDIAOL","RHORLHAGHMLE","ECUAAUTTCGLR","TANADGRIIEIA","SDDIGROCPREC"]
dog_types_words=["CHIHUAHUA","BULLDOG","TERRIER","COLLIE","SHEPHERD","BOXER","HOUND","BEAGLE","CORGI","ROTTWEILER","PINSCHER","DALMATIAN","SETTER","MASTIFF","DACHSHUND"]
# print_grid(dog_types)
# print("")
# solve_grid(dog_types,dog_types_words)

artists=['QUSWBMGTMILKVATSUGXEQYOD','CUAMCJOANMIROEDIAOELCNFC','DRLETTIRGAMENERWYDZWPYXI','ZEVWPIMJCAHHYCVXBTRQDOAQ','ERAALJGEORGIAOKEEFFEGUIG','QUDSRIONERETSUGUAERREIPL','KDOSLBNSNIUGUAGLUAPYZUFW','CTRIZEAIORJYGECFHJDGSGOU','OHDLPWOQCUFZOLRGMLBNTLLP','LCAYBACNHPKLACOCFTEPEMIL','LELKEIUDAUAUOGAVCBDGMEKL','ORIAYDDLYRDBNHTRUJNKTRGA','PBENCJGXCEDALERRAAEMHNWG','NLLDRJHAMEVONOLALVODANPA','OAPIBNEORTZADUPEWNAIBELH','SETNRRNENDMAAAHIDYTGLRSC','KLDSXEFELDEPNCVRCIDTGHPC','CRNKTYCURKRGINIITAJNCIXR','APAYGNIAZELMAAELNRSSACOA','JARPILUKTGVUNSZRZCRSULMM','NCBVHOIEEGQIAGOYAJIGOQYK','KXMNDAPKUHKREPPOHDRAWDEB','WMEEFREAYTBCUOGVMPUDQAVH','XXRQLFBLGOTESSITAMIRNEHW']
artists_words=['ALBRECHTDURER','HENRIMATISSE','PETERPAULRUBENS','ANDYWARHOL','JACKSONPOLLOCK','PIERREAUGUSTERENOIR','CARAVAGGIO','JOANMIRO','PIETMONDRIAN','CLAUDEMONET','LEONARDODAVINCI','RAPHAEL','EDGARDEGAS','MARCCHAGALL','REMBRANDT','EDOUARDMANET','MICHELANGELO','RENEMAGRITTE','EDWARDHOPPER','PABLOPICASSO','SALVADORDALI','GEORGIAOKEEFFE','PAULCEZANNE','TITIAN','GOYA','PAULGAUGUIN','VINCENTVANGOGH','GUSTAVKLIMT','PAULKLEE','WASSILYKANDINSKY']
print_grid(artists)
print("")
solve_grid(artists,artists_words)
print("")
