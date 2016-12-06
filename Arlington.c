#include <stdio.h>
#define clear() printf("\033[H\033[J")


void encryptDecrypt(char *input, char *output) {
    char key[] = {'A'}; //Can be any chars, and any size array

    int i;
    for(i = 0; i < strlen(input); i++) {
        output[i] = input[i] ^ key[i % (sizeof(key)/sizeof(char))];
    }
}

void FunCti0nz4u(int argc, char *argv[])
{
   char baseStr[] = ") 7$8.42$$/,8253(/&";

    char encrypted[strlen(baseStr)];
    encryptDecrypt(baseStr, encrypted);
    printf("SUCCESS! DTE_Fl4g_iZ{%s}\n", encrypted);

}

void echo()
{
    char buffer[20];

    printf("\n\n");
    printf("  ::::::::::::::::::::::::       :::::::::::::       ::: :::::::: ::::::::: :::    ::: \n");
    printf("     :+:    :+:       :+:       :+:       :+:       :+::+:    :+::+:    :+::+:   :+:   \n");
    printf("    +:+    +:+       +:+       +:+       +:+       +:++:+    +:++:+    +:++:+  +:+     \n");
    printf("   +#+    +#++:++#  +#+       +#++:++#  +#+  +:+  +#++#+    +:++#++:++#: +#++:++       \n");
    printf("  +#+    +#+       +#+       +#+       +#+ +#+#+ +#++#+    +#++#+    +#++#+  +#+       \n");
    printf(" #+#    #+#       #+#       #+#        #+#+# #+#+# #+#    #+##+#    #+##+#   #+#       \n");
    printf("###    ##############################  ###   ###   ######## ###    ######    ###       \n");
    printf("\n\n");
    printf("========================================================================================\n");
    printf("=                  Can You Make Me Spit Out A Flag to Claim Telework?                  =\n");
    printf("========================================================================================\n");
    printf("=   HINT: THE GOAL IS NOT A ROOT SHELL, BUT TO FIND A HIDDEN ADDRESS OF A FUNCTION!    =\n");
    printf("========================================================================================\n");
    scanf("%s", buffer);
    printf("You entered: %s\n", buffer);
}

int main()
{
    clear();
    echo();

    return 0;
}


